# Facets Analysis — 9177

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." ... "hi @tanya - this appears to be maintenance related based on Logs - webhook delivery failed"

**Rationale:**
The participant echoed Shay's email-maintenance framing multiple times and pursued it as the leading hypothesis even after Tanya explicitly stated "The email maintenance is paused and not connected to checkout." The participant eventually pivoted away from the email lead, but only after repeated NPC disconfirmation and after logs pointed clearly to PaymentService. The pivot was reactive to accumulated disconfirming evidence rather than driven by mechanism reasoning, placing this solidly in tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "PaymentService hasn't restarted since before the cert rotation. It's still running the same process from 14 days ago." ... "We did a restart just now, but the handshake errors are still happening. The process is running, but outbound SSL is failing." ... "@tanya please urgently check this"

**Rationale:**
The participant did not independently surface the "what changed beyond 24 hours" question — it was NPCs (Shay/Daniel) who surfaced the cert rotation from 7 days ago. After the first restart failed, the participant did not reframe the problem themselves; they simply asked Tanya to "urgently check this" and Daniel for "next steps." The participant did not articulate that the post-restart failure was structurally different from the original. They engaged with the cert thread only after NPCs drove it, and the reload-vs-restart distinction was surfaced entirely by NPCs. This is tier 2: pivoting only after concrete failure and NPC redirection, without independent mechanism reasoning.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@tinus - are you available as Hamed is OOO?" ... "he is at the same event, we need his approval to proceed" ... "I authorise the restart as Tinus and Hamed are unavailable"

**Rationale:**
The participant accepted Hamed's auto-reply and moved to Tinus, accepted Tinus's auto-reply and attempted Bez, then took ownership when the chain was exhausted. They named the access constraints ("Tinus and Hamed are unavailable") when authorising the restart. However, they pulled Tanya off the vendor call without articulating the cost trade-off, and they pinged Bez multiple times after Bez stated inability to approve. This shows systematic handling of the escalation chain but without the explicit cost-trade-off verbalisation or batching that would indicate tier 4.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "I authorise the restart as Tinus and Hamed are unavailable" ... "I have authorised due to hamed and Tinus' absence" ... "I autorise another restart. Please proceed"

**Rationale:**
The participant walked the escalation chain to exhaustion in observable order (Hamed → auto-reply → Tinus → auto-reply → Bez → unable → self-authorisation), satisfying tier-3 path (b). They delegated parallel work to available NPCs (Daniel on logs, Shay on banner, Tanya on platform). On the second restart (after bundle fix), they authorised without re-litigating the approval chain. However, they did not name the dependency structure aloud as a single enumerated constraint statement proactively — the naming came only at the point of authorisation — and the sequencing of cert fix + approval wasn't explicitly coordinated in advance, which limits this to tier 3 rather than 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "hi @tanya - this appears to be maintenance related based on Logs - webhook delivery failed" ... "@daniel can you confirm CHG90433 isn't related?" ... "Cert has expired - 15-day and 7-day alerts"

**Rationale:**
The participant was initially captured by the loudest signal (email maintenance/webhook delivery) rather than filtering to the relevant service. They did eventually focus on PaymentService after NPCs directed attention there, and they noted the cert expiry once Tanya surfaced it. However, they did not independently drive filtering (NPCs pulled PaymentService logs and identified the handshake failure), did not catch the reload-vs-restart distinction from the runbook, and did not reason about absence of signal. The bundle issue was entirely surfaced and resolved by NPCs. This is tier 2: accepting NPC summaries without further interrogation, engaging with key concepts only after NPCs surface them.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.40** |

---

## Caveats
- F1: The participant's repeated echoing of Shay's email-maintenance framing ("I keep coming back to the email maintenance") is borderline tier 1/2. I rated tier 2 because they did eventually pivot away and pursue PaymentService, though the pivot was slow and reactive.
- F4: The boundary between tier 3 and tier 4 is close. The participant did authorise the second restart without re-litigating, which is a tier-4 signal, but the overall dependency-structure verbalisation was minimal and reactive rather than proactive.
- F2: The participant never articulated the reload-vs-restart distinction or the "different failure" framing themselves — these were entirely NPC-driven. The rating could arguably be tier 1, but the participant did engage with the cert thread once surfaced and moved forward, which places them in tier 2.

---