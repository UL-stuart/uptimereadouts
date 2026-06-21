---

# Facets Analysis — 8936

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." [Shay's repeated nudge, which the participant pursued] ... "lets roll back CHG90433 as well please" ... "handshake error suggests a cert issue. have we reviewed all certs to ensure nothing is expired"

**Rationale:**
The participant pursued the email maintenance and recent deploy hypotheses extensively, rolling back CHG90439, CHG90440, and CHG90433 before pivoting. The pivot came only after concrete experiment failures (rollbacks didn't help) rather than from upstream mechanism reasoning. The participant did eventually move to cert investigation after multiple failed rollbacks, but never articulated "correlation needs a mechanism" reasoning. Pivot latency was well beyond 5 exchanges from disconfirming evidence (Tanya's explicit "email won't affect checkout" statements were repeated multiple times before the participant moved on). This fits tier 2: reactive pivot after failed experiments.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "can we restart the other services in the chain please?" ... "restart please? if we are hard down, it could help" ... "lets restart all of these in turn"

**Rationale:**
After the first restart failed to fix the problem, the participant's response was to restart additional services rather than reframe the failure as structurally different. The participant did not independently surface the "what changed beyond 24 hours" question — the cert rotation was surfaced by NPCs (Daniel/Tanya). After the restart failed, the participant spent multiple exchanges requesting restarts of other services before Shay identified the bundle issue ("two certificates needed — it's a bundle, not just a single cert"). The participant did not articulate that the post-restart error was different from the pre-restart error. This matches tier 2: pivots only after concrete failure of a "more of the same" reflex, with NPC redirection needed.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "struggling to escalate as @hamed and @tinus are both offline" ... "please pause given we have other members out / unavailable" ... "we have approval from Bez" ... "i will own the response"

**Rationale:**
The participant named the access constraints ("struggling to escalate as @hamed and @tinus are both offline"), accepted auto-replies as terminating after the second cycle (though did re-ping Hamed once), and eventually made the cost trade-off to pull Tanya off the vendor call. The participant escalated to Bez for restart approval when the standard approvers were unavailable. However, the participant repeatedly asked Tanya for information while she was on the vendor call without batching questions efficiently, and the interaction with Tanya was somewhat adversarial ("can you list the changes so far? please cooperate" / "CAN YOU LIST THE CHANGES YOU MADE SO FAR?"). This shows awareness of constraints but imperfect economising, fitting tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "struggling to escalate as @hamed and @tinus are both offline" ... "we have approval from Bez" ... "engineers are refusing to restart the service with out tinus or hamed approval"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), then escalated to Bez for approval and issued the restart authorisation. This matches tier 3 path (b) — walking the escalation chain to exhaustion and then taking ownership. The participant also delegated parallel work to available NPCs (Daniel on rollbacks, Tanya on cert checks, Shay on log review). However, the participant did not name the dependency structure aloud as a single enumerated constraint statement, and the second restart (after bundle fix) proceeded without re-litigating approval, which is a positive signal. The sequencing was somewhat reactive rather than proactive — the participant didn't pre-position the approval decision alongside the cert investigation.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "can we review the failures around email service?" [asked after Daniel already identified PaymentService as the failing component] ... "list all changes made re: email so far" [repeated 3 times after Tanya confirmed email is unrelated]

**Rationale:**
The participant was captured by the loudest signal (email maintenance) for an extended period and repeatedly asked Tanya to list email changes even after she explicitly stated email was unrelated to checkout. The participant did eventually ask for PaymentService-specific logs and identified the cert issue from the handshake errors, but this was largely NPC-driven. The participant did not independently catch the reload-vs-restart distinction from the runbook, and the bundle issue was surfaced entirely by Shay. The repeated requests for already-answered information ("list all changes made re: email so far" asked three times) and pursuing EmailService after it was disconfirmed indicate difficulty filtering signal from noise. This fits tier 2: accepts NPC summaries, engages with key concepts once surfaced by others, but doesn't drive the filter.

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
- F1 rating is a borderline 1/2 call. The participant did eventually pivot away from the email/deploy hypotheses, but only after multiple failed rollbacks and repeated NPC disconfirmation. The pivot was clearly reactive rather than mechanism-driven, but it did occur, placing this in tier 2 territory.
- F3 rating could be argued as a 2/3 boundary. The participant named constraints but the repeated adversarial interactions with Tanya and failure to batch questions efficiently pull toward 2. Rated 3 because the participant did ultimately make the cost trade-off explicitly and accepted auto-replies as terminating.
- F5 rating is solidly tier 2 — the repeated requests for email-related information after explicit disconfirmation is a notable signal of difficulty filtering, but the participant did eventually engage with the cert thread once NPCs surfaced it.

---