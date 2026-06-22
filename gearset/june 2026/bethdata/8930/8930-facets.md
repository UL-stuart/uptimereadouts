---

# Facets Analysis — 8930

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "@shay exactly when did the DNS changes go live?" ... "@shay why would Tanya's email maintenance has influenced this?" ... "@daniel can we rollback any of those changes?" ... "@daniel lets start by rolling back the checkout service because that is the one with all the errors"

**Rationale:**
The participant initially pursued the email maintenance timing correlation (asking Shay about DNS timing) and then pursued recent deploys as the leading hypothesis, ordering rollbacks of CheckoutService and ProductCatalogueService. However, when Shay admitted "honestly, not sure it would" and when rollbacks produced no improvement, the participant pivoted — asking Tanya about platform-side issues and eventually reaching the cert thread. The pivot was reactive (driven by failed rollback experiments) rather than by mechanism reasoning, placing this squarely in tier 2.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "@tanya the SSL rotation looks very suspicious is there anything in there which could be causing this issue?" ... "Wait — it restarted and it's still down? That shouldn't happen if the cert was the only problem." ... "@tanya what could be the cause of something like that?"

**Rationale:**
The participant engaged with the week-old cert rotation as the root cause once Daniel surfaced it ("only cert-related change is CHG90123... 7 days ago"). After the first restart failed, the participant did not repeat the restart or blame downstream services — instead, within approximately 3-4 exchanges, they asked Tanya about the cause and engaged with the bundle/chain issue. They connected "rotated 7 days ago" + "process didn't pick up new cert" into a causal chain. However, they did not independently surface the "what changed beyond 24 hours" question — Daniel/Shay raised it. The post-restart reframe was reasonably quick but not immediate, placing this at tier 3.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@tanya neither Hamed or Tinus are available right now. I am incident commander and I take responsibility for this major action" ... "Both Hamed and Linus are currently unavailable, is there any way to contact one of them urgently?"

**Rationale:**
The participant accepted auto-replies from Hamed and Tinus as terminating (did not re-ping them after the auto-reply). They named the access constraints explicitly ("Both Hamed and Linus are currently unavailable"). They initially asked Tanya to pause the vendor call appropriately given the severity, and when Tanya noted she couldn't restart without approval, the participant took ownership clearly. However, they did not batch questions to Tanya or articulate the cost trade-off verbally when pulling her off the vendor call — the pull was direct without explicit cost reasoning. This meets tier 3 but not tier 4.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@tanya neither Hamed or Tinus are available right now. I am incident commander and I take responsibility for this major action" ... "I am following emergency guidance and am making all decisions"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), asked about emergency escalation process, then explicitly took ownership and issued the authorisation. This matches tier-3 path (b) cleanly. They also delegated parallel work to available NPCs (Daniel on logs, Tanya on platform investigation, Bob on status page). On the second restart (after bundle fix), they authorised without re-litigating ("Lets kick off another service restart then"). However, they did not name the full dependency structure aloud as a single enumerated constraint or sequence cert fix and approval readiness in parallel — the approval question only arose when Tanya flagged it.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@daniel lets start by rolling back the checkout service because that is the one with all the errors" ... "@tanya can you check if the SSL certs are still valid on checkout service please?" ... "From the docs @tanya the problem is documented"

**Rationale:**
The participant initially chased the loudest signal (CheckoutService errors, email maintenance timing) rather than filtering to PaymentService specifically — Daniel and Tanya had to surface that PaymentService was the failing component. The participant did not independently identify the reload-vs-restart distinction from the runbook, nor did they drive the cert-rotation thread themselves (Daniel/Shay surfaced it). However, once the bundle issue was surfaced by NPCs, the participant engaged with the documentation reference and connected it to the fix. They accepted NPC summaries without much further interrogation. This is consistent with tier 2 — engaged but reliant on NPC filtering.

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
- F1: The participant did ask Shay "why would Tanya's email maintenance has influenced this?" which shows some mechanism-questioning, but this came after already pursuing the DNS timing lead and was followed by ordering rollbacks of recent deploys — the overall pattern is still reactive pivoting rather than mechanism-first reasoning.
- F2: Borderline 2/3. The participant did not surface the "beyond 24 hours" question independently, but their post-restart behaviour (not repeating the restart, engaging with the new error type) was reasonably skilled. Rated 3 based on the post-restart reframe quality.
- F5: The participant's question to Tanya about "SSL certs on checkout service" (rather than payment service) suggests incomplete filtering, though this may have been a naming slip given the context.

---