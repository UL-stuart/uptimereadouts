# Facets Analysis — 9268

## F1 — Misleading correlations

**Rating:** 1

**Evidence:**
> "ok, can that change be reverted easily?" ... "@tanya roll back anyway" ... "Tanya rolled back CHG90441. No change to checkout, it's still failing."

**Rationale:**
The participant adopted the email maintenance/DNS correlation as their leading hypothesis and pursued a rollback even after Tanya explicitly stated "Primary email provider hasn't been touched, it's running fine. Email confirmations are going out, so this maintenance isn't causing checkout failures." The participant ordered the rollback anyway ("@tanya roll back anyway") in the face of direct mechanism-disconfirmation from an NPC. After the rollback failed, the participant did eventually pivot, but the commitment to the prime past explicit NPC disconfirmation is the strongest possible low-skill F1 evidence per the rubric. The pivot was purely reactive to experimental failure, not mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "@tanya is the new cert not picked up? how to force that? restart service?" ... "But... payments are still failing. The service is still not recovering." ... "who can check that the cert rotation process is now ok?"

**Rationale:**
The participant engaged with the cert thread once Daniel surfaced the 7-day-old rotation (NPC-prompted, not self-initiated). After the first restart failed, the participant did not immediately reframe — instead asking "who can check that the cert rotation process is now ok?" which is a reasonable but reactive response. The participant did not articulate that the post-restart error was structurally different from the pre-restart error; they relied on NPCs (Shay: "payments service needs a two-cert bundle") to drive the investigation forward to the bundle. The "what changed beyond 24 hours" question was never self-initiated. This fits tier 2: pivots only after concrete failure, engages with the week-ago thread only when NPCs name it, and takes on NPC framing rather than driving it independently.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@hamed we are suspicious of the timing re Tanya's change..." [receives auto-reply] "@tinus I need some escalation..." [receives auto-reply] "@bez @hamed @tinus who is here to auth this?" [Hamed auto-replies again]

**Rationale:**
The participant re-pinged Hamed after already receiving the auto-reply (tier-1 signal). They also pulled Tanya off the vendor call via Bez without articulating the cost trade-off. However, they did eventually walk the escalation chain and took ownership when Bez delegated back. The participant never named the access constraints in their own words or economised on Tanya's bandwidth. The repeated pinging of auto-replied NPCs and lack of constraint articulation places this at tier 2 — walks the chain but doesn't articulate the constraint pattern.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "tanya, Bez may do this, one sec" ... "@Bez Jeffos I need you to auth Tanya to restart a service" ... "I'm at the summit but watching this thread. I don't handle technical approvals, that's for you as incident lead." ... "@tanya you will have to take my authorisation. Bez has delegated to me. Do it"

**Rationale:**
The participant eventually took the override call, but only after Bez explicitly pushed it back ("that's for you as incident lead"). The participant did not name the coordination bottleneck themselves before NPCs raised it, and the ownership reasoning was condensed to urgency rather than naming the escalation chain as exhausted. On the second restart (after bundle fix), the participant simply said "restart it" without re-litigating, which is appropriate. However, there's no evidence of proactive sequencing or parallel work delegation — the participant largely followed NPC-driven investigation threads. This fits tier 2: takes the override after explicit NPC prompting, without first articulating the dependency structure.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "can someone check system health and logs?" ... "@daniel what did you learn from that downstream app you focused on?" ... "expired cert?" ... "not sure why the process isn't picking up the new certificate"

**Rationale:**
The participant asked for logs but in a general way ("can someone check system health and logs?") rather than targeting PaymentService specifically. They accepted NPC summaries and followed NPC-driven filtering (Daniel narrowing to the downstream app, Tanya identifying the TLS issue). The participant did not independently catch the reload-vs-restart distinction from the runbook, nor did they drive the bundle investigation — Shay surfaced the bundle ordering issue. The participant engaged with key concepts once NPCs surfaced them but didn't drive the filter themselves, fitting tier 2.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 1 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **1.80** |

---

## Caveats
- F1 rating of 1 vs 2 was a boundary call. The participant did eventually pivot after the rollback failed, which is tier-2 behaviour. However, ordering the rollback *after* Tanya's explicit mechanism-disconfirmation ("Email confirmations are going out, so this maintenance isn't causing checkout failures") is the rubric's "strongest possible low-skill F1 evidence." I weighted the commitment past named disconfirmation more heavily than the eventual reactive pivot, landing at 1.
- F3 rating of 2 vs 1 was also a boundary call. The re-pinging of Hamed after auto-reply is a tier-1 signal, but the participant did eventually take ownership and didn't consume excessive Tanya bandwidth on low-value questions. Rated 2 on balance.

---