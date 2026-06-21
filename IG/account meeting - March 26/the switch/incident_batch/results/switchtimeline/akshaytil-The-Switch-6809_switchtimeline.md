# akshaytil-The-Switch-6809.csv

| Milestone | Time | Evidence | Rationale |
|---|---|---|---|
| Issue Reproduction | – | – | No attempt by PLAYER to reproduce the website issue was observed after T₀. |
| Incident Raised | – | – | Incident numbers were posted by PLAYER, but per rule this must be raised by UptimeLabs; none found. |
| Checks Recent Changes | T+3 | "Shay, Daniel, Tanya check your recent changes, please." | PLAYER explicitly asked the team to review recent code changes. |
| First Business Comms | T+7 | "Summar as of now: There is a spike in outbound connections in the edge router and the origin IP block 10.50.0.0/24." | This is PLAYER’s first non-incident-number message in the business-comms channel. |
| Scope & Impact Sizing | T+1 | "Bob What is scope of impact and regions affected?" | PLAYER directly probed for scope and regional impact. |
| Network Layer Identification | T+6 | "There is a spike in outbound connections in the edge router and the origin IP block 10.50.0.0/24."<br>"Summary: There is a spike in outbound connections in the edge router and the origin IP block 10.50.0.0/24." | The team, then PLAYER, focused the investigation on the edge router/switch and the 10.50.0.0/24 block. |
| Security Breach Diagnosis | T+15 | "Found a critical issue. Our network switch was compromised due to unpatched vulnerabilities, leading to a BotNet creating DDOS attacks" | Maya confirmed an unpatched switch compromise causing botnet-driven outbound DDoS. |
| Intervention Decision: Restart Switch | – | – | Maya discussed a restart but never stated "Switch has been restarted." |
| Intervention Decision: Failover to Redundant Switch | T+18 | "Your right restarting the switch isnt the best option as it might intruduce some more issues"<br>"You're right. We need to stop that switch and bring up a redundant one" | Maya rejected restart and endorsed failover to the redundant switch. |
| Resolution | T+24 | "the infected switch has been successfully changed over" | Maya confirmed the switch failover completed, resolving the incident. |

## Summary
- Not detected: Issue Reproduction; Incident Raised (by UptimeLabs); Intervention Decision: Restart Switch.
- Gaps/ambiguities: PLAYER did not attempt to replicate the issue; incident creation was done by PLAYER rather than via /incident (UptimeLabs), so it doesn’t count for the milestone.
- Improvements: Use /incident to formally open incidents so they’re auto-tracked; quickly perform a basic end-user repro (e.g., place an order) to validate symptoms first-hand.
