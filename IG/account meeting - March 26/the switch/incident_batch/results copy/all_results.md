# Combined RADAR Evaluations

Generated from batch processing

---

# aashishku-The-Switch-8000.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | "HI team, we are having a huge traffice, created a SEV-2 incident"; "this is sevior issue , increasing the seviority of incident to SEV-1"; "We have resolved the issue, network is good now"; [uptimelabs] "Incident Number INC100072: SEV-2 huge traffic" | Record auto-created by uptimelabs; PLAYER raised/updated severity; closure declared after restoration signals. |
| External Comms | 3 | "HI team, we are having a huge traffice, created a SEV-2 incident"; "Looks to be 50% of users have slow load times... another 7%... global"; "We have an attack on our network, we are trying to use backup system" | Mostly reactive; no cadence/ETAs; unstructured; no customer comms strategy noted. |
| Internal Comms | 5 | "Hi @tanya, @hamed , @daniel... analyse and come back in 2mins"; "@shay could you please check the recent deployment change and discuss this with @daniel"; "@maya , @hamed , can we switch back to backup now, then please do it immediately" | Recruited by name, timeboxed, delegated, sought advice, and coordinated cross-checks calmly. |
| Identify Scope | 4 | "@bob have you observe any effect from business side ?"; "@hamed , @shay , @tanya what do you think at which service, website is failing"; "Looks to be 50%... 7%... the reports for all isues are global" | Determined global impact and affected experience; leveraged logs/changes via team; limited self-replication. |
| Commanding the Incident | 5 | "Hi @tanya, @hamed , @daniel... come back in 2mins"; "this is sevior issue , increasing the seviority of incident to SEV-1"; "@maya , @hamed , can we switch back to backup now, then please do it immediately" | Clear leadership and decisions; prioritized restoration over RCA; confident, directive, evidence-seeking. |

---

# akshaytil-The-Switch-6809.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | "*Incident Number INC100046:* network issue sev3"; "network issue  - to - the switch issue sev2"; "Issue seems to be resolved"; [Maya]: "the infected switch has been successfully changed over" | Incident record created with severity; severity raised; closure declared after restoration evidence. |
| External Comms | 4 | "Summary as of now: Our investigation uncovered a critical issue: the network switch was compromised..."; "Bez team is working on pin pointing the issue, will keep you updated"; "130+ reports and this spike has started 2 weeks back" | Frequent updates in business-comms; no explicit cadence or structured template; also guided customer messaging internally. |
| Internal Comms | 5 | "Shay, Daniel, Tanya check your recent changes, please."; "Maya can check from security pov"; "Hamed S Can you please provide a hand here!" | Recruited by name, delegated clearly, sought signals and cross-checks; calm/polite; no explicit timeboxing. |
| Identify Scope | 5 | "Bob What is scope of impact and regions affected?"; "Bob how many reports so for?"; "Summary: There is a spike in outbound connections in the edge router and the origin IP block 10.50.0.0/24." | Drove scoping (global vs regional), quantified impact via reports, articulated concrete symptoms; relied on team for replication. |
| Commanding the Incident | 5 | "Tanya Can we bring in network team"; "Shay check from changes pov and Tanya please check from infra pov"; "increasing the sev level to 2"; [Hamed]: "shall we do the failover to redundant switch ?" → "Yes" | Acted as de facto IC, made clear decisions (severity raise, failover approval), prioritized restoration over RCA, confident direction. |

---

# anjalisha-The-Switch-7569.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | [context] "*Incident Number INC100067:* SEV3 reports of long load times"; "this worked, site is back up"; "the incident is resolved" | Record+SEV by uptimelabs at T+13; PLAYER declared restoration and closure after bypass success (T+31). |
| External Comms | 4 | "we have experienced long load times, we are still investigating the cause"; "we are working to notify the users via banners"; "we have identified a redundant switch, trying to bypass the infected switch and use the other one" | Proactive, frequent, and customer-focused updates; no explicit cadence or structured template. |
| Internal Comms | 4 | "Is everyone facing slow connections?"; "@maya can you heck the traffic and its legitimacy"; "@maya please go ahead and restart" | Recruited responders by name, delegated, asked for signals, approved actions; no explicit timeboxing. |
| Identify Scope | 4 | "@bob any reports from customers?"; "i tried placing an order it is working for me"; "Sales have declined by 8% in the past 2 weeks" | Validated impact/replication, sought customer reports, cited business impact; regional scope relayed via others, limited quantification. |
| Commanding the Incident | 4 | "@maya can you heck the traffic and its legitimacy"; "@maya please go ahead and restart"; "please try using the redundance switch" | Acted as de facto IC with clear tasking and decisions (restart, failover) and cross-checks; did not explicitly claim IC role or set timelines. |

---

# avinashkr-The-Switch-7888.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 4 | "\Create an incident - Network Degradation"; "upgrade the INC priority to Sev2 as its impacted the order placing"; "The failover comepleted and there are no issues observed so far" | Incident created T+5; Severity T+9; Restoration confirmed by team T+24; no explicit closure by PLAYER |
| External Comms | 4 | "Just recevied a few reports that customers facing slowness while placing the orders"; "Regarding the banner in the page for notifying the customers have been taike care"; "The failover comepleted and there are no issues observed so far" | Frequent business-comms updates and customer messaging guidance; no cadence or structured template |
| Internal Comms | 5 | "Hey @maya We have a situation with spike in traffic, could you please check"; "Copying @tinus For better visibility and help in case"; "@tanya  please confirm from your side as well" | Recruited/assigned, escalated, and cross-checked; calm and coordinating; no explicit timeboxing |
| Identify Scope | 4 | "@bob  Do we know since when the issues observed?"; "@bob  Also wanted to know if its affected all markets or anything specific"; "@bob  How about the volumes of customer reporing ?" | Scoped duration, regions, and volume; leveraged others for replication/observability |
| Commanding the Incident | 5 | "We have enaged the Cyber team to check further on their side"; "upgrade the INC priority to Sev2 as its impacted the order placing"; "also lets take that fully out of the network" | Clear decisions and direction (Sev2, failover, isolation); de facto IC though not explicitly declared |

---

# harshagar-The-Switch-7272.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | "its resolved now"; context: "Incident Number INC100031: sev2 issues with site loading"; context: "the infected switch has been successfully changed over" / "Customers have stopped reporting the issue" | Record/severity from uptimelabs; closure announced after restoration evidence. |
| External Comms | 3 | "yes @bez we are on it"; "issues all seem to be related to our network switch"; "its resolved now" | Reactive updates; no cadence/structure; no customer comms strategy shared. |
| Internal Comms | 4 | "@Shay: can you please check anything is wrong from dev side"; "@Tanya: can you look from platform side"; "@maya @hamed @tanya please coordinate to get it resolved" | Strong tasking/collab; sought advice; no explicit timeboxing. |
| Identify Scope | 3 | "@bob : is it specific to a region or global?"; "Platform seems to be working correctly"; "@Bob: from when you are getting complaints" | Determined global and tried to reproduce; limited quantification/detail on impact. |
| Commanding the Incident | 5 | "we'll take the incident first and try to look into it"; "if its not impacting anything i'm fine with it"; "please proceed" | Took charge, made decisions (approved failover), clear direction and coordination. |

---

# kshitijka-The-Switch-7062.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | "*Incident Number INC100078:* slowness while loading website for some P3"; "*Incident Number INC10008:* not able to access the site P1"; "The site is back online." | Multiple incident records with severity; final closure after restoration; earlier premature "the earlier one has been resolved" noted. |
| External Comms | 3 | "*Incident Number INC100078:* ... P3"; "yes, the issue seems to be global"; "No Decline in sales" | Proactive and frequent, but lacked cadence/structure and once contradicted sales impact. |
| Internal Comms | 5 | "sure Tanya please check it and get back in another 3 mins."; "Maya can we have this check from your end?"; "If the revert is required please go ahead and revert your changes" | Recruited named owners, sought advice, timeboxed, and cross-checked resolution. |
| Identify Scope | 5 | "Bob are the reports comings from all over globe or any particular region"; "I will try placing order in website as well"; "products page not loading P1" | Determined global scope, replicated symptoms, identified affected journey and sales impact. |
| Commanding the Incident | 4 | "please proceed with restart"; "Shay can you review this change CHG89462... Get back in another 2 min"; "Hamed ... can you please suggest here? The restart of switch did not work." | Clear tasking and decisions (restart, reroute, revert if needed); did not explicitly declare as IC. |

---

# melvinvar-The-Switch-5749.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | Incident Number INC100069; network slowness and timeouts SEV2; incident can be closed | Record/SEV T+7; restore T+23 (context: Maya "the infected switch has been successfully changed over"); closure T+25 |
| External Comms | 4 | another update in next 5 minutes; next update in 2 mins; Bob please inform clients about this downtime | Proactive at T+7; frequent cadence; discussed customer comms; no structured template |
| Internal Comms | 5 | Team, please share the recent changes that could cause network slowness?; Maya please assist the team to understand the reason for outvbound connection spike; Hamed S /Tanya could you try that? | Recruited named SMEs, asked open/closed Qs, assigned actions, timeboxed via updates; calm/polite |
| Identify Scope | 5 | Hi Bob, did we hear any issues from users?; Team, when did u start facing slowness?; What we know so far, this is not a global issue but specific to payments and frontend IP ranges | Validated user impact and timing; narrowed to frontend/payments IPs (T+10); checked recovery via orders/confirmations |
| Commanding the Incident | 4 | Daniel can you review your changes if it is impacting the network; Hamed S please share your thoughts on how to address this?; Bob please inform clients about this downtime | Clear direction, evidence-driven, decisive (approved failover); did not explicitly declare as IC |

---

# shreyarao-The-Switch-7719.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | [context] "*Incident Number INC100011:* sev3 Issues with late loading of site and placing orders"; [context] "*Incident Number INC100083:* sev1 Issue is exposure of vulnerablities and DDOS"; "Issue is resolved, reports for slow browsing have gone down" | Incident record auto-created with severity at T+8; severity updated to SEV-1 at T+18; closure declared at T+27 after restoration evidence at T+24. |
| External Comms | 4 | "Hello @bez , We are looking into this issue... will update you"; "off by 9% since last month"; "it is a DDOS attack, fixing it imediately" | Proactive in business-comms with multiple updates (T+9,+12,+15,+18,+24,+27); asked to inform customers; no explicit cadence or structured template. |
| Internal Comms | 5 | "@maya Can you help us out here ? Seems like this is a network issue ? Can we please check? @tanya can help you"; "@tanya @shay can you both check if this has anything to do with the changes..."; "Can we get an ETa?" | Recruited named responders, coordinated tasks, sought ETA/timebox; gave clear go for failover at T+23; calm and polite. |
| Identify Scope | 4 | "im able to place an order"; "@bob  is there any issue noticed so far from customers perspective?"; "@bob is this affecting our sales?" | Replicated issue; probed customer impact and sales drop; used others’ signals to confirm widespread impact; limited direct quantification by PLAYER. |
| Commanding the Incident | 5 | "@maya what is the Plan to get this sorted? do you need resources?"; "Can we get an ETa?"; "We should go ahead with the failover then. Please proceed" | Acted as IC (acknowledged by Bez); emphasized impact/ETA; prioritized restoration (failover) at T+23 with clear decision and direction. |

---

# surajjajo-The-Switch-7446.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 4 | [uptimelabs] "*Incident Number INC10002:* ... SEV-3" | Incident record auto-created (SEV-3); PLAYER did not explicitly declare closure. |
| External Comms | 3 | "nope, only some of them"; "not yet, we are still identifying the issue"; "Have asked Bob to sort this out" | Mostly reactive; no structured cadence or next-update timing; brief updates only. |
| Internal Comms | 5 | "@shay @tanya can you guys check the logs and see if you see any major errors?"; "@hamed can I please ask you to intervene in this incident"; "@bob do you see any improvements?" | Strong delegation/coordination; calm/polite; no explicit timeboxing. |
| Identify Scope | 5 | "I just tried placing an order and it worked completely fine for me"; "@bob could it be regional issue?"; "okay @bob how many reports are we talking about here?" | Replicated issue; checked regional vs global; quantified impact. |
| Commanding the Incident | 4 | "Could it be a BOS attack? @maya Can you please help us with this and check if there's any attack on the website?"; "@shay @tanya can you guys check the logs and see if you see any major errors?"; "@hamed can you please help us with implementing this fix" | Led team and approved failover via delegation; no explicit IC declaration. |

---

# vivekdube-The-Switch-5643.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | "*Incident Number INC10002:* P2-- an issue where we have found that intermittently we have network issues across the ethos system"; "We beleive that we have managed to work out the intermittent issues and all reported issues seems to be resolved." ; (context: "the infected switch has been successfully changed over") | Created incident with severity; closure after restoration confirmed |
| External Comms | 4 | "We are working to identify a slow burning issue where the network is behaving weirdly... it seems this is intemitteny"; "We have idenntified that a security switch needs a critical patch... teams continue to investigate"; "Once we bring it back we would do other mitigation steps such as patching the switch" | Proactive, frequent updates; no cadence or structured template; no explicit customer comms plan |
| Internal Comms | 5 | "Tanya can we check from the networkinng perspecitve pls"; "Hi Maya seems like your experience is required"; "Shay can validate along with Bob telling us if he is still getting calls" | Recruited by name, coordinated validation, stayed calm and focused |
| Identify Scope | 4 | "how many users"; "where from they are complaining"; "I just placed on order looks good to me" | Scoped impact and intermittency; replicated; lacked quantified customer counts |
| Commanding the Incident | 5 | "I can get an incident raised and we can work out our individual bits.."; "can we focus more on remediation quickly pleas"; "how much time to swap Hamid" | Acted as IC, made decisions, prioritized containment and managed timing |

---

