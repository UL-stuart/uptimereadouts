# Combined radar Evaluations

Generated from batch processing

---

# aoifebree-Version-confusion-7816.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 4 | "This is a bigger issue. #incident - Website slowness"; [context] "Incident Number INC100010: - website slowness"; "Incident resolved temporarily until permanent fix implemented. Thanks!" | Incident record via bot after PLAYER trigger; no explicit severity; closure after fix verified. |
| External Comms | 4 | "Hi All, we are investigating... Criticality TBC"; "~20% of customers impacted... timeouts... Trend has been building for two weeks"; "Under control for now" | Proactive in business-comms; shared impact; no explicit update cadence. |
| Internal Comms | 5 | "@bob has there been any customer reports?"; "@shay can you please double check impact of CHG89356"; "Let's go with that. @shay can you please test following the change" | Recruited/assigned by name; coordinated decisions; calm and polite; no timeboxing. |
| Identify Scope | 4 | "Let me test"; "Do other web browsers work fine with all versions?"; "I can see some checkout related errors" | Replicated, browser scoping, noted checkout impact; no explicit regional scoping. |
| Commanding the Incident | 5 | "Can we implement option 1 for now & work on option 2 in the background ?"; "Let's go with that. @shay can you please test following the change"; "@hamed could you please have a look here incase we are missing something?" | Led decisively, prioritized restoration, delegated clearly; didn’t state IC title explicitly. |

---

# elliewals-The-Big-Investor-V2-7866.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | "Stopping the tests has fixed the issue"; "website is back up and running"; context: "uptimelabs: Incident Number INC10008 ... sev-1"; context: "daniel: I'm not getting any errors" | Incident record+SEV at T+5 (by uptimelabs per rule); closure declared at T+18 after restoration evidence (T+17–18). |
| External Comms | 4 | "investigating with the team now and reviewing any changes that were made"; "will provide further updates in 5 mins"; "Looks like the chaos tests running hit Prod..." | Proactive in business-comms from T+5 with updates ~every 2–5 min; set 1 cadence; no structured template or explicit customer comms plan. |
| Internal Comms | 5 | "can you all test and see if you see the same"; "@shay are you able to rollback Change ID: CHG89359"; "@tanya can you take 5 mins to take a look at anything you could test to reduce the load" | Recruited named responders, coordinated tasks, used timeboxing (T+12), shared signals, polite and calm. |
| Identify Scope | 5 | "issue seems to be with all items when adding the the cart"; "no orders been placed"; "it appears to be checkout service"; context: "bob: ... crashes with a 500 Internal Error" | Replicated at T+2; scoped impact via orders/support; identified affected flow/services; validated via testing and logs. |
| Commanding the Incident | 4 | "can you please roll back just to rule it out please"; "@tanya can you take 5 mins to take a look..."; "can we please stop the tests" | Clear directives (rollback T+6; stop tests T+16), coordinated team, evidence-led; did not explicitly declare IC. |

---

# elliewals-The-Switch-7596.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 4 | "@bob please confirm the reports so we can raise an incident"; [context] "*Incident Number INC100076:* p2 some users experiencing slow load times and timeouts" | Record auto-created at T+9 (by uptimelabs) after PLAYER pushed at T+8; Severity present (P2); No closure declared (no restoration evidence). |
| External Comms | 4 | "Some users are reporting slow load times and timeouts"; "Sales still look good"; "will report back" | Proactive first update at T+10; frequent updates every ~1–3 min; no structured template or status-page/customer comms strategy. |
| Internal Comms | 4 | "We need to determine if this is network related to our office"; "@shay please check the logs"; "and report back in 2 mins" | Recruited multiple responders by name; timeboxed at T+14; one clarity hiccup noted by Tanya. |
| Identify Scope | 4 | "Hi Team, I just placed an order and had no issues"; "@bob please confirm if there are any users reporting issues"; "the issue seems that more users on the site the slower it is" | Replicated early (T+4); scoped office vs broader; tracked impact signals; later noted "Website fully down". |
| Commanding the Incident | 4 | "@daniel @shay have any changes been made"; "please restart maya"; "and report back in 2 mins" | Acted as de-facto IC with delegations and decisions; emphasized evidence and action (reboot at T+26); did not explicitly declare IC role. |

---

# elsasavag-The-Switch-7607.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | context: Incident Number INC100047: sev 3; we have resolved it now; we needed to swap the infected switch | Incident created by bot at T+8 (SEV-3); PLAYER declared resolution at T+20 after swap/test confirmations. |
| External Comms | 2 | hey Bez - some people experiencing poor network quality; Bob is organising them to get some metrics for us; we needed to swap the infected switch | Reactive to prompts; sparse updates (T+9, T+10, T+20); no cadence/ETAs/structured format or customer comms plan. |
| Internal Comms | 5 | @tanya could you check the anomalies and let me know how it looks; in the meantime @daniel @maya  could you look further into network related issues / the traffic flows; yes please swap over now maya | Recruited named responders, shared hypotheses, coordinated testing/retests, stayed calm and directive; minor/no explicit timeboxing. |
| Identify Scope | 4 | could anyone having issues with internet let me know; @channel could we please like this message if you seem to be having issues; ok could we confirm is this global or a specific region?; context: global issue, the reports are random | Sought impact and globalness early, prompted signal collection; relied on Bob for metrics (50% impacted); limited quantification by PLAYER. |
| Commanding the Incident | 5 | ok @maya please do some security scans @daniel could you check if it is software related or may linked to any recent chnages; yes can we please restart the switch; yes please swap over now maya | Acted as de facto IC, issued clear decisions (restart then swap), emphasized evidence and delegation; prioritized action with verification. |

---

# emmaallso-Version-confusion-7819.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 4 | context: "Incident Number INC100090: p2..."; "We are working to roll back NGINX to resolve issue for the moment"; "Roll back complete, Tanya has retried the website with V105.0 of chrome and it seems the fix worked" | Incident record and severity auto-created by uptimelabs; PLAYER reported restoration but did not explicitly declare closure. |
| External Comms | 4 | "Global issue - first reported 2 weeks ago"; "investigating recent changes on platform will report back in 5 mins"; "Notifying customers." | Frequent updates, set expectation once; discussed customer comms; format not strictly structured. |
| Internal Comms | 5 | "@shay can i get a list of recent changes deployed"; "@maya can you check proxy behaviour please"; "20% users having elevated load times due to version of website - the delay appears before JS execution" | Recruited named responders, timeboxed, shared signals/hypotheses, coordinated calmly. |
| Identify Scope | 5 | "I can access ok too, @bob any complaints on the customer front?"; "@bob is this affecting 20% of customers in a certain region?"; "Hi everyone can we please get everyone's attention here - we are having a global issue" | Replicated, probed impact and geography, confirmed global, tied to customer impact. |
| Commanding the Incident | 4 | "Hi everyone can we please get everyone's attention here - we are having a global issue"; "@daniel can you please check to see what other factors may be causing this"; "lets roll back for now as customer experience is priority and getting the site working as normal" | Clear directives and decisive rollback; did not explicitly state they were IC. |

---

# jackwalsh-Cart-astrophe-7794.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 4 | uptimelabs: Incident Number INC100033: P1 Incident - Global Outage - Customers Unable to Place Orders.; P1 Outage - Customers Unable to Place Orders, team are investigating - will provide a further update in five minutes.; monitoring before declaring as resolved. | Record and P1 severity present (via uptimelabs and PLAYER); no explicit closure by PLAYER. |
| External Comms | 5 | P1 Outage - Customers Unable to Place Orders, team are investigating - will provide a further update in five minutes.; Yes, full team on this - reviewing changes and all customers impacted.; Changes rolled back, restarting services now - orders coming back through but monitoring before declaring as resolved. | Proactive in business-comms with ~5 min cadence; set expectation; also directed customer comms via @bob. |
| Internal Comms | 5 | Were any changes pushed? @daniel please review. @tanya please check on the platform side.; Acknowledged @shay, looping in @hamed here in @tanya 's absence.; Acknowledged @daniel, please report in the next two minutes. | Recruited by name, shared signals, timeboxed, coordinated and cross-checked; calm/polite. |
| Identify Scope | 5 | did they say when the issue started / when was the first report? Is this impacting all customers or on a region basis?; I can't get onto the website at all - @daniel is this the same for you?; Seeing a downward trend at 11.36 UTC of order confirmations. | Probed region vs global, replicated, used metrics, clarified customer reachability/impact. |
| Commanding the Incident | 4 | Let's roll back the below changes: - CHG89351 - CHG89350; @hamed please assist @daniel in rolling back the changes.; Acknowledged @daniel, please report in the next two minutes. | Clear decisions, assignments, evidence focus, timeboxing; prioritized restoration; did not explicitly declare IC. |

---

# jackwalsh-Details-Matter-8027.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | [uptimelabs] "*Incident Number INC100071:* - SEV1 - Multiple Customers cannot place orders (JPY and TRY Regions)."; "Looks good on my end, tested and confirmed working."; "Issue resolved." | Incident record + SEV via bot at T+5; closure declared after restoration evidence from Tanya/Bob at ~T+22. |
| External Comms | 4 | "We have users unable to place orders in JPY and TRY regions."; "Working on it - rollback didn't work, preparing intraday changes to resolve the issue - next update in 2 minutes."; "COMMS going out now to update customers." | Proactive in biz-comms from T+8 with frequent updates and next-update promise at T+20; minor lack of structured template. |
| Internal Comms | 5 | "I am able to place orders fine - @tanya / @daniel can you place orders on your end?"; "Adding @hamed as well."; "Action Plan: @tanya contact the third party... @hamed prepare the change... @daniel be ready to update configuration..." | Recruited by name, escalated, coordinated roles/timeboxing; calm and directive; cross-checked with support and engineers. |
| Identify Scope | 5 | "Hey @bob - can you confirm if all customers are impacted?"; "I see the issue when accessing Japan and Turkey currencies."; "Error received: HTTP Status: 500 Internal Server Error" | Replicated at ~T+4, narrowed to JPY/TRY, shared concrete error details; asked support for timing/impact. |
| Commanding the Incident | 4 | "Roll this back ASAP @hamed."; "Action Plan: @tanya... @hamed... @daniel..."; "Wait until the change is compelte and confirmation is received to let customers know - @bob" | Clear decisions, prioritized restoration, controlled comms (rollback at T+16, plan at T+19); did not explicitly state IC role. |

---

# jamiedowo-Cart-astrophe-7943.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | context: 'Incident Number INC100040: Opening a SEV1 case'; "This issue is now resolved, the recent changes were rolled back and we restarted the services"; "Looks fixed now" | Record+SEV via uptimelabs; Closure after internal restoration confirmation. |
| External Comms | 4 | "This is impacting all users globally from ordering items on the website"; "We are rolling back the recent change. Update to follow."; "Roll back complete, but we continue to see issues... Updates to follow." | Proactive, frequent updates; lacked structured template and explicit cadence. |
| Internal Comms | 5 | "I am able to recreate the issue"; "Looking at the Grafana logs, orders stopped on the website at 10:04 today"; "Let's roll back Tanya's change in the next 30 seconds - I approve this" | Recruited/assigned by name, timeboxed, shared signals and hypotheses, polite and calm. |
| Identify Scope | 5 | "@bob - Can you confirm if this is impacting all users globally"; "This is impacting all users globally from ordering items on the website"; "Looking at the Grafana logs, orders stopped on the website at 10:04 today" | Reproduced issue, used observability, defined global impact and affected flow (ordering/cart). |
| Commanding the Incident | 5 | "@shay - Can you call Tanya's mobile please and try contact her urgently"; "@hamed - Can you roll back this change on Tanya's behalf asap?"; "@hamed please roll back the change now - i approve this" | Clear directives, decisive restorations, emphasized evidence and timeboxing; didn’t explicitly claim IC. |

---

# jamiedowo-Version-confusion-7595.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | we should open a SEV-3 case on this.; context: Incident Number INC100092: Opening a SEV-3 case; context: Incident Number INC100071: Upgrading to SEV-2; Since the roll back, it has been confirmed as working again now | Incident record/severity via uptimelabs; PLAYER initiated severity and confirmed resolution after rollback verification |
| External Comms | 4 | Asking internally now Bez, i'll follow up shortlly.; @bez - We have been aware of the bug for a week; @bez - Since the roll back, it has been confirmed as working again now | Proactive and frequent; some expectation-setting; lacked explicit cadence/template and no explicit customer comms plan |
| Internal Comms | 5 | @daniel - Please get back to me in a minute; @shay - Please follow up in 30 seconds with the change log.; @hamed - Understood, let's roll back the change right now | Recruited responders, timeboxed, escalated, coordinated calmly and clearly |
| Identify Scope | 4 | @bob Yes please, i would like to get a sense of the customer impact; @daniel - How long have we been aware of the bug?; @tanya please test from your browser version | Scoped by browser/version, gathered impact (5–8%), delegated replication; no regional analysis noted |
| Commanding the Incident | 5 | So we have two options at this point; Please follow up in the next 1 minute with your findings; @hamed - Understood, let's roll back the change right now | Acted as de facto IC, used evidence, made clear decisions, prioritized restoration over prolonged investigation |

---

