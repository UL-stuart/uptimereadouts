# aashishku-The-Switch-8000.csv

| Milestone | Time | Evidence | Rationale |
|---|---|---|---|
| Issue Reproduction | – | – | No explicit attempt by PLAYER to reproduce the issue on the website; another teammate (daniel) did so. |
| Incident Raised | T+2 | "*Incident Number INC100072:* SEV-2 huge traffic" | UptimeLabs created the incident record with an incident number. |
| Checks Recent Changes | T+5 | "could anyone let us know the recent deployment?"<br>"@shay could you please check the recent deployment change and discuss this with @daniel" | PLAYER proactively requested recent change info and assigned follow-up. |
| First Business Comms | T+3 | "HI team, we are having a huge traffice, created a SEV-2 incident" | First non-system message by PLAYER in business-comms after T₀. |
| Scope & Impact Sizing | T+5 | "@bob have you observe any effect from business side ?"<br>"Looks to be 50% of users have slow load times... 7% ... cannot access the site at all" | PLAYER sought and communicated impact details to size scope. |
| Network Layer Identification | T+7 | "There is a spike in outbound connections in the edge router and the origin IP block 10.50.0.0/24."<br>"@Maya, could you pelase check it" | Daniel’s observation shifted focus to edge networking; PLAYER amplified it to security. |
| Security Breach Diagnosis | T+14 | "Just ran a network security scan..."<br>"Our investigation uncovered a critical issue: the network switch was compromised... BotNet... DDOS"<br>"network switch had unpatched vulnerabilities..." | Maya ran scans and, with team input, identified an unpatched, compromised switch consistent with botnet-driven outbound DDoS. |
| Intervention Decision: Restart Switch | – | – | Maya did not report executing a restart; she instead advised against restarting. |
| Intervention Decision: Failover to Redundant Switch | T+15 | "Your right restarting the switch isnt the best option as it might intruduce some more issues" | This marked the decision to avoid restart and proceed toward failover. Follow-on messages confirm choosing the backup switch. |
| Resolution | T+19 | "the infected switch has been successfully changed over" | Maya confirmed the switch changeover, indicating resolution. |

## Summary
- Not detected: Issue Reproduction, Intervention Decision: Restart Switch
- Notable gaps: PLAYER did not attempt hands-on reproduction; network-layer identification originated from Daniel, though PLAYER relayed it to security.
- Improvement insights: PLAYER should quickly reproduce customer symptoms to validate impact; explicitly timestamp and confirm decisions (e.g., failover initiation) in business-comms for clearer auditability.
