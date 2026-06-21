# Facets Analysis — 9378

## F1 — Misleading correlations

**Rating:** 1

**Evidence:**
> "ok, this does look like it's realted to @tanya ongoing maintenance per the logs @shay has provided. @daniel or @shay, can you revert CHG90431?"
> ...
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." → "@tanya - what was the exact DNS change and can you revert it?"

**Rationale:**
The participant repeatedly committed to the email/DNS correlation as causal even after multiple NPCs explicitly disconfirmed the mechanism. After Tanya stated "Email provider is up, and email confirmations are working. This isn't connected to the checkout issue," the participant continued insisting the email logs showed the cause. Later, after Shay re-pitched the DNS timing correlation, the participant ordered a revert of email DNS changes despite Tanya explicitly stating "it won't affect the payments issue since they're separate systems." This is tier-1 behaviour: ordering rollbacks in the face of explicit NPC mechanism-disconfirmation and staying locked into the prime.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "has the SSL certificate expired? @tanya"
> ...
> "even after a restart @tanya?" ... "can you delete the old certifcate?"

**Rationale:**
The participant eventually engaged with the cert thread but only after NPCs (Shay, Daniel) surfaced the cert rotation and TLS handshake failure. The participant asked about cert expiry but did not independently surface the "what changed beyond 24 hours" question — that came from NPC investigation. After the restart failed to fix the issue, the participant did not reframe the error as structurally different (bundle/chain issue); instead they tried removing the old cert file from disk, treating it as a continuation of the same problem rather than recognising a new failure mode. The pivot to cert work was NPC-driven, and post-restart reframing did not occur, placing this at tier 2.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@hamed or @tinus - we are hard down here..." → receives auto-reply → "@tinus - we are hard down here..." → receives auto-reply → "ok. with both tinus and hamed out I will seek approval from @bez"
> ...
> "i will take the accountability, do the restart"

**Rationale:**
The participant walked the escalation chain methodically (Hamed → auto-reply, Tinus → auto-reply, then Bez, then Tanya), accepted auto-replies as terminating, and eventually took personal accountability for the restart. They also pulled Tanya off the vendor call with a clear directive. However, the participant did not explicitly articulate the access constraints as a pattern to the team or in business-comms, and the decision to pull Tanya off the vendor call lacked a stated cost trade-off ("global outage outweighs vendor window"). This meets tier 3 — names constraints implicitly through actions, accepts auto-replies, escalates appropriately — but lacks the explicit verbalisation of tier 4.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@hamed or @tinus - we are hard down here..." → auto-reply → "@tinus..." → auto-reply → "ok. with both tinus and hamed out I will seek approval from @bez" → "with @tanya the only platform team member available, we will have to revert to her" → "i will take the accountability, do the restart"

**Rationale:**
The participant walked the escalation chain to exhaustion in observable order — pinging Hamed (auto-reply), Tinus (auto-reply), Bez (told Bez can't approve), Tanya (told she can't approve without sign-off), then explicitly took ownership. This matches tier-3 path (b): walks the escalation chain to exhaustion and then issues the authorisation as a distinct message. The participant also delegated parallel work (Daniel on frontend, Shay on PaymentService). However, they did not name the dependency structure aloud as a constraint statement, and the override came only after extended back-and-forth rather than within a short window of chain exhaustion, preventing a tier-4 rating.

---

## F5 — Data overload / buried information

**Rating:** 1

**Evidence:**
> "well we can see from these logs that the EmailService is failing. @tanya can you check the emailservice?"
> ...
> "the reason the checkout failures are happening is because our email provider is unavailable. according to logs provided by @shay"

**Rationale:**
The participant was captured by the loudest signal — EmailService errors in the logs — and declared them the root cause despite Tanya explicitly stating email was unrelated. When Shay provided payment logs showing TLS handshake failures, the participant did not independently filter or interrogate the signal; NPCs drove the investigation to the cert issue. The participant did not read the rotation runbook to catch the reload-vs-restart distinction (Tanya offered both options and the participant chose without engaging the distinction). After the restart failed, the participant did not reason about the new error's structure or investigate the bundle. This is tier-1 behaviour: captured by noise, failing to integrate information NPCs surfaced.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 1 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 1 |
| **Mean Facet Score** | **2.00** |

---

## Caveats
- F1 rating is a clear tier 1: the participant ordered the email DNS revert *after* Tanya explicitly stated it wouldn't help, and said "please do it anyway" — this is commitment to the prime in the face of named disconfirmation.
- F2 could be argued as borderline 1/2. The participant did engage with the cert thread (asked "has the SSL certificate expired?") but only after NPCs surfaced it. Post-restart, they did not reframe the new error. I rated 2 because they did pivot away from the deploy/email hypotheses to cert work, even if NPC-driven.
- F3 and F4 both benefit from the escalation-chain walk, which was well-executed. The boundary between 3 and 4 on both facets turns on explicit verbalisation of constraints, which was largely absent.
- The drill ended before the bundle-ordering issue could be fully explored, limiting F2 and F5 evidence on the deepening layers.

---