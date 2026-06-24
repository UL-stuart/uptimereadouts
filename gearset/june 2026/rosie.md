# Rosie Miller - Drill 9497 Summary

Drill 9497 was the strongest Gearset cohort run because it was complete across the whole Snipe Hunt challenge, not because it dominated a single dimension. It scored 80.83%, the highest score in the Gearset cohort, with 3/3 across all five facets: misleading correlations, hidden coupling, reduced access to team, coordination bottlenecks, and data overload.

The key difference was that Rosie handled the scenario traps consistently. She treated the email maintenance timing as a plausible lead, but did not anchor on it; once the logs did not support DNS as the cause, she parked that theory and redirected the team toward PaymentService. That made the run stronger than many cohort runs that lost points on misleading correlations.

She also showed strong hidden-coupling reasoning. She asked what could change a week after a certificate rotation, connected that timing to expiry, and then noticed the certificate bundle-ordering note in the documentation before a restart could fail. That was one of the clearest reasons the run stood out: she did not just find the expired certificate, she caught the secondary dependency around how the certificate needed to be loaded.

Her incident-command pattern was also strong. She moved past unavailable approvers, weighed the cost of pulling Tanya out of a vendor session, escalated to Bez when the approval path was blocked, and then owned the restart call. Before acting, she checked consequences: the impact of losing the rollout window and whether there was a downside to restarting.

Compared with other high-scoring Gearset runs, 9497 edged ahead because it combined a perfect facet profile with a stronger marker profile around mindset, consequence-checking, and evidence-based narrowing. The main growth edge was communication inside the technical channel: Rosie mostly oriented the team through questions and directives, rather than explicit synthesis statements such as what had been ruled out and what the current working theory was. Even with that edge, the overall run was unusually balanced: good hypothesis discipline, good coupling detection, good escalation, and good business updates.

Note: the local generated score file lists 9497 as position 3 in the overall composite workbook table, while the requested framing says it was number 2 in the overall global list. The performance summary above focuses on the underlying behavioural evidence and cohort comparison.
