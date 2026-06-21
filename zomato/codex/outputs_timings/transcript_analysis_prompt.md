# Drill Transcript Analysis Prompt

Analyse exactly one drill transcript CSV at a time. The CSV has columns:

`datetime,player,channel,message`

Produce a Markdown report for that single transcript. Do not use context from other transcripts.

## Extraction Rules

1. Identify the UptimeLabs welcome message containing `Welcome to Bezs Beatles Day`.
2. Define T0 as the first message row after that welcome message. T0 can be from any sender, including NPCs/bots.
3. Define the session end as the final row in the CSV.
4. Calculate session duration in minutes from T0 to the final CSV row. If there is no row after the welcome message, mark the session as incomplete and set duration to `0`.
5. A session is successfully resolved if Tanya says `Great work everyone`, or if equivalent resolution evidence is present. Tanya's phrase is sufficient even if the player did not separately confirm with business.
6. Extract the last severity mentioned in the transcript and normalize it to one of `SEV0`, `SEV1`, `SEV2`, `SEV3`, or `SEV4`. `SEV0` indicates the highest possible severity level.
7. Treat severity variants as equivalent:
   - `SEV0`, `SEV 0`, `SEV-0`, `SEVX` where X is 0-4.
   - `S0`, `S 0`, `S-0` maps to `SEV0`.
   - `P0`, `P 0`, `P-0` maps to `SEV0`; `P1` maps to `SEV1`; `P2` maps to `SEV2`; and so on.
   - `PX` maps to `SEVX` where X is 0-4.
8. If there are several severities, use the last one mentioned chronologically.
9. Determine whether an incident record was formally created. Mark `Yes` if any generated incident record appears, such as `Incident Number INC...`, or if a non-welcome message appears to invoke the literal `/incident` command. Do not count the welcome instruction `Use /incident to create an incident record` as evidence that an incident was created.
10. Count PLAYER messages after T0 only.
11. Count PLAYER messages after T0 in any channel whose name contains `business-comms`.
12. Treat one CSV row as one message, even when the message is multi-line.
13. Include source metadata: filename, session ID, and player name inferred from the filename.
14. Include evidence fields with exact timestamp, sender, channel, and a short quote or paraphrase for key findings.
15. Flag ambiguous cases instead of forcing unsupported conclusions.

## Output Format

Return Markdown with this structure:

```markdown
# <filename>

| Field | Value |
|---|---|
| Filename | ... |
| Player from filename | ... |
| Session ID | ... |
| T0 | ... |
| Final row timestamp | ... |
| Duration minutes | ... |
| Completed/incomplete | ... |
| Successfully resolved | Yes/No/Ambiguous |
| Normalized severity | SEV0/SEV1/SEV2/SEV3/SEV4/Ambiguous/Not found |
| Incident record created | Yes/No/Ambiguous |
| PLAYER messages after T0 | ... |
| PLAYER business-comms messages after T0 | ... |

## Evidence

| Finding | Evidence |
|---|---|
| T0 | ... |
| Final row | ... |
| Resolution | ... |
| Severity | ... |
| Incident record | ... |

## Notes

- Any ambiguity or caveat.
```
