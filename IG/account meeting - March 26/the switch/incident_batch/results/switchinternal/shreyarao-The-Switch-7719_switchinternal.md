# shreyarao-The-Switch-7719.csv

| Criterion | Grade | Evidence | Rationale |
|---|---|---|---|
| Customer Impact Awareness | ✅ | "@bob Can we inform the customers about an ongoing network issue? Adn that we are fixing it ASAP" | Explicitly requested a customer-facing notice to inform users of the issue. |
| Customer Impact Assessment | ⚠️ | "@bob is there any issue noticed so far from customers perspective?"<br>"@bob is this affecting our sales?"<br>"@tanya can we check the load performace for the platform?"<br>"off by 9% since last month" | First ask was vague about impact; only later did they seek a specific metric (sales), so the earliest qualifying action is partial. |
| Issue Reproduction | ✅ | "im able to place an order" | Attempted to reproduce the problem and reported the result directly. |
| Check Platform Changes | ✅ | "@shay can i get the list of chages that recently went through?"<br>"@tanya @shay can you both check if this has anything to do with the changes done recently on paymentServices and frontend?" | Initiated checks of recent changes and targeted specific components for review. |
| Concurrent Investigations | ✅ | "@tanya @shay can you both check if this has anything to do with the changes done recently on paymentServices and frontend?"<br>"@maya Can you help us out here ? Seems like this is a network issue ? Can we please check? @tanya can help you with the affected services"<br>"@daniel can you help out Tanya to check out the spike in trafific?" | Launched parallel streams (change review and network/security triage) with clear owners and objectives. |
| Escalation | ✅ | "@hamed Do we know any point of contact for load issues? can we involve them here please" | Proactively escalated to Hamed to bring the right authority into the incident. |
| Timeboxing | ⚠️ | "Can we get an ETa?"<br>"it is a DDOS attack, fixing it imediately" | Sought timing and expressed urgency but did not set explicit deadlines or follow-up cadence. |
| Leadership & Command | ✅ | "@tanya @shay can you both check if this has anything to do with the changes done recently on paymentServices and frontend?"<br>"@maya Can you help us out here ? ... @tanya can help you with the affected services"<br>"@daniel can you help out Tanya to check out the spike in trafific?"<br>"We should go ahead with the failover then. Please proceed" | Provided clear tasking, coordinated investigators, and made a decisive restoration call. |
| Resolution Verification | ✅ | "@shay cna you check the internet speed again?"<br>"@bob can you check if the customers are reporting normalcy?"<br>"great, waiting for your confirmation @Bob"<br>"Issue is resolved, reports for slow browsing have gone down" | Sought confirmation from engineering and support before announcing resolution and referenced report trends as evidence. |

## Summary
- Strong leadership: organized investigators, assigned owners, and decisively approved failover for fast restoration.
- Proactive communications: requested customer notice and kept business stakeholders updated during the incident.
- Solid technical coordination: initiated change checks and parallel streams across app, traffic, and network/security.
- Impact assessment started vague; earlier requests for concrete metrics (failure rate, affected regions/users) would improve clarity.
- Improve time management by setting explicit timeboxes (e.g., “report back in 5 minutes with X”) and running periodic status summaries.
