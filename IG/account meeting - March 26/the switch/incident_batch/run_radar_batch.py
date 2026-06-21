import os
import json
import time
import argparse
from pathlib import Path
from typing import Optional, List

from openai import OpenAI
from openai import APIConnectionError, APITimeoutError, RateLimitError, APIStatusError
from tqdm import tqdm

DATA_DIR = Path("data")
RESULT_DIR = Path("results")
PROMPTS_DIR = Path("prompts")
MODEL = "gpt-5"

# Retry / resilience settings
MAX_RETRIES = 8
INITIAL_BACKOFF_SECONDS = 2
MAX_BACKOFF_SECONDS = 60
REQUEST_TIMEOUT_SECONDS = 1800  # 30 minutes


def atomic_write_text(path: Path, content: str, encoding: str = "utf-8") -> None:
    """
    Write to a temporary file first, then replace the target atomically.
    Prevents partial/corrupt files if the script crashes during write.
    """
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with open(tmp_path, "w", encoding=encoding, newline="\n") as f:
        f.write(content)
    os.replace(tmp_path, path)


def sanitize_name(name: str) -> str:
    """
    Make prompt/file names safe for folder/file creation.
    """
    safe = "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in name.strip())
    return safe.strip("_") or "prompt"


def list_prompt_files() -> List[Path]:
    if not PROMPTS_DIR.exists():
        raise FileNotFoundError(f"Prompts directory not found: {PROMPTS_DIR}")

    prompt_files = sorted([p for p in PROMPTS_DIR.iterdir() if p.is_file() and p.suffix.lower() == ".txt"])
    if not prompt_files:
        raise FileNotFoundError(f"No .txt prompt files found in: {PROMPTS_DIR}")
    return prompt_files


def prompt_user_for_selection(prompt_files: List[Path]) -> List[Path]:
    print("\nAvailable prompts:\n")
    for i, path in enumerate(prompt_files, start=1):
        print(f"  {i}. {path.stem}")
    print(f"  A. All prompts")

    while True:
        choice = input(
            "\nSelect prompt(s) to run "
            "(e.g. 1, 1,3,5, or A for all): "
        ).strip()

        if not choice:
            print("Please enter a selection.")
            continue

        if choice.lower() == "a":
            return prompt_files

        try:
            indexes = []
            for part in choice.split(","):
                part = part.strip()
                idx = int(part)
                if idx < 1 or idx > len(prompt_files):
                    raise ValueError
                indexes.append(idx - 1)

            # preserve order, remove duplicates
            seen = set()
            selected = []
            for idx in indexes:
                if idx not in seen:
                    selected.append(prompt_files[idx])
                    seen.add(idx)

            if not selected:
                print("Please select at least one prompt.")
                continue

            return selected

        except ValueError:
            print("Invalid selection. Use numbers like 1 or 1,3,4 or A.")


def build_prompt(prompt_text: str, csv_data: str) -> str:
    return f"""{prompt_text}

CSV DATA:
{csv_data}
"""


def call_model_with_retries(client: OpenAI, prompt: str) -> str:
    """
    Retry transient failures with exponential backoff.
    """
    last_error: Optional[Exception] = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.responses.create(
                model=MODEL,
                input=prompt,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
            return response.output_text

        except (APIConnectionError, APITimeoutError, RateLimitError) as e:
            last_error = e
            wait_time = min(INITIAL_BACKOFF_SECONDS * (2 ** (attempt - 1)), MAX_BACKOFF_SECONDS)
            print(
                f"[WARN] Transient error on attempt {attempt}/{MAX_RETRIES}: "
                f"{type(e).__name__}. Retrying in {wait_time}s..."
            )
            time.sleep(wait_time)

        except APIStatusError as e:
            last_error = e
            status = getattr(e, "status_code", None)
            if status and status >= 500 and attempt < MAX_RETRIES:
                wait_time = min(INITIAL_BACKOFF_SECONDS * (2 ** (attempt - 1)), MAX_BACKOFF_SECONDS)
                print(f"[WARN] Server error {status} on attempt {attempt}/{MAX_RETRIES}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise

        except Exception as e:
            raise RuntimeError(f"Unexpected error while calling model: {e}") from e

    raise RuntimeError(f"Model call failed after {MAX_RETRIES} attempts: {last_error}")


def load_manifest(manifest_file: Path) -> dict:
    if manifest_file.exists():
        with open(manifest_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"completed": {}, "failed": {}}


def save_manifest(manifest_file: Path, manifest: dict) -> None:
    atomic_write_text(manifest_file, json.dumps(manifest, indent=2, ensure_ascii=False))


def rebuild_combined_file(prompt_name: str, prompt_result_dir: Path, combined_file: Path) -> None:
    """
    Rebuild the combined file from all existing individual result files
    for a given prompt.
    """
    result_files = sorted(prompt_result_dir.glob("*.md"))

    # Exclude the combined file itself if it matches the glob
    result_files = [p for p in result_files if p.name != combined_file.name]

    parts = [
        f"# Combined {prompt_name} Evaluations\n\n",
        "Generated from batch processing\n\n---\n\n",
    ]

    for path in result_files:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        parts.append(content)
        parts.append("\n\n---\n\n")

    atomic_write_text(combined_file, "".join(parts))


def process_prompt(
    client: OpenAI,
    prompt_file: Path,
    csv_files: List[Path],
    args: argparse.Namespace,
) -> None:
    prompt_name = sanitize_name(prompt_file.stem)
    prompt_result_dir = RESULT_DIR / prompt_name
    prompt_result_dir.mkdir(parents=True, exist_ok=True)

    manifest_file = prompt_result_dir / "manifest.json"
    combined_file = prompt_result_dir / "all_results.md"

    with open(prompt_file, "r", encoding="utf-8") as f:
        prompt_text = f.read()

    manifest = load_manifest(manifest_file)

    files_to_process = []
    for path in csv_files:
        output_file = prompt_result_dir / f"{path.stem}_{prompt_name}.md"
        already_completed = path.name in manifest["completed"] or output_file.exists()
        previously_failed = path.name in manifest["failed"]

        if args.resume and already_completed and not (args.retry_failed and previously_failed):
            continue

        if args.resume and previously_failed and not args.retry_failed:
            continue

        files_to_process.append(path)

    print(f"\n=== Prompt: {prompt_file.stem} ===")
    print(f"Found {len(csv_files)} CSV file(s)")
    print(f"Will process {len(files_to_process)} file(s)")
    print(f"Results folder: {prompt_result_dir}\n")

    for path in tqdm(files_to_process, desc=prompt_file.stem):
        output_file = prompt_result_dir / f"{path.stem}_{prompt_name}.md"

        try:
            with open(path, "r", encoding="utf-8") as f:
                csv_data = f.read()

            full_prompt = build_prompt(prompt_text, csv_data)
            output = call_model_with_retries(client, full_prompt)

            title = f"# {path.name}\n\n"
            final_output = title + output.strip() + "\n"

            atomic_write_text(output_file, final_output)

            manifest["completed"][path.name] = {
                "output_file": str(output_file),
                "completed_at": int(time.time()),
                "status": "ok",
            }
            manifest["failed"].pop(path.name, None)
            save_manifest(manifest_file, manifest)

            rebuild_combined_file(prompt_file.stem, prompt_result_dir, combined_file)

        except Exception as e:
            manifest["failed"][path.name] = {
                "error": str(e),
                "failed_at": int(time.time()),
            }
            save_manifest(manifest_file, manifest)
            print(f"\n[ERROR] Failed processing {path.name} for prompt {prompt_file.stem}: {e}\n")

    rebuild_combined_file(prompt_file.stem, prompt_result_dir, combined_file)

    completed_count = len(manifest["completed"])
    failed_count = len(manifest["failed"])

    print(f"\n✅ Finished prompt: {prompt_file.stem}")
    print(f"Completed: {completed_count}")
    print(f"Failed: {failed_count}")
    print(f"Combined report saved to: {combined_file}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one or more prompts against CSV files")
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of CSV files to process")
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip files already completed according to manifest/output files",
    )
    parser.add_argument(
        "--retry-failed",
        action="store_true",
        help="Retry files previously marked as failed",
    )
    args = parser.parse_args()

    RESULT_DIR.mkdir(parents=True, exist_ok=True)

    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Data directory not found: {DATA_DIR}")

    prompt_files = list_prompt_files()
    selected_prompts = prompt_user_for_selection(prompt_files)

    csv_files = sorted([p for p in DATA_DIR.iterdir() if p.is_file() and p.suffix.lower() == ".csv"])
    if args.limit:
        csv_files = csv_files[:args.limit]

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in: {DATA_DIR}")

    client = OpenAI()

    print("\nSelected prompts:")
    for p in selected_prompts:
        print(f"  - {p.stem}")

    print(f"\nCSV files to process: {len(csv_files)}\n")

    for prompt_file in selected_prompts:
        process_prompt(client, prompt_file, csv_files, args)

    print("✅ All selected prompts finished.")


if __name__ == "__main__":
    main()