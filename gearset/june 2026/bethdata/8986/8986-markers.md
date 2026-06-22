---

# Markers Analysis — 8986

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "I'll approve then - do it, and I'll take responsibility."

**Rationale:**
The participant explicitly takes ownership of the restart decision when both Hamed and Tinus are unavailable, accepting responsibility for the override. Throughout the drill they direct the investigation and make decisions, though they don't proactively position themselves as IC early on or name the cost/blowback as explicitly as a tier-4 participant would. The ownership statement comes when prompted by the approval blocker rather than proactively.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob what kind of complaints?" ... "any idea what proportion of customers?" ... "How many customers are blocked from checkout right now? What's the revenue loss per minute? Is this a total outage or just some users?"

**Rationale:**
The participant's first moves after Bob's alert are clarifying questions about the nature, scope, and proportion of complaints. They ask about the type of complaints, proportion of customers affected, and revenue impact before taking any remediation action. This is solid scope-validation before acting, meeting the tier-3 expectation.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@daniel / @shay any recent changes that could be related?" ... "Shall we roll Daniel's changes back to see if it fixes the issue?" ... "Yes, let's do that just in case"

**Rationale:**
The participant asks about recent changes, which is good. However, after Daniel explicitly states "No DNS errors in the app logs. It's only outbound connections from PaymentService that are failing" and that the DNS work was isolated from payments, the participant still asks to roll back Daniel's checkout changes "just in case" without articulating a mechanism connecting those changes to the symptom. They asked the question but didn't use the answer to eliminate candidates — they used the change log as a rollback queue rather than an elimination pass.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@daniel / @shay any recent changes that could be related?" ... "Tanya, can you check if your maintenance might be related?" ... "@shay can you do that?" ... "OK, can you start work on that Tanya"

**Rationale:**
The participant delegates tasks to specific named people throughout the drill — asking Tanya about maintenance, Shay about the banner, Daniel about logs, and Tanya about certificate work. The routing is generally appropriate (Tanya for platform/cert work, Daniel for app-side). However, some early asks are broadcast-style ("@daniel / @shay") rather than targeted to the right person for the right task.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@daniel / @shay any recent changes that could be related?" ... "Tanya, can you check if your maintenance might be related?"

**Rationale:**
The participant does ask multiple people questions, but the investigation largely proceeds sequentially. After asking about recent changes, they wait for responses before moving to the next thread. There's limited evidence of deliberately fanning out multiple distinct investigation threads simultaneously. The participant tends to follow one line of inquiry at a time rather than orchestrating concurrent threads.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "Tanya we might have to pull out of that call, this needs to be fixed ASAP" ... "@hamed ?" ... "or @Tinus?" ... "I'll approve then - do it, and I'll take responsibility."

**Rationale:**
The participant escalates Tanya off the vendor call when investigation is blocked at the platform layer, and when both Hamed and Tinus are unavailable for restart approval, they don't leave the chain hanging — they take the override themselves. However, they don't explicitly name the cost of pulling Tanya off the vendor call (the 2-week reschedule), and the escalation to Hamed/Tinus is somewhat terse without full context of what's needed and why.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Definitely looks DNS related" ... "Can we roll back the DNS changes?" ... "Shall we roll Daniel's changes back to see if it fixes the issue?"

**Rationale:**
The participant forms implicit hypotheses (DNS-related, Daniel's changes) but doesn't articulate them explicitly as hypotheses to test. They jump to "Definitely looks DNS related" without framing it as a testable theory, and propose rollbacks as actions rather than tests of a named hypothesis. They don't ask "does X plausibly cause Y?" before pursuing leads. The hypothesis formation is implicit and the testing is action-based rather than mechanism-based.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "Is that expired then?" ... "that sounds like our issue"

**Rationale:**
The participant does not produce synthesis statements that combine evidence to narrow scope. When Daniel reports "No DNS errors in the app logs. It's only outbound connections from PaymentService that are failing," the participant doesn't synthesize this into a narrowing statement. They still ask to roll back DNS changes and Daniel's changes after evidence pointed away from them. The narrowing is largely done by NPCs (Daniel, Tanya) rather than the participant synthesizing and directing.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "Tanya we might have to pull out of that call, this needs to be fixed ASAP"

**Rationale:**
The participant shows limited evidence of weighing consequences before actions. They don't ask "is it safe?" before rollbacks, don't name the cost of pulling Tanya off the vendor call (2-week reschedule), and don't consider whether the restart might expose a secondary issue. The rollback of Daniel's changes is done "just in case" without weighing potential consequences. The override decision is made without naming the risk explicitly beyond "I'll take responsibility."

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "What are the logs saying now?" ... "What does that mean?" ... "@daniel is that definitely the root cause?"

**Rationale:**
After the first restart fails, the participant doesn't retry the same action — they ask what the logs show now and engage with the new error (chain verification vs. expiry). They follow the team's investigation into the bundle order issue rather than doubling down on the original cert-expiry fix. However, the adaptation is largely reactive (asking "what does that mean?" rather than recognizing the structural difference themselves), so it doesn't reach tier 4.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "We are still working on a root cause. I'll update again in 10 minutes." ... "We've narrowed it down to an expired certificate on the payments service. Working on fixing." ... "We have fixed the certificate but the issue has remained. Investigating further."

**Rationale:**
The participant provides updates to Bez but they lack business-frame quantification. The first update is vague ("still working on a root cause") with a 10-minute commitment. Later updates name the technical issue but don't quantify business impact, don't provide ETAs for recovery, and don't frame in business terms. The updates are brief and technically oriented rather than substantive for a business audience.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "How can we isolate what's wrong here?" ... "How do we fix that?" ... "Are we confident it now is all working?"

**Rationale:**
The participant rarely synthesizes the current state of knowledge for the technical team. They ask questions and delegate tasks but don't post synthesis statements like "ok so it's not deploys, not DNS, focus on PaymentService outbound now." The team's understanding is driven by NPC synthesis (Daniel's "No DNS errors... only outbound connections from PaymentService") rather than participant-driven scope communication. The participant's messages are mostly questions or approvals rather than orienting statements.

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
- For M5, the participant does adapt after the first restart fails, but the adaptation is largely NPC-driven (Daniel and Tanya identify the bundle issue). The participant follows rather than leads the pivot, which is a boundary call between 2 and 3. Rated 3 because they do engage with the new information rather than retrying the restart.
- For C3, the participant asks about changes but then rolls back Daniel's checkout changes despite evidence pointing away from them. This is a clear tier-2 pattern (asked but didn't use the answer effectively).
- For K4, the participant's technical communication is almost entirely question-based rather than synthesis-based. The NPCs do the heavy lifting on scope communication.

---