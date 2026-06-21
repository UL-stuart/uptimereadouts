# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Contents

This directory contains CSV chat log exports from incident management simulation drills. Files follow the naming pattern `username:scenario-name-id.csv` — the username identifies the player being evaluated, the scenario name identifies the drill, and the numeric ID is the session identifier.

## Players and Scenarios

Five players across four scenario types:

| Player | Scenarios |
|--------|-----------|
| andrew | Discount-Disaster-Workshop, The-Big-Investor-V2, The-Unknown-Unknown, Too-Good-To-Be-True-Workshop |
| jamiem | Discount-Disaster-Workshop, The-Big-Investor-V2, The-Unknown-Unknown, Too-Good-To-Be-True-Workshop |
| lewrad | Discount-Disaster-Workshop, The-Big-Investor-V2, Too-Good-To-Be-True-Workshop |
| nestor | DEFCON-1 |
| patric | DEFCON-1, Discount-Disaster-Workshop, The-Big-Investor-V2, The-Unknown-Unknown, Too-Good-To-Be-True-Workshop |

## Directory Structure

```
output/           ← this directory (root)
  prompts/        ← prompt templates to run against the CSV files
  output/         ← results will be written here, one file per CSV run
  *.csv           ← source chat log exports
```

The intended workflow is to run the prompt in `prompts/Incident_Radar_analysis_prompt.md` against each CSV file and write the results into `output/`.

## CSV Format

All files share the same four-column schema:

```
datetime, player, channel, message
```

- `datetime` — ISO-format timestamp (e.g. `2026-04-15 10:04:14`)
- `player` — Slack username of the message sender
- `channel` — simulation channel name, typically `online-boutique-<id>`
- `message` — message text
