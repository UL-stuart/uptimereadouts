# shreyarao-The-Switch-7719.csv

| Action | Timing | Grade | Evidence | Notes |
|---|---|---|---|---|
| Size Up | T+1 | ⚠️ | "@bob is there any issue noticed so far from customers perspective?"<br>"@tanya can we check the load performace for the platform?"<br>"Hello @bez , We are looking into this issue, so far the issue is not widespread amongst customers. will update you" | Asked about customer impact and probed scope; referenced multiple services. Lacked early explicit internal-user impact and a full scope summary to the team. |
| Team Coordination and Role Utilisation | T+2 | ✅ | "@shay can i get the list of chages that recently went through?"<br>"@tanya can we check the load performace for the platform?"<br>"@daniel can you help out Tanya to check out the spike in trafific?" | Engaged security, platform, engineering, and comms; assigned tasks and used inputs to progress the investigation. |
| Diagnose | T+9 | ⚠️ | "@maya Can you help us out here ? Seems like this is a network issue ? Can we please check?"<br>"it is a DDOS attack, fixing it imediately"<br>"We should go ahead with the failover then. Please proceed" | Prompted infra/network investigation and supported the switch-based diagnosis, but did not themselves synthesize findings into a clear root-cause narrative. |
| Decision Making Under Uncertainty | T+17 | ✅ | "@maya what does this mean in terms of downtime for the customers, or the impact overall?"<br>"@hamed is this a good idesa?"<br>"We should go ahead with the failover then. Please proceed" | Sought expert input on risk/impact and chose the lower-risk failover over a risky restart, maintaining progress. |
| Mitigation and Recovery Direction | T+19 | ✅ | "We should go ahead with the failover then. Please proceed"<br>"@shay cna you check the internet speed again?"<br>"@bob can you check if the customers are reporting normalcy?" | Directed bypass/failover, coordinated restoration, and requested verification of recovery. |
| Stakeholder Communication | T+5 | ✅ | "Hello @bez , We are looking into this issue, so far the issue is not widespread amongst customers. will update you"<br>"it is a DDOS attack, fixing it imediately"<br>"Issue is resolved, reports for slow browsing have gone down " | Proactive updates, progress, and resolution in the business channel; answered stakeholder questions. |

## Summary
- Strong coordination and clear decision-making under uncertainty; effectively chose failover after consulting experts.
- Good stakeholder communication cadence from initial notice to resolution.
- Improve early size-up by explicitly confirming internal-user impact and summarizing overall scope to the technical channel sooner.
- Consider articulating a concise root-cause synthesis to cement diagnosis before/after mitigation.
