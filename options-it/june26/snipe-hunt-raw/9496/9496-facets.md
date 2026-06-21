# Facets Analysis — 9496

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Thanks @daniel - please can we roll back Tanya's most recent change? I want to roll back change systematically"

**Rationale:**
The participant initially pursued the email maintenance/DNS correlation and systematically rolled back multiple changes (shipping, product catalogue, checkout services) before pivoting. After Tanya explicitly stated "Primary email provider is untouched. Email confirmations have been sending fine, so this maintenance isn't causing checkout failures," the participant still pulled Tanya off the vendor call to roll back. Later, after multiple failed rollbacks and Shay's repeated nudging about email, the participant eventually accepted Tanya's disconfirmation ("For the clarity, I'm 100% sure that email maintenance is not causing this issue"). The pivot was reactive — driven by concrete failure of rollbacks rather than mechanism reasoning — placing this squarely at tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "If it was done last week, why are we only experiencing this issue now?" ... "So what you are telling me, is the new certs were applied but weren't applied correctly so that payment service has continuously been using the old certs until the day of expiry (today) and now the new certs won't work?"

**Rationale:**
The participant engaged with the week-old coupling only after NPCs surfaced the cert rotation history and explicitly connected the dots. The participant did not independently ask "what changed beyond the last 24 hours?" — that came from Shay/Tanya's investigation. After the first restart failed, the participant did not immediately reframe the failure as structurally different; instead they asked about external providers, network, firewalls, and ClearBank IPs before eventually returning to the cert chain issue when Tanya surfaced the verification failure. The reload-vs-restart distinction was taken from NPC framing ("Step 3 in the doc is to reload"). Pivot latency after the restart failure was well beyond 5 exchanges. This matches tier 2: engages with the week-ago question only when NPCs name it, partial connection of timestamps, reload-vs-restart taken on NPC framing.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tanya please drop from vendor session, this is business impacting and a SEV-1 incident" ... "@tanya please can you call @hamed personal number, tell him we have a SEV-1 and require his input"

**Rationale:**
The participant pulled Tanya off the vendor call without articulating the cost trade-off or economising on her bandwidth. They repeatedly pinged Hamed after receiving the auto-reply (at least 3 times), and pinged Tinus multiple times after receiving his auto-reply. There is no statement of the access constraint pattern in the participant's own words — they never articulated "Hamed is OOO, Tinus is at the summit" as a constraint to work around. They did eventually escalate to Bez for approval, which shows some chain-walking, but the repeated re-pinging of unavailable NPCs and lack of constraint articulation places this at tier 2 rather than tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@bez can we please get your approval given Tinus and Hamed are unreachable right now? Thanks" ... "Restart the payments please. I will take the balme if anything goes wrong"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), escalated to Bez, and when Bez said "make the call and own it," the participant explicitly took ownership ("I will take the blame if anything goes wrong"). This matches tier 3 path (b) — walking the escalation chain to exhaustion and then explicitly taking ownership. They also delegated parallel work to available NPCs (Tanya on platform, Daniel/Shay on logs). However, they did not name the dependency structure aloud as a single constraint statement before being forced into it, and on the second restart (after bundle fix) they simply said "restart the service please" without re-litigating — which is appropriate. The lack of proactive constraint enumeration and the need for Bez's explicit prompt keeps this at tier 3 rather than 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Yes please, deep dive" ... "The Activity doc says Step 3 is to reload the server. That might get the process to pick up the new cert."

**Rationale:**
The participant did not drive filtering proactively — they asked Daniel to pull logs but accepted NPC summaries without further interrogation. The reload-vs-restart distinction from the runbook was surfaced by Shay, not caught by the participant reading the doc themselves. The participant did not reason about absence of signal (e.g., internal calls clean → external boundary failure). They eventually engaged with the cert chain/bundle concept but only after Tanya ran the openssl verify and Shay stated "two certificates needed, it's a bundle." The participant relied heavily on NPCs to surface and interpret buried information rather than driving the filter themselves, placing this at tier 2.

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
- F3 rating was a boundary call between 1 and 2. The repeated re-pinging of auto-replied NPCs (Hamed pinged 3+ times, Tinus pinged 2+ times) is a tier-1 anchor behaviour, but the participant did eventually walk the escalation chain and reach Bez, which is tier-2 territory. Weighted toward tier 2 based on the anti-first-impression-lock reminder and the eventual chain-walking behaviour.
- F4 tier-3 vs tier-4 boundary: the participant took ownership clearly but only after Bez explicitly said "make the call and own it" — this NPC prompting is noted in the tier-2 anchor but the chain-walking behaviour preceding it elevates to tier 3 via path (b).
- The participant gave a "firm estimate" of 10 minutes ETA early in the incident with no basis, which is not directly scored by any facet but contextualises the overall approach.

---