---

# Markers Analysis — 9021

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "You are authorized to proceed with restart. I am taking full responsibility"

**Rationale:**
The participant explicitly takes responsibility for the restart decision when both Hamed and Tinus are unavailable, using clear ownership language. Throughout the drill they also direct team members and make decisions, though they are somewhat reactive to NPC prompts rather than proactively positioning themselves as the call-maker from the start. The explicit authorization statement meets the novice expectation.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "Bob which kind of complaints?" ... "How many customers are blocked from checkout right now? What's the revenue loss per minute? Is this a total outage or partial?"

**Rationale:**
The participant's first response to Bob is a clarifying question about the type of complaints. They follow up with scope-validating questions about customer count, revenue impact, and whether it's total or partial. They also reproduce the issue before declaring the incident. This meets the novice expectation of scope-validating before acting.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "CAN WE GET LIST OF RECENT CHANGES?" ... "okay, investigation can be done later, can we adjust DNS? to previous one?" ... "will that broke something else?"

**Rationale:**
The participant asks for the change log, which is good. However, they then lock onto the DNS/email maintenance change as the likely cause based on timing correlation alone, without articulating a mechanism connecting it to checkout failures. They pursue a DNS rollback despite Tanya's explicit statement that email maintenance is unrelated. They asked the question but didn't use the information to eliminate candidates — they used it as a rollback target.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "Tanya can you please take a look too" ... "Daniel can you check what was done with that change" ... "Shay, how confident you are that DNS change is root cause?"

**Rationale:**
The participant does use @mentions and names specific people for tasks. However, the delegation is often vague ("Tanya can you please take a look too" without specifying what to look at), and they initially ask Shay to handle DNS when only Tanya has DNS access. The routing doesn't consistently reflect understanding of NPC access boundaries, placing this at tier 2.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "Tanya can you check first that email DNS who went live?" ... "Daniel can you check what was done with that change"

**Rationale:**
The participant does occasionally assign tasks to multiple people, but the investigation is largely sequential. They focus on one thread at a time — first DNS/email maintenance, then waiting for Tanya, then eventually moving to payment logs. There's limited evidence of deliberately fanning out multiple distinct investigation threads simultaneously to run concurrently.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya please finish the call and check DNS" ... "Then we need to do it, sorry Tanya" ... "please understand this is higher priority"

**Rationale:**
The participant pulls Tanya off the vendor call when the investigation is blocked, acknowledging it's not ideal but necessary. They also attempt to reach Hamed and Tinus for restart approval, and when both are unavailable, they take the decision themselves. The escalation is concrete and moves the investigation forward, meeting the novice expectation. However, they don't explicitly name the cost of pulling Tanya (losing the 2-week vendor window) in their decision framing.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "we are aware there was DNS change minutes before transactions dropped to 0, Shay is checking" ... "okay could it be that cert SSL have issue after she launched email service"

**Rationale:**
The participant forms an implicit hypothesis about DNS/email maintenance causing the issue based on timing correlation, but doesn't articulate it as a formal hypothesis with a clear test. They pursue the DNS thread despite Tanya explicitly stating email maintenance is unrelated. They don't ask "does DNS plausibly cause checkout handshake failures?" before pursuing it. The hypothesis formation is inconsistent and lacks mechanism-testing.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "i dont see any recent change sin payment services, but could be that DNS is not changed for that service?" ... "notAfter: May 19 08:43:27 2026 GMT ← EXPIRED" ... "today is may 19"

**Rationale:**
The participant does eventually notice the expired certificate and identifies it as significant. However, for much of the drill they fail to use evidence to narrow scope — they pursue the DNS/email thread despite multiple pieces of evidence ruling it out (Tanya's explicit statement, DNS probes showing clean results). The narrowing to PaymentService outbound failures is largely driven by NPC findings rather than participant synthesis. Late recognition of the cert expiry shows some evidence use, but the overall pattern is inconsistent.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "will that broke something else?" ... "how confident you are this will fix the problem?"

**Rationale:**
The participant asks "will that broke something else?" before the DNS rollback, showing some awareness of consequences. They also ask Tanya about confidence before the restart. However, these are brief and don't demonstrate deep consequence-weighing. They don't anticipate secondary failure modes after the restart, and they don't name the cost of pulling Tanya off the vendor call (2-week reschedule). The consideration is present but shallow.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "what kind of logs and errors we see now" ... "who can give 2 certificates?" ... "we need to fix the order"

**Rationale:**
After the DNS thread proves fruitless (Tanya confirms DNS is clean), the participant does eventually pivot to investigating payment logs and the cert issue. After the first restart fails, they don't retry the same action — they engage with the new error (chain verification failure) and work toward the bundle fix. The pivot away from DNS is slow (driven largely by NPCs), but the post-restart pivot to the bundle issue shows genuine adaptation.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Hello, we are receiving complaints from all over a world about checkout issue" ... "we still dont have root cause" ... "ETA is 2 minutes to adjust certificates"

**Rationale:**
The participant communicates with Bez but the updates are largely vague and reactive to Bez's demands. Early updates lack quantification, working theory, or committed next-update times. "We still dont have root cause" and "I will keep you updated" are not substantive. Later they provide an ETA ("2 minutes"), which is better, but overall the business communications lack the structure and substance expected at tier 3.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "thanks shay, okay can we please check first all this services" ... "let now focus on that errors and what might be"

**Rationale:**
The participant rarely synthesizes the current state of knowledge for the technical team. Messages like "let now focus on that errors" and "please all treat this with highest urgency" are directional but don't communicate what's been ruled in or out. They don't post synthesis statements that orient the team (e.g., "it's not DNS, not recent deploys, focus on PaymentService outbound"). The team orientation largely comes from NPCs rather than the participant.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.33** |

---

## Caveats
- The participant's language suggests English is not their first language, which may affect how clearly hypotheses and synthesis statements are articulated in text. I rated based on observable actions and content rather than language fluency.
- The boundary between M5 rating 2 and 3 was close. I gave 3 because after the first restart failed, the participant engaged with the new error type rather than retrying, even though the earlier pivot away from DNS was slow and NPC-driven.
- K2 rating was a boundary call between 1 and 2. I gave 2 because the participant does communicate with Bez multiple times and eventually provides an ETA, though most updates lack substance.

---