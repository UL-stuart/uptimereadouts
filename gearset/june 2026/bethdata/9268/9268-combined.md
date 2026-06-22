# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to navigate systemic complexity under pressure — sorting misleading signals from real causes, working through access constraints, and coordinating a team when the path forward isn't obvious. This report covers what showed up in your run and where the growth edges are for your next rep.

---

## F1 — Misleading correlations

**Operating at: Not yet evident**

Early in the drill, you locked onto the email maintenance timing as your leading hypothesis and pursued a rollback even after a team member explicitly disconfirmed the mechanism — noting that email confirmations were still going out and the maintenance hadn't touched the relevant system. Ordering the rollback past that direct disconfirmation shows the correlation was driving your actions rather than mechanism reasoning. You did eventually move on once the rollback produced no change, but that pivot was reactive to experimental failure rather than to the evidence already available.

*Growth edge:* When a teammate names a specific reason why a correlation can't be causal, treat that as a filter — not as something to override with "roll back anyway." Practice pausing to ask yourself: "What mechanism would connect these two things?" before committing to action on a timing coincidence.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the certificate thread once a teammate surfaced the week-old rotation, and you asked reasonable follow-up questions about why the new cert wasn't being picked up. However, you didn't independently frame the question of what might have changed beyond the 24-hour window, and when the first restart didn't resolve the issue, you didn't articulate how the post-restart error differed structurally from the pre-restart error. The team drove the investigation to the bundle-ordering issue while you followed their framing.

*Growth edge:* Practice expanding your change-window scan beyond the obvious recent timeline. When a fix doesn't work, name what's different about the new failure state — that reframing is what surfaces hidden coupling layers.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You encountered multiple unavailable team members and did eventually walk the escalation chain to find someone who could authorize action. However, you re-pinged a teammate after already receiving their auto-reply, and when you needed a key person pulled off another engagement, you routed that through a third party rather than articulating the cost trade-off yourself. You never explicitly named the access constraint pattern — that key approvers were unavailable and this was shaping your options.

*Growth edge:* When you hit an auto-reply or unavailability signal, name the constraint out loud for the team: "Hamed is out, Tinus is out — here's what that means for our options." This makes the constraint visible and helps you reason about workarounds rather than retrying the same path.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You did ultimately take the override decision on the restart authorization, claiming delegated authority and directing the action. That moment showed ownership. However, you arrived there only after a senior stakeholder explicitly pushed the decision back to you as incident lead. You didn't proactively name the coordination bottleneck or sequence the escalation chain before NPCs raised it. Your delegation also tended toward serial rather than parallel — you largely followed investigation threads one at a time rather than fanning out work to multiple people simultaneously.

*Growth edge:* Practice naming the dependency structure early: "I need X to happen, which requires Y's approval, and Y is unavailable — so here's my plan." Proactive sequencing reduces the back-and-forth that slows resolution. Also look for moments where two people could be working different threads at the same time.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked for logs and system health checks, which is appropriate, but your requests were broad ("can someone check system health and logs?") rather than targeted at the specific service showing failures. You accepted teammate summaries and followed their filtering rather than driving the triage yourself. Key distinctions — like the reload-versus-restart difference in the runbook, or the bundle ordering issue — were surfaced by teammates rather than caught through your own directed investigation.

*Growth edge:* When you ask for logs, name the specific service and the specific signal you're looking for. Targeted requests produce faster, more useful answers and help you maintain ownership of the diagnostic thread rather than waiting for teammates to synthesize for you.

---

## Looking Forward

You showed a willingness to step up and make decisions under pressure — particularly when you claimed authority for the restart. That ownership instinct is a real asset. For your next rep, the biggest leverage comes from slowing down at two moments: before committing to a hypothesis (ask "what's the mechanism?") and before delegating (ask "who specifically, and what exactly am I asking them to find?"). Those two pauses will shift you from reactive to directive, which is where the next level of incident leadership lives.# Facets Analysis — 9268

## F1 — Misleading correlations

**Rating:** 1

**Evidence:**
> "ok, can that change be reverted easily?" ... "@tanya roll back anyway" ... "Tanya rolled back CHG90441. No change to checkout, it's still failing."

**Rationale:**
The participant adopted the email maintenance/DNS correlation as their leading hypothesis and pursued a rollback even after Tanya explicitly stated "Primary email provider hasn't been touched, it's running fine. Email confirmations are going out, so this maintenance isn't causing checkout failures." The participant ordered the rollback anyway ("@tanya roll back anyway") in the face of direct mechanism-disconfirmation from an NPC. After the rollback failed, the participant did eventually pivot, but the commitment to the prime past explicit NPC disconfirmation is the strongest possible low-skill F1 evidence per the rubric. The pivot was purely reactive to experimental failure, not mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "@tanya is the new cert not picked up? how to force that? restart service?" ... "But... payments are still failing. The service is still not recovering." ... "who can check that the cert rotation process is now ok?"

**Rationale:**
The participant engaged with the cert thread once Daniel surfaced the 7-day-old rotation (NPC-prompted, not self-initiated). After the first restart failed, the participant did not immediately reframe — instead asking "who can check that the cert rotation process is now ok?" which is a reasonable but reactive response. The participant did not articulate that the post-restart error was structurally different from the pre-restart error; they relied on NPCs (Shay: "payments service needs a two-cert bundle") to drive the investigation forward to the bundle. The "what changed beyond 24 hours" question was never self-initiated. This fits tier 2: pivots only after concrete failure, engages with the week-ago thread only when NPCs name it, and takes on NPC framing rather than driving it independently.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@hamed we are suspicious of the timing re Tanya's change..." [receives auto-reply] "@tinus I need some escalation..." [receives auto-reply] "@bez @hamed @tinus who is here to auth this?" [Hamed auto-replies again]

**Rationale:**
The participant re-pinged Hamed after already receiving the auto-reply (tier-1 signal). They also pulled Tanya off the vendor call via Bez without articulating the cost trade-off. However, they did eventually walk the escalation chain and took ownership when Bez delegated back. The participant never named the access constraints in their own words or economised on Tanya's bandwidth. The repeated pinging of auto-replied NPCs and lack of constraint articulation places this at tier 2 — walks the chain but doesn't articulate the constraint pattern.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "tanya, Bez may do this, one sec" ... "@Bez Jeffos I need you to auth Tanya to restart a service" ... "I'm at the summit but watching this thread. I don't handle technical approvals, that's for you as incident lead." ... "@tanya you will have to take my authorisation. Bez has delegated to me. Do it"

**Rationale:**
The participant eventually took the override call, but only after Bez explicitly pushed it back ("that's for you as incident lead"). The participant did not name the coordination bottleneck themselves before NPCs raised it, and the ownership reasoning was condensed to urgency rather than naming the escalation chain as exhausted. On the second restart (after bundle fix), the participant simply said "restart it" without re-litigating, which is appropriate. However, there's no evidence of proactive sequencing or parallel work delegation — the participant largely followed NPC-driven investigation threads. This fits tier 2: takes the override after explicit NPC prompting, without first articulating the dependency structure.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "can someone check system health and logs?" ... "@daniel what did you learn from that downstream app you focused on?" ... "expired cert?" ... "not sure why the process isn't picking up the new certificate"

**Rationale:**
The participant asked for logs but in a general way ("can someone check system health and logs?") rather than targeting PaymentService specifically. They accepted NPC summaries and followed NPC-driven filtering (Daniel narrowing to the downstream app, Tanya identifying the TLS issue). The participant did not independently catch the reload-vs-restart distinction from the runbook, nor did they drive the bundle investigation — Shay surfaced the bundle ordering issue. The participant engaged with key concepts once NPCs surfaced them but didn't drive the filter themselves, fitting tier 2.

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
- F1 rating of 1 vs 2 was a boundary call. The participant did eventually pivot after the rollback failed, which is tier-2 behaviour. However, ordering the rollback *after* Tanya's explicit mechanism-disconfirmation ("Email confirmations are going out, so this maintenance isn't causing checkout failures") is the rubric's "strongest possible low-skill F1 evidence." I weighted the commitment past named disconfirmation more heavily than the eventual reactive pivot, landing at 1.
- F3 rating of 2 vs 1 was also a boundary call. The re-pinging of Hamed after auto-reply is a tier-1 signal, but the participant did eventually take ownership and didn't consume excessive Tanya bandwidth on low-value questions. Rated 2 on balance.

------

# Markers Analysis — 9268

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "@tanya you will have to take my authorisation. Bez has delegated to me. Do it"

**Rationale:**
The participant takes the override decision when both Tinus and Hamed are unavailable, explicitly claiming authority delegated by Bez. They drive the response throughout — directing team members, making decisions on rollbacks and restarts. However, they don't proactively name the cost or blowback risk of the override; they only act after Bez says "If you feel confident enough on doing a restart then please go ahead." This is solid ownership but not the proactive, cost-naming tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob how many complaints, what about, and where geographically??"

**Rationale:**
The participant's very first message after Bob's alert is a multi-part clarifying question covering volume, nature, and geography. They also ask "Is this a total checkout outage or are some transactions still going through? I need clarity on scope." These are scope-validating questions before any remediation action. They don't deeply probe error patterns or payment method specifics, but the initial scoping is solid and precedes any action.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing."

**Rationale:**
The participant fixates on the email maintenance timing correlation rather than systematically reviewing the change log. They order a rollback of Tanya's change without articulating a mechanism connecting it to checkout failures, even after Tanya states "Primary email provider hasn't been touched... Email confirmations are going out, so this maintenance isn't causing checkout failures." They asked about changes but didn't use the information to eliminate candidates — they used it as a rollback queue.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "can someone check system health and logs?" ... "@tanya roll back anyway"

**Rationale:**
The participant uses some named delegation (e.g., "@tanya roll back anyway," "@daniel what did you learn from that downstream app"), but also broadcasts vague requests like "can someone check system health and logs?" twice. They don't consistently route tasks to the right person based on access boundaries — for example, asking Bob to authorize a restart when Bob has no such authority. Delegation is present but inconsistent and sometimes misdirected.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "can someone check system health and logs? I don't want to fixate on one change when it could be another thing"

**Rationale:**
The participant expresses intent to run parallel threads ("I don't want to fixate on one change when it could be another thing") but in practice works mostly sequentially — pursuing the email maintenance thread, then waiting for its rollback result, then moving to logs. They don't fan out multiple distinct tasks to multiple named people simultaneously. The investigation is largely serial rather than parallel.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@bez I may need your help with an escalation, it could be Tanya's change but she is with a customer. Anyone else that can help?"

**Rationale:**
When Hamed and Tinus are both unavailable via auto-reply, the participant escalates to Bez with context about why they need help. They work through the chain (Hamed → Tinus → Bez) without excessive delay. For the restart authorization, they eventually get Bez to delegate authority. However, the escalation to pull Tanya off the vendor call came via Bez rather than the participant directly making that call, and the restart authorization took several back-and-forth messages. Solid but not exceptional escalation.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing."

**Rationale:**
The participant forms a hypothesis about the email maintenance but doesn't explicitly frame it as a testable hypothesis or articulate the mechanism. They order a rollback as a test, but when Tanya had already stated email wasn't causing checkout failures, the participant persisted ("@tanya roll back anyway"). They don't articulate alternative hypotheses until the team surfaces them. The hypothesis work is implicit and reactive rather than explicit and structured.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "does this seem cert or dns related?"

**Rationale:**
The participant does some narrowing — asking about scope ("Is this a total checkout outage or are some transactions still going through?") and acknowledging the PaymentService handshake failure. However, they don't produce synthesis statements that combine evidence to rule things out. After the email rollback fails, they don't explicitly state "email is ruled out, moving on." Much of the narrowing is done by the NPCs (Daniel, Tanya) rather than synthesized by the participant. The question "does this seem cert or dns related?" shows uncertainty rather than evidence-based narrowing.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "can someone check system health and logs? I don't want to fixate on one change when it could be another thing"

**Rationale:**
The participant shows some awareness of not fixating on one path, but doesn't explicitly consider consequences before high-impact actions. They order the email rollback without weighing the cost to Tanya's vendor session (Bez had to intervene). They order the restart without asking "is it safe?" or considering what could go wrong. After the first restart fails, they don't anticipate secondary issues before the second restart. Consequence-weighing is largely absent from their action decisions.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "@daniel what did you learn from that downstream app you focused on?"

**Rationale:**
After the email rollback doesn't fix the issue, the participant does pivot — they move to investigating logs and the downstream service. They don't repeat the email rollback or stay stuck on that thread. After the first restart fails, they engage with the team's suggestion to check the cert bundle rather than just retrying the restart. However, the pivots are largely prompted by NPC suggestions rather than self-initiated reframing. The adaptation is present but reactive.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "May have an issue, investigating" ... "Investigating recent email change" ... "have rolled back changes, issue persists, still investigating" ... "seems to be related to a cert rotation, making progress"

**Rationale:**
The participant's business communications are brief and lack substance. They don't quantify impact in business terms, don't provide ETAs, and don't share working theories in a business-friendly frame. Messages like "May have an issue, investigating" and "have rolled back changes, issue persists, still investigating" are vague reassurances rather than substantive updates. They never commit a next-update time or frame the impact for stakeholders.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "@here any other ideas please? how can we resolve without knowing full cause?"

**Rationale:**
The participant rarely synthesizes the current state for the technical team. They don't post messages like "here's what we know, here's what's ruled out, here's where to focus." Instead, they ask open-ended questions ("@here any other ideas please?") or relay individual findings without synthesis. The technical team is largely self-directing based on their own findings rather than being oriented by the participant's synthesis of the situation.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.33** |

---

## Caveats
- L3 rating is a boundary call between 2 and 3. The participant does take the override decision, but only after Bez explicitly delegates ("If you feel confident enough... please go ahead"). Rated 3 because they do claim authority and direct the action, but it's not fully proactive.
- M5 is a boundary call between 2 and 3. The participant does pivot away from the email thread, but pivots are largely NPC-prompted. Rated 3 because they don't repeat failed actions and do engage with new directions.
- K2 updates to the business channel are consistently thin throughout the drill, never reaching the substantive threshold despite multiple opportunities.

---