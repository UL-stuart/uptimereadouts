# anjalisha-The-Switch-7569.csv

| Action | Timing | Grade | Evidence | Notes |
|---|---|---|---|---|
| Size Up | T+8 | ✅ | "Is everyone facing slow connections?"<br>"@bob any reports from customers?"<br>"Some customers are placing orders without issues, while others report long load times" | Timing anchored to first stakeholder summary; earlier asked about internal users (T+1) and customers (T+6). |
| Team Coordination and Role Utilisation | T+6 | ✅ | "can @daniel and @tanya check if it is change related?"<br>"@maya can you heck the traffic and its legitimacy"<br>"@tanya @hamed please help @maya to get this sorted out" | Engaged platform, security, and network; assigned tasks and used inputs to progress. |
| Diagnose | T+17 | ✅ | "@maya can you heck the traffic and its legitimacy"<br>"We have identified the issue: Our network switch was compromised due to unpatched vulnerabilities, leading to a BotNet creating DDOS attacks" | Requested infra/network investigation and then supported and communicated the switch-compromise root cause. |
| Decision Making Under Uncertainty | T+18 | ⚠️ | "@maya any impact of restarting?"<br>"@hamed are we okay with the downtime?"<br>"@maya please go ahead and restart" | Considered risks and consulted experts, but chose a risky restart that worsened impact; later pivoted to failover. |
| Mitigation and Recovery Direction | T+22 | ✅ | "please do so"<br>"please try using the redundance switch"<br>"can someone confirm?" | [Context–Tanya]: "We could failover to the redundant switch"<br>[Context–Maya]: "the infected switch has been successfully changed over" |
| Stakeholder Communication | T+8 | ✅ | "we have experienced long load times, we are still investigating the cause"<br>"We have identified the issue: Our network switch was compromised..."<br>"this worked, site is back up" | Provided timely impact, cause, next steps, and resolution in business-comms. |

## Summary
- Strengths: Proactive size-up across internal and customer impact; strong team coordination; clear stakeholder updates; decisive pivot to failover and verification after restart failed.
- Improvement: When warned of high restart risk, prefer lower-impact mitigations first (e.g., immediate failover/bypass), then validate before taking disruptive actions.
