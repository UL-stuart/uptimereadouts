# melvinvar-The-Switch-5749.csv

| Action | Timing | Grade | Evidence | Notes |
|---|---|---|---|---|
| Size Up | T+7 | ✅ | "Hi Bob, did we hear any issues from users?"<br>"Team, when did u start facing slowness?"<br>"What we know so far, this is not a global issue but specific to payments and frontend IP ranges" | Covered customer and internal impact, scoped to multiple systems; also set SEV2 in business comms at T+3 |
| Team Coordination and Role Utilisation | T+4 | ✅ | "Tanya please review your last changes along with Daniel, to see for any potential impacts"<br>"Maya please assist the team to understand the reason for outvbound connection spike"<br>"Hamed S \\/Tanya could you try that?" | Engaged engineering, security, and platform with clear asks and follow-through |
| Diagnose | T+12 | ✅ | "We know that there is a spike in outbound connections as reported by Tanya"<br>"Maya please assist the team to understand the reason for outvbound connection spike"<br>"Our understanding so far, Issue with network switch (must be hardware issue)..."<br>[Maya]: "Security scan shows issues related to our network switch."<br>[Hamed]: "the network switch was compromised due to unpatched vulnerabilities" | Drove infra/network-focused investigation and supported switch as the cause; minor early mislabel as hardware |
| Decision Making Under Uncertainty | T+14 | ⚠️ | "Hamed S please share your thoughts on how to address this?"<br>"Maya how to remove the botnet from netweok"<br>"Hamed S \\/Tanya could you try that?"<br>[Maya]: "Suggesting a switch restart. Though I'm not sure"<br>[Hamed]: "Restart isn't advisable" | Sought expert input and avoided risky restart; limited explicit discussion of risks before choosing failover |
| Mitigation and Recovery Direction | T+18 | ✅ | "Hamed S \\/Tanya could you try that?"<br>"Bob please inform clients about this downtime"<br>"Team, do u still face network slowness" | Directed failover to redundant switch, coordinated comms, and verified recovery |
| Stakeholder Communication | T+3 | ✅ | "*Incident Number INC100069:* network slowness and timeouts SEV2"<br>"There had been a spike on network outbound connections, investigating further"<br>"Bez we are moving to a redundant switch" | Provided early, frequent updates, time-boxed next steps, and confirmed resolution |

## Summary
- Strengths: Rapid size-up, strong cross-functional coordination, decisive mitigation with verification, and clear stakeholder updates.
- Improvement: Make risk trade-offs explicit when considering disruptive actions (e.g., articulate potential blast radius/rollback) before choosing the path forward.
