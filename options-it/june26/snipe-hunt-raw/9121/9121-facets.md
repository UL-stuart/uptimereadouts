# Facets Analysis — 9121

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Hi @shay can you please rollback the following: CheckoutService — 08:43 UTC (28 mins ago) Shipping Service — 08:53 UTC (18 mins ago)"

**Rationale:**
The participant initially pursued the email maintenance and recent deploys as leading hypotheses, ordering a rollback of CheckoutService. After the rollback failed ("No change in checkout behaviour—still seeing failures"), the participant pivoted reactively — moving to investigate downstream services rather than continuing to chase the same lead. However, the pivot was driven by the concrete failure of the experiment rather than by upstream mechanism reasoning. The participant never articulated why email maintenance couldn't plausibly break checkout, and Shay's repeated nudges about email timing went unaddressed rather than explicitly dismissed. This is consistent with tier 2: treats the coincident factor as leading hypothesis, pursues it to disconfirmation, then pivots reactively.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "Potentially The only activity I can see is a certificate rotation — CHG90123 | Tanya | PROD | SSL Certificate Rotation (ProductCatalogueService, PaymentService, CheckoutService, CartService) — 7 days ago. is related as the issue is PaymentService is failing at SSL certificate verification"

**Rationale:**
The participant connected the 7-day-old cert rotation to the current SSL verification failure once Daniel surfaced it, articulating the connection in their own words. After the first restart failed, the participant did not immediately reframe — they asked "Does anyone have any ideas" and "How do we resolve this," showing some confusion. However, they did not repeat-restart or blame downstream services. When Shay surfaced "two certificates needed — it's a bundle, not just a single cert," the participant acted on it within a few exchanges. The participant engaged the week-ago coupling thread when prompted by NPC evidence and drove it forward, but did not independently surface the "what changed beyond 24 hours" question — Daniel found it. Post-restart reframing took ~5+ exchanges but the participant didn't fall into a "restart more things" reflex. This fits tier 3: engages with the cert-rotation thread when prompted, connects the causal chain, but reframes somewhat slowly after the first restart fails.

---

## F3 — Decreased access to team / remote

**Rating:** 3

**Evidence:**
> "@Tanya can you please leave the call and check the connection layer please. This is the priority"

**Rationale:**
The participant recognized Tanya's vendor-call constraint, initially asking if anyone else could help and respecting her unavailability for several exchanges. When the evidence pointed to a platform-level issue only Tanya could address, the participant made the explicit trade-off call to pull her off the vendor call, framing it as priority. They accepted Hamed's auto-reply as terminating and moved on after one ping. They did not re-ping Hamed. The participant named access constraints implicitly through their actions (asking about other team members, acknowledging unavailability) and escalated Tanya only when her expertise was actually needed. This aligns with tier 3: accepts auto-replies as terminating, sends targeted high-leverage requests to Tanya, and preserves the vendor-call constraint until the cost of preserving it exceeds the cost of breaking it.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "@Bez can you please approve a full restart to load the new cert" ... "@Bez Jeffos can you please approve a full restart to load the new cert. Hamed and Tinus are both out and we need approval in order to get the checkout up and running"

**Rationale:**
The participant recognized that restart approval was needed and that Hamed and Tinus were unavailable. However, rather than walking the escalation chain cleanly (ping Hamed → auto-reply → ping Tinus → unavailable → own the call), the participant attempted to route the approval to Bez, who is not the standard approver. After NPCs repeatedly stated that "whoever proceeds without that sign-off takes on personal accountability," the participant interpreted Bez's "you have my backing to move fast" as approval rather than explicitly owning the override themselves. They never clearly stated "this is my call" — instead framing it as "Bez confirmed you have his backing." On the second restart (bundle fix), they again sought Bez's approval rather than authorizing independently. This pattern — taking the override call only after NPC prompting and framing it through Bez's backing rather than personal ownership — fits tier 2.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@daniel yes please investigate that service" [after Daniel noted one downstream service showing higher error rate]

**Rationale:**
The participant delegated investigation to Daniel and Shay but largely accepted NPC summaries without further interrogation. They did not independently filter logs to PaymentService — Daniel surfaced the payment logs and the critical errors. The participant did not read the activity document/runbook themselves to catch the reload-vs-restart distinction; Tanya offered the options. When Shay surfaced "two certificates needed — it's a bundle," the participant acted on it but didn't drive that discovery. The participant engaged with key concepts once NPCs surfaced them but didn't proactively filter signal or reason about absence of signal. This is consistent with tier 2: asks for investigation but accepts summaries, reads docs only when directed, surfaces buried information slowly and incompletely.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.40** |

---

## Caveats
- F4 rating is a boundary call between 2 and 3. The participant did ping Hamed (auto-reply) and then attempted Bez, but never explicitly took personal ownership — they consistently framed the authorization as coming from Bez rather than themselves. The tier-3 (b) path requires the participant to "explicitly take ownership and issue the authorisation as a distinct message," which did not clearly occur.
- F2 post-restart reframing was slow (~5+ exchanges of confusion) but the participant did not fall into repeat-restart behavior, which keeps them out of tier 1 territory. The boundary between 2 and 3 here is close; I weighted the participant's independent connection of the cert rotation to the SSL failure (before the restart) as tier-3 evidence.
- The participant reached resolution, but per anti-outcome-bias, this did not influence ratings — process evidence drove all scores.

---