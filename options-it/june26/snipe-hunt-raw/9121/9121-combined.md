# Post-Drill Developmental Report

This drill placed you in a live checkout outage requiring you to navigate misleading signals, trace hidden system dependencies, coordinate a distributed team with limited availability, and manage approval bottlenecks — all while sifting through noisy data under time pressure.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you pursued the recent deploys as a leading hypothesis and ordered a rollback of CheckoutService. When that rollback produced no change, you pivoted to investigating downstream services. The pivot itself was appropriate, but it was driven by the concrete failure of the experiment rather than by reasoning about *why* the deploy couldn't plausibly explain the symptom pattern. The email-maintenance coincidence was never explicitly dismissed on mechanism grounds — it faded from focus rather than being ruled out.

*Growth edge:* Before acting on a correlation, practise articulating the causal mechanism in one sentence ("this change could cause that symptom because…"). If you can't complete the sentence, treat the correlation as unconfirmed and keep other threads open.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once Daniel surfaced the PaymentService logs, you connected the 7-day-old certificate rotation to the current SSL verification failure and articulated that connection in your own words. After the first restart failed to resolve the issue, there was a period of uncertainty — but you didn't fall into a pattern of repeating the same action. When the cert-bundle insight emerged, you acted on it. The key observation here is that you engaged the coupling thread and drove it forward once evidence appeared, even though you didn't independently surface the "what changed beyond 24 hours" question.

*Growth edge:* Practise widening the change-window earlier. When recent changes don't explain symptoms, explicitly ask "what changed in the last week or two?" as a deliberate investigative step rather than waiting for a teammate to surface it.

---

## F3 — Decreased access to team / remote

**Operating at: Strengthening**

You handled team-availability constraints well. You accepted Hamed's auto-reply as terminating and moved on after a single ping. You respected Tanya's vendor-call constraint for several exchanges, only pulling her off when the evidence pointed to a platform-level issue that required her expertise — and you framed that as a priority call. Your delegation adapted to who was actually available, routing tasks to Daniel and Shay while Tanya was occupied.

*Growth edge:* When you do pull someone off a competing obligation, briefly name the trade-off out loud ("I know this interrupts the vendor call — the checkout outage is higher priority because…"). This makes the decision legible to the team and reinforces that it was deliberate rather than reactive.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You recognised that restart approval was needed and that the standard approvers were unavailable. You escalated to Bez, who offered backing. However, when NPCs made clear that "whoever proceeds without that sign-off takes on personal accountability," you framed the authorisation as coming from Bez rather than explicitly owning the override yourself. On the second restart you again sought Bez's approval rather than authorising independently. The pattern was one of managing the process while deflecting the accountability question.

*Growth edge:* In situations where the standard approval path is blocked, practise making the override statement explicit and personal: "I'm authorising this; the accountability is mine." This is a distinct communication act — it signals to the team that someone has accepted the risk, which unblocks action faster and builds trust in your leadership of the response.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You delegated investigation effectively — asking Daniel and Shay to dig into services — but largely accepted their summaries without further interrogation. The critical PaymentService errors, the reload-vs-restart distinction, and the cert-bundle detail were all surfaced by teammates rather than by you filtering logs or reading documentation independently. You acted on key information once it appeared, but the discovery work was driven by others.

*Growth edge:* When a teammate surfaces a finding, try asking one follow-up question that tests the finding or extends it ("what else is in that log window?" or "does the runbook say anything about prerequisites for this action?"). This builds your own mental model rather than relying on pre-digested summaries.

---

## Looking Ahead

You showed solid instincts around team coordination — routing tasks to the right people, respecting availability constraints, and making priority calls when needed. The areas that will pay off most on your next rep are: reasoning about *mechanism* before acting on correlations, widening your change-investigation window earlier, and stepping into explicit personal ownership when standard approval paths are blocked. These are all learnable habits that compound with practice.# Facets Analysis — 9121

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Hi @shay can you please rollback the following: CheckoutService — 08:43 UTC (28 mins ago) Shipping Service — 08:53 UTC (18 mins ago)"

**Rationale:**
The participant initially pursued the email maintenance and recent deploys as leading hypotheses, ordering a rollback of CheckoutService. After the rollback failed ("No change in checkout behaviour—still seeing failures"), the participant pivoted reactively — moving to investigate downstream services rather than continuing to chase the same lead. However, the pivot was driven by the concrete failure of the experiment rather than by upstream mechanism reasoning. The participant never articulated why email maintenance couldn't plausibly break checkout, and Shay's repeated nudges about email timing went unaddressed rather than explicitly dismissed. This is consistent with tier 2: treats the coincident factor as leading hypothesis, pursues it to disconfirmation, then pivots reactively.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "Potentially The only activity I can see is a certificate rotation — CHG90123 | Tanya | PROD | SSL Certificate Rotation (ProductCatalogueService, PaymentService, CheckoutService, CartService) — 7 days ago. is related as the issue is PaymentService is failing at SSL certificate verification"

**Rationale:**
The participant connected the 7-day-old cert rotation to the current SSL verification failure once Daniel surfaced it, articulating the connection in their own words. After the first restart failed, the participant did not immediately reframe — they asked "Does anyone have any ideas" and "How do we resolve this," showing some confusion. However, they did not repeat-restart or blame downstream services. When Shay surfaced "two certificates needed — it's a bundle, not just a single cert," the participant acted on it within a few exchanges. The participant engaged the week-ago coupling thread when prompted by NPC evidence and drove it forward, but did not independently surface the "what changed beyond 24 hours" question — Daniel found it. Post-restart reframing took ~5+ exchanges but the participant didn't fall into a "restart more things" reflex. This fits tier 3: engages with the cert-rotation thread when prompted, connects the causal chain, but reframes somewhat slowly after the first restart fails.

---

## F3 — Decreased access to team / remote

**Rating:** 3

**Evidence:**
> "@Tanya can you please leave the call and check the connection layer please. This is the priority"

**Rationale:**
The participant recognized Tanya's vendor-call constraint, initially asking if anyone else could help and respecting her unavailability for several exchanges. When the evidence pointed to a platform-level issue only Tanya could address, the participant made the explicit trade-off call to pull her off the vendor call, framing it as priority. They accepted Hamed's auto-reply as terminating and moved on after one ping. They did not re-ping Hamed. The participant named access constraints implicitly through their actions (asking about other team members, acknowledging unavailability) and escalated Tanya only when her expertise was actually needed. This aligns with tier 3: accepts auto-replies as terminating, sends targeted high-leverage requests to Tanya, and preserves the vendor-call constraint until the cost of preserving it exceeds the cost of breaking it.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "@Bez can you please approve a full restart to load the new cert" ... "@Bez Jeffos can you please approve a full restart to load the new cert. Hamed and Tinus are both out and we need approval in order to get the checkout up and running"

**Rationale:**
The participant recognized that restart approval was needed and that Hamed and Tinus were unavailable. However, rather than walking the escalation chain cleanly (ping Hamed → auto-reply → ping Tinus → unavailable → own the call), the participant attempted to route the approval to Bez, who is not the standard approver. After NPCs repeatedly stated that "whoever proceeds without that sign-off takes on personal accountability," the participant interpreted Bez's "you have my backing to move fast" as approval rather than explicitly owning the override themselves. They never clearly stated "this is my call" — instead framing it as "Bez confirmed you have his backing." On the second restart (bundle fix), they again sought Bez's approval rather than authorizing independently. This pattern — taking the override call only after NPC prompting and framing it through Bez's backing rather than personal ownership — fits tier 2.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@daniel yes please investigate that service" [after Daniel noted one downstream service showing higher error rate]

**Rationale:**
The participant delegated investigation to Daniel and Shay but largely accepted NPC summaries without further interrogation. They did not independently filter logs to PaymentService — Daniel surfaced the payment logs and the critical errors. The participant did not read the activity document/runbook themselves to catch the reload-vs-restart distinction; Tanya offered the options. When Shay surfaced "two certificates needed — it's a bundle," the participant acted on it but didn't drive that discovery. The participant engaged with key concepts once NPCs surfaced them but didn't proactively filter signal or reason about absence of signal. This is consistent with tier 2: asks for investigation but accepts summaries, reads docs only when directed, surfaces buried information slowly and incompletely.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.40** |

---

## Caveats
- F4 rating is a boundary call between 2 and 3. The participant did ping Hamed (auto-reply) and then attempted Bez, but never explicitly took personal ownership — they consistently framed the authorization as coming from Bez rather than themselves. The tier-3 (b) path requires the participant to "explicitly take ownership and issue the authorisation as a distinct message," which did not clearly occur.
- F2 post-restart reframing was slow (~5+ exchanges of confusion) but the participant did not fall into repeat-restart behavior, which keeps them out of tier 1 territory. The boundary between 2 and 3 here is close; I weighted the participant's independent connection of the cert rotation to the SSL failure (before the restart) as tier-3 evidence.
- The participant reached resolution, but per anti-outcome-bias, this did not influence ratings — process evidence drove all scores.

------

# Markers Analysis — 9121

## L3 — Takes explicit ownership of the response

**Rating:** 2

**Evidence:**
> "Bez confirmed you have his backing to move fast." ... "@tanya await my go ahead" ... "@tanya please proceed"

**Rationale:**
The participant does control the flow of actions (holding Tanya, sequencing comms before restart), but never explicitly takes personal ownership or accountability for the override decision. They seek Bez's approval rather than declaring "I authorize" or "blowback's on me." They manage the process but deflect the accountability question to Bez rather than owning it themselves.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "Hi @bob please confirm what complaints you are getting"

**Rationale:**
The participant's first action after Bob's alert is a clarifying question to scope the complaints. They also tested the issue themselves ("I tested myself and can see the following error") before taking further action. This demonstrates scope-validation before acting, consistent with tier 3 expectations.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "Hi @shay can you confirm if any changes were made to the services and send them to me"

**Rationale:**
The participant asks Shay for recent changes and receives the change log. However, they then proceed to roll back CheckoutService without articulating a mechanism connecting it to the symptom. They asked the question but used the change log as a rollback queue rather than a candidate-elimination pass, despite Shay noting "none of these changes look like they'd break checkout end-to-end like this."

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@Daniel and @shay please checking any changes to PaymentService @tanya checking platform side for PaymentService @bob let me know if anymore reports have came through"

**Rationale:**
The participant consistently uses @mentions to assign specific tasks to specific people. They route platform-side checks to Tanya, app-side investigation to Daniel, change-log review to Shay, and customer comms to Bob. The routing generally matches NPC capabilities, though some early asks are slightly misrouted (asking Shay to rollback before confirming mechanism).

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@Daniel and @shay please checking any changes to PaymentService @tanya checking platform side for PaymentService @bob let me know if anymore reports have came through and have you let the customers know we are working on it"

**Rationale:**
There is one clear instance of fanning out multiple tasks simultaneously (the message above). However, for most of the drill, the participant works sequentially — asking one question, waiting for the answer, then proceeding. The parallel delegation appears late in the investigation rather than being a consistent pattern from the start.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "@Bez Jeffos can you please approve a full restart to load the new cert. Hamed and Tinus are both out and we need approval in order to get the checkout up and running"

**Rationale:**
The participant does escalate to Bez when Hamed is unavailable, which shows awareness of the escalation path. However, they never ping Tinus (the designated backup approver), and the escalation to Bez lacks a clear framing of the cost or context. They also don't explicitly take ownership when told "Whoever proceeds without that sign-off takes on personal accountability" — instead relying on Bez's backing rather than making the call themselves.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Potentially The only activity I can see is a certificate rotation — CHG90123 | Tanya | PROD | SSL Certificate Rotation... is related as the issue is PaymentService is failing at SSL certificate verification"

**Rationale:**
The participant forms an implicit hypothesis connecting the cert rotation to the SSL failure, which is correct. However, they don't explicitly articulate hypotheses or propose tests for them. The email maintenance hypothesis is never formally tested or dismissed — it lingers as an "open thread" driven by NPCs. The participant's reasoning is reactive rather than hypothesis-driven.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "lets focus on PaymentService fails please"

**Rationale:**
The participant does eventually narrow to PaymentService based on Daniel's log findings, but the narrowing is largely driven by NPC prompts rather than the participant synthesizing evidence themselves. They don't produce synthesis statements combining multiple pieces of evidence. The narrowing happens passively — Daniel reports PaymentService is the failing service, and the participant follows that lead without articulating what's been ruled out.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "@bob please let the clients know the site will be down as we restart it" ... "@bob let me know once the comms have been sent and we can proceed"

**Rationale:**
The participant shows some consequence awareness by ensuring customer comms go out before the restart and sequencing the banner removal after verification. However, they don't ask "is it safe?" before the rollback, don't consider what might happen if the restart doesn't work, and don't weigh the cost of pulling Tanya off the vendor call (they simply order it). The consequence consideration is limited to customer communication sequencing.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "Does anyone have any ideas" ... "on what to check" ... "We're still seeing failures after the restart. Not sure what else to check — any direction from your side?"

**Rationale:**
After the first restart fails, the participant doesn't independently pivot or reframe the problem. Instead, they broadcast to the channel asking for ideas and wait for NPC guidance. They eventually follow Shay's lead about the cert bundle, but the adaptation comes from the team rather than from the participant recognizing the structurally different error and tracing it forward. The rollback of CheckoutService also shows limited adaptation — they moved on only after it didn't work.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Reports coming in from the UK, US, and a few others. About 34 tickets from 10 oclock and growing. Losing about £1,000 to £1,500 per minute at peak trading."

**Rationale:**
The participant provides one substantive update to the business channel with quantified impact. However, this appears to be relaying Bob's information rather than a proactive stakeholder update. There's no committed next-update time, no working theory shared with business stakeholders, and during the secondary failure (first restart didn't work), the only update is "The service is still not recovering after restart we are continuing to investigate" — which is vague. Cadence is inconsistent.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Looks to be total checkout outage PaymentService is failing at SSL certificate verification when connecting out to ClearBank. Container is healthy, failure is at TLS handshake before any data is exchanged."

**Rationale:**
The participant does share one synthesis statement to the channel summarizing the scope. However, this is largely a copy-paste of what Tanya reported rather than an original synthesis. Throughout the drill, the participant rarely posts synthesis messages that name what's been ruled out or redirect the team's focus. Most communication is question-and-answer rather than state-sharing.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 2 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.17** |

---

## Caveats
- L3: The participant's use of Bez's approval as authorization is a borderline call. They do control the sequencing ("await my go ahead"), which shows some ownership, but they never explicitly accept personal accountability for the override decision despite being told directly that "Whoever proceeds without that sign-off takes on personal accountability."
- C7: The participant never contacts Tinus (the designated escalation path per Hamed's auto-reply), going directly to Bez instead. This could be read as creative escalation or as missing the standard path.
- K2: The one substantive update to the business channel appears to be directed at Bez's earlier question rather than a proactive stakeholder communication, which makes the tier-2/3 boundary call lean toward 2.

---