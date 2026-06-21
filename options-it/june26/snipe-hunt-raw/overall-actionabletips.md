# Overall Actionable Tips

These cohort-level tips were synthesised from the 15 folder-specific `actionabletips.md` files generated for the Snipe Hunt drill runs. Each folder summary was based on that player's combined report, with the markers and facets catalogues used as background context for interpreting performance.

The aim here is not to describe every individual growth area. Instead, these are the three patterns that appeared most often across the cohort and seemed most likely to improve player performance against the Snipe Hunt markers and facets. The evidence snippets under each tip show examples of how the same theme surfaced repeatedly in the individual folder-level recommendations.

1. **Use mechanism-first reasoning before acting on correlations.** Across the cohort, the most common performance limiter was treating timing overlap or noisy logs as stronger evidence than they deserved. Before rolling back, restarting, or pulling people into a thread, state the causal path in one sentence: "I think X caused Y because Z." If the mechanism is weak or a teammate with system knowledge disconfirms it, explicitly lower that lead's priority and move attention to the service path that can actually produce the customer symptom.

   **Why this was chosen:** This pattern appeared across many individual tip files. Players were repeatedly advised to avoid acting on timing alone, stop treating change logs as rollback queues, and rank log signals by whether they could actually explain the customer-facing symptom.

   **Evidence snippets:**
   - 8936: "Before rolling back or restarting based on timing, say the causal path aloud."
   - 9378: "Do not order a DNS or email revert unless you can name the causal path to payment failure."
   - 9390: "Before rolling back, state which change could cause the observed payment failure and why."
   - 9401: "Hypothesis: email is not causal because orders do not require email; test: focus on payment handshake logs."

2. **Turn evidence into visible narrowing.** Players often gathered useful information but did not consistently convert it into shared synthesis. After each major finding or failed fix, post a short ruled-in/ruled-out update: "Email and recent deploys are ruled out; PaymentService outbound TLS is failing; Tanya is checking cert chain while Daniel tails the first failure window." This improves technical coordination, keeps teams from circling back to closed leads, and makes stakeholder updates more substantive.

   **Why this was chosen:** A second broad cohort pattern was that useful evidence was collected, but not consistently turned into a shared mental model. Multiple folder-level tips asked for explicit ruled-in/ruled-out summaries, stronger technical synthesis, or business updates that combined scope, impact, current theory, action, and next update.

   **Evidence snippets:**
   - 8936: "Every few exchanges, post what is known, what has been ruled out, and what is being checked next."
   - 9173: "Post technical synthesis, not just relayed findings."
   - 9390: "DNS ruled out, deploy timings do not fit, PaymentService outbound TLS is the focus."
   - 9458: "Deploys ruled out, PaymentService TLS confirmed, bundle order is wrong, restart approval is the blocker."

3. **Handle access and approval bottlenecks decisively.** Many runs lost time re-pinging unavailable approvers or asking for sign-off from people who could not provide it. Once the chain is exhausted, name the constraint and the decision path: "Hamed and Tinus are unavailable; Bez cannot approve technical restarts; given the outage impact, I am authorising this and accepting the consequences." Pair that ownership with a quick consequence check before disruptive actions: what could get worse, who needs to know, and how will we verify?

   **Why this was chosen:** The approval and access constraint appeared often enough to be a cohort-level performance lever. Several individual tips focused on avoiding repeated pings to unavailable people, naming the dependency map earlier, setting a Plan B timer, and making the ownership statement once the chain was exhausted.

   **Evidence snippets:**
   - 9121: "When the standard approvers are unavailable, make the decision statement personal and clear."
   - 9177: "Restart requires Hamed/Tinus, both are unavailable, so I may need to authorise."
   - 9427: "When Tinus/Hamed are unreachable and Bez cannot approve technical work, name the exhausted chain and make the ownership call sooner."
   - 9458: "If Bez or Tinus does not respond within a short window, stop repeating the same ask and switch strategy."
   - 9496: "Once Hamed/Tinus auto-reply, tell the team the chain is blocked and what path you will use next."
