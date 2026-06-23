# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate ambiguous signals, coordinate a partially-available team, and narrow a complex problem space under time pressure. The observations below focus on how you moved through that complexity — your reasoning process, coordination choices, and information management.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you treated the email maintenance timing as a leading hypothesis and assigned investigation effort to it. You also pursued the S3 bucket policy change as a candidate cause, even after a teammate noted that none of the recent changes appeared to explain the checkout failure pattern. Your pivot toward payment service outbound failures came after multiple team members redirected attention there, rather than from your own mechanism reasoning about whether a plausible causal chain existed between the correlations you were tracking and the observed symptoms.

*Growth edge:* When a correlation catches your attention, pause to articulate the causal chain before assigning investigation effort. Ask yourself: "How would this thing *cause* that symptom?" If you can't sketch a mechanism in one sentence, it's a weaker candidate than it feels. This habit will help you deprioritise loud-but-unrelated signals earlier and preserve team bandwidth for higher-probability threads.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You recognised access constraints clearly — noting that Tanya was locked in a vendor session, accepting Hamed's auto-reply as a signal of unavailability, and escalating to Bez with a concrete ask about pulling Tanya off the vendor rollout. You named the trade-off cost (a two-week delay) when making that escalation, which gave the decision-maker the information they needed. Your initial clarifying questions to Bob before declaring an incident also showed discipline in validating scope before pulling people in.

*Growth edge:* You escalated the prioritisation decision to Bez rather than owning it yourself. In future reps, consider whether you have enough context to make the call and frame it as a recommendation with your reasoning attached, rather than routing the decision entirely upward. This strengthens your authority as incident lead and reduces the time cost of the escalation loop.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You identified the key bottleneck — needing Tanya's platform expertise while she was unavailable — and took action to resolve it through Bez. You also ran parallel threads with Shay and Daniel on different investigation paths. However, the coordination was somewhat reactive: you delegated the prioritisation decision rather than owning it, and your sequencing of investigation threads followed NPC suggestions rather than a plan you articulated yourself.

*Growth edge:* Try explicitly stating your coordination plan to the team: "Here's what we're running in parallel, here's what's blocked, here's what I need from whom by when." This makes your sequencing visible and lets you catch bottlenecks before they stall progress. It also positions you as the person driving the sequence rather than responding to it.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked Daniel for filtered information (recent change requests) and directed investigation toward PaymentService logs — both good filtering moves. However, when the change log came back, you latched onto the loudest signal (the S3 bucket change) rather than the most diagnostically relevant one. Even after Daniel confirmed that PaymentService was failing all outbound gateway handshakes, you continued to mention the S3 change alongside the payment issue without synthesising the evidence into a clear scope statement that ruled things out.

*Growth edge:* When you receive a batch of information, practice producing a one-sentence synthesis before your next action: "Based on X and Y, we can rule out Z; the failure boundary is here." This forces you to use evidence as an elimination tool rather than accumulating open threads. It also gives your team a shared mental model to work from, which supports clearer scope communication — something that would have helped orient both your technical team and your stakeholders in this run.

---

## Looking Ahead

You showed real strength in your opening moves — gathering scope before acting, splitting work across people, and recognising when access constraints required escalation. The consistent growth edge across this run is moving from *reactive* to *proactive* reasoning: articulating mechanisms before pursuing correlations, synthesising evidence into elimination statements, and owning coordination decisions rather than routing them. On your next rep, pick one of these and make it deliberate — even if it feels slow in the moment, it will compress the overall investigation timeline.