# kshitijka-The-Switch-7062.csv

| Milestone | Time | Evidence | Rationale |
|---|---|---|---|
| Issue Reproduction | T+1 | "I will try placing order in website as well"<br>"no lag while placing the orders" | PLAYER explicitly attempted to replicate the issue on the website. The first attempt occurred within a minute of T₀. |
| Incident Raised | – | – | No incident record posted by uptimelabs; incident numbers were posted by PLAYER instead. |
| Checks Recent Changes | T+4 | "Shay can you provide me the list of changes that has gone throught in last two weeks"<br>"Shay can you review this change *CHG89462." | PLAYER proactively requested recent change details and asked for a specific change to be reviewed. |
| First Business Comms | T+7 | "yes, the issue seems to be global" | This is PLAYER’s first non-incident-number message in business-comms after T₀. |
| Scope & Impact Sizing | T+2 | "Bob are we seeing any customers complaints regarding the slowness"<br>"Bob are the reports comings from all over globe or any particular region" | PLAYER sought to quantify impact (complaints) and scope (global vs regional). |
| Network Layer Identification | T+7 | "There is a spike in outbound connections in the edge router and the origin ip block 10.50.0.0/24." | Team identified abnormal activity on the edge router tied to 10.50.0.0/24, focusing the investigation at the network layer. |
| Security Breach Diagnosis | T+12 | "identified unpatched vulnerabilities exploited by attackers"<br>"the network security scan revealed an infected network switch" | Maya confirmed an unpatched, infected switch consistent with a security compromise. |
| Intervention Decision: Restart Switch | T+13 | "switch has been restarted" | Maya confirmed the restart intervention was executed. |
| Intervention Decision: Failover to Redundant Switch | T+21 | "I have a solution I've identified a back-up switch"<br>"redirect through the backup switch, bypassing the infected switch." | Maya proposed and initiated failover via a backup switch, superseding the restart approach. |
| Resolution | T+22 | "the infected switch has been successfully changed over" | Maya confirmed the switchover completion, indicating resolution. |

## Summary
- Not detected: Incident Raised (by uptimelabs)

- Gaps/Ambiguities: Conflicting business updates ("No Decline in sales" vs. reports of decline) created mixed signals; initial restart increased user-facing errors before failover was chosen.

- Improvements: Use the /incident command early so the incident is formally raised by uptimelabs; validate stakeholder metrics with owners before posting to business-comms to avoid contradictions.
