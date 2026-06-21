# Post-Drill Report — Snipe Hunt

This drill puts you in the middle of a live checkout outage with multiple competing signals, constrained team availability, and a root cause that doesn't surface through obvious channels. It's designed to stress your ability to reason through misleading data, coordinate under pressure, and drive an investigation forward when the system is actively resisting simple answers.

---

## F1 — Misleading correlations

**Operating at: Not yet evident**

Early in the drill, you anchored on the email maintenance timing as the likely cause and returned to that thread repeatedly — even after a team member explicitly confirmed it was unrelated. The pivot away from that lead came when another team member surfaced payment logs, rather than from your own reasoning about why the email hypothesis didn't fit the symptoms. On your next rep, the growth edge here is building a habit of asking "what mechanism would connect this change to this symptom?" before investing investigation time. When a lead is disconfirmed, name *why* you're dropping it — that reasoning is what prevents you from circling back.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the certificate thread once it was surfaced by a team member and followed along through the fix. However, the key investigative move — asking what changed beyond the obvious 24-hour window — came from your team rather than from you. The growth edge is developing the instinct to widen the change window yourself when recent changes don't explain the symptoms. When rollbacks fail, that's a signal to ask "what else changed that we haven't looked at yet?" and to drive that question rather than waiting for someone else to raise it.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You pulled a team member off a vendor call to focus on the production issue, which shows awareness of priority. You also pinged an unavailable manager for help. However, the way you used your available team members' time could be sharper — you asked the same questions about runbook steps multiple times without integrating earlier answers, which consumed bandwidth on a constrained resource. The growth edge is batching your questions and being deliberate about what you need from each person before you ask. When someone is your only available expert, every repeated question is a cost.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

When the approval blocker surfaced — a restart needed sign-off from people who were unavailable — you took the override call. That's a meaningful ownership moment. The growth edge is in how you get there: you didn't attempt the full escalation chain (a second approver was available but never contacted), and the approval itself came without articulating why you had authority or what the cost of waiting would be. On the next rep, try naming the constraint out loud: "Hamed is out, Tinus hasn't responded, we're losing £1,000/min — I'm taking the call." That reasoning protects you and orients the team.

Your delegation pattern also showed up here — you tended to pursue one thread at a time rather than running parallel investigations, which meant team members were idle while you worked sequentially through possibilities.

---

## F5 — Data overload / buried information

**Operating at: Not yet evident**

The drill surfaced multiple error signals — frontend errors, recommendation service issues, email maintenance timing — and you engaged with the loudest ones rather than filtering toward the service most likely to explain the checkout symptom. You didn't drive log filtering yourself; the payment logs that broke the case open were surfaced by a team member's initiative. You also asked for the same information repeatedly without integrating what had already been shared. The growth edge is building a filtering discipline: when you have multiple signals, ask "which of these could actually cause the symptom I'm seeing?" before chasing each one. Absence of signal in a service is also data — if checkout is failing but the frontend is serving pages, the frontend errors are probably noise.

---

## Looking Forward

Two things to carry into your next rep. First, build the habit of stating your working theory out loud — even a wrong hypothesis, named explicitly, gives your team something to confirm or challenge, and it forces you to connect your actions to reasoning. Second, practice fanning out: when you have multiple team members available, give each a distinct task and let them work in parallel rather than sequencing everything through one person. These two shifts — explicit reasoning and parallel coordination — will change the shape of your next drill significantly.
# Facets Analysis — 9311

## F1 — Misleading correlations

**Rating:** 1

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." [Shay's nudge repeated twice] ... Participant: "@tanya - what have you cahnges in email service ?" ... "@tanya - can you shar ethe steps changed ?"

**Rationale:**
The participant repeatedly pursued the email maintenance lead even after Tanya explicitly stated "Email maintenance is paused and on hold. It's a separate system, not related to the checkout failures." The participant continued asking about email changes multiple times after this disconfirmation. They also pursued the recent deploys (rollbacks of CheckoutService, ShippingService, CartService) without mechanism reasoning, only pivoting away after each rollback failed concretely. The pivot to PaymentService came only when Daniel surfaced the payment logs showing handshake failures — not from the participant's own mechanism reasoning. This is tier 1: locked into false leads past disconfirming evidence, pivoting only when NPCs drove the investigation forward.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "can you please look into Command to verify bundle: openssl verify -CAfile /etc/ssl/certs/ca-bundle.crt payment-gateway.crt" ... "we have foudn the cert change has wrong bundle ?"

**Rationale:**
The participant engaged with the cert thread only after Daniel surfaced the payment logs and Shay/Daniel explicitly pointed to the cert rotation. The participant did not independently surface the "what changed beyond the last 24 hours?" question — this came from Daniel ("Did anything change on the platform side?"). Once the cert thread was surfaced by NPCs, the participant followed along but did not independently articulate the reload-vs-restart distinction or the week-old coupling. The bundle order issue was identified by Shay ("order's flipped"), not the participant. The participant engaged with the cert fix but was led through it by NPCs, consistent with tier 2 — engaging only when NPCs named the thread, partial connection of timestamps, taking NPC framing rather than driving it.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tanya - I would leave the maintainence at the mo as we have Prod down so i need you here please" ... "@hamed - can you please help here" [receives auto-reply] ... "i approve" [when Tanya says she needs Hamed or Tinus approval]

**Rationale:**
The participant pulled Tanya off the vendor call without articulating the cost trade-off explicitly — no statement like "global outage outweighs the vendor window." They pinged Hamed once and received an auto-reply but did not re-ping, which is appropriate. However, they did not name the access constraints in their own words or visibly economise on Tanya's bandwidth — instead repeatedly asking Tanya the same questions about her changes (runbook steps asked 5+ times). The participant did not batch questions or sequence escalations cleanly. The eventual ownership of the restart approval ("i approve") came without articulating the constraint pattern. This is tier 2: walks the escalation chain but does not articulate the constraint pattern or economise on constrained resources.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "i approve" ... "pease go ahead" [after Tanya says "I can't restart payments without approval from Hamed or Tinus, and both are out right now."]

**Rationale:**
The participant took the override call when Tanya raised the approval blocker, but did not walk the escalation chain (Hamed was pinged earlier for general help, not specifically for restart approval; Tinus was never contacted). The participant did not name the dependency structure or articulate why they had authority to approve. The ownership statement was minimal ("i approve") without reasoning about the escalation chain being exhausted or naming the constraint. Earlier in the drill, the participant did delegate some parallel work (asking Daniel and Shay to investigate, putting up a banner), but sequencing was largely reactive — they pursued one thread at a time (email → rollbacks → Tanya's changes → payment logs) rather than running parallel investigations. This fits tier 2: takes the override without first attempting the full escalation chain, ownership without reasoning.

---

## F5 — Data overload / buried information

**Rating:** 1

**Evidence:**
> "I keep coming back to the email maintenance" ... repeated requests to Tanya: "Send the steps please @tanya" (5+ times) ... "@tanya - i see errors with recomendation service" ... "I can see Front end errors @daniel - what do you suggest?"

**Rationale:**
The participant was captured by the loudest signals — email maintenance timing, frontend errors, recommendation service errors — rather than filtering to the relevant service. They did not filter logs to PaymentService themselves; Daniel had to surface the payment logs. They repeatedly asked Tanya for the same runbook steps (5+ times) without integrating the information already provided. When Daniel shared the developer investigation logs image showing errors across services, the participant did not use that to narrow scope. They did not reason about absence of signal or drive filtering proactively. Key distinctions (reload vs. restart, bundle ordering) were surfaced entirely by NPCs. This is tier 1: captured by noise, failed to filter or integrate information already surfaced.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 1 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 1 |
| **Mean Facet Score** | **1.60** |

---

## Caveats
- F1 borderline 1/2: The participant did eventually move off the email lead, but only because NPCs drove the investigation to PaymentService. The participant never articulated mechanism reasoning for abandoning the email hypothesis — they simply stopped asking about it when Daniel surfaced payment logs. Given the rubric's emphasis on pivot being driven by mechanism reasoning vs. concrete failure, and the participant's repeated return to the email lead after explicit disconfirmation, tier 1 is the appropriate call.
- F2: The participant reached the cert fix, but entirely through NPC guidance. The "what changed beyond 24 hours" question was never asked by the participant. The bundle fix was identified by Shay. Rating on the lower end of tier 2.
- F4: The participant never contacted Tinus for approval despite Hamed's auto-reply directing to Tinus. The escalation chain was not walked to exhaustion before taking ownership.

---
---

# Markers Analysis — 9311

## L3 — Takes explicit ownership of the response

**Rating:** 2

**Evidence:**
> "Let me create a incident" / "i approve" / "pease go ahead"

**Rationale:**
The participant creates the incident and eventually approves the restart, but does so only after being prompted by Tanya asking "Do you want me to go ahead?" The participant never explicitly positions themselves as the decision-maker driving the response — they react to NPC prompts rather than proactively owning the call. The "i approve" is late and lacks any framing of cost or accountability.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "How many customers are blocked from checkout right now? What's the revenue loss per minute? Is this a total outage or partial?"

**Rationale:**
The participant asks scope-validating questions early — about the number of affected customers, revenue impact, and whether it's total or partial. They also reproduce the error themselves ("Yes i can validate and see the error in checkout"). These questions come before major remediation actions, meeting the novice expectation for this marker.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@daniel @shay @tanya - Can you please look into this and look for changes in the system"

**Rationale:**
The participant asks for recent changes early and receives the change log. However, they then order rollbacks of CheckoutService changes, Shipping, and CartService without articulating a mechanism connecting those changes to the symptom. They asked the question but used the answers as a rollback queue rather than a candidate-elimination pass, fitting the tier 2 description.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "@daniel @shay @tanya - Can you please look into this and look for changes in the system" / "@tanya - can you please verify the steps you have followed"

**Rationale:**
The participant uses @mentions frequently but often broadcasts to multiple people simultaneously without distinct tasks ("look into this"). Many delegations to Tanya are repetitive requests for the same information (runbook steps, changes made). The participant rarely routes tasks based on NPC access boundaries — repeatedly asking Tanya for application-level information rather than leveraging Daniel for app-side and Tanya for platform-side work.

---

## C6 — Runs parallel investigation threads

**Rating:** 1

**Evidence:**
> Repeated sequential questions to @tanya about the same topics (runbook, changes, Redis pool) without concurrent threads to other team members.

**Rationale:**
The participant works almost entirely sequentially, spending the majority of the drill asking Tanya the same questions repeatedly. There is no evidence of multiple distinct investigation threads running concurrently — Daniel and Shay are largely idle until Daniel eventually surfaces the payment logs. The participant does not fan out distinct tasks to different people in parallel.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "@hamed - can you please help here" / Then after Hamed's auto-reply, no follow-up to Tinus or alternative escalation path.

**Rationale:**
The participant pings Hamed but receives an auto-reply directing them to Tinus for approvals. The participant does not follow up with Tinus or articulate a Plan B. Later, when Tanya says she can't restart without approval, the participant simply says "i approve" without naming authority or cost. The escalation lacks context and follow-through.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Can you pleas eupdate" / "Can you please rollback those changes @tanya" / repeated requests for Tanya's runbook steps without articulating why.

**Rationale:**
The participant never explicitly articulates a hypothesis. They order rollbacks (CheckoutService, Shipping, CartService) without stating what they believe is causing the issue or how the rollback would test that belief. The closest to hypothesis-testing is the implicit assumption that recent changes caused the issue, but this is never stated or tested on mechanism. Actions are taken without linked reasoning.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "@bob - this is the global issue right?" / "yes its isolated to checkout only"

**Rationale:**
The participant confirms the issue is global and isolated to checkout, which provides some narrowing. However, after rollbacks fail, the participant does not synthesize the negative results to narrow scope further. They spend extensive time re-asking Tanya about changes already confirmed as unrelated. The eventual narrowing to PaymentService outbound happens largely through Daniel's initiative, not the participant's synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "Can you please rollback those changes @tanya" / "do the restart" / "pease go ahead"

**Rationale:**
The participant orders rollbacks and restarts without any "is it safe?" checks or consideration of side effects. When pulling Tanya off the vendor call, there's no acknowledgment of the 2-week cost. The restart is ordered without verifying the bundle state first. No evidence of consequence-weighing before any action throughout the drill.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> After multiple failed rollbacks, the participant eventually asks "ok, @shay @daniel - any more suggestions?" and agrees to deep-dive into the specific downstream service.

**Rationale:**
The participant does eventually shift away from rollbacks, but only after multiple failures and largely at the NPCs' suggestion ("Want us to deep dive into that service specifically?"). The pivot is reactive rather than proactive — the participant asks the team for suggestions rather than synthesizing the failed rollbacks into a new direction themselves. This is inconsistent adaptation driven by NPC nudging, fitting tier 2.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "@bez - its a global outage and revenue is £1000/min" / "not yet, we are tried to rollback changes we have deployed" / "We are woking on this Bez. Looking at the changes today"

**Rationale:**
The participant provides some quantification (revenue loss) early on, which is positive. However, subsequent updates to Bez are vague ("we are working on this," "not yet") without a working theory, next-update commitment, or concrete ETA. The updates lack the substance expected at tier 3 — no current hypothesis, no committed timeline, no structured business framing.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 1

**Evidence:**
> No synthesis statements to the technical channel summarizing what's been ruled out or what the current working picture is.

**Rationale:**
The participant never posts a synthesis message to the team summarizing the state of the investigation. They ask individual questions but never consolidate findings ("rollbacks didn't help, so it's not recent deploys; focus on X"). The team receives no orientation from the participant about what's been eliminated or what the current focus should be. Daniel and Shay eventually self-direct to the payment logs without IC guidance.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 2 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 1 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 1 |
| **Mean Marker Score** | **1.83** |

---

## Caveats
- The participant's repeated requests to Tanya for the same runbook information (asked 5+ times) consumed significant drill time and made it difficult to assess whether the participant had a mental model they were testing or was simply stuck in a loop. I rated M2 conservatively at 2 rather than 1 because the rollback actions do imply an implicit (if unarticulated) hypothesis.
- The participant did reach resolution (cert bundle fix + restart), but per anti-outcome-bias instructions, this outcome did not influence ratings. The resolution was largely driven by NPC initiative (Daniel surfacing payment logs, Shay identifying the bundle order issue).
- C7 is a borderline 1/2 — the participant did ping Hamed, which is more than zero escalation effort, but the lack of follow-through to Tinus and the absence of context in the escalation keeps it at 2.

---