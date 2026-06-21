# Facets Analysis — 9150

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "hey — not trying to distract from this, but tanya kicked off the email maintenance right before the complaints started. probably nothing, but the timing is a bit close." ... "@tanya we have p1 issue. there is revenue loss. could you please check this on priority"

**Rationale:**
The participant initially pulled Tanya off her vendor call based on the timing correlation between email maintenance and checkout failures, treating it as a leading hypothesis. However, they did not persist on the email theory after Tanya stated email wasn't causing checkout failures. They pivoted reactively — moving to investigate downstream services and deployments — but this pivot was driven by Tanya's explicit disconfirmation rather than by the participant's own mechanism reasoning. They never articulated "correlation isn't causation" or questioned the causal chain independently. This fits tier 2: pursued the coincident factor, then pivoted after NPC disconfirmation.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "looks like something is expired @tanya can you fix it?" ... "@tanya is there any cache that we need to clear"

**Rationale:**
The participant never independently surfaced the "what changed beyond the last 24 hours?" question — Daniel/Shay found the cert rotation from 7 days ago. After the first restart failed, the participant did not recognise the new error as structurally different. They asked about cache clearing and seemed confused ("@tanya site is not coming only. did you check TLS time?") rather than reframing. It took multiple NPC messages (Shay noting "SSL chain broken errors" and "two certificates needed — it's a bundle") before the participant engaged with the bundle issue. Pivot latency was well beyond 5 exchanges after the restart failed, and the reframing was NPC-driven rather than participant-driven.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tanya we have p1 issue. there is revenue loss. could you please check this on priority" ... "@tinus could you please give signoff" ... "@bez Infra team need signoff for loading new certificate from tinus or hameed. both are not available at the moment. could you please give singoff"

**Rationale:**
The participant pulled Tanya off her vendor call without visible economising or acknowledging the trade-off cost. They pinged Tinus after Hamed's auto-reply, which shows walking the chain, but they then asked Bez for sign-off (which Bez cannot give). They never articulated the access constraints in their own words or batched questions for Tanya. The escalation chain was walked but without reasoning about the constraint pattern. This fits tier 2: walks the escalation chain in order but does not articulate the constraint pattern or economise on constrained channels.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "@bez Infra team need signoff for loading new certificate from tinus or hameed. both are not available at the moment. could you please give singoff" ... "@tanya i am giving you signoff to do so. since there is revenue impact"

**Rationale:**
The participant attempted to route the approval decision to Bez (who explicitly cannot approve technical actions), showing incomplete understanding of the dependency structure. They eventually took ownership but only after Bez refused and Tanya explicitly prompted them ("Just say the word that you're taking or owning the outcome of restart"). The reasoning was outcome-pressure-based ("since there is revenue impact") rather than naming the escalation chain as exhausted. They did not sequence parallel work effectively — much of the investigation was serial with repeated "could you please check" messages. On the second restart (after bundle fix), they authorised more quickly. This fits tier 2: takes the override call after explicit NPC prompting, without first cleanly walking the escalation chain or naming the bottleneck.

---

## F5 — Data overload / buried information

**Rating:** 1

**Evidence:**
> "all this services are failing @tanya" ... "Issue summary is all this servies are not working any throwing error" ... "@shay remove the maintaince banner" ... "@bob I am able to place order"

**Rationale:**
The participant repeatedly misread the situation — listing all deployed services as "failing" when only PaymentService was the issue, claiming they could place an order when checkout was still broken, and toggling the maintenance banner on and off without understanding the state. They did not filter logs to the relevant service themselves (Daniel/Shay did this), did not read the rotation runbook to catch the reload-vs-restart distinction, and did not engage with the bundle/chain issue until NPCs explicitly surfaced it. The participant delegated nearly all investigative filtering to NPCs and failed to integrate information already in-channel (e.g., asking Tanya about cache when she'd already said a restart was needed). This represents failure to filter or integrate available information.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 1 |
| **Mean Facet Score** | **1.80** |

---

## Caveats
- F5 rating of 1 is a boundary call with 2. The participant did eventually direct investigation toward PaymentService and third-party connections, but this was largely NPC-driven. The maintenance banner confusion and the false claim of being able to place an order weigh toward tier 1 as evidence of not integrating available information.
- F4 tier-2 vs tier-3 boundary: the participant did walk Hamed → Tinus → (Bez, incorrectly) before taking ownership, but the Bez detour and the need for explicit NPC prompting ("Just say the word") place this firmly in tier 2 rather than tier 3.

---