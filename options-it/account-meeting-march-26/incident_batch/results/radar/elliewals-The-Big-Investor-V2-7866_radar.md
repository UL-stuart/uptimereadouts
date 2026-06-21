# elliewals-The-Big-Investor-V2-7866.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | "Stopping the tests has fixed the issue"; "website is back up and running"; context: "uptimelabs: Incident Number INC10008 ... sev-1"; context: "daniel: I'm not getting any errors" | Incident record+SEV at T+5 (by uptimelabs per rule); closure declared at T+18 after restoration evidence (T+17–18). |
| External Comms | 4 | "investigating with the team now and reviewing any changes that were made"; "will provide further updates in 5 mins"; "Looks like the chaos tests running hit Prod..." | Proactive in business-comms from T+5 with updates ~every 2–5 min; set 1 cadence; no structured template or explicit customer comms plan. |
| Internal Comms | 5 | "can you all test and see if you see the same"; "@shay are you able to rollback Change ID: CHG89359"; "@tanya can you take 5 mins to take a look at anything you could test to reduce the load" | Recruited named responders, coordinated tasks, used timeboxing (T+12), shared signals, polite and calm. |
| Identify Scope | 5 | "issue seems to be with all items when adding the the cart"; "no orders been placed"; "it appears to be checkout service"; context: "bob: ... crashes with a 500 Internal Error" | Replicated at T+2; scoped impact via orders/support; identified affected flow/services; validated via testing and logs. |
| Commanding the Incident | 4 | "can you please roll back just to rule it out please"; "@tanya can you take 5 mins to take a look..."; "can we please stop the tests" | Clear directives (rollback T+6; stop tests T+16), coordinated team, evidence-led; did not explicitly declare IC. |
