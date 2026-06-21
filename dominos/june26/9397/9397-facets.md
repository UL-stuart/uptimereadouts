# Facets Analysis — 9397

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "also, the email maintenance started right when the checkout failures began. still feels worth keeping an eye on — that timing hasn't gone away." ... "dont you think if we rollback the deployements on checkout service will resolve this issue"

**Rationale:**
The participant pursued both the email maintenance and recent deployments as leading hypotheses. They ordered a CheckoutService rollback, and when it failed ("No change in error pattern"), they pivoted away from the deployment hypothesis and moved toward platform-side investigation. However, they never articulated a mechanism-based reason for dismissing the email lead — they pivoted reactively after the rollback failed rather than from upstream reasoning. The pivot latency was moderate (several exchanges after disconfirmation), consistent with tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "Oh ok, What could be the reason for it. And can you update the new certificate immediately" ... "Can we remove old certificate manually and run the reload?"

**Rationale:**
The participant engaged with the cert thread only after NPCs surfaced it (Shay found the 7-day-old rotation, Tanya investigated). They did not independently ask "what changed beyond the last 24 hours?" — that question was effectively answered by NPC investigation. When the reload failed, the participant proposed removing the old cert manually rather than recognizing the reload-vs-restart distinction from the runbook. They showed partial engagement with the coupling (expired cert in memory vs. new cert on disk) but took NPC framing rather than driving it themselves. The drill ended before a restart could be attempted, limiting deeper F2 evidence.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "Hi @hamed could you please look into this" ... "Hi @tinus we could see logs of this issue stating that errors on outbound gateway handshakes, we want have a look if this is caused due to email maintenance."

**Rationale:**
The participant pinged both Hamed and Tinus after receiving auto-replies, though they did not re-ping after the auto-replies fired. They repeatedly asked Tanya for help during her vendor call without batching or economising questions, eventually pulling her off with "Need help from platform team" and "Please prioritize this one." They never explicitly named the access constraints in their own words or articulated the cost trade-off of pulling Tanya off the vendor call. This pattern — walking the escalation chain without articulating the constraint — aligns with tier 2.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "We need to check this issue from platform side, Hamed is off today and Tanya is busy with Vendor call on email maintenance." ... "Will restarting impact anything?"

**Rationale:**
The participant did identify that Hamed was unavailable and Tanya was busy, stating this once in-channel. However, they did not proactively sequence work around these constraints — they waited passively for Tanya to become available rather than preparing parallel investigation threads. When the restart question arose, they asked "Will restarting impact anything?" but the drill ended before they could take ownership of the approval decision. They recognized some bottlenecks but didn't sequence around them or own the override, consistent with tier 2.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Yes @shay need information on checkout and shipping service deployments, can very the logs of the issue and let me know if it is causing due to the deployments" ... "Is it causing the issue now ? Can you verify it ?"

**Rationale:**
The participant asked for filtered information (checkout and shipping deployments specifically) and engaged with the payment logs when Daniel surfaced them. However, they did not independently drive filtering to PaymentService — Daniel and Shay surfaced the critical log evidence. They did not catch the reload-vs-restart distinction from the runbook (Tanya had to explain it). They accepted NPC summaries without further interrogation and relied on NPCs to surface the cert rotation and the expired-cert-in-memory finding. This pattern of engaging with information once surfaced but not driving the filter aligns with tier 2.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.00** |

---

## Caveats
- The drill ended before the participant could attempt the restart or face the post-restart bundle-order failure, limiting the depth of evidence available for F2 and F4.
- F4 rating is a borderline 2/3 call: the participant did state "Hamed is off today and Tanya is busy" once, which partially meets tier-3(a) criteria for naming the bottleneck. However, this was a reactive observation rather than a proactive coordination statement, and they did not sequence work around it or take ownership of the override, keeping the rating at 2.
- F1 pivot latency was moderate — the participant moved on from the deployment hypothesis after rollback failure but never explicitly dismissed the email hypothesis with mechanism reasoning; it simply faded from their attention once Tanya joined.

---