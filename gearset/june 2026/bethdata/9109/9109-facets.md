---

# Facets Analysis — 9109

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "@shay will an email failure cause the checkout to crash?" ... "It looks like Tanya's release was quite a while before the problem started." ... "@tanya - what would be involved in rolling back what you've started? There were also some changes to the CartService this morning?"

**Rationale:**
The participant initially pursued the email maintenance correlation as a leading hypothesis, asking whether email could cause checkout to crash and later asking about rolling back Tanya's work — even after Shay and Tanya both stated email is separate from checkout. However, the participant did pivot reactively: after receiving multiple disconfirmations (Shay's "separate flows," Tanya's "different system," Daniel's "nothing points to infra or recent app changes"), they eventually moved to PaymentService investigation. The pivot was slow (many exchanges) and driven by exhaustion of the email lead rather than proactive mechanism reasoning, placing this at tier 2.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "Were the certificates rolled out to the other services as per the playbook - checkout service for example." ... "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
The participant engaged with the cert-rotation thread once Shay surfaced the CHG90123 change from 7 days ago. After the first restart failed, the participant did not repeat the restart or blame downstream services — instead, within a few exchanges, they asked about whether certs were rolled out to other services and then drove toward the bundle investigation. The participant recognized the post-restart failure was structurally different (chain verification vs. expiry) and continued tracing forward. However, the "what changed beyond 24 hours" question was surfaced by Shay/Daniel, not the participant independently, which limits the rating. The reframe after restart failure happened within ~5 exchanges with forward-tracing behavior, consistent with tier 3.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@tanya - we need you to come out of your call, if we lose the slot, then that's going to have to be ok." ... "@daniel - they are both off, I'm happy to say sign it off."

**Rationale:**
The participant accepted Hamed's and Tinus's auto-replies as terminating and did not re-ping them. They initially preserved Tanya's vendor-call constraint, asking Daniel and Shay first, and only pulled Tanya when the investigation required platform-level access. The cost trade-off was articulated ("if we lose the slot, then that's going to have to be ok"). For the restart approval, the participant explicitly owned the override ("they are both off, I'm happy to say sign it off"). This demonstrates naming access constraints and making cost trade-offs, consistent with tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@daniel - they are both off, I'm happy to say sign it off." ... "@tanya - lets do that." ... "@bob - can you let the customers know that we're rolling out a hopeful fix now."

**Rationale:**
The participant walked the escalation chain: pinged Hamed (auto-reply), pinged Tinus via Bez (unavailable), then explicitly took ownership of the restart approval. They delegated parallel work appropriately — Daniel on logs, Tanya on platform checks, Bob on customer comms. They surfaced blockers to Bez in business-comms. This matches tier-3 path (b): walking the escalation chain to exhaustion and then explicitly taking ownership. However, the participant did not enumerate the full dependency structure aloud in a single statement or sequence the cert fix and approval decision to be ready simultaneously — the second restart was authorized without re-litigating, which is a tier-4 signal, but overall the pattern is tier 3.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@tanya - I can see `healthz` 500 errors in the logs - can you look at those please?" ... "OK, is the Payments app anywhere near the email service at all."

**Rationale:**
The participant initially chased the loudest signals (email correlation, broad error logs) and took considerable time to narrow to PaymentService. They did not independently filter to PaymentService logs — Daniel and Shay surfaced the PaymentService focus. The participant asked Tanya about healthz 500 errors without clear filtering logic. Once the cert information was surfaced by NPCs, the participant engaged with it but didn't independently catch the reload-vs-restart distinction from the runbook (Daniel flagged it). The participant accepted NPC summaries and followed their leads rather than driving the filter proactively, consistent with tier 2.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.60** |

---

## Caveats
- F2 tier-3 vs tier-4 was a boundary call. The participant reframed after the restart failure within a reasonable window and drove forward to the bundle, but the week-ago question was NPC-originated, which caps the rating at 3 per the tier-4 anchor requiring the participant to surface that question themselves.
- F4 tier-3 vs tier-4 was also a boundary call. The participant showed clean ownership and delegation but did not verbalize the full dependency structure in a single enumerated statement; the incremental pattern was present but not as explicit as the tier-4 anchor requires.
- F5 rating considered that the participant did eventually engage with cert and bundle information but was consistently led by NPCs rather than driving the filter independently.

---