# 2026 Drill Usage Summary

**Source:** `usage_2026.csv`  
**Coverage:** 12 Jan 2026 to 11 Jun 2026  
**Note on drill grouping:** drill names are grouped after removing a trailing `Workshop` suffix and normalising whitespace. For example, `Discount Disaster` and `Discount Disaster Workshop` are treated as the same drill. Raw names are preserved in the mapping table below.

## Executive Summary

| Metric | Value |
| --- | --- |
| Total sessions | 46 |
| Players represented | 10 |
| Different drills, exact raw `name` values | 17 |
| Different drills, grouped similar names | 16 |
| Valid GUOT scores | 46 |
| Blank / non-numeric GUOT values ignored | 0 |
| Average GUOT | 9.48 |
| Median GUOT | 10 |

## 1. Number of Sessions

There are **46 sessions** in the file.

## 2. Sessions by Player

| Player | Sessions |
| --- | --- |
| chris.watts | 10 |
| swetha.nayudu | 8 |
| vallabh.vyas | 5 |
| pradeep.c | 5 |
| vaishnavi.b | 5 |
| praveen.sadul | 5 |
| latif.khan | 4 |
| ramesh.matta | 2 |
| ranjan.padhi | 1 |
| gowthamkumar.b | 1 |

## 3. GUOT Scores

GUOT calculations ignore blanks and non-numeric values. In this file, all 46 rows have numeric GUOT scores.

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
| swetha.nayudu | 8 | 8 | 9.62 | 10 | 8: 1, 9: 1, 10: 6 |
| pradeep.c | 5 | 5 | 10.00 | 10 | 10: 5 |
| praveen.sadul | 5 | 5 | 8.80 | 9 | 8: 1, 9: 4 |
| vaishnavi.b | 5 | 5 | 10.00 | 10 | 10: 5 |
| vallabh.vyas | 5 | 5 | 9.60 | 10 | 9: 2, 10: 3 |
| latif.khan | 4 | 4 | 9.00 | 9 | 9: 4 |
| ramesh.matta | 2 | 2 | 9.00 | 9 | 8: 1, 10: 1 |
| gowthamkumar.b | 1 | 1 | 10.00 | 10 | 10: 1 |
| ranjan.padhi | 1 | 1 | 10.00 | 10 | 10: 1 |

## 4. Different Drills

There are **16 grouped drills** after treating similar names as the same drill. There are **17 exact raw `name` values** before grouping.

### Sessions by Grouped Drill

| Grouped drill | Sessions |
| --- | --- |
| Snipe Hunt | 7 |
| The Chain | 6 |
| Version confusion | 6 |
| The Switch | 5 |
| Cart-astrophe | 4 |
| Details Matter | 3 |
| The Big Investor | 2 |
| Bezs Beatles Day! | 2 |
| Discount Disaster | 2 |
| The Unknown Unknown | 2 |
| Roblox | 2 |
| Rumours | 1 |
| Missing Delivery | 1 |
| Radio Silence | 1 |
| Once Upon A Time In Production | 1 |
| Tech Beatles Day! | 1 |

### Drill Name Grouping Map

| Grouped drill | Raw name values included | Sessions |
| --- | --- | --- |
| Bezs Beatles Day! | Bezs Beatles Day! | 2 |
| Cart-astrophe | Cart-astrophe | 4 |
| Details Matter | Details Matter | 3 |
| Discount Disaster | Discount Disaster, Discount Disaster Workshop | 2 |
| Missing Delivery | Missing Delivery | 1 |
| Once Upon A Time In Production | Once Upon A Time In Production | 1 |
| Radio Silence | Radio Silence | 1 |
| Roblox | Roblox Workshop | 2 |
| Rumours | Rumours | 1 |
| Snipe Hunt | Snipe Hunt | 7 |
| Tech Beatles Day! | Tech Beatles Day! | 1 |
| The Big Investor | The Big Investor Workshop | 2 |
| The Chain | The Chain Workshop | 6 |
| The Switch | The Switch | 5 |
| The Unknown Unknown | The Unknown Unknown | 2 |
| Version confusion | Version confusion | 6 |

## 5. Themes from `what_to_take_into_next_incident`

### Understand dependencies and system coupling before acting

- Several respondents said they need to understand service dependencies, interdependent changes, backup systems, and broader technical context before choosing a fix.
- Example quotes:
  - “We need to understand the dependencies of the services.”
  - “I think I rushed for rollback for the 1st change rather getting all the details ad rolling back interdependent changes first ..”
  - “Engage people and think in broader view not specific to default things like recent deployments”

### Bring the right people in quickly, including backup owners

- A strong theme was faster engagement of the right people, knowing backup contacts, and involving all relevant teams rather than relying only on the obvious group.
- Example quotes:
  - “Reach out to right people”
  - “I should look for the backup person if someone is not around.”
  - “we need to understand the team availability, and need to know backup person.”

### Use evidence, logs, metrics, and change records more deliberately

- Participants repeatedly identified a need to gather concrete information, compare current metrics, refer to change registers, and inspect logs more deeply.
- Example quotes:
  - “We should gather the all the information and compare with todays metrics”
  - “learned to ensure all parties are involved and always refer to Change register”
  - “check each metrics in more details. communicate to customer and vendors about the impact”

### Stronger command, escalation, and decision-making under uncertainty

- Reflections emphasised taking command, escalating sooner, changing severity when appropriate, and making decisions when senior guidance is unavailable.
- Example quotes:
  - “Taking a command and directing team to one solution.”
  - “taking decisions when no one around to guide”
  - “Escalating quicker for help”

### Communicate, coordinate, and keep pressure on participation

- Several comments highlighted communication, collaboration, forcing engagement when people are busy, and using experts rather than trying to solve everything alone.
- Example quotes:
  - “I learned how to communicate and check the issue.”
  - “That you need to force people to join in and resolve issues, they wont always be willing or be busy doing other things”
  - “Good communication, using the team sufficiently instead of digging through logs and changes myself.”

### Think beyond standard rollback / obvious-change responses

- Participants noted that the obvious fix or recent change was not always the answer, and that they need to avoid jumping too quickly to rollback or default actions.
- Example quotes:
  - “Need to analyze more and look for concrete information”
  - “What we saw is not right all the time. We need detailed investigation before take actions”
  - “Have to keep asking questions to get something that will pinpoint the issue”

## 6. Themes from `what_was_surprising`

### Incidents were more complex, non-linear, or multi-causal than expected

- Many respondents were surprised by complexity, multiple simultaneous issues, and first fixes revealing further problems.
- Example quotes:
  - “I found it quite taxing and was not expecting it to be that complex”
  - “I had decisions to make and it was very stressful, It wasnt linear”
  - “I like that it ended up being two issues, the first solution identified a second so had to be attacked on two fronts.”

### Obvious causes and recent changes were often misleading

- Participants were surprised that the apparent cause was often not the real cause, including cases where changes looked normal or unrelated.
- Example quotes:
  - “Its not related to any change.”
  - “Dev mentioned some test script might have impacted which was not the case.”
  - “All the things we had was normal, we could not identify the cause.”

### Team availability and coordination constraints were a major stressor

- Unavailable people, busy colleagues, and unclear backup ownership stood out as unexpected operational challenges.
- Example quotes:
  - “How to handle situation when senior people are not around”
  - “I wasnt expecting people to be unavailable. Had to call in people from engagements and depustize. I also had to be a change authority.”
  - “I was surprises tanya was busy and hamed out off office”

### Scope and impact changed in unexpected ways

- Several comments noted surprises around incidents starting small, becoming global, affecting only certain users/currencies, or having business impact despite limited technical scope.
- Example quotes:
  - “incident which is with region specific and later it became global it was some of panic situation.”
  - “only few currency has problem. while overall website was performing well and customer were able to place order”
  - “its affected limited users but its impact the business. looks like version mismatch , older version users are not facing an issue”

### Backups, failover, and environments behaved unexpectedly

- Backup capacity, UAT refreshes, and failover assumptions emerged as repeated sources of surprise.
- Example quotes:
  - “UAT DB back up was not expected ..”
  - “That back up system PCS wasnt tested to  the capacity that it can handle the live traffic.. which is key for the systems”
  - “UAT data refresh - as mostly engineers are confident that they won't mess up with env's.”

### Technical root causes were harder to isolate than expected

- Participants were surprised by hidden technical details such as certificates, DNS/network ambiguity, browser versions, and issues not visible in change requests.
- Example quotes:
  - “Certificate chages”
  - “DNS and network looks good but still issue couldn't resolve”
  - “Challenging drill as nothing in change request to able isolate issue”

## Overall Interpretation

- The cohort rates the sessions very highly on GUOT: **91.3%** of numeric scores are **9 or 10**, with an average of **9.48**.
- The main developmental pattern is shifting from reactive incident handling toward more deliberate sensemaking: understand dependencies, gather evidence, use logs/change records, and avoid defaulting too quickly to recent changes or rollback.
- Coordination pressure is a recurring theme. Players repeatedly mention the need to involve the right people, know backup contacts, escalate sooner, and make decisions when senior people are unavailable.
- The surprises suggest the drills are working as intended: participants frequently encountered non-linear, multi-causal, or misleading scenarios that challenged assumptions about obvious causes, backups, environments, and team availability.