# Combined switchspecific Evaluations

Generated from batch processing

---

# aashishku-The-Switch-8000.csv

| Action | Timing | Grade | Evidence | Notes |
|---|---|---|---|---|
| Size Up | T+5 | ⚠️ | "@bob have you observe any effect from business side ?"<br>"Looks to be 50% of users have slow load times but are able to make purchases with no issues. There is another 7% of users who cannot access the site at all, the reports for all isues are global"<br>"this is sevior issue , increasing the seviority of incident to SEV-1" | Established customer impact and summarized scope/severity; did not explicitly check internal user impact or distinguish systems |
| Team Coordination and Role Utilisation | T+4 | ✅ | "Hi @tanya, @hamed , @daniel we have a incident, could you pelase analyse and come back in 2mins"<br>"@shay could you please check the recent deployment change and discuss this with @daniel"<br>"@maya  could you please check any thing from the security side" | Engaged engineering, platform/security; assigned owners and timeboxes; referenced team findings to drive work |
| Diagnose | T+11 | ⚠️ | "@maya we have lot of huge traffice, could you please check any issue form network side"<br>"@daniel have mentioned this ---There is a spike in outbound connections in the edge router and the origin IP block 10.50.0.0/24... @Maya, could you pelase check it"<br>"We have an attack on our network, we are trying to use backup system"<br>[Maya] "Just ran a network security scan and our issues all seem to be related to our network switch" | Initiated infra/network investigation and leveraged findings; supported infra/switch cause via actions but did not explicitly articulate the switch as the single root cause |
| Decision Making Under Uncertainty | T+14 | ✅ | "@maya will restart affect other issue?"<br>"if not then please restart it @Maya"<br>"@maya , @hamed , can we switch back to backup now, then please do it immediately" | Sought expert input on risky restart, evaluated consequences, and chose a lower-risk path (failover) |
| Mitigation and Recovery Direction | T+18 | ✅ | "@maya , @hamed , can we switch back to backup now, then please do it immediately"<br>"@Bob, could you confirm the current situation"<br>"@shay , @tanya , @hamed , @daniel could you pelase check the network ping and logs if everythibg is correct?" | Directed isolation/bypass via backup switch, coordinated assistance, and verified recovery with stakeholders and team |
| Stakeholder Communication | T+3 | ✅ | "HI team, we are having a huge traffice, created a SEV-2 incident"<br>"We have an attack on our network, we are trying to use backup system"<br]"We have resolved the issue, network is good now" | Provided early, clear updates, escalated severity, and confirmed resolution in the business channel |

## Summary
- Strengths: Clear role-based tasking and timeboxing; proactive stakeholder updates; prudent risk assessment before disruptive actions; decisive mitigation with verification.
- Improvements: Ask explicitly about internal user/employee impact; more clearly synthesize and state root cause (e.g., “compromised core switch causing outbound spikes”).

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

# surajjajo-The-Switch-7446.csv

| Action | Timing | Grade | Evidence | Notes |
|---|---|---|---|---|
| Size Up | T+2 | ⚠️ | "@bob are any customers affected by this?"<br>"okay @bob how many reports are we talking about here?"<br>"okay so the impact is not that much right now but it's spreading"<br>Context: Bob: "Some customers are placing orders without issues, while others report long load times" | Promptly probed customer impact and scale; gave a scope summary. Did not explicitly ask about internal user impact or call out multiple user groups/systems. |
| Team Coordination and Role Utilisation | T+5 | ✅ | "@shay menawhile, can I please get a list of reent changes that went to PROD?"<br>"@shay @tanya can you guys check the logs and see if you see any major errors?"<br>"Could it be a BOS attack? @maya Can you please help us with this and check if there's any attack on the website?" | Engaged engineering/platform and security with clear asks; later escalated to @hamed and tasked @bob for banner, using inputs (e.g., outbound spike) to steer work. |
| Diagnose | T+13 | ⚠️ | "Could it be a BOS attack? @maya ... check if there's any attack on the website?"<br>"We are noticing a spike in outbound connections."<br>Context: Hamed: "Our network switch was compromised..." | Drove infra/security investigation and surfaced abnormal network behavior, but did not explicitly connect findings to the compromised switch as the singular root cause. |
| Decision Making Under Uncertainty | T+17 | ⚠️ | "@Maya can you please suggest the best option?"<br>"what are the actions required in that solution?"<br>"@hamed can you please help us with implementing this fix"<br>Context: Tanya: "Suggesting a switch restart"<br>Context: Maya: "restarting the switch isnt the best option" | Sought expert input and supported a lower‑risk failover over a risky restart; did not personally articulate risks/impacts of restart. |
| Mitigation and Recovery Direction | T+23 | ✅ | "@hamed can you please help us with implementing this fix"<br>"what are the actions required in that solution?"<br>"@bob do you see any improvements?"<br>Context: Hamed: "Preparing to bypass the infected switch" | Supported isolating/bypassing the infected switch, coordinated execution, and verified recovery with stakeholders. |
| Stakeholder Communication | T+5 | ✅ | "nope, only some of them"<br>"not yet, we are still identifying the issue"<br>"We are checking if there was any security breach" | Multiple timely updates in business channel; also guided customer messaging ("working on an immediate fix", ask for patience). Maintained awareness throughout. |

## Summary
- Strengths: Active coordination across roles; timely stakeholder updates; chose safer mitigation by deferring to expert judgment; verified recovery.
- Gaps: Did not explicitly assess internal user impact or clearly state multi‑group/system scope; limited synthesis of diagnostics into a single root cause; minimal explicit risk analysis of disruptive actions.
- Improve by: Asking directly about internal impact and affected services, summarizing scope explicitly; articulating risks/benefits of options before choosing; concluding root cause in your own words once confirmed.

---

# vivekdube-The-Switch-5643.csv

| Action | Timing | Grade | Evidence | Notes |
|---|---|---|---|---|
| Size Up | T+6 | ⚠️ | "how many users"<br>"Bob do we have any users complaining"<br>"so how come we are havingn issues in accessing and loading Youtube, git hub etx" | Asked about customer complaints and noted internal user impact; recognized multiple services. Lacked a clear scope/severity summary to the team. |
| Team Coordination and Role Utilisation | T+2 | ✅ | "Bob do we have any users complaining"<br>"Tanya can we check from the networkinng perspecitve pls"<br>"Shay can validate along with Bob telling us if he is still getting calls" | Engaged support, network, security; assigned validation and used inputs to progress. |
| Diagnose | T+11 | ✅ | "Tanya can we check from the networkinng perspecitve pls"<br>"We have idenntified that a security switch needs a critical patch..."<br>"I think we first need to know what we are investigating..." | Requested infra-focused investigation and then endorsed the switch as the cause using team findings. |
| Decision Making Under Uncertainty | T+10 | ✅ | "Certainly would help but someone should do the assessment"<br>"Whats are our alternatives.. swapping the switch"<br>"Yes if we are certain that it wont get affected" | Weighed restart risk, sought expert input, and backed a lower-risk path. |
| Mitigation and Recovery Direction | T+11 | ✅ | "Whats are our alternatives.. swapping the switch"<br>"how much time to swap Hamid"<br>"Shay can validate along with Bob telling us if he is still getting calls" | Directed bypass via backup switch, coordinated execution, and requested verification of recovery. |
| Stakeholder Communication | T+8 | ✅ | "*Incident Number INC10002:* P2... across the ethos system"<br>"We are working to identify... intermittent"<br>"We beleive that we have managed to work out the intermittent issues..." | Provided timely impact/status updates and closure to business stakeholders. |

## Summary
- Strong coordination, mitigation direction, and stakeholder comms drove quick recovery.
- Good risk-aware decision-making (avoiding risky restart).
- Improve by delivering an early, concise scope/severity summary to the technical team to solidify common understanding.

---

