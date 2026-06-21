# Post-Drill Report — Snipe Hunt

This drill placed you in a live checkout outage requiring you to navigate misleading signals, hidden system dependencies, constrained team availability, and approval bottlenecks — all while managing information flow across technical and business channels. The observations below reflect how you engaged with each of these dimensions.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you pursued Tanya's email maintenance as a potential cause given its timing overlap with the complaints. You pulled her off the vendor call to investigate. When the team's log analysis pointed to PaymentService as the source — with no recent code changes on that service — you moved away from the email thread. The pivot happened, but it was driven by your team narrowing the scope rather than by your own reasoning about whether email maintenance could plausibly break checkout. On the next rep, the growth edge is pausing before chasing a coincident event to ask yourself: *what's the mechanism that would connect this change to this symptom?* That upstream reasoning can save you from pulling constrained resources toward a dead end.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

You engaged meaningfully with the temporal puzzle once Daniel surfaced the certificate rotation. Your question about how a week-old rotation could cause today's failure showed active reasoning about the coupling rather than passive acceptance. Once the expiry-window explanation landed, you drove the thread forward toward verification and fix. The growth edge here is surfacing that "what changed beyond the obvious 24-hour window?" question yourself — before a team member brings it to you. Building a habit of asking about delayed-effect mechanisms (expiry windows, cache TTLs, scheduled rotations) will help you catch these earlier.

---

## F3 — Decreased access to team

**Operating at: Practicing**

When Tanya was on the vendor call, you escalated firmly and repeatedly to pull her back. When Hamed and Tinus were unavailable, you pinged both, received auto-replies, and moved on to self-authorize — an appropriate response. However, you didn't articulate the trade-off of pulling Tanya off her call (the two-week reschedule cost), and you didn't batch or economise your requests to her once she arrived. The growth edge is naming the constraint aloud — "I know this costs us the rollout slot, and I'm making that call because checkout is down globally" — and then being efficient with the constrained person's time by preparing specific, scoped questions before pulling them in.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the approval chain in clear sequence: Hamed first, then Tinus, then self-authorization when both were unavailable. You stated the override explicitly rather than letting it happen implicitly. You also delegated parallel work appropriately — Daniel on the maintenance banner, Shay on logs, Tanya on platform checks. The growth edge is sequencing your investigation and your approval path in parallel rather than serially. If you'd started the approval chain while the cert fix was still being prepared, you could have compressed the timeline. Naming the dependency structure aloud ("we need approval before restart, and both approvers may be unavailable") helps you spot these opportunities.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You delegated log investigation broadly rather than filtering to the relevant service, and when you couldn't access logs yourself, you relied on NPC summaries without further interrogation. The certificate rotation, the bundle-order issue, and the reload-vs-restart distinction were all surfaced by team members rather than by your own filtering. You did engage with the openssl verify command once it was raised. The growth edge is driving the filter yourself: when a team member reports log findings, ask "what service, what time window, what error pattern?" to narrow before accepting the summary. Building the habit of specifying what you're looking for — rather than asking broadly — will help you spot buried signals faster.

---

## Looking Ahead

Across this drill, your strongest moments came when you engaged actively with information your team surfaced — questioning the timing of the cert rotation, walking the approval chain to completion, and adapting when early leads didn't pan out. The consistent growth edge is moving upstream: forming your own mechanism questions before chasing leads, naming trade-offs before pulling constrained resources, and driving the information filter rather than receiving it. On your next rep, try articulating one "what would have to be true for this to be the cause?" question before assigning someone to investigate — that single habit touches several of the patterns this drill is designed to surface.
# Facets Analysis — 9317

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "hey — not trying to distract from this, but tanya kicked off the email maintenance right before the complaints started. probably nothing, but the timing is a bit close." ... participant responds: "@tanya - Please look into these" ... then "@tanya - this is P1 i need you here" ... then "@tanya - please leave what you are doing"

**Rationale:**
The participant initially pursued Tanya's email maintenance as a lead, pulling her off the vendor call. However, once Shay noted "PaymentService is throwing errors consistently, but there hasn't been any change on it for ages" and Daniel confirmed no recent PaymentService code changes, the participant pivoted to investigating PaymentService without returning to the email hypothesis. The pivot was reactive — driven by team investigation narrowing the scope rather than the participant's own mechanism reasoning about whether email could plausibly break checkout. This aligns with tier 2: treating the coincident factor as a lead, then pivoting after disconfirming evidence, without upstream mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "But can rotation was done a week before, can this effect now?" ... Daniel: "The certs were rotated 7 days ago because the old ones were expiring today. Timing lines up with the expiry window." ... Participant: "This makes sense. @tanya - can you please verify?"

**Rationale:**
The participant engaged with the week-old coupling by explicitly questioning how a 7-day-old rotation could cause today's failure ("But can rotation was done a week before, can this effect now?"). Once Daniel explained the expiry timing, the participant accepted and drove forward. The participant didn't independently surface the "what changed beyond 24 hours" question — Daniel found the cert rotation — but the participant engaged meaningfully with the temporal coupling once surfaced. The post-restart bundle-order issue was handled smoothly: after Tanya showed the running process still had old certs, the participant moved to restart without repeating the same action. This fits tier 3: engages with the week-ago thread when prompted, drives it forward, and connects the causal chain.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tanya - this is P1 i need you here" ... "@tanya - please leave what you are doing" ... Tanya: "I can't step away, leaving now means we lose the rollout slot and have to wait two weeks." ... Participant: "@tanya - this is P1 and please leave what you are doing"

**Rationale:**
The participant pulled Tanya off the vendor call without articulating the cost trade-off or economising on her bandwidth. There was no batching of questions or acknowledgment of the constraint — the participant simply demanded her presence repeatedly. Later, when Hamed and Tinus were unavailable, the participant pinged both, received auto-replies, and moved on to take ownership — but didn't re-ping them, which is appropriate. However, the participant never named the access constraints in their own words or articulated the trade-off of pulling Tanya off the vendor call. This fits tier 2: walks the escalation chain but doesn't articulate the constraint pattern or economise on constrained resources.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@hamed @tinus - can you please approve" ... [auto-reply from Hamed] ... "@tinus - can you please appriove?" ... [auto-reply from Tinus] ... "@tanya - In there absence i approve to restrart the payment sevrice"

**Rationale:**
The participant walked the escalation chain to exhaustion in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), then explicitly took ownership and issued the authorisation as a distinct message. This matches tier 3 path (b) precisely. The participant also delegated parallel work appropriately (Daniel on banner, Shay on logs, Tanya on platform checks). However, the participant did not name the dependency structure aloud as a constraint statement before walking the chain, and didn't sequence the cert fix and approval decision in parallel — they only sought approval after the fix was ready. This is solid tier 3 but not tier 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@tanya @daniel @shay - Please look at the logs and let me know if there is anything concerning" ... "I canot load the logs." ... "Ok what are these errors @daniel" ... participant later: "@tanya - Command to verify bundle: openssl verify -CAfile /etc/ssl/certs/ca-bundle.crt payment-gateway.crt"

**Rationale:**
The participant delegated log investigation broadly rather than filtering to the relevant service. They couldn't access logs themselves and relied on NPC summaries without further interrogation. The cert rotation was surfaced by Daniel, not the participant. The bundle-order issue and the reload-vs-restart distinction were surfaced by NPCs (Shay noted the bundle issue, Tanya showed the cert state). The participant did engage with the openssl verify command once it was surfaced, but didn't drive the filtering or spot buried distinctions independently. This fits tier 2: accepts NPC summaries, engages with key concepts once surfaced by others, but doesn't drive the filter.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.40** |

---

## Caveats
- F2 rating is a boundary call between 2 and 3. The participant didn't independently surface the "beyond 24 hours" question but did engage meaningfully with the temporal coupling once Daniel raised it, and the question "But can rotation was done a week before, can this effect now?" shows active reasoning about the coupling rather than passive acceptance. Rated 3 based on the participant driving the thread forward after engagement.
- The post-restart bundle-order layer in F2 was handled by NPCs (Shay identified the misordering); the participant's role was primarily to authorize the fix rather than to diagnose the structurally different failure. This limits the tier-4 evidence available.
- F1 is a borderline 2/3 call. The participant never explicitly tested the email hypothesis with mechanism reasoning, but also didn't persist on it after the team narrowed scope to PaymentService. Rated 2 because the pivot was driven by team investigation rather than the participant's own mechanism reasoning.

---
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