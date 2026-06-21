# harshagar-The-Switch-7272.csv

| Action | Timing | Grade | Evidence | Notes |
|---|---|---|---|---|
| Size Up | T+7 | ✅ | "are you getting any issues from clients as well regarding this?"<br>"are you guys experiencing same things.. for me also it sworking fine"<br>"seems to be a global issue" | Asked about both customer and internal impact, recognised global scope, and signalled severity via scope and rising complaints |
| Team Coordination and Role Utilisation | T+7 | ✅ | "can you check if logs are fine from app side"<br>"@Tanya: its not looks like app issue"<br>"can you please check from network side" | Engaged dev/app, platform/network, security; reassigned focus using inputs and coordinated multiple roles |
| Diagnose | T+15 | ✅ | "can you please check from network side"<br>"its not looks like app issue"<br>"issues all seem to be related to our network switch"<br>Context: daniel: "Logs are filled with timeouts at the network layer, not in the app layer" | Drove investigation beyond app, interpreted findings, and supported switch/network as the source |
| Decision Making Under Uncertainty | T+21 | ✅ | "any impact ?"<br>"@hamed : any suggestion from your side"<br>"please proceed" | Questioned risks of a restart, sought expert input, and backed a lower-risk failover path |
| Mitigation and Recovery Direction | T+21 | ✅ | "please proceed"<br>"@Bob: now can you help us with the reports"<br>"its resolved now" | Supported isolating the faulty switch via failover, coordinated verification, and confirmed recovery |
| Stakeholder Communication | T+6 | ✅ | "yes @bez we are on it"<br>"its basically creates a DDOS (Distributed Denial of Service) to attack an external party"<br>"its resolved now" | Gave timely business updates on status, impact, and resolution |

## Summary
- Strengths: Prompt sizing-up across internal and customer impact; clear multi-role coordination; prudent decision-making that avoided risky restart; strong stakeholder updates through to resolution.
- Improvement: Provide a single concise situation summary earlier (scope, cause hypothesis, customer impact, next steps) to reduce back-and-forth across channels.
