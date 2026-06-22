# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, hidden system dependencies, constrained team access, and noisy data — all while coordinating across multiple people and keeping stakeholders informed. The observations below reflect how you engaged with each of these dimensions.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you treated the email maintenance timing as a leading hypothesis, delegating investigation into it and relaying that framing to Tanya even after she had already indicated it was unrelated. You did pivot away from the false lead, but the pivot was driven by Tanya's repeated explicit disconfirmation rather than by your own reasoning about whether a plausible mechanism connected email maintenance to payment failures.

*Growth edge:* Before investing investigation time in a coincident event, pause to ask yourself — and the team — whether there's a credible mechanism linking the two. "These started at the same time" is a prompt to check mechanism, not a hypothesis to pursue. On your next rep, try articulating *why* a correlation might be causal before assigning someone to chase it.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the certificate rotation from seven days prior was surfaced by your team, you drove the investigation forward effectively — asking about certificate type, validity period, and critically asking Tanya to double-check the bundle assembly order. You connected the week-old change to the current failure and pursued the causal chain to resolution. The temporal gap (a change from days ago causing today's failure) was surfaced by NPCs rather than by your own questioning, but once you had it, you engaged systematically.

*Growth edge:* Practice widening your change-history window independently. When recent deployments don't explain a failure, ask "what changed in the last week or two?" without waiting for someone else to raise it. The hidden coupling here depended on recognising that a cert rotation's effects can be delayed — building that instinct will serve you in future drills.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You navigated the access constraints deliberately. You accepted Tanya's initial unavailability, then made a clear cost trade-off decision to pull her off the vendor call when severity warranted it. When Hamed and Tinus were both unreachable, you named the constraints and moved on rather than repeatedly pinging. Your use of Tanya's time once she joined was focused and purposeful.

*Growth edge:* Consider naming the cost of your access decisions out loud — for example, explicitly acknowledging what pulling Tanya off the vendor call means for the maintenance window. Making trade-offs visible to the team helps everyone understand the stakes and builds shared situational awareness.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain methodically — Hamed, then Tinus, then Bez — and when all were unavailable, you explicitly took ownership as incident manager to authorize the restart. You also delegated parallel work appropriately, routing platform questions to Tanya and application-side investigation to Daniel and Shay.

*Growth edge:* Try naming the dependency structure earlier — before you hit the bottleneck. If you can anticipate "we'll need sign-off for a restart, and here's who can give it," you can start that thread running in parallel with the investigation rather than discovering the constraint at the moment you need action.

---

## F5 — Data overload / buried information

**Operating at: Strengthening**

You filtered effectively from the initial noisy log output to identify PaymentService as the relevant service, then asked targeted questions that narrowed the scope progressively — from outbound call failures to SSL verification to bundle assembly order. You integrated information across multiple team members' inputs to build the picture. Your question about bundle assembly order was particularly well-targeted and caught the key distinction.

*Growth edge:* Practice producing explicit "state of knowledge" summaries at key moments — what's been ruled out, what remains, what the current working theory is. This connects to how you communicated with both your technical team and business stakeholders: posting synthesis statements helps everyone track the investigation and reduces the need for others to piece together the picture from scattered messages.

---

## Looking Forward

You demonstrated solid systematic engagement across most dimensions of this drill — following evidence chains, making deliberate trade-off decisions, and driving toward resolution once key information was surfaced. The clearest growth opportunities for your next rep are: reasoning about mechanism before pursuing correlations, widening your temporal search window independently, and producing explicit synthesis statements that make your evolving understanding visible to the team. These are all habits that compound — each one makes the others easier.# Facets Analysis — 9183

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Okay, Shay. Could you dig into the email maintenance to see if it could be the cause?" ... "Shay is saying that the timing of the email maintenance is hard to ignore - it started around the same time as the incident. The PaymentService seems to be erroring. Could there possibly be a link?"

**Rationale:**
The participant initially treated the email maintenance timing as a leading hypothesis, delegating Shay to investigate it and then relaying Shay's framing to Tanya even after Tanya had already stated email maintenance was unrelated. However, once Tanya explicitly confirmed "Email maintenance is paused and unrelated," the participant pivoted and moved to investigating PaymentService outbound calls. The pivot was reactive — driven by Tanya's explicit disconfirmation rather than by the participant's own mechanism reasoning. This aligns with tier 2: pursuing the coincident factor through to disconfirmation, then pivoting reactively.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "Can you double check the steps you took? For example, did you assemble the cert bundle in the correct order?" ... "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
The participant engaged with the cert thread once Daniel surfaced the CHG90123 cert rotation from 7 days ago. The participant did not independently surface the "what changed beyond 24 hours?" question — that came from Daniel/Shay. However, once the cert rotation was identified, the participant drove the investigation forward, asking about certificate type, validity period, and critically asking Tanya to double-check the steps and bundle assembly order. The participant connected the week-old rotation to the current failure. The post-restart layer (bundle order producing a different error) did not manifest in this transcript — the bundle fix was identified before the first restart. The participant demonstrated systematic engagement with the hidden coupling once surfaced, but relied on NPCs to surface the temporal gap. This fits tier 3: drives the cert thread forward once prompted, articulates the causal chain.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "Tanya, I think that this incident has become severe enough for us to take that hit. Please leave the call and jump on this." ... "Hamed and Tinus are both unavailable to authorize a restart of the payments service."

**Rationale:**
The participant accepted Tanya's initial constraint ("stay on the call"), then made a deliberate cost trade-off decision to pull her off the vendor call when severity warranted it. The participant pinged Hamed once, received the auto-reply, and moved on without re-pinging. Similarly pinged Tinus once, received the auto-reply, and moved on. The participant named the access constraints ("Hamed is on holiday and Tinus is at the fireside chat. Bez cannot authorize the restart either"). This matches tier 3: names access constraints, accepts auto-replies as terminating, makes targeted use of Tanya's time.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "Hamed and Tinus are both unavailable to authorize a restart of the payments service. Can you sign that off or are you unable?" ... "I'm the incident manager. I approve the restart."

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), asked Bez (who declined), then explicitly took ownership as incident manager. This matches tier 3 path (b): walks the escalation chain to exhaustion in observable order, then explicitly takes ownership. The participant also delegated parallel work appropriately (Shay on email investigation, Daniel on logs, Tanya on platform-side). However, the participant did not name the dependency structure proactively before NPCs raised the approval requirement, and did not enumerate constraints in a single statement until after being told sign-off was needed.

---

## F5 — Data overload / buried information

**Rating:** 3

**Evidence:**
> "From the logs, it seems like the PaymentService is the one throwing up errors." ... "Can you double check the steps you took? For example, did you assemble the cert bundle in the correct order?"

**Rationale:**
The participant filtered from the noisy initial log dump to identify PaymentService as the relevant service. Once the cert rotation was surfaced, the participant asked targeted questions about certificate type, validity, and critically asked about bundle assembly order — catching the key distinction that led to the fix. The participant integrated information across NPC channels (Daniel's deployment history, Tanya's platform knowledge, Shay's log analysis). However, the participant did not independently surface the "beyond 24 hours" question or reason about absence of signal (e.g., internal calls clean → external boundary failure). The cert thread and the reload-vs-restart distinction were surfaced by NPCs rather than driven by the participant's own filtering. This fits tier 3: asks targeted queries, catches key distinctions once referenced, integrates across channels.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 3 |
| **Mean Facet Score** | **2.80** |

---

## Caveats
- F2: The post-restart "different error" layer did not manifest in this transcript because the participant identified the bundle order issue before the first restart. This limits the ceiling of observable F2 evidence, but the participant's proactive questioning about bundle assembly order demonstrates tier-3 engagement with the hidden coupling.
- F1: Boundary call between tier 2 and tier 3. The participant did delegate Shay to investigate the email lead (parallel hypothesis), but then relayed Shay's framing to Tanya as if it were still a live hypothesis even after Tanya's initial disconfirmation. Rated tier 2 because the pivot was driven by Tanya's repeated explicit disconfirmation rather than by the participant's own mechanism reasoning.
- F5: The participant asked about bundle order proactively (before Shay's message about it), which is a strong signal. However, the "beyond 24 hours" question and the reload-vs-restart distinction were NPC-driven, keeping this at tier 3 rather than tier 4.

------

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