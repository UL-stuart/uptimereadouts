# Snipe Hunt — Combined Facet and Marker Scores

One row per Snipe Hunt run, sorted by session ID. Ratings are taken from each run’s two `Score Summary` tables: facets and markers. Overall Score is calculated as `((sum of facet scores / 20) * 0.7) + ((sum of marker scores / 48) * 0.3)`. Leaderboard Position is calculated from the uploaded leaderboard by ranking `Composite Score` descending; tied composite scores share the same position. Time Leaderboard is calculated from the uploaded timings CSV by ranking completed sessions by `minutes` ascending; tied minutes share the same rank, and sessions with no minutes value are marked `DNF`.

| Player Name | Session ID | Leaderboard Position | time_leaderboard | Time to Complete | Overall Score | F1 — Misleading correlations | F2 — Hidden coupling | F3 — Decreased access to team | F4 — Interdependencies / coordination bottlenecks | F5 — Data overload / buried information | Mean Facet Score | L3 — Takes explicit ownership | C1 — Asks clarifying questions before acting | C3 — Checks for recent changes | C4 — Delegates tasks to specific people | C6 — Runs parallel investigation threads | C7 — Escalates when stuck | M2 — Forms and tests working hypotheses | M3 — Uses evidence to narrow the scope | M4 — Considers potential consequences before acting | M5 — Adapts approach when initial path isn't working | K2 — Provides substantive updates to business stakeholders | K4 — Communicates issue scope clearly to the technical team | Mean Marker Score |
| :-------------- | -------------: | -----------------------: | :------------------- | :---------------- | ----------------: | -------------------------------: | -----------------------: | --------------------------------: | ----------------------------------------------------: | ------------------------------------------: | -------------------: | --------------------------------: | -----------------------------------------------: | ---------------------------------: | ------------------------------------------: | -------------------------------------------: | ----------------------------: | ------------------------------------------: | -----------------------------------------: | ------------------------------------------------------: | -------------------------------------------------------: | -------------------------------------------------------------: | --------------------------------------------------------------: | --------------------: |
| Vallabh | 9150 | 118 | 84 | 42m 08s | 0.459 | 2 | 2 | 2 | 2 | 1 | 1.8 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 1.92 |
| Chris | 9196 | 45 | 37 | 29m 57s | 0.601 | 2 | 2 | 3 | 3 | 2 | 2.4 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2.42 |
| Swetha3 | 9317 | 55 | 2 | 20m 40s | 0.595 | 2 | 3 | 2 | 3 | 2 | 2.4 | 3 | 3 | 3 | 2 | 2 | 3 | 2 | 2 | 1 | 3 | 2 | 2 | 2.33 |
| Vaishnavi | 9380 | 116 | DNF | – | 0.465 | 2 | 1 | 2 | 2 | 2 | 1.8 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 |
| Pradeep | 9397 | 101 | DNF | – | 0.494 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1.92 |
| Praveen | 9418 | 119 | DNF | – | 0.453 | 2 | 2 | 2 | 1 | 2 | 1.8 | 2 | 3 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1.83 |
| Latif | 9421 | 86 | 63 | 35m 50s | 0.519 | 1 | 2 | 2 | 3 | 2 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 1 | 2 | 2 | 2 | 2.25 |

## Columns included

- Player Name: mapped from the session ID
- Leaderboard Position: rank in the uploaded overall leaderboard, based on `Composite Score` descending
- Overall Score: weighted score using 70% facets and 30% markers
- Facets: F1 — Misleading correlations, F2 — Hidden coupling, F3 — Decreased access to team, F4 — Interdependencies / coordination bottlenecks, F5 — Data overload / buried information, Mean Facet Score
- Markers: L3 — Takes explicit ownership, C1 — Asks clarifying questions before acting, C3 — Checks for recent changes, C4 — Delegates tasks to specific people, C6 — Runs parallel investigation threads, C7 — Escalates when stuck, M2 — Forms and tests working hypotheses, M3 — Uses evidence to narrow the scope, M4 — Considers potential consequences before acting, M5 — Adapts approach when initial path isn't working, K2 — Provides substantive updates to business stakeholders, K4 — Communicates issue scope clearly to the technical team, Mean Marker Score

## Cohort Averages Excluding Sessions 9058 and 9311

These averages exclude sessions **9058** and **9311**, which were Swetha's first two runs. The calculations include only the raw facet columns (`F1`–`F5`) and raw marker columns (`L`, `C`, `M`, `K`). They do not include `Overall Score`, `Mean Facet Score`, or `Mean Marker Score`.

### Average by Facet and Marker Column

| Type / Group | Column | Average Score |
| --- | --- | --- |
| Facet | F1 — Misleading correlations | 1.86 |
| Facet | F2 — Hidden coupling | 2.00 |
| Facet | F3 — Decreased access to team | 2.14 |
| Facet | F4 — Interdependencies / coordination bottlenecks | 2.29 |
| Facet | F5 — Data overload / buried information | 1.86 |
| Leadership | L3 — Takes explicit ownership | 2.57 |
| Coordination | C1 — Asks clarifying questions before acting | 2.86 |
| Coordination | C3 — Checks for recent changes | 2.14 |
| Coordination | C4 — Delegates tasks to specific people | 2.29 |
| Coordination | C6 — Runs parallel investigation threads | 1.71 |
| Coordination | C7 — Escalates when stuck | 2.43 |
| Mindset | M2 — Forms and tests working hypotheses | 2.00 |
| Mindset | M3 — Uses evidence to narrow the scope | 2.00 |
| Mindset | M4 — Considers potential consequences before acting | 1.29 |
| Mindset | M5 — Adapts approach when initial path isn't working | 2.29 |
| Communication | K2 — Provides substantive updates to business stakeholders | 1.86 |
| Communication | K4 — Communicates issue scope clearly to the technical team | 1.71 |

### Average by Marker Grouping

For each marker grouping, I first averaged each marker column across the included sessions, then averaged those marker-column averages within the grouping.

| Marker Group | Included Marker Columns | Average of Column Averages |
| --- | --- | --- |
| Leadership | L3 | 2.57 |
| Coordination | C1, C3, C4, C6, C7 | 2.29 |
| Communication | K2, K4 | 1.79 |
| Mindset | M2, M3, M4, M5 | 1.89 |
