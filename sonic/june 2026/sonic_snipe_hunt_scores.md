# Sonic Snipe Hunt Scores

Sources:

- `allsessionsfacetsandmarkersbycategory.md` for category and facet scores
- `sonic_all_drills.csv` for player names, drill names, dates, and GUOT scores

Scope: Snipe Hunt drill IDs `9062`, `9142`, `9159`, and `9330`.

## Scores

| Session ID | Player | Drill | Session start | GUOT | Rank | leadership | coordination | mindset | communication | F1 | F2 | F3 | F4 | F5 | Mean Facet Score | Overall Score Percentage |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 9062 | leigh.burton | Snipe Hunt | 20/05/2026 15:04 |  | 125 | 3.00 | 3.00 | 2.50 | 2.00 | 2 | N/A | 2 | 2 | 2 | 2.00 | 54.67% |
| 9142 | joe.muller | Snipe Hunt | 26/05/2026 15:09 | 7 | 9 | 3.00 | 2.80 | 2.75 | 3.00 | 2 | 3 | 3 | 3 | 3 | 2.80 | 77.33% |
| 9159 | seth.lohr | Snipe Hunt | 27/05/2026 12:09 | 10 | 117 | 3.00 | 2.60 | 2.25 | 2.00 | 1 | 2 | 2 | 2 | 2 | 1.80 | 55.67% |
| 9330 | leigh.burton | Snipe Hunt | 03/06/2026 15:03 | 9 | 25 | 3.00 | 2.80 | 2.50 | 2.00 | 2 | 3 | 3 | 3 | 2 | 2.60 | 71.33% |

## Snipe Hunt Time Leaderboard

Source: `Snipe Hunt Leaderboard.xlsx`, `Snipe Hunt Time` tab.

The tab contains 154 Snipe Hunt rows, of which 113 have a recorded `duration` and are ranked below. Ranks are calculated from the parsed `duration` field, fastest first, using shared ranks for exact ties. Rows without a recorded duration are listed as not ranked.

| Session ID | Player | Started | Duration | Time rank | Ranked entries | Attempts | Attempt number |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| 9062 | leigh.burton | 2026-05-20 15:06:41 | Not recorded | Not ranked | 113 | 2 | 1 |
| 9142 | joe.muller | 2026-05-26 15:09:54 | 45m 04s | 111 | 113 | 1 | 1 |
| 9159 | seth.lohr | 2026-05-27 12:14:06 | 36m 39s | 85 | 113 | 1 | 1 |
| 9330 | leigh.burton | 2026-06-03 15:04:02 | 42m 35s | 102 | 113 | 2 | 2 |

## Cohort Summary Statistics

Statistics are calculated from the four Snipe Hunt rows above. Standard deviation is sample standard deviation. `N/A` values are excluded from the relevant calculation, so F2 uses 3 scored rows.

| Score | N | Average | Min | Max | Standard deviation |
| --- | ---: | ---: | ---: | ---: | ---: |
| leadership | 4 | 3.00 | 3.00 | 3.00 | 0.00 |
| coordination | 4 | 2.80 | 2.60 | 3.00 | 0.16 |
| mindset | 4 | 2.50 | 2.25 | 2.75 | 0.20 |
| communication | 4 | 2.25 | 2.00 | 3.00 | 0.50 |
| F1 | 4 | 1.75 | 1.00 | 2.00 | 0.50 |
| F2 | 3 | 2.67 | 2.00 | 3.00 | 0.58 |
| F3 | 4 | 2.50 | 2.00 | 3.00 | 0.58 |
| F4 | 4 | 2.50 | 2.00 | 3.00 | 0.58 |
| F5 | 4 | 2.25 | 2.00 | 3.00 | 0.50 |

## Facet Key

| Facet | Meaning |
| --- | --- |
| F1 | Misleading correlations |
| F2 | Hidden coupling |
| F3 | Decreased access to team |
| F4 | Interdependencies / coordination bottlenecks |
| F5 | Data overload / buried information |

## Entire Dataset Average Scores

These averages are calculated across all 156 rows in `allsessionsfacetsandmarkersbycategory.md`. `N/A` values are excluded from the relevant calculation, so F2 uses 150 scored rows.

| Score | N | Entire dataset average |
| --- | ---: | ---: |
| leadership | 156 | 2.76 |
| coordination | 156 | 2.50 |
| mindset | 156 | 2.23 |
| communication | 156 | 1.89 |
| F1 | 156 | 1.89 |
| F2 | 150 | 2.41 |
| F3 | 156 | 2.43 |
| F4 | 156 | 2.56 |
| F5 | 156 | 2.05 |

## Sonic Cohort vs Entire Dataset

Difference is calculated as Sonic Snipe Hunt cohort average minus entire dataset average.

| Score | Sonic cohort average | Entire dataset average | Difference |
| --- | ---: | ---: | ---: |
| leadership | 3.00 | 2.76 | +0.24 |
| coordination | 2.80 | 2.50 | +0.30 |
| mindset | 2.50 | 2.23 | +0.27 |
| communication | 2.25 | 1.89 | +0.36 |
| F1 | 1.75 | 1.89 | -0.14 |
| F2 | 2.67 | 2.41 | +0.26 |
| F3 | 2.50 | 2.43 | +0.07 |
| F4 | 2.50 | 2.56 | -0.06 |
| F5 | 2.25 | 2.05 | +0.20 |
