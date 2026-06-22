# Facets Analysis — 9497

## F1 — Misleading correlations

**Rating:** 3

**Evidence:**
> "wait hang on, okay that's a lot of errors, checkout is completely broken right now. Tanya kicked off the email maintenance just before this, I wonder if that's related." ... "Ok @shay lets park the DNS theory for now until there is more evidence"

**Rationale:**
The participant initially treated the email maintenance timing as a lead worth investigating, which is expected. However, they pivoted relatively quickly once Shay couldn't provide hard proof of DNS involvement and Daniel's logs showed PaymentService outbound failures with no DNS errors. The participant explicitly parked the DNS theory ("lets park the DNS theory for now until there is more evidence") and redirected investigation to PaymentService. This pivot occurred within approximately 3-4 exchanges of disconfirming evidence (Daniel's logs showing no DNS errors, only outbound PaymentService failures). The participant didn't articulate "correlation needs a mechanism" explicitly but did ask Shay for confirming evidence before acting, showing hypothesis-testing behavior rather than blind commitment.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "Its interesting that this was rotated 7 days ago though? Is there any kind of change that happens a week after rotation?" ... "Can you both check to see if the cert rotation was successful? If not we would be pointing at the old one and it would expire?"

**Rationale:**
The participant independently surfaced the "what changed beyond the last 24 hours" question by asking about the cert rotation from 7 days ago and reasoning about what could happen a week later. They connected the temporal gap (rotation 7 days ago → expiry today) into a causal hypothesis before NPCs spelled it out. The post-restart layer (bundle misordering) didn't manifest as a "restart failed" moment — instead, the participant noticed the bundle note in the documentation and asked about it proactively before the restart. They traced the chain from expired cert → disk cert not loaded → bundle misordering, showing systematic engagement with the hidden coupling. The participant didn't need to reframe after a failed restart because they caught the bundle issue before restarting, which demonstrates strong coupling-awareness.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "Why can't you step away from the vendor session? This is a P1 incident and no customers can use our checkout" ... "What is the impact of losing that rollout window?" ... "The incident takes precedent. Please pause the vendor session"

**Rationale:**
The participant named the access constraints implicitly by attempting Hamed (auto-reply received, moved on), Tinus (auto-reply received, moved on), and then making the cost trade-off decision to pull Tanya off the vendor call. They asked about the impact of losing the rollout window before making the call, showing deliberate cost-benefit reasoning. They accepted auto-replies as terminating after one cycle. However, they did re-ping Tinus later during the restart approval phase, and the cost trade-off verbalization was somewhat brief ("The incident takes precedent") rather than fully articulated. This places them solidly at tier 3 — naming constraints and economizing access — but not quite at tier 4's level of explicit orchestration language.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@hamed" "@tinus, are either of you receiving messages?" ... "@bez we need to restart the payments service and need approval from either Hamed or Tinus. Can you get one of them to join us to approve?" ... "Ok I am good to own the call. Lets restart"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), asked Bez to facilitate, then took ownership of the restart decision after Bez indicated they could approve if confident. This matches tier-3 path (b) — walking the escalation chain to exhaustion and then explicitly taking ownership. They also delegated parallel work appropriately throughout (Daniel/Shay on logs, Tanya on platform). However, they didn't name the dependency structure aloud as a single constraint statement before walking the chain, and the ownership moment required Bez's explicit prompting ("If you are confident on doing the restart then command the team to move forward on your call as an approver"), which slightly weakens the case for tier 4.

---

## F5 — Data overload / buried information

**Rating:** 3

**Evidence:**
> "Ok, it looks like we are using the expired one. There is a note at the bottom of that doc - 'PaymentService - The external payment gateway performs strict chain validation and will reject connections where the bundle is incomplete or incorrectly ordered.'"

**Rationale:**
The participant demonstrated strong filtering behavior: they moved past the noisy EmailService errors to focus on PaymentService, asked targeted questions about certs and handshakes, and critically, read the referenced documentation and caught the buried note about bundle ordering — surfacing it themselves before NPCs pointed it out. They also reasoned about absence of signal (no DNS errors in logs → not DNS). They asked Daniel specifically about whether certs are used for handshakes, showing targeted querying. The bundle-ordering catch from the documentation is a strong tier-3/tier-4 signal. However, the initial log investigation was somewhat NPC-driven (Daniel pulled the logs), and the participant didn't independently drive the "what's not in the noise" framing as strongly as tier 4 requires.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 3 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 3 |
| **Mean Facet Score** | **3.00** |

---

## Caveats
- F2 boundary call between 3 and 4: The participant surfaced the "what changed beyond 24 hours" question independently (tier-4 signal) and caught the bundle issue proactively from documentation. However, the post-restart reframing layer never fired as a test because they pre-empted it, making it harder to assess the full tier-4 pattern. Rated 3 conservatively because the week-ago question, while self-generated, was partially prompted by Daniel's mention of "cert rotation 7 days ago."
- F5 boundary call between 3 and 4: The participant caught the bundle note from documentation independently, which is a tier-4 anchor signal. However, the overall filtering pattern was collaborative rather than solely participant-driven, keeping this at tier 3.
- F1: The participant did initially echo Shay's framing ("Tanya kicked off the email maintenance just before this, I wonder if that's related") but pivoted cleanly within a few exchanges, placing them at tier 3 rather than tier 2.

---