---

# Markers Analysis — 9317

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "@tanya - In there absence i approve to restrart the payment sevrice"

**Rationale:**
The participant takes the override decision when both Hamed and Tinus are unavailable, explicitly stating they approve the restart. Throughout the drill they direct team members and make decisions. However, they don't explicitly name the cost or consequences of overriding ("blowback's on me"), which would elevate to tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "How many customers are blocked from checking out? What's the estimated revenue loss per minute right now?" ... "Is this a total checkout outage or are some transactions still going through? I need to know the scope."

**Rationale:**
The participant's first substantive moves after Bob's alert are scope-validating questions about the number of affected customers, revenue impact, and whether it's a total or partial outage. They ask multiple clarifying questions before taking any remediation action, meeting the tier 3 expectation of scope-validation before acting.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "@tanya - please checek the changes you have done today so as @daniel & @shay" ... "Thanks Shay, may not be related to these changes"

**Rationale:**
The participant explicitly asks all three team members to review their recent changes. When Shay reports that deployment times don't line up with the failures, the participant acknowledges this ("may not be related to these changes") and moves on. They use the change log as a candidate-elimination pass rather than a rollback queue, meeting tier 3. They don't quite reach tier 4 because they don't explicitly frame the absence as elimination evidence in a synthesis statement.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "@daniel @shay @tanya - Please look at the logs and let me kow if there is anything concerning" ... "@shay - checek logs" ... "@daniel - please out the maintenece banner"

**Rationale:**
The participant uses @mentions to direct tasks to specific people, but the initial delegation is a broadcast to all three ("Please look at the logs") rather than routing specific tasks to specific people based on their access boundaries. Later delegations become more targeted (Daniel for banner, Tanya for platform checks), but the routing is often imprecise or generic. This is inconsistent delegation — sometimes specific, sometimes broadcast.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@daniel @shay @tanya - Please look at the logs and let me kow if there is anything concerning"

**Rationale:**
The participant's initial delegation is a single broadcast request rather than distinct parallel threads. Throughout the drill, investigation proceeds mostly sequentially — one question, one answer, then the next step. While multiple people are involved, they aren't given distinct concurrent tasks. The participant doesn't fan out multiple distinct investigation threads simultaneously.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya - this is P1 i need you here" ... "@tanya - this is P1 and please leave what you are doing" ... "@hamed @tinus - can you please approve" ... "@tinus - can you please appriove?"

**Rationale:**
The participant escalates Tanya off the vendor call when investigation is blocked, and when both Hamed and Tinus auto-reply, they don't wait passively — they move to self-authorize the restart. The escalation is concrete and purposeful. However, they don't explicitly name the cost of pulling Tanya away or the cost of the override, which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "But can rotation was done a week before, can this effect now?" ... "Its rotation of Certs which is expired and new rotation hasnt kicked off"

**Rationale:**
The participant doesn't explicitly articulate hypotheses before testing them. They follow the team's leads rather than forming and naming their own theories. When Daniel surfaces the cert rotation, the participant questions the timing but doesn't frame it as a formal hypothesis to test. They largely react to information provided by NPCs rather than driving hypothesis-test cycles themselves.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "Thanks Shay, may not be related to these changes" ... "We can see the hand shake error?"

**Rationale:**
The participant acknowledges when evidence rules things out ("may not be related to these changes") but doesn't produce synthesis statements that combine multiple pieces of evidence into a tighter scope. They confirm findings from the team (handshake errors) but don't independently synthesize or articulate what's been ruled in and out. The narrowing is largely driven by NPCs rather than the participant.

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "Please fix" ... "So can you please restart the service" ... "yes please, restart now"

**Rationale:**
The participant does not demonstrate consideration of potential consequences before taking actions. They order the fix and restart without asking "is it safe?" or considering what could go wrong. They don't weigh the cost of pulling Tanya off the vendor call (the 2-week reschedule), and they don't consider whether the restart might expose a secondary issue. Actions are fired without consequence-weighing qualifiers.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Thanks Shay, may not be related to these changes" ... "Ok what are these errors @daniel"

**Rationale:**
When the recent changes don't line up with the failure, the participant moves on rather than doubling down on rollbacks. They redirect investigation to the PaymentService logs and follow the cert thread when it emerges. They don't get stuck on false primes. However, the adaptation is somewhat passive — driven by NPC suggestions rather than the participant independently reframing the problem. The drill didn't surface the secondary failure (misordered bundle restart) as a separate pivot moment since the bundle was fixed before restart.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Hi @bez - We have issue with checkout" ... "Its global, all customer" ... "We dont know yet" ... "We are getting handshake errors we are looking into" ... "We are restarting hte payment service cert is corrected now"

**Rationale:**
The participant communicates with Bez but the updates are thin — "We have issue with checkout," "We dont know yet," "Its global, all customer." They don't quantify impact in business terms, don't commit a next-update time, and don't provide a working theory until very late. The updates lack the substance (scope, ETA, theory) expected at tier 3.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Its rotation of Certs which is expired and new rotation hasnt kicked off" ... "we need to fix the order"

**Rationale:**
The participant rarely posts synthesis statements to the technical channel. They confirm findings from team members but don't independently summarize the state of the investigation or articulate what's been ruled out. The team largely self-organizes around the evidence rather than being directed by participant synthesis. The late statement about cert rotation is a partial synthesis but comes after the team has already converged on the answer.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 3 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.33** |

---

## Caveats
- The drill resolved successfully (bundle fixed, service restarted, customers recovered), but per anti-outcome-bias instructions, this outcome did not influence ratings.
- M5 is a borderline 2/3 call. The participant didn't get stuck on false primes (supporting 3), but the pivots were largely NPC-driven rather than participant-initiated. Rated 3 because the participant accepted disconfirmation and moved on without doubling down.
- M4 is rated 1 rather than N/A because the drill surfaced multiple consequence-weighing moments (pulling Tanya off vendor call, restart approval) and the participant engaged with none of them from a consequence-consideration standpoint.
- The secondary failure mode (misordered bundle after restart) didn't manifest as a separate pivot challenge because the bundle was identified and fixed before the restart was executed, which limits discrimination on M5's second pivot moment.

---