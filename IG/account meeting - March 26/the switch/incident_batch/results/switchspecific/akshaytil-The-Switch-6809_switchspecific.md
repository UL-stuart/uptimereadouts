# akshaytil-The-Switch-6809.csv

| Action | Timing | Grade | Evidence | Notes |
|---|---|---|---|---|
| Size Up | T+1 | ⚠️ | "Bob What is scope of impact and regions affected?"<br>"Summary: There is a spike in outbound connections ... the frontend and payments are hosted on"<br>"network issue sev3" | Good customer impact and multi-system scope; severity set. Did not explicitly probe internal user impact. |
| Team Coordination and Role Utilisation | T+3 | ✅ | "Shay, Daniel, Tanya check your recent changes, please."<br>"Maya can check from security pov"<br>"Tanya Can we bring in network team" | Engaged security, infra/network, and engineers with clear asks; drove work across roles. |
| Diagnose | T+5 | ✅ | "Tanya Can we bring in network team"<br>"Shay check from changes pov and Tanya please check from infra pov"<br>"Summary as now: Seems to an issue with \"The Switch\"" | Sought infra investigation, synthesized inputs, and supported switch as root cause. |
| Decision Making Under Uncertainty | T+18 | ⚠️ | "Can we fix immediately or we need time to fix this??"<br>"Cool, fingers crossed!!"<br>"Yes" | Sought expert input and ultimately approved safer failover, but initially endorsed restart without weighing risks. |
| Mitigation and Recovery Direction | T+23 | ✅ | "Yes"<br>"Summary as now: doing the failover to redundant switch - inProgress"<br>"Bob Can youu check any reports now?" | Approved failover (isolation), coordinated progress, and verified recovery with customers. |
| Stakeholder Communication | T+7 | ✅ | "Summar as of now: There is a spike in outbound connections ..."<br>"Bez team is working on pin pointing the issue, will keep you updated"<br)"Issue seems to be resolved" | Proactive, clear updates to business; maintained awareness through resolution. |

## Summary
- Strengths: Clear coordination across roles; rapid synthesis toward a network switch diagnosis; decisive approval of failover; strong, continuous stakeholder comms.
- Improvement: Ask explicitly about internal user impact early to complete size-up; evaluate and discuss risks before endorsing disruptive actions (e.g., restarts) to strengthen decision-making under uncertainty.
