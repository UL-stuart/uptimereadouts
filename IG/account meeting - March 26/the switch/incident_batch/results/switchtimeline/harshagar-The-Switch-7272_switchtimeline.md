# harshagar-The-Switch-7272.csv

| Milestone | Time | Evidence | Rationale |
|---|---|---|---|
| Issue Reproduction | T+2 | "Platform seems to be working correctly"<br>"for me also it sworking fine" | PLAYER reported results from trying the platform, implying a direct reproduction attempt. This is the earliest post-T₀ indication that they tested the site. |
| Incident Raised | T+5 | "*Incident Number INC100031:* sev2 issues with site loading" | uptimelabs created an incident record with an incident number, satisfying the criterion. |
| Checks Recent Changes | T+10 | "LOOKS LIKE THE DEPLOYMENT IS 24 hrs ago" | PLAYER explicitly referenced the timing of recent deployments, indicating a check of recent changes. |
| First Business Comms | T+6 | "yes @bez we are on it" | This is PLAYER’s first non-incident-number message in the business-comms channel after T₀. |
| Scope & Impact Sizing | T+3 | "are you getting any issues from clients"<br>"@bob : is it specific to a region or global?"<br>"seems to be a global issue" | PLAYER probed customer impact and geographic scope, then summarized impact as global. |
| Network Layer Identification | T+9 | "There is a spike in outbound connections in the edge router and the origin IP block 10.50.0.0/24."<br>"I'm looking at Tanya's message about spike in outbound connections" | The team explicitly identified abnormal outbound traffic on the edge router in the 10.50.0.0/24 block, shifting focus to network gear. |
| Security Breach Diagnosis | T+16 | "the network switch was compromised due to unpatched vulnerabilities"<br>"We have identified a BotNet in the switch" | Maya diagnosed an unpatched, compromised switch and a botnet causing outbound DDoS activity. |
| Intervention Decision: Restart Switch | – |  | No message from Maya indicating a restart was performed; the team decided against restarting. |
| Intervention Decision: Failover to Redundant Switch | T+19 | "Your right restarting the switch isnt the best option as it might intruduce some more issues"<br>"ok working on this now" | Maya rejected restart and proceeded toward the alternative, implying failover to the redundant switch. |
| Resolution | T+21 | "the infected switch has been successfully changed over" | Maya confirmed successful changeover to the redundant switch, indicating resolution. |

## Summary
- Not detected: Intervention Decision: Restart Switch
- Gaps/ambiguities: PLAYER’s reproduction lacked explicit steps; recent-change check came later than initial impact scoping; network-layer shift was initiated by Tanya, with PLAYER coordinating rather than leading that discovery.
- Improvement insights: When reproducing, state explicit steps and outcomes; ask for or link the changelog earlier to quickly rule in/out recent changes.
