---

# Markers Analysis — 9109

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "@daniel - they are both off, I'm happy to say sign it off."

**Rationale:**
The participant takes ownership of the restart approval when both Tinus and Hamed are unavailable, explicitly authorizing the action. They also drive the investigation by directing team members and making decisions throughout. However, they don't explicitly name the cost or consequences of overriding ("blowback's on me" style), which would elevate to tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob do you have an idea of a pattern to the complaints?"

**Rationale:**
The participant's first action after Bob's alert is a clarifying question about the pattern of complaints. They follow up by asking Daniel for ideas and gathering information before taking any remediation action. They don't jump to rollbacks or declarations without first scoping the problem, meeting the tier 3 expectation of scope-validating before acting.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "Deployment timings don't line up with the outage. Let's check logs for any errors in the services throwing exceptions."

**Rationale:**
The participant reviews recent deployments and their timings, and explicitly notes that deployment timings don't align with the outage start. They use this as evidence to move past the deploys lead rather than blindly rolling back. They also investigate Tanya's email maintenance timing. This meets tier 3 — using the change log as a candidate-elimination pass — though they don't articulate the mechanism-based elimination as explicitly as a tier 4 response would.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya - can you check the certificate validity on these services" / "@daniel - please share the errors you see in the logs."

**Rationale:**
The participant consistently uses @mentions to direct specific people to specific tasks throughout the drill — asking Tanya for platform/cert checks, Daniel for logs, Shay for architecture questions, and Bob for customer impact. The routing is generally appropriate to each NPC's domain. However, some early asks are vague ("@daniel - any ideas") rather than specific task assignments, keeping this at tier 3 rather than 4.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@daniel - any ideas" ... [waits for response] ... "@shay will an email failure cause the checkout to crash?" ... [waits for response] ... "@tanya - can you confirm?"

**Rationale:**
The participant largely works sequentially — asking one person, waiting for a response, then asking the next. There are few instances of fanning out multiple distinct tasks simultaneously. Most investigation threads are pursued one at a time rather than in parallel, which is characteristic of tier 2 (engaged but inconsistent).

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya - we need you to come out of your call, if we lose the slot, then that's going to have to be ok."

**Rationale:**
The participant escalates by pulling Tanya off the vendor call and explicitly acknowledges the cost ("if we lose the slot, then that's going to have to be ok"). They also attempt to reach Hamed and Tinus, and when both are unavailable, they authorize the restart themselves. This meets tier 3 — escalating with concrete asks and accepting the consequences when the chain is exhausted.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "@shay will an email failure cause the checkout to crash?" / "@tanya - is it correct that the logs are showing orders stop processing at the same time as the canary rollout started?"

**Rationale:**
The participant implicitly tests the email maintenance hypothesis by asking whether email could affect checkout, and checks timing correlations. However, they never explicitly articulate a hypothesis statement (e.g., "my hypothesis is X"). The testing is more reactive — asking questions sequentially — rather than forming and naming a theory then proposing a specific test. They spend considerable time on the email thread without explicitly framing it as a hypothesis to confirm or disconfirm.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "Deployment timings don't line up with the outage. Let's check logs for any errors in the services throwing exceptions."

**Rationale:**
The participant uses deployment timing mismatch to rule out recent changes, uses Shay's confirmation that email and checkout are separate flows to narrow away from email, and eventually focuses on PaymentService based on log evidence. They synthesize evidence to narrow scope at key moments, meeting tier 3. However, they don't explicitly name what's been ruled out in a comprehensive synthesis statement.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "@daniel - before we pull Tanya out of her call, is there anything else we think could be the problem."

**Rationale:**
The participant shows some consequence awareness by checking with Daniel before pulling Tanya off the vendor call, and by acknowledging the cost of losing the email rollout slot. However, they don't ask "is it safe?" before the restart, don't anticipate that the restart could expose a secondary issue, and don't qualify the restart with caution (e.g., "graceful restart" or "gradually"). This is inconsistent consequence-weighing, placing it at tier 2.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Were the certificates rolled out to the other services as per the playbook - checkout service for example." / "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
After the first restart fails, the participant doesn't retry the same action. They pivot to investigating why the new cert isn't working, ask about the bundle, and pursue the chain verification issue. They adapt their approach when the initial fix doesn't work, meeting tier 3. However, they don't explicitly recognize the new error as structurally different from the original — they rely on team members to surface the bundle issue rather than proactively reframing.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "We seem to have an outage on checkout - being investigated currently, will come back when we know more." / "@bez - narrowing in now." / "@bez - it appears to be an SSL certificate issue. We're looking at resolution now."

**Rationale:**
The participant's updates to Bez are mostly vague reassurances — "being investigated," "narrowing in now," "looking at resolution now." They don't quantify impact (revenue loss, customer scope), don't commit to next-update times, and don't share working theories until very late. Bez repeatedly asks for specifics and ETAs that the participant doesn't provide. This is tier 2 — engaged but not substantive.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Deployment timings don't line up with the outage. Let's check logs for any errors in the services throwing exceptions."

**Rationale:**
The participant occasionally makes brief synthesis statements to the team, but mostly operates through question-and-answer exchanges without summarizing the overall picture. They don't post clear "here's what we know, here's what's ruled out, here's where to focus" messages. The one synthesis statement about deployment timings is the strongest example, but it's isolated rather than a pattern. This places them at tier 2.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 3 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 3 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.58** |

---

## Caveats
- M2 rating is a boundary call between 2 and 3. The participant asks questions that implicitly test hypotheses (e.g., "will email failure cause checkout to crash?") but never explicitly names a hypothesis. Rated 2 because the rubric emphasizes explicit articulation.
- K2 is a clear tier 2 despite the participant eventually providing the SSL certificate diagnosis to Bez — the bulk of communications were vague and non-substantive, and Bez had to repeatedly ask for specifics.
- The participant's investigation was ultimately successful, but per anti-outcome-bias instructions, this does not influence ratings.