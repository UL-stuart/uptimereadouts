# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, coordinate a partially unavailable team, and trace a failure through layered system dependencies. The observations below reflect how you engaged with each of these challenges and where your next growth edges sit.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you latched onto the email/DNS maintenance as your leading hypothesis based on timing alone — the change went live just before transactions dropped. You pursued this thread to the point of pulling a team member off another task to verify it, and only pivoted once you received concrete disconfirmation that DNS was clean. The growth edge here is pausing before committing resources to a correlation and asking yourself: *does this change have a plausible mechanism to cause the symptom I'm seeing?* Email DNS and payment handshakes operate in different domains — reasoning about that connection before acting would have saved time and preserved team capacity for more productive threads.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the certificate thread surfaced, you engaged with it effectively. You recognized the temporal gap — a cert rotated seven days ago, expiring today — and connected it to the failure. When the first restart didn't resolve the issue, you shifted your framing rather than repeating the same action, asking what new errors were appearing and engaging with the bundle-ordering problem when it was identified. The next growth edge is surfacing these "beyond the obvious window" questions yourself rather than waiting for a teammate to raise them. Asking early on, "what changed in the last week, not just the last hour?" would have brought you to this thread faster.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You explicitly named the access constraints — identifying which team members were unavailable and accepting auto-replies as terminating signals rather than re-pinging. When you needed Tanya, you made a deliberate cost trade-off, acknowledging the priority conflict and pulling her off her vendor call. You also took explicit ownership of the restart decision when both approvers were unreachable. This showed solid constraint management. To build further, consider naming the *cost* of your trade-offs out loud when you make them — articulating what you're giving up (e.g., the vendor call window) helps the team understand your reasoning and builds shared situational awareness.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the approval chain methodically — reaching out to Hamed, then Tinus, recognizing both were unavailable, and then explicitly authorizing the restart yourself with clear ownership language. You also distributed work across available team members. The growth edge is anticipating these bottlenecks before they block you. If you'd identified early that restart approval might be needed and checked approver availability proactively, you could have shortened the delay. On your next rep, try mapping the decision dependencies at the start of an incident: who do you need, for what, and what's your fallback if they're unavailable?

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked for filtered information — change logs, specific service logs — which is a good instinct. However, you frequently accepted NPC summaries without further interrogation and chased a UAT-only change before being corrected. The critical cert-expiry data was surfaced by a teammate rather than through your own filtering. On your next rep, work on driving the filter yourself: when you receive a data dump, actively ask "what's missing?" and "what would I expect to see if my hypothesis were wrong?" This moves you from receiving information to interrogating it.

---

## Looking Forward

You showed clear strengths in owning decisions under pressure and managing team constraints — stepping up when the approval chain was exhausted and making explicit trade-offs about team capacity. The consistent growth edge across this drill is moving from reactive to proactive: questioning causal mechanisms before committing to a hypothesis, surfacing broader change windows earlier, and synthesizing the current state of knowledge for your team rather than waiting for teammates to surface findings. On your next rep, try articulating your working theory and its test criteria out loud to the team early — this will sharpen your own reasoning and help others contribute more effectively to narrowing the problem.
---

# Facets Analysis — 9021

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." ... "okay, investigation can be done later, can we adjust DNS? to previous one?" ... "We need to revert that maintenance and back to old DNS"

**Rationale:**
The participant adopted Shay's email/DNS correlation as their leading hypothesis and pursued it through to action — pulling Tanya off her vendor call specifically to revert DNS. They did not independently question the causal mechanism ("does email DNS plausibly break payment handshakes?"). However, after Tanya confirmed DNS was clean and email was unrelated, the participant pivoted reactively and moved on to investigating downstream services. This is classic tier-2 behaviour: treating the coincident factor as the leading hypothesis, pursuing it to disconfirmation, then pivoting only after concrete failure rather than from upstream mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "checked payments deployment history — only cert-related change is CHG90123, Tanya, PROD, SSL cert rotation across four services — 7 days ago." ... "notAfter: May 19 08:43:27 2026 GMT ← EXPIRED" ... "today is may 19" ... "okay can clear cache or restart help in that case?"

**Rationale:**
The participant engaged with the week-old cert rotation thread once Daniel surfaced it, recognized the expired cert as the issue, and connected the temporal gap (rotated 7 days ago, expired today). After the first restart failed, the participant asked "what kind of logs and errors we see now" — showing recognition that the situation had changed rather than simply repeating the restart. They engaged with the bundle ordering issue when Tanya surfaced it and drove toward the fix. However, they did not independently surface the "what changed beyond 24 hours" question — that came from Daniel/Shay. The post-restart reframing happened within a reasonable window (~5 exchanges). This meets tier 3: engages with the cert thread when prompted, drives it forward, and recognizes the structural difference after restart failure.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "so we don't have Tinus, Hamed and Tanya" ... "Then we need to do it, sorry Tanya" ... "please understand this is higher priority" ... "You are authorized to proceed with restart. I am taking full responsibility"

**Rationale:**
The participant explicitly named the access constraints ("so we don't have Tinus, Hamed and Tanya"), accepted auto-replies as terminating after one cycle (Hamed, Tinus), and made the cost trade-off when pulling Tanya off the vendor call ("please understand this is higher priority"). They took explicit ownership of the restart decision when both approvers were unavailable. They did not re-ping auto-replied NPCs. This meets tier 3: names constraints, accepts terminating signals, escalates appropriately, and preserves Tanya's constraint until the cost of preserving it exceeded the cost of breaking it.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "so we don't have Tinus, Hamed and Tanya" ... "lovely, and since they are both off who can give it?" ... "Okay I am fine with that" ... "You are authorized to proceed with restart. I am taking full responsibility"

**Rationale:**
The participant walked the escalation chain in observable order: asked Hamed (auto-reply), asked about Tinus (auto-reply), then recognized the bottleneck and took ownership. They named the dependency structure ("so we don't have Tinus, Hamed and Tanya") and explicitly authorized the restart. They delegated parallel work to available NPCs (Shay investigating, Daniel pulling logs, Tanya checking platform). This meets tier 3 path (b): walks the escalation chain to exhaustion, then explicitly takes ownership. They did not quite reach tier 4 because the naming of the dependency structure was somewhat reactive (prompted by Tanya saying she needed sign-off) rather than proactively articulated before the bottleneck surfaced, and on the second restart (bundle fix) Tanya proceeded without re-litigating, but the participant didn't explicitly pre-authorize it.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "CAN WE GET LIST OF RECENT CHANGES?" ... "this look sus CHG90432" ... "okay could it be that cert SSL have issue after she luanched emal service" ... "did we do this Copy cert and key to target path on all pods?"

**Rationale:**
The participant asked for filtered information (change logs, specific service logs) but frequently accepted NPC summaries without further interrogation. They chased a UAT-only change (CHG90432) before being corrected, showing incomplete filtering. They did not independently catch the reload-vs-restart distinction from the runbook — Tanya surfaced the cert findings. The participant did engage with the cert expiry data once presented ("notAfter... today is may 19") but did not drive the filtering proactively or reason about absence of signal. They relied heavily on NPCs to surface and interpret buried information. This is tier 2: asks for filtered data but accepts summaries, engages with key concepts once surfaced but doesn't drive the filter independently.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.60** |

---

## Caveats
- F1 rating is a borderline 1/2 call. The participant did eventually pivot away from the DNS hypothesis, but only after pulling Tanya off her vendor call and having her confirm DNS was clean — a significant resource expenditure on the false lead. Rated 2 because they did pivot once disconfirmed rather than persisting.
- F2 tier 3 vs 4 boundary: the participant did not independently surface the "beyond 24 hours" question, which is a key tier-4 differentiator. The post-restart reframing was adequate but not notably fast.
- F4 second restart: Tanya proceeded autonomously with the second restart after the bundle fix without the participant needing to re-authorize, which could be read as implicit pre-authorization or simply as Tanya acting independently. Did not weight this heavily either way.

---
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
