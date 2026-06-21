# melvinvar-The-Switch-5749.csv

| Milestone | Time | Evidence | Rationale |
|---|---|---|---|
| Issue Reproduction | – | – | No evidence that PLAYER personally attempted to reproduce the issue on the website or perform an order. |
| Incident Raised | – | – | No UptimeLabs-created incident record found; the incident number was posted by PLAYER, which does not satisfy the restriction. |
| Checks Recent Changes | T+4 | "Team, please share the recent changes that could cause network slowness?" | PLAYER explicitly requested recent change details to assess potential causes. |
| First Business Comms | T+3 | "network slowness and timeouts SEV2" | This is the first non-incident-number message by PLAYER in the business-comms channel. |
| Scope & Impact Sizing | T+1 | "Hi Bob, did we hear any issues from users?"<br>"Team, when did u start facing slowness?"<br>"What we know so far, this is not a global issue but specific to payments and frontend IP ranges" | PLAYER investigated user impact and onset time, later articulating a narrowed scope. |
| Network Layer Identification | T+11 | "Noticing a spike in outbound connections. The IP range affected is the same as our frontend and payments"<br>"Security scan shows issues related to our network switch." | After spikes were observed, the investigation focused on the network switch, indicating a shift to the network layer. |
| Security Breach Diagnosis | T+12 | "Found a critical issue. Our network switch was compromised due to unpatched vulnerabilities, leading to a BotNet creating DDOS attacks." | Maya confirmed an unpatched switch compromised by a botnet performing outbound DDoS. |
| Intervention Decision: Restart Switch | – | – | Maya discussed a restart as a possibility but did not state that the switch was restarted. |
| Intervention Decision: Failover to Redundant Switch | T+15 | "Your right restarting the switch isnt the best option as it might intruduce some more issues" | Maya rejected restart, aligning the team toward failover to a redundant switch. |
| Resolution | T+19 | "the infected switch has been successfully changed over" | Maya confirmed successful changeover to the redundant switch, indicating resolution. |

## Summary
- Not detected: Issue Reproduction, Incident Raised, Intervention Decision: Restart Switch
- Ambiguities/gaps: Incident creation was performed by PLAYER rather than UptimeLabs (process mismatch); network IP block (10.50.0.0/24) was not explicitly referenced though the shift to the switch was clear; an early business reply suggested possible data loss before confirmation, which could confuse stakeholders.
- Improvements: PLAYER should perform a quick end-to-end reproduction early; ensure the designated system (UptimeLabs) opens the incident record and maintain strictly verified statements in business communications.
