# Facets Analysis — 9173

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "hey — not trying to distract from this, but tanya kicked off the email maintenance right before the complaints started. probably nothing, but the timing is a bit close." ... "thanks Daniel @tanya can you look into your email maintenance change" ... "@tanya please can you leave the maintenace and help investigate urgently"

**Rationale:**
The participant initially pursued the email maintenance lead after Shay raised it, asking Tanya to investigate her email changes. However, after Tanya explicitly stated "Primary email provider is untouched. Email confirmations have been sending fine, so this maintenance isn't causing checkout failures," the participant did not continue pursuing email as the cause. They pivoted reactively — Tanya's disconfirmation was concrete and the participant moved on, but they never articulated mechanism reasoning ("does email plausibly break payment?"). The pivot was reactive to NPC disconfirmation rather than driven by upstream reasoning, placing this at tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "So is this a certificate error? 'Certificate on disk (not loaded by process):'" ... "can we restart the process?" ... "@tanya any other ideas?" [after restart failed]

**Rationale:**
The participant did not surface the "what changed beyond the last 24 hours?" question themselves — it was Tanya who volunteered the cert rotation information. After the first restart failed, the participant did not reframe the failure as structurally different; instead they asked "@tanya any other ideas?" and waited for NPCs to drive the investigation forward. They did not articulate the reload-vs-restart distinction or connect the week-old rotation to today's failure in their own words. The pivot after the failed restart was passive — they relied on Daniel and Tanya to identify the chain verification issue. This matches tier 2: engages with the cert thread only when NPCs name it, partial connection of timestamps, and the reload-vs-restart distinction taken on NPC framing.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tinus do you think we should pull Tanya" [after Tinus already sent auto-reply] ... "@hamed is there anything else we can check in the meanwhile" [after Hamed's auto-reply] ... "please step away and help us review" [third ping to Tanya during vendor call]

**Rationale:**
The participant pinged Hamed after receiving the auto-reply, and pinged Tinus after already knowing he was at the summit. They sent multiple messages to Tanya during the vendor call without batching or economising, requiring three separate requests before making the call to pull her. They did not articulate the access constraints in their own words or make a cost trade-off statement when pulling Tanya. This matches tier 2: walks the escalation chain but without articulating the constraint pattern, and consumes Tanya's bandwidth without visible economising.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "Hamad and Tinus are OOO" ... "Can anyone else sign off?" ... "As they are both out I will own the risk. Please restart the process"

**Rationale:**
The participant walked the escalation chain to exhaustion in observable order: asked Tanya about restart, learned sign-off was needed from Hamed or Tinus, acknowledged both were OOO, asked if anyone else could sign off, then explicitly took ownership ("As they are both out I will own the risk"). This matches tier 3 path (b) — walks the escalation chain to exhaustion and then explicitly takes ownership. They also delegated parallel work appropriately (Shay on banner, Daniel on logs). On the second restart (after bundle fix), they authorised without re-litigating. However, they did not name the dependency structure aloud as a single constraint statement or verbalise it proactively before the moment arose, which would be needed for tier 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "So is this a certificate error? 'Certificate on disk (not loaded by process):'" ... "how do we fix the chain?" ... "Can you restart the process"

**Rationale:**
The participant noticed the expired certificate information when Tanya surfaced it but did not drive the filtering themselves — they relied on Daniel to pull PaymentService logs and on Tanya to identify the TLS handshake failure. They did not read the activity doc or catch the reload-vs-restart distinction. After the restart failed, they asked "@tanya any other ideas?" rather than engaging with the structural difference in the error. They asked "how do we fix the chain?" only after Daniel and Tanya surfaced the chain verification failure. This matches tier 2: engages with key concepts once NPCs surface them but doesn't drive the filter or read docs to catch distinctions.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.20** |

---

## Caveats
- F1 is a borderline 2/3 call. The participant did not explicitly pursue the email lead after Tanya's first disconfirmation, which could suggest mechanism reasoning. However, they never articulated *why* email couldn't cause checkout failures — the pivot appears reactive to Tanya's authority rather than to mechanism reasoning. Rated 2 on the basis that no mechanism reasoning is observable in the text.
- F4 is a clean tier 3 via path (b). The participant did not verbalise the dependency structure proactively or name it as a constraint statement, which would be needed for tier 4.
- The participant reached resolution, but per anti-outcome-bias, this does not influence ratings.

---