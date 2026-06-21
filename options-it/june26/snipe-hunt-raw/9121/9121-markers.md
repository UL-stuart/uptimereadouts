---

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