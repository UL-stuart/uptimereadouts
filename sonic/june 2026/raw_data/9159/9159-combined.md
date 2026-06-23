# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to reason through systemic complexity under pressure — sorting misleading signals from real ones, navigating hidden dependencies, coordinating a team with constrained access, and synthesizing noisy information into actionable direction. This report covers what showed up in your run and where the growth edges are for your next rep.

---

## F1 — Misleading correlations

**Operating at: Not yet evident**

Early in the drill, you locked onto the email maintenance correlation and continued pursuing it — including ordering a rollback — even after a team member explicitly disconfirmed the mechanism ("Email service is invoked after payments"). You also ordered a blanket rollback of all recent production changes without articulating a mechanism connecting any specific change to the symptom. The pivot away from these false leads came only after the remediation attempts failed, not from reasoning about *why* the correlation didn't hold.

*Growth edge:* When a team member provides mechanism-disconfirmation (not just "I don't think so" but "here's why it can't be that"), practice treating that as a hard elimination rather than something to override. On your next rep, try naming aloud what would have to be true for a correlation to be causal — and check whether that mechanism exists before acting on it.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You noticed something was structurally wrong when the first restart failed ("it restarted and it's still down? That shouldn't happen if the cert was the only problem"), which is a good instinct. However, the deeper coupling — a cert rotation from days earlier interacting with a service restart — was surfaced by team members rather than by your own reframing. You engaged with the coupling once it was named, but reactively.

*Growth edge:* When a restart or rollback doesn't resolve the issue, practice asking "what else changed that I haven't looked at yet?" before waiting for the team to surface it. Expand your change window beyond the last 24 hours as a deliberate move.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You recognized that key people were unavailable and attempted to route around them — assigning Tanya to fill a gap, escalating to Bez for authorization. However, you assigned tasks to Tanya while she was on a vendor call without explicitly weighing the cost of pulling her off, and you didn't batch your questions to constrained resources. Your delegation was active but didn't economize on the limited bandwidth available.

*Growth edge:* When a key person is occupied, name the trade-off explicitly before pulling them ("Tanya is on a vendor call — pulling her costs us X, but we need Y"). This forces you to be intentional about when and how you use constrained access. Your instinct to route around was solid — the next step is making that routing efficient.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You worked the approval chain for the restart — going to Bez when Hamed and Tinus were unavailable — and eventually took the override call yourself. But the path there was somewhat forced: you claimed authority that wasn't clearly granted, and you needed a team member to prompt you to own the decision. On the second restart, you authorized cleanly without re-litigating, which is a positive signal. The dependency structure (who can approve what, and what happens when they're unavailable) wasn't named proactively.

*Growth edge:* Practice mapping the approval chain early: "If I need to restart a service, who signs off? If they're out, who's next? If no one's available, what's my threshold for self-authorizing?" Naming this structure up front saves time when the pressure hits. Your willingness to eventually take the call is the foundation — the next step is getting there faster and more deliberately.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You delegated log investigation and changelog review to others, which is appropriate. However, when results came back, you accepted summaries without driving further filtering — for example, when told that PaymentService was throwing errors consistently with no recent changes, you didn't independently narrow to that service's dependencies. The critical distinction between a service reload and a full restart (buried in the runbook) wasn't caught. Your team members drove the filtering that ultimately mattered.

*Growth edge:* When a team member surfaces a finding, practice asking one more question before moving on: "What does that rule out? What does it point to?" This turns you from a delegator-and-receiver into someone actively shaping the filter. Also, when runbooks are available, scan for conditional steps (reload vs. restart, partial vs. full) — those distinctions often hide the real fix.

---

## Looking Forward

You showed consistent willingness to take the lead, delegate to named people, and adapt when your initial approach didn't work — these are real strengths to build on. The primary growth area across this run is moving from reactive to proactive reasoning: eliminating hypotheses based on mechanism rather than failed experiments, synthesizing what's been ruled out for your team rather than asking open-ended questions, and naming constraints and trade-offs explicitly before acting on them. On your next rep, try narrating your reasoning out loud — even briefly — before each major action. That single habit tends to surface the gaps before they cost you time.
# Facets Analysis — 9159

## F1 — Misleading correlations

**Rating:** 1

**Evidence:**
> "Roll the email maintenance back anyway, if you can at all." ... "Tanya, investigate Shay's theory on email maintenance timing." ... "a rollback of all the changes that occurred after the incident, as well as any changes up to an hour before the first reported issue"

**Rationale:**
The participant locked onto the email maintenance correlation and ordered rollbacks despite multiple explicit disconfirmations from Tanya ("Email maintenance is not impacting the checkout outage. Email service is invoked after payments") and the fact that maintenance was already paused. They continued pursuing the email lead ("Roll the email maintenance back anyway") even after mechanism-disconfirmation. They also ordered a blanket rollback of all recent PROD changes without mechanism reasoning. This matches tier 1: staying locked into false primes past disconfirming evidence, ordering rollbacks in the face of explicit NPC mechanism-disconfirmation.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "Wait — it restarted and it's still down? That shouldn't happen if the cert was the only problem." ... "Tanya, follow up on Shay's thought on the cert chain."

**Rationale:**
The participant did not independently surface the "what changed beyond the last 24 hours?" question — it was Daniel who flagged the cert rotation from 7 days ago. After the first restart failed, the participant expressed surprise but did not independently reframe the failure as structurally different. They delegated to Tanya to follow up on Shay's cert chain theory rather than driving the reframing themselves. The pivot came reactively after NPC prompting (Shay's "could this be something with the cert chain?"), placing this in tier 2 territory — engaging with the coupling only after NPC direction, not from own mechanism reasoning.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "Tanya, you're up to fill Hamed's shoes." ... "I'm assuming since Tinus is out, I can throw that question I asked him, to you Bez." ... "Hamed and Tinus are out. Bez has handed me authority. Restart payments, Tanya and get the cert working."

**Rationale:**
The participant recognized that Hamed and Tinus were unavailable and attempted to route around them, but did not economize on Tanya's vendor-call bandwidth — they assigned her tasks while she was on the call, then pulled her off without articulating the cost trade-off. They did not batch questions to Tanya or explicitly name the access constraints in a structured way. The escalation to Bez for authorization showed awareness of the chain but lacked explicit reasoning about the constraint pattern. This matches tier 2: walking the escalation chain without articulating the constraint pattern or economizing on constrained resources.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "Please authorize this action..." ... "Hamed and Tinus are out. Bez has handed me authority. Restart payments, Tanya and get the cert working." ... "I got authorization (basically). Go for the payments restart."

**Rationale:**
The participant attempted to get Bez to authorize the restart, was told Bez doesn't do technical sign-off, then claimed Bez "handed me authority" — a somewhat forced interpretation. They did take ownership eventually but only after explicit NPC prompting ("If you feel confident in doing a restart, then own it and move forward"). They did not name the dependency structure proactively or walk the escalation chain cleanly (they skipped Hamed/Tinus auto-replies before going to Bez). The reasoning was outcome-pressure-driven ("Hamed and Tinus are out") rather than a structured articulation of the exhausted chain. On the second restart, they authorized without re-litigating, which is a positive signal. Overall this fits tier 2: taking the override call only after explicit NPC prompting, without first cleanly exhausting the escalation chain.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Daniel and Hamed, please start looking into the changelogs for pushes your teams have done." ... "Shay, you can work that theory on payment timeout bump from 10s to 12s"

**Rationale:**
The participant delegated log investigation and changelog review to others rather than driving targeted filtering themselves. They did not independently filter to PaymentService logs — Daniel surfaced the payment logs and the cert rotation. The participant accepted NPC summaries without further interrogation (e.g., when Tanya posted the cert comparison, the participant asked "can you rollback?" rather than reasoning about the reload-vs-restart distinction). They did not catch the reload-vs-restart distinction from the runbook, nor did they reason about absence of signal. The cert chain bundle issue was surfaced entirely by Shay and Tanya. This matches tier 2: asking for information but accepting NPC summaries without driving the filter or catching buried distinctions independently.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 1 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **1.80** |

---

## Caveats
- F1 rating of 1 is a strong call. The participant did eventually move past the email/deploy primes, but only after exhausting those leads through failed rollbacks — not from mechanism reasoning. The blanket rollback of all PROD changes without mechanism reasoning is particularly strong tier-1 evidence.
- F4 boundary between 2 and 3: the participant did eventually name "Hamed and Tinus are out" but only after being told by Bez to own the call. The second restart authorization without re-litigating is a mild positive signal but insufficient to elevate to tier 3 given the overall pattern.
- Anti-first-impression-lock applied: the participant's later engagement with the cert thread was considered, but the F1 rating reflects that the pivot was entirely reactive (failed experiments) rather than mechanism-driven.

---
---

# Markers Analysis — 9159

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "Hey Bob. I'll take lead here. Can you get more details from customers on what's happening?" ... "Hamed and Tinus are out. Bez has handed me authority. Restart payments, Tanya and get the cert working."

**Rationale:**
The participant takes lead immediately and drives the response throughout. They make the restart override call when both approvers are unavailable, claiming Bez handed them authority. However, they don't explicitly name personal accountability or consequences ("blowback's on me") — they needed prompting from Shay ("own it and move forward... tell team that you're taking responsibility") before proceeding. This places them at tier 3 rather than 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "Is this impacting all customers or just a subset? How much revenue are we losing per minute right now?" ... "Is checkout fully blocked or are some transactions still going through? I need to know the scale of the impact."

**Rationale:**
The participant's early moves include scope-validating questions about customer impact, regional scope, and whether checkout is fully blocked. They also ask Shay to replicate the issue. These are substantive clarifying questions before taking remediation action. They don't deeply probe the error pattern (same error vs. variants, same step vs. different), which would push to tier 4.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "Daniel and Hamed, please start looking into the changelogs for pushes your teams have done. See if there's anything that looks like a smoking gun." ... "a rollback of all the changes that occurred after the incident, as well as any changes up to an hour before the first reported issue"

**Rationale:**
The participant asks for changelogs, which is good. However, when the team reports nothing obvious ("None of the PROD deployment timings line up exactly"), the participant orders a blanket rollback of all six PROD changes without articulating a mechanism connecting any specific change to the symptom. They asked the question but didn't use the answer as an elimination pass — they used it as a rollback queue. This is the tier 1–2 pattern described in the rubric.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "Daniel and Hamed, please start looking into the changelogs..." ... "Tanya, look at changelogs and see if there's anything suspect to this issue." ... "Shay, you can work that theory on payment timeout bump..."

**Rationale:**
The participant consistently names specific people for specific tasks throughout the drill. They route platform-side work to Tanya, log/app work to Daniel, and theory-testing to Shay. Some routing is slightly off (asking Hamed who is OOO, initially asking Tanya to fill Hamed's shoes when she's on a vendor call), but overall delegation is named and directed. Not quite tier 4 because of some misrouting early on.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "Shay, you can work that theory on payment timeout bump from 10s to 12s... Find any changelogs related and see how to rollback if needed." ... "Tanya, follow up on Shay's thought on the cert chain."

**Rationale:**
The participant mostly works sequentially — asking for changelogs, waiting, then ordering blanket rollbacks, waiting for those to complete, then asking "ideas, anyone?" Only after the rollbacks fail do they begin to fan out. The Shay/Tanya parallel assignment comes late in the drill. For most of the investigation, the participant pursued one thread at a time (changelogs → rollbacks → deep dive), which is a tier 2 pattern.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "Ok Tanya, I'm authorizing you to push that vendor call to lower priority. Move to investigating this P1 outage." ... "Hamed and Tinus are out. Bez has handed me authority. Restart payments, Tanya and get the cert working."

**Rationale:**
The participant escalates Tanya off the vendor call (though somewhat delayed) and works the approval chain for the restart. When Hamed auto-replies, they go to Bez, and when Bez declines technical sign-off, they take the call themselves. The escalations are concrete and move the investigation forward. However, they don't explicitly name the cost of pulling Tanya off the vendor call (the 2-week delay), which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Roll the email maintenance back anyway, if you can at all." ... "a rollback of all the changes that occurred after the incident, as well as any changes up to an hour before the first reported issue"

**Rationale:**
The participant does not explicitly articulate hypotheses before acting. They pursue the email maintenance angle despite Tanya repeatedly stating it's unrelated, and order blanket rollbacks without naming a mechanism. They don't frame actions as hypothesis tests ("if X is the cause, then rolling back X should fix it"). The cert thread emerges from team investigation rather than participant-driven hypothesis formation. This is a tier 2 pattern — acting without naming the theory.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "Ok. Site is still broke. Ideas, anyone?" ... "Thoughts, anyone?"

**Rationale:**
The participant struggles to synthesize evidence into scope-narrowing conclusions. When told "None of the PROD deployment timings line up exactly" and "PaymentService is throwing errors consistently — but there's been no change on it for a long time," they still order blanket rollbacks rather than narrowing to PaymentService. After rollbacks fail, they ask the team for ideas rather than synthesizing what's been ruled out. The narrowing to the cert issue is driven by Daniel and Tanya's investigation, not participant synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "What are the implications of the restart?" ... "Do we have a backend site testing method that gets around the banner? Also, I thought the banner was an actual banner. Not a frontpage."

**Rationale:**
The participant asks about restart implications, which shows some consequence awareness. However, they order blanket rollbacks of six PROD changes without weighing consequences, and the maintenance banner deployment catches them off guard (they didn't realize it would block the entire site). They don't anticipate secondary failure modes after the first restart fails. The single "what are the implications" question earns tier 2 but not tier 3.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Ok. Site is still broke. Ideas, anyone?" ... "Daniel, yes do so." [re: deep dive into downstream service] ... "Tanya, follow up on Shay's thought on the cert chain."

**Rationale:**
After the blanket rollbacks fail, the participant does pivot — they stop rolling back and redirect to deep-diving the specific failing service. When the first restart fails, they don't retry the same action but instead follow the team's suggestion about the cert chain. The pivots happen, though they're somewhat passive (asking "ideas, anyone?" rather than driving the reframe). This meets tier 3 — doesn't repeat failed actions, redirects investigation.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Still scoping the issue. Will update you in 5 or 10mins." ... "Purchases can't be completed. Seems to be multiple regions." ... "Not yet. We paused some maintenance work and we're working on rolling back any changes that could be at all related."

**Rationale:**
The participant's business communications to Bez are largely vague and reactive. They don't quantify revenue impact (despite Bob providing the numbers), don't share working theories, and don't commit firm next-update times. Updates like "Still working on that" and "Team still in dark - I'm scrounging SMEs" lack substance. The later update "restart did not fix. Cert issue with ordering of cert chain. Fixing. ETA 2mins" is better but comes very late. Overall tier 2 — engaged but inconsistent.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Ok. Site is still broke. Ideas, anyone?" ... "Thoughts, anyone?" ... "Let's all put out the other theories we have. Please format list for readability."

**Rationale:**
The participant rarely synthesizes the current state of knowledge for the technical team. They don't post messages like "we've ruled out deploys, focus on PaymentService outbound now." Instead, they ask open-ended questions ("Ideas, anyone?") without framing what's been eliminated. The team drives its own narrowing (Daniel identifies PaymentService, Shay suggests cert chain) without synthesis from the IC. This is a tier 1–2 pattern.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.42** |

---

## Caveats
- L3 is a borderline 3/4 call. The participant does take the override decision, but only after Shay explicitly prompts them to "own it." Rated 3 because the ownership was reactive to prompting rather than proactive.
- M5 is a borderline 2/3 call. The participant does pivot after rollbacks fail, but the pivot is somewhat passive ("ideas, anyone?"). Rated 3 because they don't repeat the failed approach and do redirect when the team offers alternatives.
- K4 rated 2 rather than 1 because the participant does occasionally relay information (e.g., forwarding Bob's revenue numbers to Bez channel), but doesn't synthesize for the technical team specifically.

---
