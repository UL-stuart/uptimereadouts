---

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