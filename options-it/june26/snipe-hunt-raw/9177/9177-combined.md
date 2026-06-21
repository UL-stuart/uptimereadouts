# Post-Drill Developmental Report

This drill placed you in a live incident with systemic complexity: misleading signals, unavailable approvers, layered technical dependencies, and a team generating information faster than any one person can synthesize. The challenge is less about knowing the answer and more about how you navigate ambiguity, coordinate others, and reason through competing explanations under pressure.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you anchored on the email maintenance and DNS timing overlap as the likely cause, returning to it multiple times even after a team member explicitly stated it was unrelated to checkout. You did eventually move away from this framing, but the pivot came after repeated disconfirmation rather than from your own mechanism reasoning — asking yourself *how* email maintenance could cause payment failures.

*Growth edge:* When a correlation feels compelling, try naming the causal mechanism aloud before pursuing it. "If email maintenance caused this, the path would be X → Y → Z." If you can't articulate the mechanism, that's a signal to hold the hypothesis more loosely and invest attention elsewhere.

---

## F2 — Hidden coupling

**Operating at: Practicing**

The cert rotation from seven days prior — and its delayed impact on PaymentService — was surfaced by team members rather than through your own investigation. After the first restart failed to resolve the handshake errors, you escalated to Tanya but didn't reframe the problem yourself: the post-restart failure was structurally different from the original, and that distinction carried diagnostic weight you didn't leverage.

*Growth edge:* When a remediation fails, pause to ask what the failure *tells* you. A restart that doesn't fix a handshake error is different information than a restart that doesn't fix a timeout. Naming that difference aloud can unlock the next investigative step without waiting for someone else to surface it.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You handled the unavailability of key approvers systematically — moving from Hamed to Tinus to Bez, acknowledging each constraint, and ultimately taking ownership of the restart decision yourself when the chain was exhausted. You named the access gap clearly when authorising the action.

*Growth edge:* When pulling someone off another commitment (like a vendor call), explicitly naming the trade-off — even briefly — helps the team understand your reasoning and builds trust in the decision. The cost acknowledgement doesn't need to be long, just present.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the approval chain to exhaustion in a logical sequence and delegated parallel work to available team members — logs to one person, customer comms to another, platform investigation to a third. When the second restart was needed after the bundle fix, you authorised without re-litigating the approval path, which showed you'd internalised the earlier decision.

*Growth edge:* Try naming the dependency structure earlier and as a single statement: "We need approval from X, access from Y, and a fix from Z — here's the order I'm pursuing." This gives the team a map of what's blocking progress and lets them self-organise around it rather than waiting for sequential instructions.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

The initial signal environment was noisy — webhook failures, change records, email maintenance — and you were drawn to the loudest signal rather than filtering toward the service most likely to explain the symptom. Once team members pulled PaymentService logs and identified the handshake failure, you followed their lead, but the filtering work was largely done for you rather than by you.

*Growth edge:* When multiple signals compete for attention, try a quick triage pass: "Which of these could *mechanistically* produce zero successful transactions?" That question alone would have pointed toward PaymentService earlier, since email maintenance has no path to blocking payment processing. Asking clarifying questions — which you did well at the start of the drill — is even more powerful when paired with this kind of filtering logic.

---

## Looking Ahead

You showed clear strength in ownership and coordination: you claimed the incident lead role, worked through access constraints methodically, and kept people tasked throughout. The consistent growth edge across this run is in *independent reasoning under noise* — forming your own causal models, using failed actions as diagnostic information, and filtering signals by mechanism rather than timing. On your next rep, try treating each piece of disconfirming evidence as a gift: it's one fewer place the problem can hide.# Facets Analysis — 9177

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." ... "hi @tanya - this appears to be maintenance related based on Logs - webhook delivery failed"

**Rationale:**
The participant echoed Shay's email-maintenance framing multiple times and pursued it as the leading hypothesis even after Tanya explicitly stated "The email maintenance is paused and not connected to checkout." The participant eventually pivoted away from the email lead, but only after repeated NPC disconfirmation and after logs pointed clearly to PaymentService. The pivot was reactive to accumulated disconfirming evidence rather than driven by mechanism reasoning, placing this solidly in tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "PaymentService hasn't restarted since before the cert rotation. It's still running the same process from 14 days ago." ... "We did a restart just now, but the handshake errors are still happening. The process is running, but outbound SSL is failing." ... "@tanya please urgently check this"

**Rationale:**
The participant did not independently surface the "what changed beyond 24 hours" question — it was NPCs (Shay/Daniel) who surfaced the cert rotation from 7 days ago. After the first restart failed, the participant did not reframe the problem themselves; they simply asked Tanya to "urgently check this" and Daniel for "next steps." The participant did not articulate that the post-restart failure was structurally different from the original. They engaged with the cert thread only after NPCs drove it, and the reload-vs-restart distinction was surfaced entirely by NPCs. This is tier 2: pivoting only after concrete failure and NPC redirection, without independent mechanism reasoning.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@tinus - are you available as Hamed is OOO?" ... "he is at the same event, we need his approval to proceed" ... "I authorise the restart as Tinus and Hamed are unavailable"

**Rationale:**
The participant accepted Hamed's auto-reply and moved to Tinus, accepted Tinus's auto-reply and attempted Bez, then took ownership when the chain was exhausted. They named the access constraints ("Tinus and Hamed are unavailable") when authorising the restart. However, they pulled Tanya off the vendor call without articulating the cost trade-off, and they pinged Bez multiple times after Bez stated inability to approve. This shows systematic handling of the escalation chain but without the explicit cost-trade-off verbalisation or batching that would indicate tier 4.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "I authorise the restart as Tinus and Hamed are unavailable" ... "I have authorised due to hamed and Tinus' absence" ... "I autorise another restart. Please proceed"

**Rationale:**
The participant walked the escalation chain to exhaustion in observable order (Hamed → auto-reply → Tinus → auto-reply → Bez → unable → self-authorisation), satisfying tier-3 path (b). They delegated parallel work to available NPCs (Daniel on logs, Shay on banner, Tanya on platform). On the second restart (after bundle fix), they authorised without re-litigating the approval chain. However, they did not name the dependency structure aloud as a single enumerated constraint statement proactively — the naming came only at the point of authorisation — and the sequencing of cert fix + approval wasn't explicitly coordinated in advance, which limits this to tier 3 rather than 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "hi @tanya - this appears to be maintenance related based on Logs - webhook delivery failed" ... "@daniel can you confirm CHG90433 isn't related?" ... "Cert has expired - 15-day and 7-day alerts"

**Rationale:**
The participant was initially captured by the loudest signal (email maintenance/webhook delivery) rather than filtering to the relevant service. They did eventually focus on PaymentService after NPCs directed attention there, and they noted the cert expiry once Tanya surfaced it. However, they did not independently drive filtering (NPCs pulled PaymentService logs and identified the handshake failure), did not catch the reload-vs-restart distinction from the runbook, and did not reason about absence of signal. The bundle issue was entirely surfaced and resolved by NPCs. This is tier 2: accepting NPC summaries without further interrogation, engaging with key concepts only after NPCs surface them.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.40** |

---

## Caveats
- F1: The participant's repeated echoing of Shay's email-maintenance framing ("I keep coming back to the email maintenance") is borderline tier 1/2. I rated tier 2 because they did eventually pivot away and pursue PaymentService, though the pivot was slow and reactive.
- F4: The boundary between tier 3 and tier 4 is close. The participant did authorise the second restart without re-litigating, which is a tier-4 signal, but the overall dependency-structure verbalisation was minimal and reactive rather than proactive.
- F2: The participant never articulated the reload-vs-restart distinction or the "different failure" framing themselves — these were entirely NPC-driven. The rating could arguably be tier 1, but the participant did engage with the cert thread once surfaced and moved forward, which places them in tier 2.

------

# Markers Analysis — 9177

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "That would be me." ... "I authorise the restart as Tinus and Hamed are unavailable," ... "I have authorised due to hamed and Tinus' absence"

**Rationale:**
The participant explicitly identifies themselves as the incident leader and takes the override decision when both approvers are unavailable. They direct team members throughout and make the restart call. However, they don't proactively name the cost or consequences of the override ("blowback's on me") — they simply state the authorization. This meets tier 3 but lacks the explicit cost-naming of tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob can you please elaborate?" ... "How many customers are blocked right now? Are we talking full checkout outage or just some regions? What's the revenue loss per minute?"

**Rationale:**
The participant's first action after Bob's complaint is to ask for elaboration, and they follow up with scope-validating questions about regions, volume, and revenue impact before taking remediation actions. They gather information before declaring the incident or ordering rollbacks. This meets the tier 3 expectation of scope-validating before acting.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@daniel @shay I can see various changes made in relation to checkout service recently. Can you verify these didn't have impact?" ... "There was an automated change on checkout service which links to payment - related? CHG90432"

**Rationale:**
The participant asks about recent changes and has the team verify them. However, they don't use the change log as a candidate-elimination pass — they don't synthesize the absence of a mechanism connecting changes to the failure. They also repeatedly pursue the email maintenance correlation despite Tanya's explicit statements that it's unrelated. They asked the question but didn't effectively use the answers to narrow scope.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@daniel please start pulling logs, @bob tell customers we are investigating" ... "@shay please do so" ... "@shay work with Tanya and check change records" ... "@tanya please prioritise this over the maintenance session"

**Rationale:**
The participant consistently names specific people for specific tasks throughout the drill. They direct Daniel to pull logs, Shay to deploy the banner and check change records, Tanya to investigate platform-side issues, and Bob to handle customer communications. The routing is generally appropriate, though there are some instances of asking people to do things outside their access (asking Shay/Daniel to assist with Tanya's vendor session).

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@daniel please start pulling logs, @bob tell customers we are investigating" ... "@shay work with Tanya and check change records"

**Rationale:**
The participant does delegate to multiple people, but the investigation largely proceeds sequentially — one thread at a time. After asking Daniel to pull logs, they wait for results before moving to the next step. There are a few instances of parallel tasking (Daniel on logs + Bob on comms), but the technical investigation itself is mostly serial rather than fanning out multiple distinct technical threads simultaneously.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya please prioritise this over the maintenance session" ... "@hamed can you assist here please?" ... "@tinus - are you available as Hamed is OOO?" ... "Hi @bez I require your assistance with approval for restarting of payments service, can you reach Tinus?"

**Rationale:**
The participant escalates Tanya off the vendor call when needed and works through the approval chain (Hamed → Tinus → Bez) when the restart is blocked. They persist through auto-replies and eventually take ownership of the decision themselves. However, the escalation to Bez lacks a crisp context handoff, and they spend several messages trying to get Bez to approve something Bez can't approve before accepting they need to self-authorize. This meets tier 3 but lacks the efficiency and cost-naming of tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "hi @tanya - this appears to be maintenance related based on Logs - webhook delivery failed" ... "Checkout service appears to be where the errors lie."

**Rationale:**
The participant forms an implicit hypothesis around the email maintenance correlation and pursues it, but doesn't explicitly name it as a hypothesis or articulate a mechanism. When Tanya repeatedly states the maintenance is unrelated, the participant continues to push the email maintenance angle ("timing overlap confirmed — worth investigating"). They eventually shift focus to PaymentService but don't explicitly articulate hypotheses or propose clear tests. The hypothesis formation is implicit and inconsistent.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "IF not impacting, then no." ... "@daniel let's do a deep dive into payment services"

**Rationale:**
The participant does eventually narrow to PaymentService based on team findings, but they don't produce synthesis statements that combine evidence to rule things out. They rely heavily on the team (Daniel, Shay, Tanya) to do the narrowing for them rather than actively synthesizing. They dismiss the UAT change but don't articulate what's been ruled out alongside what remains. The narrowing happens but is largely team-driven rather than participant-driven.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "Can we restart the checkout or payment service?" ... "Please proceed. I have let Bez know." ... "I autorise another restart. Please proceed"

**Rationale:**
The participant does not explicitly consider consequences before high-impact actions. They order the restart without asking "is it safe?" or considering what could go wrong. When pulling Tanya off the vendor session, they don't acknowledge the 2-week cost. The restarts are authorized without weighing potential secondary failures. Daniel and Tanya actually push back on the restart multiple times, noting it won't fix the issue, but the participant insists without articulating why or considering consequences.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "How can we fix this to retrieve the local issuer cert" ... "@tanya let me know when to re test"

**Rationale:**
After the first restart fails, the participant doesn't simply retry the same action — they ask Tanya to urgently check what's happening, and when the cert chain bundle issue is identified, they pivot to fixing the bundle order. They don't get stuck in a loop of retrying restarts. However, earlier in the drill they persisted with the email maintenance hypothesis longer than warranted despite Tanya's repeated denials. The adaptation after the failed restart meets tier 3.

---

## M5 — Adapts approach when initial path isn't working

*Already scored above.*

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Total checkout failure, Could be DNS related, TBC" ... "I have authorised due to hamed and Tinus' absence" ... "ETA around a minutte"

**Rationale:**
The participant's business communications are sparse and lack substance. The update to Bez ("Total checkout failure, Could be DNS related, TBC") is brief and doesn't quantify impact, commit a next-update time, or provide a working theory in business terms. Later communications to Bez are focused on getting approval rather than providing status updates. There's no proactive cadence of substantive updates — Bez has to ask for updates multiple times.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Checkout service appears to be where the errors lie. @tanya can you assist the team with investigating further here" ... "@tanya in this case let's focus on the handshake failure."

**Rationale:**
The participant makes some directional statements to the team but doesn't produce clear synthesis messages that name what's been ruled out and what remains. They don't summarize the state of the investigation at decision points. The team largely self-organizes around the evidence (Daniel and Shay do the synthesis work), and the participant's contributions to team orientation are brief and lack the "ruled in / ruled out" framing expected at tier 3.

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
- The participant persisted with the email maintenance hypothesis despite repeated NPC denials, which affected multiple markers (M2, M3, C3). This is a consistent pattern rather than isolated instances.
- For M4, the participant's insistence on restarting despite Daniel's repeated pushback ("Restarting PaymentService won't fix the issue") could be read as either ignoring consequences or having a valid intuition (the restart did eventually help surface the cert issue). Per anti-outcome-bias, I rated based on the absence of explicit consequence-weighing language rather than the outcome.
- K2 is a borderline 1/2 call — the participant does provide some information to Bez but it's minimal and reactive rather than proactive. Rated 2 because there is *some* engagement with business communication, just inconsistent and lacking substance.

---