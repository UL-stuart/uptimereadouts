# vivekdube-The-Switch-5643.csv

| Milestone | Time | Evidence | Rationale |
|---|---|---|---|
| Issue Reproduction | T+2 | "I just placed on order looks good to me" | PLAYER explicitly attempted to place an order to replicate the issue. This satisfies the reproduction milestone. |
| Incident Raised | – | – | No incident record was raised by UptimeLabs; the incident number was posted by PLAYER instead. Per restriction, only an UptimeLabs-created record qualifies. |
| Checks Recent Changes | – | – | PLAYER did not ask about recent deployments, changelogs, or code changes. No semantic equivalent was found. |
| First Business Comms | T+8 | "P2-- an issue where we have found that intermittently we have network issues across the ethos system" | This is the first non-incident-number message by PLAYER in the business-comms channel. It communicates initial status and priority to the business. |
| Scope & Impact Sizing | T+2 | "ok i sthis happening in a particular time of the day"<br>"how many users"<br>"Bob do we have any users complaining" | PLAYER probed time patterns, user counts, and complaints to size scope and impact. These are classic impact validation questions. |
| Network Layer Identification | T+6 | "spike in outbound connections in the edge router"<br>"ip block 10.50.0.0/24" | The investigation pivoted to the network layer after the edge router and 10.50.0.0/24 spike were called out. This shifted focus toward router/switch analysis. |
| Security Breach Diagnosis | T+7 | "the network switch was compromised due to unpatched vulnerabilities"<br>"identified a BotNet ... creates a DDOS" | Maya confirmed an unpatched switch compromised by a botnet conducting outbound DDoS, satisfying the diagnosis milestone. |
| Intervention Decision: Restart Switch | – | – | Maya discussed a potential restart but did not perform or announce a restart. The required confirmation line is absent. |
| Intervention Decision: Failover to Redundant Switch | T+11 | "Your right restarting the switch isnt the best option as it might intruduce some more issues"<br>"Shall we migrate the traffic to back up switch" | Maya rejected restart and proposed migration to a backup switch, indicating a failover decision. |
| Resolution | T+14 | "the infected switch has been successfully changed over" | Maya explicitly confirmed the changeover to the backup switch, signaling resolution. |

## Summary
- Not detected milestones: Incident Raised, Checks Recent Changes, Intervention Decision: Restart Switch
- Gaps/ambiguities: No UptimeLabs-created incident record; PLAYER did not inquire about recent deployments; some early uncertainty about outbound vs inbound delayed a decisive network pivot by PLAYER even after the edge-router spike surfaced.
- Improvements: Use the official incident bot/workflow to open the record promptly; add a standard “recent changes” check early to rapidly rule in/out change-related causes.
