# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to navigate systemic complexity under pressure — sorting misleading signals from real ones, working through coordination constraints when key people are unavailable, and making sense of layered technical failures where the first explanation isn't the whole story.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you pursued both the DNS/email maintenance thread and Daniel's checkout changes as leading hypotheses, ordering rollbacks on both. When the rollback produced no change in symptoms, you accepted the negative result and moved on. The pivot itself was sound — you didn't keep chasing a dead lead — but it was driven by the experiment failing rather than by reasoning about mechanism beforehand. On your next rep, the growth edge is pausing before action to ask: "Is there a plausible causal chain connecting this change to the symptom I'm seeing?" That question, asked before committing to a rollback, would let you eliminate candidates faster and avoid spending time on coincident-but-unrelated factors.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

When the service restart didn't resolve the issue, you recognized quickly that something structurally different was happening — the new error wasn't the same as the original certificate expiry. You engaged with the bundle-ordering issue once it was surfaced and traced it back to the prior week's rotation. This reframing happened within a few exchanges of the restart failing, which shows good responsiveness to unexpected results. The growth edge here is surfacing the "what else changed beyond the obvious?" question yourself, rather than waiting for a team member to uncover the deeper coupling. Proactively asking about the broader change history — not just the last 24 hours — would move you toward independently identifying hidden dependencies.

---

## F3 — Decreased access to team / remote

**Operating at: Strengthening**

You walked the escalation chain methodically — checking with Hamed, then Tinus — and when both were unavailable, you didn't stall. You accepted the auto-replies as terminal and took ownership of the restart decision yourself. You also recognized when Tanya needed to be pulled off her vendor call to focus on the active incident. The next growth edge is naming the trade-off explicitly when you make these calls — articulating to the team why the current situation outweighs the cost of interrupting other work. That framing helps the team understand your reasoning and builds shared context about priority decisions.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You navigated the approval chain to exhaustion in a logical order and took the override when needed. Your delegation was generally well-routed — assigning platform investigation to the right person, directing the customer-facing banner to someone who could act on it. When the second restart was needed after the bundle fix, you authorized it without re-litigating the approval chain, which shows you were tracking the coordination state. The growth edge is making the dependency structure visible to the team — naming aloud what's blocked, who's working what, and where the bottlenecks sit. This kind of explicit coordination statement helps the team self-organize and reduces the chance of duplicated or dropped work.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

Early in the drill, you jumped to a DNS-related conclusion from noisy logs that contained signals across multiple services. Later, when technical outputs were posted, you relied on team members to interpret them rather than driving the filtering yourself. You did ask for logs and engaged with findings once surfaced, which shows willingness to work with data — but the synthesis and distinction-catching (like the difference between a reload and a restart, or what the certificate chain output actually meant) came from others. On your next rep, try to slow down when logs or outputs arrive and ask yourself: "What's actually here, and what's conspicuously absent?" Driving your own filtering — rather than accepting the first loud signal or waiting for someone else to interpret — will sharpen your ability to find buried information in noisy environments.

---

## Looking Forward

Across this drill, your coordination instincts — taking ownership, delegating, adapting when a path fails — are developing well. The consistent growth edge is on the analytical side: slowing down to reason about mechanism before acting, synthesizing what you know into orienting statements for the team, and driving your own interpretation of technical data rather than relying on others to surface the key distinctions. On your next rep, try narrating your reasoning aloud — even briefly — before committing to an action. That single habit tends to surface gaps in logic early and helps the team follow your thinking.---

# Facets Analysis — 8986

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Can we roll back the DNS changes?" ... "Shall we roll Daniel's changes back to see if it fixes the issue?" ... "Yes, let's do that just in case" ... After rollback: "Rollback complete on CheckoutService. No change in symptoms — checkout is still failing for customers."

**Rationale:**
The participant pursued both the DNS/email maintenance lead and Daniel's checkout changes as leading hypotheses, ordering rollbacks on both. They did pivot after the rollback failed — accepting the negative result and moving on to investigate PaymentService and certificates. However, the pivot was reactive (driven by experiment failure) rather than by upstream mechanism reasoning. They never articulated "is there a plausible causal chain?" before acting. This aligns with tier 2: treats coincident factors as leading hypotheses, pursues through to disconfirmation, then pivots reactively.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> After restart failed: "Wait — it restarted and it's still down? That shouldn't happen if the cert was the only problem." ... "What are the logs saying now?" ... Participant engaged with the bundle order issue and traced it back to "last week's rotation."

**Rationale:**
The participant recognized the post-restart failure as unexpected ("That shouldn't happen if the cert was the only problem"), indicating they understood the new error was structurally different from the original expiry issue. They reframed within a few exchanges of the restart failing and continued investigating rather than repeating restarts. However, they did not independently surface the "what changed beyond 24 hours?" question — the cert thread emerged through NPC-driven investigation (Tanya checking certificates). They engaged with the week-old coupling once surfaced and connected the bundle ordering to last week's rotation. This fits tier 3: reframes within ~5 exchanges, recognizes the structural difference, and traces forward to the bundle.

---

## F3 — Decreased access to team / remote

**Rating:** 3

**Evidence:**
> "@hamed ?" ... "or @Tinus?" ... "Both Hamed and Tinus are out, so no one here can approve a restart. Whoever's leading would need to take responsibility." ... "I'll approve then - do it, and I'll take responsibility."

**Rationale:**
The participant walked the escalation chain (Hamed → Tinus) and accepted the auto-replies as terminating, then took ownership. They also initially tried to preserve Tanya's vendor call but pulled her when needed ("Tanya we might have to pull out of that call, this needs to be fixed ASAP"). They didn't re-ping auto-replying NPCs after the first cycle. However, they didn't explicitly articulate the cost trade-off when pulling Tanya off the vendor call (no "global outage outweighs email maintenance" framing), and the ownership statement was brief rather than elaborated. This fits tier 3: accepts auto-replies as terminating, escalates only when needed, and takes ownership after walking the chain.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@hamed ?" ... "or @Tinus?" ... "I'll approve then - do it, and I'll take responsibility." ... On second restart after bundle fix: "Let's do that" — authorized without re-litigating.

**Rationale:**
The participant walked the escalation chain to exhaustion in observable order (pinged Hamed, then Tinus, received indication both were out, then explicitly took ownership). This matches tier 3 path (b). They also delegated work appropriately (Shay on banner, Tanya on cert investigation, Daniel on logs). On the second restart after the bundle fix, they authorized without re-litigating the approval chain. However, they did not explicitly name the dependency structure aloud as a constraint statement — the ownership was taken but without verbalizing the broader coordination pattern to the team. This places them solidly at tier 3 but not quite tier 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Definitely looks DNS related" — said after viewing logs showing errors across multiple services. ... "What does that mean?" — asked after Tanya posted the openssl verify output. ... "How's this happened?" and "How do we fix that?" — asked after NPC surfaced the bundle order issue.

**Rationale:**
The participant initially jumped to "Definitely looks DNS related" from noisy logs (captured by a loud signal), and later relied heavily on NPCs to interpret technical outputs. They asked for logs ("Yes please") but accepted NPC summaries and interpretations without further interrogation. Key distinctions (reload vs. restart, bundle ordering) were surfaced entirely by NPCs — the participant asked follow-up questions but didn't drive the filtering or catch distinctions independently. They engaged with concepts once surfaced but didn't proactively filter or reason about absence of signal. This aligns with tier 2.

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
- F2 tier 3 vs. tier 2 was a boundary call. The participant did reframe quickly after the restart failed and recognized the structural difference, but they never independently surfaced the "beyond 24 hours" question. The quick reframe ("That shouldn't happen") and forward-tracing to the bundle tipped toward tier 3.
- F4 tier 3 vs. tier 4 was close. The participant authorized the second restart without re-litigating, which is a tier-4 anchor signal, but the absence of explicit dependency-structure verbalization kept the rating at 3.
- F5 could arguably be tier 1 given the "Definitely looks DNS related" statement from noisy logs, but the participant did ask for targeted logs and engaged with NPC findings, which moves them above pure tier-1 behavior.

------

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