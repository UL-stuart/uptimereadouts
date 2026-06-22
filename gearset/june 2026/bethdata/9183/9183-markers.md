---

# Markers Analysis — 9183

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "I'm the incident manager. I approve the restart."

**Rationale:**
The participant explicitly takes ownership of the restart decision when both Hamed and Tinus are unavailable and Bez declines to authorize. They use "I" framing and make the call themselves. However, they don't proactively name the cost or blowback risk — they simply state their authority. This meets the novice expectation but doesn't reach tier 4's explicit cost-naming.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "Any details on the problems being experienced, Bob?" ... "How many customers are blocked right now? What's the revenue loss per minute? Is this a total checkout outage or just partial?"

**Rationale:**
The participant's first moves are scope-validating questions to Bob about the nature of the complaints, the number of affected customers, and the revenue impact. They ask multiple clarifying questions before declaring the incident or ordering any remediation actions. This meets the novice expectation of scope-validation before acting.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "Was there any release to Production for any of those downstream services whose timing seems to coincide with the onset of this incident?"

**Rationale:**
The participant explicitly asks about recent production releases. When Shay reports that prod deployments don't line up with the failure window, the participant doesn't pursue blind rollbacks. They move on to investigating logs and the PaymentService specifically. They use the change-log information as elimination evidence rather than a rollback queue, meeting tier 3. They don't explicitly articulate the elimination reasoning as strongly as a tier 4 response would.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "Daniel, Shay, can you investigate what might be causing this? Tanya says the email maintenance isn't the cause." ... "Shay is saying that the timing of the email maintenance is hard to ignore... Tanya, could you look at the outbound gateway handshake failures?"

**Rationale:**
The participant names specific people for specific tasks throughout — asking Shay to investigate email maintenance, directing Tanya to look at outbound gateway handshake failures, asking Daniel for timestamps. The routing is generally appropriate (Tanya for platform/cert work, Daniel/Shay for app-side). This meets tier 3 expectations of naming specific people for specific tasks.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "Daniel, Shay, can you investigate what might be causing this?" ... "Okay, Shay. Could you dig into the email maintenance to see if it could be the cause?"

**Rationale:**
The participant mostly works sequentially through the investigation. They delegate to Daniel and Shay together but with a single broad ask rather than distinct parallel threads. They don't fan out multiple distinct investigation tasks simultaneously — they follow one thread (email maintenance), then move to logs, then to platform. The investigation is largely serial rather than parallel.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "Tanya, I think that this incident has become severe enough for us to take that hit. Please leave the call and jump on this." ... "Tinus - can you please authorize a restart of the payments service?"

**Rationale:**
The participant escalates Tanya off the vendor call when the investigation is blocked at the platform layer, naming the severity as justification. They also work through the approval chain (Hamed → Tinus → Bez) when the restart is needed. When all are unavailable, they take the decision themselves. They don't explicitly name the cost of pulling Tanya (the 2-week window loss), which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 3

**Evidence:**
> "Tanya, do you think the email maintenance is likely to have anything to do with this incident?" ... "From the logs, it seems like the PaymentService is the one throwing up errors. Could that have anything to do with the email maintenance?"

**Rationale:**
The participant forms the email maintenance hypothesis and tests it by asking Tanya directly. When Tanya confirms it's unrelated, they pivot to the PaymentService. They later form the cert bundle hypothesis by asking Tanya to check the bundle order. They articulate hypotheses and propose tests, meeting tier 3. However, they don't explicitly test on mechanism before pursuing (e.g., asking "how could email maintenance affect payment handshakes?").

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "From the logs, it seems like the PaymentService is the one throwing up errors." ... "Outbound calls? Where to?"

**Rationale:**
The participant uses evidence progressively to narrow scope: from broad checkout failure → PaymentService errors → outbound calls failing → SSL certificate verification failure → cert bundle order. They follow the evidence chain logically. They ask targeted follow-up questions that narrow the scope. However, they don't produce explicit synthesis statements naming what's been ruled out alongside what remains, which would push to tier 4.

---

## M4 — Considers potential consequences before acting

**Rating:** 3

**Evidence:**
> "Any downside to restarting the service?" ... "Given the current ongoing disruption, I think that restarting will be worth it - checkouts are already failing."

**Rationale:**
The participant explicitly asks about downsides before restarting the service, and when told about the risk of a short checkout failure window, they weigh it against the current ongoing disruption. They also tell Tanya to stay on the vendor call initially before the severity warrants pulling her off. This meets tier 3's "asks 'is it safe?' before high-impact actions." They don't anticipate secondary failure modes proactively.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Tanya, do you think the email maintenance is likely to have anything to do with this incident?" [Tanya: unrelated] ... "Are you able to get any more insight into what might be causing the errors in payments?"

**Rationale:**
The participant pivots away from the email maintenance hypothesis when Tanya confirms it's unrelated, and moves to investigating PaymentService logs. They don't get stuck on the false prime or attempt rollbacks of unrelated changes. However, the drill didn't surface the secondary failure mode (first restart failing with a different error), so the second pivot moment wasn't tested. The participant adapted cleanly from the email maintenance lead.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "It seems that not customers can check out currently. We're losing around £1,000 to £1,500 every minute at peak." ... "We have some information but not enough for a fix yet. ETA 20 mins, but that's not based on much evidence."

**Rationale:**
The participant provides some impact quantification to Bez (revenue loss, scope), but the updates are relatively thin — no working theory is shared, the ETA is acknowledged as poorly grounded, and later updates ("Mistake in SSL certificate bundle assembly seems to be the cause - fix will be in place in 2 minutes") are brief. They don't proactively maintain a comms cadence or provide board-ready framing. This is practicing but inconsistent.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Daniel, Shay, can you investigate what might be causing this? Tanya says the email maintenance isn't the cause." ... "Tanya, can we fix this now?"

**Rationale:**
The participant shares some scope information with the team (email maintenance ruled out, PaymentService is erroring) but doesn't produce clear synthesis statements that summarize the current state of knowledge for the technical team. They mostly ask questions and relay information between team members rather than posting explicit "here's what we know, here's what's ruled out" summaries. This is below the tier 3 expectation of posting synthesis statements at decision points.

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
| M2 — Forms and tests working hypotheses | 3 |
| M3 — Uses evidence to narrow the scope | 3 |
| M4 — Considers potential consequences before acting | 3 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.75** |

---

## Caveats
- The secondary failure mode (first restart loading misordered bundle and producing a different TLS error) did not appear in this transcript — Tanya identified and fixed the bundle order *before* the restart, so the participant never faced the "restart fails with a new error" pivot moment. This means M5 was only testable on the email maintenance pivot, not the more discriminating second pivot.
- K2 is a borderline 2/3 call. The participant does share revenue impact numbers with Bez, but doesn't provide a working theory or maintain proactive comms cadence. Rated 2 because the updates lack the substance expected at tier 3 (no theory, no committed next-update time in most messages).
- The participant's investigation path was notably clean — they didn't pursue false rollbacks — which makes it harder to observe M5 adaptation since they didn't go far down a wrong path. This is not penalized but noted.

---