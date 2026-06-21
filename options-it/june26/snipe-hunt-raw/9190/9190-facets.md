# Facets Analysis — 9190

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Are you saying its every region affected? Was it five minutes ago the first report of this?" ... "@tanya Can you elaborate on what change you made that Shay is reffering to? Email maintenance? Does the change affect anything else?" ... "This is more important than the secondary email rollout"

**Rationale:**
The participant initially treated Tanya's email maintenance as the leading hypothesis, pulling Tanya off the vendor call to investigate her changes. Tanya explicitly stated "Email confirmations have been fine, so this maintenance can't be causing checkout failures," yet the participant continued pursuing this thread for several more exchanges. The participant did eventually pivot away from the email hypothesis once Daniel's logs pointed to PaymentService SSL failures, but this pivot was driven by concrete disconfirming evidence (the logs showing TLS handshake failures) rather than upstream mechanism reasoning. The pivot latency from Tanya's disconfirmation was substantial (many exchanges), placing this in tier 2 territory.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "No certs have expired have they?" ... "Can we please redirect it to point to the new cert asap please?" ... "Can we reload it asap? Or if that doesn't work restart?" ... "Can we check the logs to see where it's failing now @tanya?"

**Rationale:**
The participant engaged with the cert thread once Daniel surfaced CHG90123 (the 7-day-old cert rotation). After the first restart failed, the participant pivoted within approximately 3-4 exchanges — asking to check logs, and then engaging with the bundle/chain issue once Tanya surfaced the verification failure. The participant did not independently surface the "what changed beyond 24 hours" question (Daniel found CHG90123), but once the restart failed, the participant reframed relatively quickly by asking for new logs rather than proposing another restart. The participant connected the cert rotation → reload-vs-restart → bundle ordering chain with NPC assistance, meeting tier 3 criteria.

---

## F3 — Decreased access to team / remote

**Rating:** 3

**Evidence:**
> "With both absent I authorise the change" ... "@hamed Can you please reach out to the payment service provider..." [receives auto-reply] ... "@tinus Can you please reach out..." [receives auto-reply] ... "Pause It" ... "Please don't pause the vendor window, postpone it all together"

**Rationale:**
The participant accepted auto-replies from Hamed and Tinus and moved on after one cycle each. They made the cost trade-off with Tanya explicitly — pulling her off the vendor call and later escalating from "pause" to "postpone." They named the access constraint when authorising the restart ("With both absent I authorise the change"). However, there was some inefficiency — they continued pinging Tinus via Bob and Daniel even after receiving auto-replies multiple times, and the initial handling of Tanya's vendor-call constraint required multiple exchanges before being decisive. This places the participant solidly at tier 3 with some tier-2 elements.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "With both absent I authorise the change" ... "I dont think we need any further approvals from Tinus or Hamed since you're at command here in the incident" [NPC affirming participant's earlier decision] ... "Please restart @tanya"

**Rationale:**
The participant walked the escalation chain in observable order — pinged Hamed (auto-reply), pinged Tinus (auto-reply), then explicitly took ownership and authorised the restart. This matches tier-3 path (b). They delegated parallel work appropriately (Daniel on logs, Shay/Daniel on banner). On the second restart (after bundle fix), the participant authorised without re-litigating the approval chain ("Please restart @tanya"). However, they did not articulate the full dependency structure aloud in a single enumerated statement, and continued attempting to reach Tinus even after the first authorisation, which slightly undermines the tier-4 case.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Can we please go over the steps in the cert documentation to ensure they were all followed?" ... "Can we reload it asap? Or if that doesn't work restart?" ... "Lets get that second cert on asap please @tanya"

**Rationale:**
The participant did not independently filter logs to PaymentService — Daniel drove that investigation. The participant did not independently surface the reload-vs-restart distinction from the runbook; Tanya surfaced the cert status and the bundle issue. The participant's request to "go over the steps in the cert documentation" shows awareness of the doc but they didn't catch the key distinctions themselves. They accepted NPC summaries without further interrogation and engaged with key concepts (bundle, chain order) only once NPCs surfaced them. This matches tier 2: asks for filtered information but doesn't drive the filter or catch buried distinctions independently.

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
- F1 rating is a boundary call between 1 and 2. The participant pursued the email hypothesis persistently despite Tanya's explicit disconfirmation, but did eventually pivot once logs pointed elsewhere. Rated 2 because the pivot occurred (driven by concrete evidence from Daniel's logs) rather than the participant staying locked on the email hypothesis through the entire drill.
- F3 rating is a boundary call between 2 and 3. The participant's repeated attempts to reach Tinus (via Bob, Daniel) after already receiving auto-replies and already having authorised the change themselves is a tier-2 signal, but the explicit ownership statement and the decisive Tanya trade-off push toward tier 3.
- Anti-outcome-bias note: The successful resolution and NPC praise at the end are not factored into ratings. The participant reached resolution largely through NPC-driven investigation (Daniel finding logs, Tanya identifying cert issues and bundle problems).

---