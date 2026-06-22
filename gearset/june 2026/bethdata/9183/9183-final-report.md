# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, hidden system dependencies, constrained team access, and noisy data — all while coordinating across multiple people and keeping stakeholders informed. The observations below reflect how you engaged with each of these dimensions.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you treated the email maintenance timing as a leading hypothesis, delegating investigation into it and relaying that framing to Tanya even after she had already indicated it was unrelated. You did pivot away from the false lead, but the pivot was driven by Tanya's repeated explicit disconfirmation rather than by your own reasoning about whether a plausible mechanism connected email maintenance to payment failures.

*Growth edge:* Before investing investigation time in a coincident event, pause to ask yourself — and the team — whether there's a credible mechanism linking the two. "These started at the same time" is a prompt to check mechanism, not a hypothesis to pursue. On your next rep, try articulating *why* a correlation might be causal before assigning someone to chase it.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the certificate rotation from seven days prior was surfaced by your team, you drove the investigation forward effectively — asking about certificate type, validity period, and critically asking Tanya to double-check the bundle assembly order. You connected the week-old change to the current failure and pursued the causal chain to resolution. The temporal gap (a change from days ago causing today's failure) was surfaced by NPCs rather than by your own questioning, but once you had it, you engaged systematically.

*Growth edge:* Practice widening your change-history window independently. When recent deployments don't explain a failure, ask "what changed in the last week or two?" without waiting for someone else to raise it. The hidden coupling here depended on recognising that a cert rotation's effects can be delayed — building that instinct will serve you in future drills.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You navigated the access constraints deliberately. You accepted Tanya's initial unavailability, then made a clear cost trade-off decision to pull her off the vendor call when severity warranted it. When Hamed and Tinus were both unreachable, you named the constraints and moved on rather than repeatedly pinging. Your use of Tanya's time once she joined was focused and purposeful.

*Growth edge:* Consider naming the cost of your access decisions out loud — for example, explicitly acknowledging what pulling Tanya off the vendor call means for the maintenance window. Making trade-offs visible to the team helps everyone understand the stakes and builds shared situational awareness.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain methodically — Hamed, then Tinus, then Bez — and when all were unavailable, you explicitly took ownership as incident manager to authorize the restart. You also delegated parallel work appropriately, routing platform questions to Tanya and application-side investigation to Daniel and Shay.

*Growth edge:* Try naming the dependency structure earlier — before you hit the bottleneck. If you can anticipate "we'll need sign-off for a restart, and here's who can give it," you can start that thread running in parallel with the investigation rather than discovering the constraint at the moment you need action.

---

## F5 — Data overload / buried information

**Operating at: Strengthening**

You filtered effectively from the initial noisy log output to identify PaymentService as the relevant service, then asked targeted questions that narrowed the scope progressively — from outbound call failures to SSL verification to bundle assembly order. You integrated information across multiple team members' inputs to build the picture. Your question about bundle assembly order was particularly well-targeted and caught the key distinction.

*Growth edge:* Practice producing explicit "state of knowledge" summaries at key moments — what's been ruled out, what remains, what the current working theory is. This connects to how you communicated with both your technical team and business stakeholders: posting synthesis statements helps everyone track the investigation and reduces the need for others to piece together the picture from scattered messages.

---

## Looking Forward

You demonstrated solid systematic engagement across most dimensions of this drill — following evidence chains, making deliberate trade-off decisions, and driving toward resolution once key information was surfaced. The clearest growth opportunities for your next rep are: reasoning about mechanism before pursuing correlations, widening your temporal search window independently, and producing explicit synthesis statements that make your evolving understanding visible to the team. These are all habits that compound — each one makes the others easier.