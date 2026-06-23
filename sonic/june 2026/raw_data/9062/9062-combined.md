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
---

# Facets Analysis — 9062

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Shay, please check DNS changes and IF it could be the cause, I don't need speculation but evidence based facts"

**Rationale:**
The participant initially engages with the email maintenance correlation by asking Tanya about it and pulling her off the vendor call to investigate. However, they do show some skepticism by asking Shay for "evidence based facts" rather than assuming causation. They pivot reactively once Daniel narrows the issue to PaymentService (which had no recent changes), but this pivot is driven by NPC investigation results rather than the participant's own mechanism reasoning. The participant never articulates why email maintenance couldn't plausibly break checkout. This is tier-2 behaviour: treating the coincident factor as a leading hypothesis and pivoting only after disconfirming evidence arrives from NPCs.

---

## F2 — Hidden coupling

**Rating:** N/A

**Evidence:**
> "well, that is unknown righ tnow, we are still investigating, Daniel has narrowed it down to payments service but no changes made recently so thats where our focus is right now"

**Rationale:**
The transcript ends before the participant engages with the cert thread. They never reach the "what changed beyond the last 24 hours?" question, never surface the cert rotation, and never encounter the restart/reload distinction. The participant was still working through the F1 garden path and narrowing to PaymentService when the drill ended. Per the N/A semantics guidance, F1-driven F2 absence (participant timed out without ever engaging cert work) is N/A, not tier 1.

---

## F3 — Decreased access to team / remote

**Rating:** 2

**Evidence:**
> "@Tanya. step away. this is a sev 1 incident. the rollout can be delayed."

**Rationale:**
The participant pulls Tanya off the vendor call without visible cost-benefit reasoning — no acknowledgment of the two-week delay or batching of questions. They do not articulate the access constraints (Tinus at summit, Hamed on holiday) anywhere in the transcript. They appropriately direct work to available team members (Daniel, Shay), but the decision to pull Tanya is made without economising or naming the trade-off. This is tier-2 behaviour: walking the escalation path without articulating the constraint pattern, and consuming Tanya's vendor-call bandwidth without visible cost reasoning.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "ok who is free that can take a look? @Daniel? @shay" ... "@Shay, while Tanya is looking at that focus on those other systems you have mentioned and see if any of those could be the issue."

**Rationale:**
The participant does delegate work to available NPCs (Daniel and Shay) and attempts some parallel investigation. However, they never name the dependency structure (who can do what, who is unavailable), never articulate coordination bottlenecks, and the delegation is reactive rather than structured. The drill timed out before the restart-approval moment arose, limiting the highest-leverage F4 evidence. On the broader sequencing signals available, the participant shows basic coordination but without naming constraints or proactively surfacing blockers — consistent with tier 2.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Daniel when you say outbound failures please expand, outbound from where?"

**Rationale:**
The participant does ask some targeted follow-up questions (asking Daniel to expand on "outbound failures") and eventually focuses on PaymentService after NPC guidance. However, they initially chase the email/DNS correlation (the loudest signal), accept NPC summaries without deeper interrogation, and don't independently filter logs or reason about absence of signal. They rely heavily on Daniel and Shay to surface the relevant information rather than driving the filter themselves. The targeted asks happen but without follow-through into raw evidence — consistent with tier 2.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | N/A |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.00** |

---

## Caveats
- The transcript appears to end relatively early in the drill — the participant had narrowed to PaymentService but had not yet reached the cert thread, restart decision, or bundle discovery. This limits evidence available for F2 (rated N/A) and F4 (highest-leverage evidence never surfaced).
- F1 is a borderline 2/3 call. The participant's "I don't need speculation but evidence based facts" statement shows some resistance to the prime, but they still pulled Tanya off the vendor call specifically to investigate her change's impact, suggesting the email correlation was still their leading hypothesis. Rated 2 because the pivot away from email was driven by NPC investigation results rather than the participant's own mechanism reasoning.

---
---

# Markers Analysis — 9062

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "everyone, its consistent across the board, getting the team together now to troubleshoot and will get back to you in 5 minutes"

**Rationale:**
The participant positions themselves as the person driving the response — they direct team members, make the call to pull Tanya off the vendor call ("step away. this is a sev 1 incident. the rollout can be delayed"), and push back on Bez's pressure ("if we had a credible ETA right now there wouldn't be this issue. please let us focus"). They use directive language throughout. However, the drill appears to end before the restart-approval moment, so the explicit "override with consequences on me" moment isn't observed.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob what information do you have?" ... "How many customers are blocked from checking out? What's the revenue loss per minute right now?" ... "Is checkout completely down for all users or are any transactions getting through at all?"

**Rationale:**
The participant's first move after Bob's alert is to ask for information. They follow up with scope-validating questions about customer impact, revenue loss, and whether any transactions are getting through. They gather information before taking remediation actions. This meets the novice expectation of scope-validating before acting.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "@Daniel, what was in CHG90439 can you please check to see if this is the cause?" ... "Shay, please check DNS changes and IF it could be the cause, I don't need speculation but evidence based facts"

**Rationale:**
The participant asks about recent changes (CHG90439, DNS changes, Tanya's maintenance) and uses the responses to narrow scope. When Daniel reports "CheckoutService deployed 25 mins ago, ShippingService 15 mins ago... None match failure start," the participant accepts this and moves focus to PaymentService. They ask for evidence-based assessment rather than blindly rolling back, meeting tier 3.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@Daniel, what was in CHG90439 can you please check to see if this is the cause?" ... "@Shay, while Tanya is looking at that focus on those other systems you have mentioned and see if any of those could be the issue."

**Rationale:**
The participant delegates specific tasks to named individuals — Daniel for change investigation, Shay for DNS and downstream systems, Tanya for platform-side checks. They route tasks to appropriate people (pulling Tanya in for platform-level work). The delegation is generally well-targeted, though some asks are slightly vague ("focus on those other systems").

---

## C6 — Runs parallel investigation threads

**Rating:** 3

**Evidence:**
> "@Tanya. step away. this is a sev 1 incident." ... "@Shay, while Tanya is looking at that focus on those other systems you have mentioned and see if any of those could be the issue."

**Rationale:**
The participant runs multiple threads concurrently — Tanya investigating her changes/platform side, Shay checking downstream systems, Daniel checking logs and recent deployments. They explicitly set up parallel work ("while Tanya is looking at that, focus on those other systems"). This demonstrates concurrent investigation threads with distinct people on distinct tasks.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@Tanya. step away. this is a sev 1 incident. the rollout can be delayed."

**Rationale:**
When investigation is blocked at the platform layer and Tanya initially declines to leave the vendor call, the participant escalates firmly and decisively, pulling Tanya off despite the cost. They name the priority ("sev 1 incident") and accept the consequence ("the rollout can be delayed"). The drill ends before the restart-approval escalation moment, but the Tanya escalation is handled well. They don't explicitly name the 2-week cost, which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Shay, please check DNS changes and IF it could be the cause, I don't need speculation but evidence based facts" ... "looking at your previous change, do we need to roll it back? what is the impact."

**Rationale:**
The participant investigates potential causes (DNS/email maintenance, recent deploys, Tanya's change) but doesn't explicitly articulate hypotheses in a "my hypothesis is X, let's test it by doing Y" format. They ask others to check things but the hypothesis-test linkage is implicit rather than explicit. They do pivot away from deploys when timing doesn't match, showing some hypothesis testing behavior, but it's inconsistent and largely reactive to NPC suggestions.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "Daniel when you say outbound failures please expand, outbound from where?" ... "ok folks, lets all focus on the payments service"

**Rationale:**
The participant uses evidence to narrow scope progressively. When Daniel reports deployment times don't match, they move on. When Daniel identifies PaymentService as the anomaly ("throwing errors consistently, but there haven't been any changes on it for ages"), the participant redirects the team's focus there. They ask clarifying questions about the outbound failures to further narrow the scope to the PaymentService-to-gateway connection layer.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "@Tanya. step away. this is a sev 1 incident. the rollout can be delayed."

**Rationale:**
The participant acknowledges the consequence of pulling Tanya ("the rollout can be delayed") but doesn't deeply weigh it — it's more of a dismissal than a considered trade-off. They don't ask "is it safe?" before other actions. The drill ends before the restart moment where consequence-weighing would be most visible. The evidence is limited but shows some awareness of trade-offs without explicit cost-naming.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "ok folks, lets all focus on the payments service"

**Rationale:**
The participant pivots effectively when initial paths don't pan out. After deployment timing doesn't match the outage, they move away from the deploys hypothesis. After Tanya's shipping service change is cleared, they redirect. When Daniel identifies PaymentService as the anomaly, the participant consolidates the team's focus there. They don't get stuck repeating failed approaches, though the pivots are largely driven by NPC findings rather than participant-initiated reframing.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "potenitally something related to checkout, we have folks looking through the various systems to see what the issue is." ... "no ETA but will update you in 5 minutes"

**Rationale:**
The participant's updates to Bez are vague — "potentially something related to checkout" lacks specificity about impact or working theory. They commit to a 5-minute update cadence, which is good, but the content is thin. They don't quantify impact in business terms for Bez (despite having the £1,000-1,500/min figure from Bob). The later update naming PaymentService is slightly better but still lacks business framing.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "ok folks, lets all focus on the payments service" ... "Daniel when you say outbound failures please expand, outbound from where?"

**Rationale:**
The participant redirects the team to PaymentService and asks clarifying questions, but doesn't provide synthesis statements that name what's been ruled out or summarize the current state of knowledge. Their technical channel communication is mostly directive ("focus on X") rather than synthesizing ("we've ruled out deploys because timing doesn't match, email maintenance is cleared, so the issue is PaymentService outbound to gateway"). The team orientation is adequate but lacks the synthesis that would reach tier 3.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 3 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 3 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 3 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.67** |

---

## Caveats
- The transcript appears to end mid-investigation (before restart/resolution), which limits observation of M4 (restart consequence-weighing), M5 (post-restart pivot), and the full L3 override moment. Ratings reflect only what is observable in the transcript.
- K2 is a borderline 2/3 call — the participant commits to update cadence but content is thin. Rated 2 because the updates lack business-frame quantification despite having the data.
- M2 is borderline — the participant investigates causes but doesn't explicitly name hypotheses. The "evidence based facts" request to Shay shows some hypothesis-testing intent but the linkage is implicit.

---
