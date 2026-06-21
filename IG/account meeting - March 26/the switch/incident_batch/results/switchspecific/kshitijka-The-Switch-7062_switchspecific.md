# kshitijka-The-Switch-7062.csv

| Action | Timing | Grade | Evidence | Notes |
|---|---|---|---|---|
| Size Up | T+5 | ⚠️ | "Bob are we seeing any customers complaints regarding the slowness"<br>"Daniel were you able to place the deal on website?"<br>"slowness while loading website for some P3" | Asked about customer and internal impact; summarized severity. Also queried global scope. Some inconsistency on sales updates reduced clarity. |
| Team Coordination and Role Utilisation | T+3 | ✅ | "sure Tanya please check it and get back in another 3 mins."<br>"Shay can you review this change CHG89462... Get back in another 2 min"<br>"Maya can we have this check from your end?" | Engaged SRE/engineering/security, assigned clear tasks with timeboxes, and leveraged inputs to progress. |
| Diagnose | T+3 | ⚠️ | "Tanya any anomalies found in the outbound traffic?"<br>"Maya any update from security checks?"<br>"Hamed S, can you please suggest here? The restart of switch did not work." | Drove infra/network-focused probing and accepted the switch diagnosis, but did not clearly synthesize symptoms to a single root cause. Context—Maya: "…infected network switch…" |
| Decision Making Under Uncertainty | T+13 | ⚠️ | "Maya what do you suggest as a resolution?"<br>"please proceed with restart" | Sought expert input but approved a risky restart without discussing consequences or alternatives; action worsened impact. |
| Mitigation and Recovery Direction | T+21 | ✅ | "Maya lets give it a try once"<br>"sure thing. Please update us once the solution is implemented."<br>"i am able to access the site now" | Supported bypass via backup switch, coordinated implementation and verification, and confirmed recovery with team and stakeholders. |
| Stakeholder Communication | T+5 | ⚠️ | "*Incident Number INC100078:* slowness while loading website for some P3"<br>"yes, the issue seems to be global"<br>"The site is back online." | Created incident, provided scope and resolution updates. One conflicting sales update reduced accuracy. |

## Summary
- Strengths: Clear coordination across roles; effective timeboxing; proactive verification and closure with both team and business.
- Gaps: Risk evaluation before disruptive actions; earlier articulation of a single shared root cause; ensure business updates are accurate and consistent.
