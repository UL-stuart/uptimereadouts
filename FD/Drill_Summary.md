# Drill Summary — May–June 2026

Summary of all incident drills run over the period, with GUOT scores and the recurring themes from players' post-drill reflections.

## At a glance

- **Drills run:** 15
- **Players:** 4 — shea_h, joseph, shea_m, conor
- **Period:** 11 May 2026 → 3 June 2026 (~3.5 weeks)
- **Scenarios:** 5 — The Big Investor (4 runs), Too Good To Be True (3), Discount Disaster (3), Snipe Hunt (3), DEFCON 1 (2)
- **GUOT average:** 8.3 / 10 (range 7–10; 7 of 15 drills scored ≥9)
- **Typical duration:** ~23 min (range 10–39 min; 3 sessions had no duration recorded)

## GUOT scores

GUOT (Good Use of Time) is the post-drill self-rated score, 1–10.

**Distribution:** 7 → ×4 · 8 → ×3 · 9 → ×7 · 10 → ×1. Mean 8.3, median 9.

### By player

| Player | Drills | GUOT scores | Mean |
|---|---|---|---|
| **conor** | 2 | 9, 10 | **9.5** |
| **joseph** | 4 | 9, 9, 9, 9 | **9.0** |
| **shea_m** | 4 | 8, 9, 8, 7 | **8.0** |
| **shea_h** | 5 | 7, 8, 9, 7, 7 | **7.6** |

### By scenario

| Scenario | Runs | GUOT scores | Mean |
|---|---|---|---|
| **DEFCON 1** | 2 | 9, 9 | **9.0** |
| **Discount Disaster** | 3 | 9, 8, 8 | **8.3** |
| **Too Good To Be True** | 3 | 7, 9, 9 | **8.3** |
| **The Big Investor** | 4 | 9, 9, 8, 7 | **8.3** |
| **Snipe Hunt** | 3 | 7, 10, 7 | **8.0** |

## Main themes — *what to take into the next incident*

The reflections cluster around five recurring lessons:

- **Stakeholder communication cadence** is the single most-cited takeaway (5 of 15). Players repeatedly resolved to keep the business side updated more often and faster — "keep everyone on the business side updated and informed of progress" (joseph, TGTBT); "more updates to management team" (shea_h, Big Investor); "keep Bez posted when he is constantly looking for updates" (shea_m, Snipe Hunt); "updating chat quicker" (shea_h, Snipe Hunt).
- **Engage the whole team early and broadly.** Contact responders as soon as the incident opens and make sure everyone is actively looking — "contact each team member asap to check if they have any issues" (shea_h, Discount Disaster); "make sure everyone is looking into [the] issue" (shea_h, Snipe Hunt).
- **Don't anchor on the first theory.** Question the working hypothesis, probe it, and keep assessing impact — "not to take one POV/theory for granted, to ensure to question it, probe and assess impact" (conor, Big Investor); "keep an open mind and to really assess customer and organisational impact" (joseph, DEFCON 1).
- **Change-checking and faster rollback / RCA.** Look at recent changes first, and move through rollback to a root-cause analysis more quickly — "checking certain changes that may have went in first" (shea_h, TGTBT); "be faster with getting the changes rolled back… and get an RCA asap" (joseph, Big Investor).
- **Escalation and working-theory discipline.** "The importance of early escalation and how valuable a feasible working theory is" (conor, Snipe Hunt); balancing ETA expectations on resolution (joseph, Discount Disaster). Security hygiene also surfaced — "make sure everyone didn't click any suspicious emails" (shea_h, DEFCON 1).

## Main themes — *what was surprising*

- **The security / attack angle caught people off guard** (4 of 15). It was perceived as rare, was identified late, or relied on resources players didn't know existed — "a security issue is a rarer issue so having to pull in all of the team… was surprising" (joseph, Discount Disaster); "the security threat, I asked late… Maya may have been the last person I asked" (shea_h, Discount Disaster); "the phishing email was a twist" (shea_h, DEFCON 1); "the fact there was [an] external security vendor we could reach out to — I thought it was limited to the org chart" (joseph, DEFCON 1).
- **People availability and responsiveness** was a repeated shock, especially in Snipe Hunt — "people off, and Tanya not prioritizing this issue when I said it should be priority" (shea_h); "the number of personnel on leave/unavailable" (conor); "not clear guidance on who to consult with when Tinus and Hamed were out of the office" (shea_m); "people were slow to respond, hard to get people to look into this" (shea_h, Big Investor).
- **Initial assumptions were disproven.** The obvious cause turned out not to be the cause — "the changes made were not the issue" (joseph, Big Investor); "the issue stemmed back to chaos tests which were initially dismissed" (conor, Big Investor).
- **Process / governance gaps.** Changes going in without the IC's knowledge — "there were 3 changes implemented without me first being informed" (joseph, TGTBT) — and unexpectedly tight time pressure — "the time limit… thought I had a bit more time to solve the issue" (shea_m, Big Investor).
- **Realism of the simulation.** Despite being bot-driven, the scenarios felt convincing — "the realistic nature of the incident was surprising considering it was Bots… response times of each person on the team were pretty good" (shea_m, TGTBT); the assistant bot was noted as a helpful prompt for who to contact and what to check (shea_h, TGTBT).

## Data-quality notes

- **Truncated entry:** the *what was surprising* field for shea_m's Discount Disaster run (id 9163) reads only "I fou" — it appears cut off in the source CSV.
- **Missing durations:** 3 sessions have no recorded duration (joseph 9027, shea_m 8992, shea_m 9305), so the duration average covers 12 of 15 drills.
- The CSV contains duplicated `session_id` and `player` columns; values agree across the duplicates.
