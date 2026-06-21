---

# Markers Analysis — 9196

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "@daniel both I cant reach, who can approve, I will happily take this on my shoulders"

**Rationale:**
The participant explicitly takes ownership of the restart approval decision when both Hamed and Tinus are unavailable, stating they'll "take this on my shoulders." They also drive the response throughout — directing team members, making decisions, and providing stakeholder updates. However, this ownership moment comes relatively late and only after Daniel prompts that approval is needed, rather than proactively positioning themselves as the decision-maker earlier.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob can you give me the impact, number of markets?" ... "@bob so appears to be a checkout issue?" ... "@bob is this all customers? @tanya are any orders successful?"

**Rationale:**
The participant's first actions after Bob's alert are scope-validating questions about impact, number of markets, and whether it's all customers. They ask multiple clarifying questions before taking action. They also ask Shay about recent changes. This represents solid scope-validation before acting, meeting the novice expectation.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@shay any changes we should be aware of?" ... "@shay lets have a look at the change records and pinpoint when it started" ... "@tanya your checkout changes were the LAST CHANGES?"

**Rationale:**
The participant asks for recent changes and reviews the change log. However, they don't use the information to eliminate candidates — instead they fixate on the timing correlation ("@bob DOES THIS CORRELATE to the complaints? around 08:55?") and direct Daniel to look at his change more closely, even after Shay notes "none of these changes look like they'd break checkout end-to-end." They asked the question but didn't effectively use the answer for elimination.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya can you have a look at the logs?" ... "@tanya i need to you to scrutinize the changes alongside @daniel somewhere a change has impacted live" ... "@daniel please keep an eye on this as it goes live...@tanya you also please"

**Rationale:**
The participant consistently delegates to named individuals throughout the drill — Tanya for platform/cert checks, Daniel for logs and app-side investigation, Shay for change records, Bob for customer impact. Tasks are generally routed to appropriate people. However, some delegations are vague ("@tanya please help Shay understand this") rather than specific, and early routing shows some confusion about who can do what.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@tanya can you have a look at the logs?" ... "@shay any changes we should be aware of?"

**Rationale:**
The participant does issue some parallel asks early on (Tanya for logs, Shay for changes, Bob for scope). However, the investigation largely proceeds sequentially — they wait for one thread to complete before moving to the next. The middle portion of the drill shows mostly serial question-answer exchanges rather than concurrent investigation threads running simultaneously. This is inconsistent parallelism.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya we will need your support, this is a sev 1" ... "@tanya you will need to prioritize this please" ... "@daniel both I cant reach, who can approve, I will happily take this on my shoulders"

**Rationale:**
The participant escalates Tanya off the vendor call when needed, pulling her into the incident despite the cost. When both Hamed and Tinus are unavailable via auto-reply, the participant doesn't leave the chain hanging — they take the approval on themselves. The escalation of Tanya required two attempts but was ultimately successful with a clear rationale (Sev 1). The self-authorization for the restart shows appropriate escalation handling.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "@tanya your checkout changes were the LAST CHANGES?" ... "@bob DOES THIS CORRELATE to the complaints? around 08:55?" ... "@tanya i need to you to scrutinize the changes alongside @daniel somewhere a change has impacted live"

**Rationale:**
The participant pursues the timing correlation hypothesis (changes around 08:55 correlating with complaints at 09:00) but doesn't explicitly articulate it as a hypothesis or propose a clear test. They follow the email maintenance red herring for a while despite Tanya's explanation. They don't clearly pivot based on disconfirmation — rather, the team (Daniel, Shay) drives the narrowing to PaymentService. Hypotheses are implicit rather than explicit.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "@bob is it failed payments alone, or anything else mentioned?" ... "ok so lets focus on checkout @everyone"

**Rationale:**
The participant makes some narrowing moves — confirming it's a payment-step issue, asking if it's all customers. However, they don't produce synthesis statements that combine evidence to narrow scope. The narrowing to PaymentService is largely driven by Daniel and Shay's findings rather than the participant's own synthesis. They don't explicitly name what's been ruled out or use absence of signal as evidence.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "@tanya can you switch them around, that wont make it any worse?!" ... "@daniel please keep an eye on this as it goes live...@tanya you also please"

**Rationale:**
The participant shows some consequence awareness — asking if switching the cert order won't make things worse, and asking the team to monitor the restart. However, the first restart was authorized without any discussion of what could go wrong, and pulling Tanya off the vendor call happened without explicitly naming the cost (2-week delay). The "that wont make it any worse?!" is a consequence check but comes late and is somewhat reactive.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "ok @daniel , @tanya next steps? Do we see a success with the cert errors though?" ... "@tanya so its still certificate?"

**Rationale:**
After the first restart fails, the participant doesn't simply retry it — they ask what's happening now and engage with the new information (chain verification failure vs. expiry). When Tanya identifies the bundle issue, the participant adapts and pursues the bundle fix. However, the adaptation is largely reactive to team findings rather than the participant independently recognizing the structural difference in the new error. They follow the team's lead rather than reframing independently.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Investigating now, next update in 5 minutes, appears to be high numbers of customers. Looking to resolve quickly" ... "Cusotmers are unable to checkout orders and payments appear to be failing across the board. Investigating now and checking latest changes"

**Rationale:**
The participant provides several updates to Bez but they are largely generic — "investigating now," "appears to be high numbers." When Bez explicitly asks for specifics (revenue per minute, number of customers, full vs. partial outage), the participant doesn't provide numbers until much later ("Each minute we are losing approx 1-1.5k pounds"). The later update about certificates being in the wrong order is more substantive but comes very late in the drill. Updates lack committed next-update times and working theories for most of the incident.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "ok so lets focus on checkout @everyone" ... "@daniel its two certs, not one. Tanya is checking"

**Rationale:**
The participant provides some direction to the technical team ("focus on checkout") but rarely synthesizes the current state of knowledge. They don't post messages that combine evidence into a tighter scope or name what's been ruled out. The "@daniel its two certs, not one" is a relay of Tanya's finding rather than a synthesis statement. Most of the participant's technical channel messages are questions or acknowledgments rather than orienting summaries.

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
- L3 rating is a borderline 3: the participant does take ownership of the restart approval explicitly, but the moment comes after Daniel prompts the need for approval rather than proactively. Rated 3 because the explicit "take this on my shoulders" language meets the novice expectation.
- M5 is a borderline 2/3: the participant doesn't retry the restart (meeting tier 3 minimum) and engages with the new error, but the reframing is largely team-driven. Gave benefit of the doubt for tier 3.
- K2 is borderline 2/3: Bez explicitly asks for specifics twice and the participant doesn't provide them promptly. The later certificate-order update is more substantive but the overall pattern is inconsistent. Rated 2 because updates were largely reactive to Bez's prompting rather than proactive.

---