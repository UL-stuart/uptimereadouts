# melvinvar-The-Switch-5749.csv

| Expertise | Score | Evidence | Notes |
|-----------|-------|----------|-------|
| Incident Mechanics | 5 | Incident Number INC100069; network slowness and timeouts SEV2; incident can be closed | Record/SEV T+7; restore T+23 (context: Maya "the infected switch has been successfully changed over"); closure T+25 |
| External Comms | 4 | another update in next 5 minutes; next update in 2 mins; Bob please inform clients about this downtime | Proactive at T+7; frequent cadence; discussed customer comms; no structured template |
| Internal Comms | 5 | Team, please share the recent changes that could cause network slowness?; Maya please assist the team to understand the reason for outvbound connection spike; Hamed S /Tanya could you try that? | Recruited named SMEs, asked open/closed Qs, assigned actions, timeboxed via updates; calm/polite |
| Identify Scope | 5 | Hi Bob, did we hear any issues from users?; Team, when did u start facing slowness?; What we know so far, this is not a global issue but specific to payments and frontend IP ranges | Validated user impact and timing; narrowed to frontend/payments IPs (T+10); checked recovery via orders/confirmations |
| Commanding the Incident | 4 | Daniel can you review your changes if it is impacting the network; Hamed S please share your thoughts on how to address this?; Bob please inform clients about this downtime | Clear direction, evidence-driven, decisive (approved failover); did not explicitly declare as IC |
