# Facets Analysis — 9311

## F1 — Misleading correlations

**Rating:** 1

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." [Shay's nudge repeated twice] ... Participant: "@tanya - what have you cahnges in email service ?" ... "@tanya - can you shar ethe steps changed ?"

**Rationale:**
The participant repeatedly pursued the email maintenance lead even after Tanya explicitly stated "Email maintenance is paused and on hold. It's a separate system, not related to the checkout failures." The participant continued asking about email changes multiple times after this disconfirmation. They also pursued the recent deploys (rollbacks of CheckoutService, ShippingService, CartService) without mechanism reasoning, only pivoting away after each rollback failed concretely. The pivot to PaymentService came only when Daniel surfaced the payment logs showing handshake failures — not from the participant's own mechanism reasoning. This is tier 1: locked into false leads past disconfirming evidence, pivoting only when NPCs drove the investigation forward.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "can you please look into Command to verify bundle: openssl verify -CAfile /etc/ssl/certs/ca-bundle.crt payment-gateway.crt" ... "we have foudn the cert change has wrong bundle ?"

**Rationale:**
The participant engaged with the cert thread only after Daniel surfaced the payment logs and Shay/Daniel explicitly pointed to the cert rotation. The participant did not independently surface the "what changed beyond the last 24 hours?" question — this came from Daniel ("Did anything change on the platform side?"). Once the cert thread was surfaced by NPCs, the participant followed along but did not independently articulate the reload-vs-restart distinction or the week-old coupling. The bundle order issue was identified by Shay ("order's flipped"), not the participant. The participant engaged with the cert fix but was led through it by NPCs, consistent with tier 2 — engaging only when NPCs named the thread, partial connection of timestamps, taking NPC framing rather than driving it.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tanya - I would leave the maintainence at the mo as we have Prod down so i need you here please" ... "@hamed - can you please help here" [receives auto-reply] ... "i approve" [when Tanya says she needs Hamed or Tinus approval]

**Rationale:**
The participant pulled Tanya off the vendor call without articulating the cost trade-off explicitly — no statement like "global outage outweighs the vendor window." They pinged Hamed once and received an auto-reply but did not re-ping, which is appropriate. However, they did not name the access constraints in their own words or visibly economise on Tanya's bandwidth — instead repeatedly asking Tanya the same questions about her changes (runbook steps asked 5+ times). The participant did not batch questions or sequence escalations cleanly. The eventual ownership of the restart approval ("i approve") came without articulating the constraint pattern. This is tier 2: walks the escalation chain but does not articulate the constraint pattern or economise on constrained resources.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "i approve" ... "pease go ahead" [after Tanya says "I can't restart payments without approval from Hamed or Tinus, and both are out right now."]

**Rationale:**
The participant took the override call when Tanya raised the approval blocker, but did not walk the escalation chain (Hamed was pinged earlier for general help, not specifically for restart approval; Tinus was never contacted). The participant did not name the dependency structure or articulate why they had authority to approve. The ownership statement was minimal ("i approve") without reasoning about the escalation chain being exhausted or naming the constraint. Earlier in the drill, the participant did delegate some parallel work (asking Daniel and Shay to investigate, putting up a banner), but sequencing was largely reactive — they pursued one thread at a time (email → rollbacks → Tanya's changes → payment logs) rather than running parallel investigations. This fits tier 2: takes the override without first attempting the full escalation chain, ownership without reasoning.

---

## F5 — Data overload / buried information

**Rating:** 1

**Evidence:**
> "I keep coming back to the email maintenance" ... repeated requests to Tanya: "Send the steps please @tanya" (5+ times) ... "@tanya - i see errors with recomendation service" ... "I can see Front end errors @daniel - what do you suggest?"

**Rationale:**
The participant was captured by the loudest signals — email maintenance timing, frontend errors, recommendation service errors — rather than filtering to the relevant service. They did not filter logs to PaymentService themselves; Daniel had to surface the payment logs. They repeatedly asked Tanya for the same runbook steps (5+ times) without integrating the information already provided. When Daniel shared the developer investigation logs image showing errors across services, the participant did not use that to narrow scope. They did not reason about absence of signal or drive filtering proactively. Key distinctions (reload vs. restart, bundle ordering) were surfaced entirely by NPCs. This is tier 1: captured by noise, failed to filter or integrate information already surfaced.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 1 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 1 |
| **Mean Facet Score** | **1.60** |

---

## Caveats
- F1 borderline 1/2: The participant did eventually move off the email lead, but only because NPCs drove the investigation to PaymentService. The participant never articulated mechanism reasoning for abandoning the email hypothesis — they simply stopped asking about it when Daniel surfaced payment logs. Given the rubric's emphasis on pivot being driven by mechanism reasoning vs. concrete failure, and the participant's repeated return to the email lead after explicit disconfirmation, tier 1 is the appropriate call.
- F2: The participant reached the cert fix, but entirely through NPC guidance. The "what changed beyond 24 hours" question was never asked by the participant. The bundle fix was identified by Shay. Rating on the lower end of tier 2.
- F4: The participant never contacted Tinus for approval despite Hamed's auto-reply directing to Tinus. The escalation chain was not walked to exhaustion before taking ownership.

---