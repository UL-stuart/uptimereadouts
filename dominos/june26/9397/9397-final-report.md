# Snipe Hunt — Post-Drill Developmental Report

This drill puts you in the middle of a live incident where multiple systems interact in non-obvious ways, team availability is constrained, and the information environment is noisy. It's designed to stress your ability to reason through misleading signals, coordinate under pressure, and drive investigation when easy answers don't hold up.

---

## F1 — Misleading correlations

**Operating at: Practicing**

You noticed the timing overlap between the email maintenance window and the checkout failures, and you kept it in view as a possible factor. When you pursued the CheckoutService rollback and it produced no change, you moved away from the deployment hypothesis — but the pivot came from the rollback failing rather than from reasoning about *why* the deployment couldn't explain outbound gateway handshake errors. The email-maintenance lead similarly faded from attention without an explicit dismissal.

*Growth edge:* Before committing to a remediation action (like a rollback), practice stating the mechanism you expect: "If the deployment caused this, I'd expect the rollback to resolve handshake failures because…" That framing makes disconfirmation faster and more deliberate when the action doesn't work.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the certificate thread once the team surfaced it — asking about updating the new certificate and later proposing manual removal of the old one. However, the critical insight (expired cert still loaded in memory despite a new cert on disk) was driven by NPC investigation rather than your own questioning. The distinction between a config reload and a full service restart — which the runbook describes — didn't surface in your reasoning until Tanya explained it.

*Growth edge:* When a "fix" (like a cert rotation) appears to already be in place but the problem persists, ask what layer the fix lives at versus what layer the running service is using. That question — "is the running process actually using the new state?" — is the unlock for this class of coupling.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You reached out to both Hamed and Tinus after receiving auto-replies, and you escalated to Tanya with increasing urgency. The escalation chain eventually worked. What was missing was an explicit acknowledgement of the cost: pulling Tanya off the vendor call has consequences, and naming that trade-off ("I'm pulling you because revenue loss exceeds the risk of delaying the vendor migration") would have made the decision visible to the team and to stakeholders.

*Growth edge:* When you need to pull someone off another commitment, state the trade-off out loud in the channel. This isn't just politeness — it creates a decision record and signals to the team that you're weighing constraints, not just reacting to urgency.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You identified that Hamed was unavailable and Tanya was occupied, stating it once in-channel. That's a useful observation. The next step — sequencing work around those constraints — didn't follow. You waited for Tanya to become available rather than preparing investigation threads that could run without her, or identifying what you could pre-stage (logs, runbook steps, approval context) so her time would be used efficiently once she joined.

*Growth edge:* When you name a bottleneck, follow it immediately with "what can I do *before* this person is free?" Even gathering and posting a summary of what's been tried so far saves time when the constrained resource arrives. Your initial clarifying questions to Bob showed good instinct for scoping before acting — apply that same instinct to preparing for constrained teammates.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked Shay for filtered information about specific service deployments, which is a good instinct for managing the information flow. Once Daniel and Shay surfaced the payment-layer evidence and the cert rotation finding, you engaged with it. The pattern, though, was reactive: the critical filtering (narrowing to PaymentService, identifying the cert-in-memory issue) was done by teammates rather than driven by your own interrogation of the data.

*Growth edge:* When a teammate surfaces a finding, practice asking "what else in the logs would confirm or contradict this?" before accepting it as the working theory. Driving the filter — rather than receiving filtered results — builds the muscle for incidents where your team is smaller or less experienced.

---

## Looking Forward

Across this drill, you showed consistent willingness to engage: asking questions, reaching out to teammates, and following up when actions didn't produce results. The recurring growth theme is moving from *reactive* engagement to *proactive* framing — stating mechanisms before testing them, naming trade-offs before making them, and driving the information filter rather than waiting for teammates to surface the critical evidence. On your next rep, pick one of these edges (mechanism-stating, trade-off-naming, or filter-driving) and make it deliberate. One at a time is enough.