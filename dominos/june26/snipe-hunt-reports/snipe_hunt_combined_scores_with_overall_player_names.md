# Snipe Hunt — Combined Facet and Marker Scores

One row per Snipe Hunt run, sorted by session ID. Ratings are taken from each run’s two `Score Summary` tables: facets and markers. Overall Score is calculated as `((sum of facet scores / 20) * 0.7) + ((sum of marker scores / 48) * 0.3)`.

| Player Name | Session ID | Overall Score | F1 — Misleading correlations | F2 — Hidden coupling | F3 — Decreased access to team | F4 — Interdependencies / coordination bottlenecks | F5 — Data overload / buried information | Mean Facet Score | L3 — Takes explicit ownership | C1 — Asks clarifying questions before acting | C3 — Checks for recent changes | C4 — Delegates tasks to specific people | C6 — Runs parallel investigation threads | C7 — Escalates when stuck | M2 — Forms and tests working hypotheses | M3 — Uses evidence to narrow the scope | M4 — Considers potential consequences before acting | M5 — Adapts approach when initial path isn't working | K2 — Provides substantive updates to business stakeholders | K4 — Communicates issue scope clearly to the technical team | Mean Marker Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Swetha1 | 9058 | 0.481 | 2 | 2 | 2 | 2 | 2 | 2.00 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1.75 |
| Vallabh | 9150 | 0.459 | 2 | 2 | 2 | 2 | 1 | 1.80 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 1.92 |
| Chris | 9196 | 0.601 | 2 | 2 | 3 | 3 | 2 | 2.40 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2.42 |
| Swetha2 | 9311 | 0.417 | 1 | 2 | 2 | 2 | 1 | 1.60 | 2 | 3 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 1.83 |
| Swetha3 | 9317 | 0.595 | 2 | 3 | 2 | 3 | 2 | 2.40 | 3 | 3 | 3 | 2 | 2 | 3 | 2 | 2 | 1 | 3 | 2 | 2 | 2.33 |
| Vaishnavi | 9380 | 0.465 | 2 | 1 | 2 | 2 | 2 | 1.80 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2.00 |
| Pradeep | 9397 | 0.494 | 2 | 2 | 2 | 2 | 2 | 2.00 | 2 | 3 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 1.92 |
| Praveen | 9418 | 0.453 | 2 | 2 | 2 | 1 | 2 | 1.80 | 2 | 3 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1.83 |
| Latif | 9421 | 0.519 | 1 | 2 | 2 | 3 | 2 | 2.00 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 1 | 2 | 2 | 2 | 2.25 |

## Columns included

- Player Name: mapped from the session ID
- Overall Score: weighted score using 70% facets and 30% markers
- Facets: F1 — Misleading correlations, F2 — Hidden coupling, F3 — Decreased access to team, F4 — Interdependencies / coordination bottlenecks, F5 — Data overload / buried information, Mean Facet Score
- Markers: L3 — Takes explicit ownership, C1 — Asks clarifying questions before acting, C3 — Checks for recent changes, C4 — Delegates tasks to specific people, C6 — Runs parallel investigation threads, C7 — Escalates when stuck, M2 — Forms and tests working hypotheses, M3 — Uses evidence to narrow the scope, M4 — Considers potential consequences before acting, M5 — Adapts approach when initial path isn't working, K2 — Provides substantive updates to business stakeholders, K4 — Communicates issue scope clearly to the technical team, Mean Marker Score
