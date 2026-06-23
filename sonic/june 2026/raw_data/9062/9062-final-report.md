# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to navigate systemic complexity under time pressure — sorting misleading signals from real ones, coordinating a distributed team with constrained availability, and making sense of noisy information while stakeholders press for answers. This report covers what surfaced in your run and where the growth edges sit for your next rep.

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you engaged with the email maintenance coincidence as a leading line of investigation — pulling Tanya off her vendor call to look into it and directing Shay to check DNS changes. You did show healthy instinct by asking for "evidence based facts" rather than speculation, which signals awareness that correlation isn't causation. However, the pivot away from the email thread came because NPCs returned disconfirming evidence, not because you independently reasoned about *why* email maintenance couldn't plausibly break checkout. On the next rep, try articulating the mechanism question yourself before dispatching someone to investigate: "How would this change produce *this* symptom?" That self-check can save you from spending team bandwidth on low-probability paths.

## F3 — Decreased access to team / remote

**Operating at: Practicing**

You made a decisive call to pull Tanya off the vendor call, naming the severity as justification. That directness is valuable. What's missing is the cost-benefit reasoning around access constraints — you didn't visibly acknowledge the two-week delay consequence or batch your questions to economise Tanya's time once you had her. You also didn't name the broader constraint picture (who's unavailable and why) as a factor shaping your plan. For the next rep, try making the constraint map explicit early: who do you have, who are you missing, and what does that mean for how you sequence work? Naming the trade-off out loud — even briefly — sharpens your own decision-making and signals to the team that you're operating with awareness of the full picture.

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You delegated work to available team members and set up some parallel threads — Tanya on platform-side checks, Shay on downstream systems, Daniel on logs and deployments. You explicitly structured concurrent work, which is a solid coordination instinct. The gap is in naming the dependency structure: who can do what, what blocks what, and where the sequencing risks sit. Your delegation was reactive rather than planned — you assigned tasks as they occurred to you rather than mapping the investigation space and allocating deliberately. On the next rep, try spending thirty seconds at the start sketching the investigation lanes and who owns each. That small upfront investment tends to prevent the "everyone converges on the same thread" failure mode.

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked some good targeted questions — pressing Daniel on what "outbound failures" meant and where they originated. That kind of specificity helps cut through noise. However, you largely relied on NPCs to surface and filter the relevant information rather than driving the filter yourself. You accepted summaries without pushing into raw evidence or asking what *wasn't* showing up in the data. The growth edge here is developing the habit of asking "what's absent?" alongside "what's present?" — silence in a log can be as diagnostic as an error spike. On the next rep, try requesting raw evidence at least once rather than relying solely on team-member interpretations.

## Looking Forward

You showed solid ownership instincts throughout this run — stepping in decisively, directing people, and pushing back on pressure when it threatened focus. Your clarifying questions at the start were well-targeted and your willingness to redirect the team when evidence pointed to PaymentService showed adaptability. The consistent growth edge across facets is moving from *reactive* to *proactive*: articulating your reasoning before dispatching others, naming constraints and trade-offs explicitly, and driving the information filter rather than waiting for NPCs to hand you the answer. Carry that "say the reasoning out loud" discipline into your next rep — it compounds quickly.