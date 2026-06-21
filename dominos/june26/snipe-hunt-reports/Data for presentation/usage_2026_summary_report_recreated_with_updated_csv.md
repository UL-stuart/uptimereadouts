# 2026 Drill Usage Summary

**Source:** `updated_dom_usage.csv`  
**Coverage:** 07 Jan 2026 to 11 Jun 2026  
**Note on drill grouping:** drill names are grouped after removing a trailing `Workshop` suffix and normalising whitespace. For example, `Discount Disaster` and `Discount Disaster Workshop` are treated as the same drill. Raw names are preserved in the mapping table below.  
**Additional activity note:** In addition to the drill sessions recorded in the CSV, there were **9 PIR sessions**. These are counted separately because they are not drill rows in the CSV.

## Executive Summary

| Metric | Value |
| --- | --- |
| Drill sessions in CSV | 55 |
| Additional PIR sessions | 9 |
| Total sessions including PIR | 64 |
| Players represented in CSV | 12 |
| Different drills, exact raw `name` values | 17 |
| Different drills, grouped similar names | 16 |
| Valid GUOT scores | 46 |
| Blank / non-numeric GUOT values ignored | 9 |
| Average GUOT | 9.48 |
| Median GUOT | 10 |

## 1. Number of Sessions

There are **55 drill sessions** in the CSV file. Including the **9 PIR sessions** provided separately, there are **64 total sessions** represented in this summary.

## 2. Sessions by Player

| Player | Sessions |
| --- | --- |
| chris.watts | 10 |
| swetha.nayudu | 9 |
| vallabh.vyas | 8 |
| praveen.sadul | 6 |
| pradeep.c | 6 |
| vaishnavi.b | 5 |
| latif.khan | 4 |
| gowthamkumar.b | 2 |
| ramesh.matta | 2 |
| yeshwanth.tp | 1 |
| ranjan.padhi | 1 |
| neil.campbell | 1 |

## 3. GUOT Scores

GUOT calculations ignore blanks and non-numeric values. In this file, **46** rows have numeric GUOT scores and **9** rows have blank or non-numeric values.

### Overall GUOT Summary

| Metric | Value |
| --- | --- |
| Valid numeric scores | 46 |
| Average | 9.48 |
| Minimum | 8 |
| Q1 | 9 |
| Median | 10 |
| Q3 | 10 |
| Maximum | 10 |

### Count by Score Value

| GUOT score | Count | Percentage |
| --- | --- | --- |
| 8 | 4 | 8.7% |
| 9 | 16 | 34.8% |
| 10 | 26 | 56.5% |

### Histogram / Ranges

| GUOT range | Count | Percentage |
| --- | --- | --- |
| 0–6 | 0 | 0.0% |
| 7–8 | 4 | 8.7% |
| 9–10 | 42 | 91.3% |

### GUOT by Player

| Player | Sessions | Valid GUOT | Average GUOT | Median | Distribution |
| --- | --- | --- | --- | --- | --- |
| chris.watts | 10 | 10 | 9.30 | 9 | 8: 1, 9: 5, 10: 4 |
| swetha.nayudu | 9 | 8 | 9.62 | 10 | 8: 1, 9: 1, 10: 6 |
| vallabh.vyas | 8 | 5 | 9.60 | 10 | 9: 2, 10: 3 |
| pradeep.c | 6 | 5 | 10.00 | 10 | 10: 5 |
| praveen.sadul | 6 | 5 | 8.80 | 9 | 8: 1, 9: 4 |
| vaishnavi.b | 5 | 5 | 10.00 | 10 | 10: 5 |
| latif.khan | 4 | 4 | 9.00 | 9 | 9: 4 |
| gowthamkumar.b | 2 | 1 | 10.00 | 10 | 10: 1 |
| ramesh.matta | 2 | 2 | 9.00 | 9 | 8: 1, 10: 1 |
| neil.campbell | 1 | 0 | – | – | – |
| ranjan.padhi | 1 | 1 | 10.00 | 10 | 10: 1 |
| yeshwanth.tp | 1 | 0 | – | – | – |

## 4. Different Drills

There are **16 grouped drills** after treating similar names as the same drill. There are **17 exact raw `name` values** before grouping.

### Sessions by Grouped Drill

| Grouped drill | Sessions |
| --- | --- |
| Snipe Hunt | 9 |
| The Chain | 7 |
| Version confusion | 7 |
| The Switch | 7 |
| Cart-astrophe | 5 |
| Details Matter | 3 |
| Roblox | 3 |
| Bezs Beatles Day! | 3 |
| Discount Disaster | 2 |
| The Big Investor | 2 |
| The Unknown Unknown | 2 |
| Rumours | 1 |
| Missing Delivery | 1 |
| Radio Silence | 1 |
| Once Upon A Time In Production | 1 |
| Tech Beatles Day! | 1 |

### Drill Name Grouping Map

| Grouped drill | Raw name values included | Sessions |
| --- | --- | --- |
| Bezs Beatles Day! | Bezs Beatles Day! | 3 |
| Cart-astrophe | Cart-astrophe | 5 |
| Details Matter | Details Matter | 3 |
| Discount Disaster | Discount Disaster, Discount Disaster Workshop | 2 |
| Missing Delivery | Missing Delivery | 1 |
| Once Upon A Time In Production | Once Upon A Time In Production | 1 |
| Radio Silence | Radio Silence | 1 |
| Roblox | Roblox Workshop | 3 |
| Rumours | Rumours | 1 |
| Snipe Hunt | Snipe Hunt | 9 |
| Tech Beatles Day! | Tech Beatles Day! | 1 |
| The Big Investor | The Big Investor Workshop | 2 |
| The Chain | The Chain Workshop | 7 |
| The Switch | The Switch | 7 |
| The Unknown Unknown | The Unknown Unknown | 2 |
| Version confusion | Version confusion | 7 |

## 5. Session Duration Data

Duration data is present for **27** of the **55** CSV drill sessions. Blank duration values are ignored in the summary below.

| Metric | Value |
| --- | --- |
| Sessions with duration | 27 |
| Average minutes | 22.15 |
| Median minutes | 20 |
| Minimum minutes | 10 |
| Maximum minutes | 42 |

## 6. Themes from `what_to_take_into_next_incident`

### Understand dependencies and system coupling before acting

- Several reflections focused on understanding service dependencies, interdependent changes, backup capacity, and wider system context before choosing a remediation.
- Example quotes:
  - “We need to understand the dependencies of the services.”
  - “I think I rushed for rollback for the 1st change rather getting all the details ad rolling back interdependent changes first ..”
  - “Engage people and think in broader view not specific to default things like recent deployments”

### Bring the right people in quickly, including backup owners

- Participants repeatedly mentioned involving the right teams, knowing backup contacts, and bringing in unavailable or specialist people quickly.
- Example quotes:
  - “Reach out to right people”
  - “I should look for the backup person if someone is not around.”
  - “we need to understand the team availability, and need to know backup person.”

### Use evidence, logs, metrics, and change records more deliberately

- A strong theme was the need to gather concrete evidence, compare current metrics, inspect logs, and use change registers instead of relying on first impressions.
- Example quotes:
  - “We should gather the all the information and compare with todays metrics”
  - “learned to ensure all parties are involved and always refer to Change register”
  - “check each metrics in more details. communicate to customer and vendors about the impact”

### Stronger command, escalation, and decision-making under uncertainty

- Several comments point to taking command, escalating sooner, changing severity when appropriate, and making decisions when senior guidance is unavailable.
- Example quotes:
  - “Taking a command and directing team to one solution.”
  - “taking decisions when no one around to guide”
  - “Escalating quicker for help”

### Communicate, coordinate, and keep pressure on participation

- Participants highlighted communication, collaboration, and the need to keep pressure on colleagues who are busy, reluctant, or outside the immediate response.
- Example quotes:
  - “I learned how to communicate and check the issue.”
  - “Good communication, using the team sufficiently instead of digging through logs and changes myself.”
  - “That you need to force people to join in and resolve issues, they wont always be willing or be busy doing other things”

## 7. Themes from `what_was_surprising`

### Incidents were more complex, non-linear, or stressful than expected

- Several respondents were surprised by the complexity, stress, ambiguity, or non-linear path to resolution.
- Example quotes:
  - “I found it quite taxing and was not expecting it to be that complex”
  - “I had decisions to make and it was very stressful, It wasnt linear”
  - “It just felt really hard to co-ordinate the team.”

### Multiple or misleading causes appeared in the same incident

- A recurring surprise was that incidents often involved more than one issue, misleading first causes, or apparent causes that turned out not to be causal.
- Example quotes:
  - “Two issues were reported”
  - “I like that it ended up being two issues, the first solution identified a second so had to be attacked on two fronts.”
  - “Dev mentioned some test script might have impacted which was not the case.”

### Unavailable people and unclear backup ownership created pressure

- Unavailable senior people, busy colleagues, vendor calls, and unclear backup routes were repeatedly noted as unexpected operational challenges.
- Example quotes:
  - “How to handle situation when senior people are not around”
  - “I wasnt expecting people to be unavailable. Had to call in people from engagements and depustize. I also had to be a change authority.”
  - “I was surprises tanya was busy and hamed out off office”

### Scope and impact changed in unexpected ways

- Participants were surprised by incidents moving from regional to global, affecting only certain users/currencies, or having high business impact despite a limited technical footprint.
- Example quotes:
  - “incident which is with region specific and later it became global it was some of panic situation.”
  - “only few currency has problem. while overall website was performing well and customer were able to place order”
  - “its affected limited users but its impact the business. looks like version mismatch , older version users are not facing an issue”

### Backups, failover, and environments behaved unexpectedly

- Backup capacity, UAT refreshes, and failover assumptions emerged as repeated surprise areas.
- Example quotes:
  - “UAT DB back up was not expected ..”
  - “That back up system PCS wasnt tested to  the capacity that it can handle the live traffic.. which is key for the systems”
  - “UAT data refresh - as mostly engineers are confident that they won't mess up with env's.”

### Technical root causes were hard to isolate from normal-looking data

- Certificate changes, DNS/network ambiguity, browser versions, and missing change-record clues made root cause isolation harder than expected.
- Example quotes:
  - “Certificate chages”
  - “DNS and network looks good but still issue couldn't resolve”
  - “Challenging drill as nothing in change request to able isolate issue”

## Overall Interpretation

- The CSV now records **55 drill sessions**, up from the earlier 46-session report structure, and the broader activity total is **64 sessions** when the **9 PIR sessions** are included.
- The cohort continues to rate the sessions highly on GUOT: **91.3%** of numeric scores are **9 or 10**, with an average of **9.48**.
- The main developmental pattern remains a shift from reactive incident handling toward more deliberate sensemaking: understanding dependencies, using evidence, inspecting logs/change records, and avoiding default assumptions around recent changes or rollback.
- Coordination pressure is a recurring theme. Players repeatedly mention the need to involve the right people, know backup contacts, escalate sooner, and make decisions when senior people are unavailable.
- The surprise themes suggest the drills are producing useful complexity: participants encountered misleading signals, multi-causal situations, hidden dependencies, constrained team access, and technical root causes that were not obvious from change records alone.