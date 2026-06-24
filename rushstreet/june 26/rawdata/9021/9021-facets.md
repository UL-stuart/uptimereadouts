---

# Facets Analysis — 9021

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." ... "okay, investigation can be done later, can we adjust DNS? to previous one?" ... "We need to revert that maintenance and back to old DNS"

**Rationale:**
The participant adopted Shay's email/DNS correlation as their leading hypothesis and pursued it through to action — pulling Tanya off her vendor call specifically to revert DNS. They did not independently question the causal mechanism ("does email DNS plausibly break payment handshakes?"). However, after Tanya confirmed DNS was clean and email was unrelated, the participant pivoted reactively and moved on to investigating downstream services. This is classic tier-2 behaviour: treating the coincident factor as the leading hypothesis, pursuing it to disconfirmation, then pivoting only after concrete failure rather than from upstream mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "checked payments deployment history — only cert-related change is CHG90123, Tanya, PROD, SSL cert rotation across four services — 7 days ago." ... "notAfter: May 19 08:43:27 2026 GMT ← EXPIRED" ... "today is may 19" ... "okay can clear cache or restart help in that case?"

**Rationale:**
The participant engaged with the week-old cert rotation thread once Daniel surfaced it, recognized the expired cert as the issue, and connected the temporal gap (rotated 7 days ago, expired today). After the first restart failed, the participant asked "what kind of logs and errors we see now" — showing recognition that the situation had changed rather than simply repeating the restart. They engaged with the bundle ordering issue when Tanya surfaced it and drove toward the fix. However, they did not independently surface the "what changed beyond 24 hours" question — that came from Daniel/Shay. The post-restart reframing happened within a reasonable window (~5 exchanges). This meets tier 3: engages with the cert thread when prompted, drives it forward, and recognizes the structural difference after restart failure.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "so we don't have Tinus, Hamed and Tanya" ... "Then we need to do it, sorry Tanya" ... "please understand this is higher priority" ... "You are authorized to proceed with restart. I am taking full responsibility"

**Rationale:**
The participant explicitly named the access constraints ("so we don't have Tinus, Hamed and Tanya"), accepted auto-replies as terminating after one cycle (Hamed, Tinus), and made the cost trade-off when pulling Tanya off the vendor call ("please understand this is higher priority"). They took explicit ownership of the restart decision when both approvers were unavailable. They did not re-ping auto-replied NPCs. This meets tier 3: names constraints, accepts terminating signals, escalates appropriately, and preserves Tanya's constraint until the cost of preserving it exceeded the cost of breaking it.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "so we don't have Tinus, Hamed and Tanya" ... "lovely, and since they are both off who can give it?" ... "Okay I am fine with that" ... "You are authorized to proceed with restart. I am taking full responsibility"

**Rationale:**
The participant walked the escalation chain in observable order: asked Hamed (auto-reply), asked about Tinus (auto-reply), then recognized the bottleneck and took ownership. They named the dependency structure ("so we don't have Tinus, Hamed and Tanya") and explicitly authorized the restart. They delegated parallel work to available NPCs (Shay investigating, Daniel pulling logs, Tanya checking platform). This meets tier 3 path (b): walks the escalation chain to exhaustion, then explicitly takes ownership. They did not quite reach tier 4 because the naming of the dependency structure was somewhat reactive (prompted by Tanya saying she needed sign-off) rather than proactively articulated before the bottleneck surfaced, and on the second restart (bundle fix) Tanya proceeded without re-litigating, but the participant didn't explicitly pre-authorize it.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "CAN WE GET LIST OF RECENT CHANGES?" ... "this look sus CHG90432" ... "okay could it be that cert SSL have issue after she luanched emal service" ... "did we do this Copy cert and key to target path on all pods?"

**Rationale:**
The participant asked for filtered information (change logs, specific service logs) but frequently accepted NPC summaries without further interrogation. They chased a UAT-only change (CHG90432) before being corrected, showing incomplete filtering. They did not independently catch the reload-vs-restart distinction from the runbook — Tanya surfaced the cert findings. The participant did engage with the cert expiry data once presented ("notAfter... today is may 19") but did not drive the filtering proactively or reason about absence of signal. They relied heavily on NPCs to surface and interpret buried information. This is tier 2: asks for filtered data but accepts summaries, engages with key concepts once surfaced but doesn't drive the filter independently.

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
- F1 rating is a borderline 1/2 call. The participant did eventually pivot away from the DNS hypothesis, but only after pulling Tanya off her vendor call and having her confirm DNS was clean — a significant resource expenditure on the false lead. Rated 2 because they did pivot once disconfirmed rather than persisting.
- F2 tier 3 vs 4 boundary: the participant did not independently surface the "beyond 24 hours" question, which is a key tier-4 differentiator. The post-restart reframing was adequate but not notably fast.
- F4 second restart: Tanya proceeded autonomously with the second restart after the bundle fix without the participant needing to re-authorize, which could be read as implicit pre-authorization or simply as Tanya acting independently. Did not weight this heavily either way.

---