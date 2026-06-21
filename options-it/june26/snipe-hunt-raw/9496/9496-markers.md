---

# Markers Analysis — 9496

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "Restart the payments please. I will take the balme if anything goes wrong"

**Rationale:**
The participant explicitly takes ownership of the restart decision when both Tinus and Hamed are unavailable, accepting personal accountability for consequences. They also drive the response throughout — declaring the incident, directing rollbacks, pulling Tanya off the vendor session. However, the ownership statement comes only after Bez prompts them to "make the call and own it," which slightly reduces the proactiveness compared to tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "What are the complaints @bob ? Please expand. I need to know where these customers are based and numbers. Thanks"

**Rationale:**
The participant's first response to Bob's vague complaint is a clarifying question asking for specifics about the nature of complaints, customer locations, and numbers. They also attempt to reproduce the issue themselves before taking action. This demonstrates scope-validation before declaring or acting, meeting the tier 3 expectation.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "Ok thanks, please can I have an overview of all changes?" ... "Thanks @daniel - please can we roll back Tanya's most recent change? I want to roll back change systematically"

**Rationale:**
The participant asks for the change log, which is good. However, they then proceed to roll back changes systematically without articulating a mechanism connecting any specific change to the symptom. They roll back shipping, product catalogue, and checkout changes sequentially without using the change log as a candidate-elimination tool. This is the "asked the question but used it as a rollback queue" pattern described as tier 1–2 in the rubric.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya please take a look from your side re: handshake failure thanks" ... "@maya anything on your end in terms of security?" ... "@bob how many customers do we have on the site right now?"

**Rationale:**
The participant consistently uses @mentions to assign specific tasks to specific people — Tanya for platform/cert checks, Daniel for logs, Bob for customer numbers, Maya for security. They route platform-level cert work to Tanya appropriately. Some early delegation is slightly misrouted (asking Daniel to roll back Tanya's change), but overall the pattern is solid and meets tier 3.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@maya anything on your end in terms of security?" ... "@bob how are we looking, please give me an update on numbers"

**Rationale:**
The participant does occasionally fan out to multiple people (Maya for security, Bob for numbers), but the overall investigation pattern is largely sequential — roll back one change, wait for result, roll back next change, wait for result. The security check to Maya is a parallel thread, but the core investigation proceeds one step at a time rather than running multiple distinct hypothesis threads concurrently.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya please drop from vendor session, this is business impacting and a SEV-1 incident" ... "Please drop now and roll back"

**Rationale:**
The participant escalates Tanya off the vendor session decisively when investigation is blocked, overriding her initial refusal. They also attempt to reach Hamed and Tinus multiple times, and when both are unavailable, they escalate to Bez for restart approval. The escalations include context (SEV-1, business impact). However, they don't explicitly name the cost of pulling Tanya (the 2-week vendor slot loss), which keeps this at tier 3 rather than 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Thanks @daniel - please can we roll back Tanya's most recent change? I want to roll back change systematically"

**Rationale:**
The participant does not explicitly articulate hypotheses before acting. Their approach is to "roll back changes systematically" rather than forming a theory about what might be causing the issue and testing it. They don't name a mechanism connecting any specific change to the symptom. Later, when the cert issue is identified, they engage with it, but the early investigation lacks explicit hypothesis formation and testing.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "So what you are telling me, is the new certs were applied but weren't applied correctly so that payment service has continuously been using the old certs until the day of expiry (today) and now the new certs won't work?"

**Rationale:**
The participant does eventually synthesize the cert situation into a coherent understanding. However, during the early investigation, they don't use failed rollbacks as elimination evidence to narrow scope. They roll back multiple changes without synthesizing the negatives. The narrowing largely happens through NPC guidance (Daniel identifying PaymentService errors, Tanya finding the cert) rather than participant-driven evidence synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "I would no like to roll back Daniel's change. The error being seen relates to paymentservice that links directly from CheckoutService."

**Rationale:**
The participant shows some reasoning about why to roll back specific changes (connecting PaymentService to CheckoutService), but generally fires rollbacks without asking "is it safe?" or considering side effects. They don't anticipate that the restart could expose a secondary issue, and they don't name costs when pulling Tanya off the vendor session. The "I will take the blame" statement addresses accountability but not technical consequences of the restart itself.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "I think by now we should be looking into the logs to understand the root failure, which is not surfacing on either our dashboards or in the alerts"

**Rationale:**
After multiple failed rollbacks, the participant recognizes the rollback approach isn't working and pivots to log analysis. This is a clear adaptation. After the first restart fails, they also adapt — checking with the vendor, investigating network, and eventually pulling logs again to discover the bundle issue. They don't stay stuck in the rollback frame indefinitely, meeting tier 3.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Hello! Major incident. No successful checkouts coming through on our side. Zero successful transactions since this started @ 5.18pm. Affecting customers globally." ... "ETA to resolution: 10 mins" ... "Firm estimate"

**Rationale:**
The initial business update names the scope (zero transactions, global) which is good. However, the "ETA to resolution: 10 mins" and "Firm estimate" are unfounded — the participant has no basis for this claim at that point. Later updates are thin: "We have rolled back a number of changes to no avail" and "the team are doing great" — which Bez explicitly rejects. No working theory is shared with business stakeholders, and the cadence drops during the secondary failure.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "The logs are showing checkout errors across multiple services, not isolated to one area"

**Rationale:**
The participant rarely synthesizes state for the technical team. They relay information back (repeating what Daniel says) but don't post synthesis statements that orient the team on what's been ruled out or what the current working theory is. The technical team largely drives itself through Daniel and Tanya's findings, with the participant asking for updates rather than framing the investigation scope.

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
- L3: The ownership statement ("I will take the balme") comes after Bez explicitly prompts "make the call and own it." This is a boundary call between 2 and 3; rated 3 because the participant does ultimately make the call and accept responsibility, and they drive the response throughout (pulling Tanya, declaring incident, directing rollbacks).
- K2: The "Firm estimate" of 10 minutes with no basis is problematic — it's substantive in form but misleading in content. Rated 2 rather than 1 because the initial update does contain scope information.
- M5: The pivot to logs is partially NPC-prompted (Daniel suggests "if we could follow the logs"), but the participant had already expressed the same idea moments before ("I think by now we should be looking into the logs"). Credited to the participant.

---