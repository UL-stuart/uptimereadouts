# avinashkr-The-Switch-7888.csv

| Action | Timing | Grade | Evidence | Notes |
|---|---|---|---|---|
| Size Up | T+1 | ✅ | "@daniel Do you see a ny ossues while trying to place the order ?" <br> "Nothing major that have been reported, except afew netwoek issues which identified internally." <br> "upgrade the INC priority to Sev2 as its impacted the order placing" | Asked about customer impact and internal users; recognized broad impact and set severity appropriately |
| Team Coordination and Role Utilisation | T+1 | ✅ | "@daniel Do you see a ny ossues while trying to place the order ?" <br> "Hey @maya We have a situation with spike in traffic, could you please check" <br> "@bob May be better to put a banner on the page regarding the slowness in the application" | Engaged engineering, security, infra and business; assigned clear tasks and followed up |
| Diagnose | T+4 | ✅ | "Hey @tanya Are you seeing anything from the logs, seems we have slow network" <br> "ALso any update on this what posted by Hameed \" we've seen some weird traffic from our data centre network\" ?" <br> "We just figured out some issues withoin out netwoek switches and team working on that" | Drove network-focused investigation and adopted the switch-compromise finding as the unifying cause |
| Decision Making Under Uncertainty | T+16 | ✅ | "@maya Do we have an alternative switch to divert the traffic ?" <br> "@hamed Is there any reduntancy for this switch ?" <br> "@hamed Hope that failover will not create any outage" | Sought safer alternatives, consulted infra, and weighed outage risk before proceeding |
| Mitigation and Recovery Direction | T+19 | ✅ | "Can we move the traffic to the alternative Switch if that helps ?" <br> "Team working on failing over the affected switch to another one" <br> "@maya are you seeing any changes in the logs now ?" | Directed failover/bypass, asked to remove the infected switch, and verified recovery with multiple teams |
| Stakeholder Communication | T+5 | ✅ | "Nothing major that have been reported, except afew netwoek issues which identified internally." <br> "We have enaged the Cyber team to check further on their side" <br> "The failover comepleted and there are no issues observed so far" | Provided timely business updates on impact, actions, and resolution; maintained awareness throughout |

## Summary
- Strong coordination across security, infra, and business; clear tasking and follow-through.
- Good sizing-up progression: confirmed customer impact, noted internal effects, set Sev2, and reported scope.
- Sound risk management: avoided risky restart, pursued failover, and validated recovery.
- Improvement: Avoid definitive public statements on cause ("not an attack") before confirmation; keep customer comms neutral and factual.
