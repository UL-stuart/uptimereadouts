---

# Markers Analysis — 9503

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "Agreed. What're the consequences of us restarting, @daniel ? I'll accept responsibility for the call but I need to know the impact first." ... "I'll confirm with Tinus and Hamed that I've given the go-ahead to restart, once the incident is over."

**Rationale:**
The participant explicitly accepts responsibility for the restart decision and commits to following up with approvers afterward. They drive the response throughout, directing team members and making decisions. However, they don't quite reach tier 4 — the ownership statement comes after some deliberation and prompting about the approval chain, rather than proactively positioning themselves as the call-maker from the outset.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "What complaints are you seeing, Bob?" ... "Do you know if this is globally or just one region?" ... "Let me check if I can reproduce it on production."

**Rationale:**
The participant's first actions are clarifying questions to Bob about the nature and scope of complaints, followed by a reproduction attempt. They gather information before declaring or acting on remediation. This meets the novice expectation of scope-validating before acting, though the questions are somewhat basic (type, region) rather than deeply probing pattern differences across reports.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "Shay: can you check just before 14:44 to see if that's when it started? Daniel: can you have a look to see any changes that occurred around then?" ... "What facts do we have? 1. We don't think it's an app code change 2. It looks to be cert related 3. No recent deployments for the payments service 4. We did rotate certs across four services 7 days ago"

**Rationale:**
The participant asks for recent changes and reviews them. They synthesize the findings into a candidate-elimination pass ("We don't think it's an app code change," "No recent deployments for the payments service") and use the absence of relevant changes to redirect toward the cert thread. This meets tier 3 — using the change log as elimination rather than a rollback queue. They don't quite reach tier 4 because they don't explicitly articulate the mechanism-based reasoning for why deploys can't be the cause before moving on.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "Shay, can you look at the backend logs and tell us what you see please?" ... "Shay: can you check just before 14:44... Daniel: can you have a look to see any changes that occurred around then?" ... "@daniel please restart the service. Tanya can you please keep an eye on the logs."

**Rationale:**
The participant consistently names specific people for specific tasks throughout the drill — Shay for logs, Daniel for changes and restart, Tanya for network/cert investigation, Bob for customer comms. The routing is generally appropriate to each NPC's domain. They meet tier 3 by naming the right person for the right task most of the time, though there are a few moments of slightly imprecise routing (asking Daniel about IAM when Hamed made the change).

---

## C6 — Runs parallel investigation threads

**Rating:** 3

**Evidence:**
> "Shay: can you check just before 14:44 to see if that's when it started? Daniel: can you have a look to see any changes that occurred around then?"

**Rationale:**
The participant delegates multiple distinct tasks to different people in close temporal sequence — Shay checking logs while Daniel checks changes, and later Bob handling customer comms while Tanya investigates network/certs. This demonstrates concurrent investigation threads. It meets tier 3 as multiple threads run simultaneously, though the parallelism isn't as aggressively fanned out as tier 4 examples.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "Tanya: I'm going to need you to drop on the call, sorry. We're seeing a lot of connection issues that's causing a P1 outage." ... "I'll confirm with Tinus and Hamed that I've given the go-ahead to restart, once the incident is over."

**Rationale:**
The participant escalates Tanya off the vendor call when investigation is blocked at the platform layer, naming the severity ("P1 outage") as justification. When both Hamed and Tinus are unavailable for restart approval, they make the call themselves rather than leaving the chain hanging. This meets tier 3 — concrete escalation with context when blocked. They don't fully reach tier 4 because they don't explicitly name the cost of pulling Tanya (the 2-week vendor window loss).

---

## M2 — Forms and tests working hypotheses

**Rating:** 3

**Evidence:**
> "Tanya: can you tell me more about the changes? Would it impact the checkout process?" ... "What facts do we have? 1. We don't think it's an app code change 2. It looks to be cert related 3. No recent deployments for the payments service 4. We did rotate certs across four services 7 days ago"

**Rationale:**
The participant forms hypotheses (email maintenance, app code changes, cert-related) and tests them through investigation. They explicitly synthesize findings to eliminate hypotheses and converge on the cert thread. The hypothesis-test linkage is visible, and they pivot after disconfirmation. This meets tier 3. They don't quite reach tier 4 because they don't explicitly ask "does X plausibly cause Y?" as a mechanism question to dispose of false primes in one pass — they work through them more sequentially.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "What facts do we have? 1. We don't think it's an app code change 2. It looks to be cert related 3. No recent deployments for the payments service 4. We did rotate certs across four services 7 days ago"

**Rationale:**
The participant uses evidence to systematically narrow scope — ruling out app code changes, using the absence of payment service deployments, and converging on the cert rotation as the last relevant touch. The synthesis statement explicitly names what's been ruled out. This meets tier 3. They don't fully reach tier 4 because they don't explicitly use absence-of-signal reasoning (e.g., "internal calls clean → outbound boundary") as prominently, though they do arrive at the correct narrowing.

---

## M4 — Considers potential consequences before acting

**Rating:** 3

**Evidence:**
> "What's the impact of restarting the service now? What's the cost/loss if we do so?" ... "Agreed. What're the consequences of us restarting, @daniel ? I'll accept responsibility for the call but I need to know the impact first." ... "Can we test ourselves before removing the banner?"

**Rationale:**
The participant explicitly asks about consequences before the restart ("What's the impact?", "I need to know the impact first") and verifies the fix before removing the maintenance banner. This demonstrates consistent consequence-weighing before high-impact actions, meeting tier 3. They don't reach tier 4 because they don't anticipate secondary failure modes (e.g., checking the bundle before restarting) — the bundle issue surprised them.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Cert issue is resolved. What else are we seeing in the logs? @Shay and @daniel can you check the application logs?" ... "payments service needs a two-cert bundle to authenticate, tanya can you open the bundle file and check what's in there?"

**Rationale:**
After the first restart fails, the participant doesn't retry the same action. They immediately redirect investigation to the logs and ask what else is failing. When the bundle issue is identified, they pivot to fixing the bundle order. This meets tier 3 — redirecting investigation to other surfaces after a failed action. They don't fully reach tier 4 because they don't independently recognize the structurally different error (chain verification vs. expiry) — Daniel and Tanya surface the bundle insight, and the participant follows their lead.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 3

**Evidence:**
> "Yes. Checkout is down - users cannot proceed to payment. Global outage. Still investigating the root cause to determine if we can rollback or fix forward. Next update in 10 minutes." ... "We've identified an issue with our certificates - it's expired. We're looking at resolutions right now."

**Rationale:**
The participant provides multiple updates to business-comms that name the impact (global outage, checkout down), current status (investigating, identified cert issue), and commit next-update times. This meets tier 3 — impact in business terms with committed cadence. They don't fully reach tier 4 because the updates lack quantified revenue impact and the cadence doesn't explicitly cover the secondary failure (first restart didn't work) — Bez has to ask follow-up questions about customer numbers.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 3

**Evidence:**
> "What facts do we have? 1. We don't think it's an app code change 2. It looks to be cert related 3. No recent deployments for the payments service 4. We did rotate certs across four services 7 days ago"

**Rationale:**
The participant posts a clear synthesis statement to the technical channel that names what's been ruled out and what the current working theory is. This orients the team and prevents redundant investigation. They also redirect focus after the first restart fails ("Cert issue is resolved. What else are we seeing in the logs?"). This meets tier 3 — synthesis at decision points. They don't fully reach tier 4 because earlier in the drill they could have synthesized sooner (e.g., explicitly naming "PaymentService outbound boundary" as the scope before the cert thread emerged).

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 3 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 3 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 3 |
| M3 — Uses evidence to narrow the scope | 3 |
| M4 — Considers potential consequences before acting | 3 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 3 |
| K4 — Communicates issue scope clearly to the technical team | 3 |
| **Mean Marker Score** | **3.00** |

---

## Caveats

- **L3 boundary call:** The participant's ownership statement ("I'll accept responsibility for the call") is clear but comes after deliberation rather than proactively. This is solidly tier 3 but could be argued as borderline 3/4 given the explicit acceptance of consequences.
- **M5 boundary call:** The participant adapts well after the first restart fails, but the bundle insight comes primarily from NPCs (Daniel: "I just realised something. The payments service actually needs two certificates"). The participant follows the lead rather than independently reframing. This keeps it at tier 3 rather than 4.
- **K2 boundary call:** The participant provides substantive updates but Bez has to ask follow-up questions about customer numbers and revenue impact, suggesting the updates could be more proactive in quantifying business impact. Solidly tier 3.
- **Uniform scoring note:** All markers rated 3 — this reflects a consistently competent performance that meets novice expectations across all dimensions without notably exceeding them on any single marker.

---