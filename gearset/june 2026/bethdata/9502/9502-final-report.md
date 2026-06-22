# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, hidden system dependencies, constrained team availability, and a volume of technical detail that needed active filtering. The observations below reflect how you engaged with each of these dimensions during the run.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill you explored the email maintenance timing as a possible cause, asking team members whether it was related. You moved away from this thread once concrete log evidence pointed elsewhere — specifically when PaymentService handshake failures surfaced. The pivot was driven by what others brought you rather than by your own reasoning about whether the email maintenance *could* mechanistically affect payment handshakes. On the next rep, try pausing when a coincidence surfaces and asking yourself: "What would the causal chain have to look like for this to be the cause?" If you can't sketch one, you can deprioritise it earlier and preserve investigation bandwidth.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

After the first restart failed to resolve the issue, you moved quickly to investigate the new error rather than retrying the same action. You engaged with the structural difference — asking what the "unable to get local issuer certificate" error meant — and followed the thread toward the certificate bundle fix. This showed recognition that the situation had changed and that a different failure mode was now in play. The growth edge here is surfacing the "what changed beyond the obvious?" question yourself rather than waiting for a team member to volunteer it. Asking "why would a fresh cert still fail?" before someone else explains it would move you toward independently tracing hidden dependencies.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You encountered multiple unavailable team members (auto-replies from Hamed and Tinus) and worked through the escalation chain to unblock the restart. You also pulled Tanya off a vendor call when the situation demanded it. However, you didn't name the constraint pattern aloud — articulating something like "we've lost access to the two people who normally approve this, so here's how I'm going to handle it." You also didn't visibly batch or economise your asks to Tanya, who was your most constrained resource. On the next rep, try explicitly naming access constraints when they appear: who's unavailable, what that blocks, and how you'll route around it. This makes your reasoning visible and helps the team anticipate bottlenecks.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You navigated the approval dependency for the restart by working through available contacts, and on the second restart you authorised without re-litigating — showing some learning within the drill. The growth area is in how you take override decisions. Rather than routing the decision through an indirect claim of someone else's approval, owning the call explicitly ("I'm authorising this; here's why") makes the decision structure clear to the team and creates an auditable record. You delegated well to available people — assigning platform investigation, log review, and security checks to the right individuals — which supported parallel progress. The next step is naming the dependency structure itself: "We're blocked on X, the normal approver is unavailable, I'm unblocking us by doing Y."

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You made targeted asks — requesting PaymentService logs specifically, asking about downstream service errors — which shows awareness that you need to filter. However, when information came back (cert comparisons, bundle output), you tended to ask "what's the issue now?" rather than interpreting the data yourself. You relied on team members to surface and explain key signals rather than driving the filter independently. On the next rep, when a team member presents output, try stating what you see before asking what it means: "I see the in-memory cert is expired but the on-disk cert is valid — so the service didn't pick up the new cert?" This builds your own interpretive muscle and keeps you in the driver's seat.

---

## Looking Forward

Across this drill, your strongest process was recognising when the situation changed after a failed remediation and redirecting investigation rather than repeating the same approach. You also fanned out work to multiple people early, which kept threads moving in parallel. The consistent growth edge is moving from reactive to proactive: naming constraints before they block you, articulating hypotheses before evidence forces a pivot, and interpreting data before asking others to summarise it. On your next rep, pick one of these — perhaps stating your working hypothesis aloud before asking someone to check it — and see how it changes the shape of the investigation.