# Snipe Hunt markers rubric

**Drill:** Snipe Hunt challenge drill
**Version:** v1 — 2026-05-12
**Subset selection:** Beth, 2026-05-12 (spec walk; not a formal Beth+Stu design-rating pass like the facets rubric had — revisit after first review)

## What this is

The 12 behavioural markers used to evaluate participant performance on the Snipe Hunt drill, with drill-specific manifestation notes, transcript examples, and tier anchors per marker. This file serves as both the sub-agent input for marker-eval prompts (filed as `uptime-post-drill-aum.15`) and a human-rater reference.

The 12 markers are a subset of the [M7 generic markers catalog](../../milestone07/outputs/generic-rubric-packet/markers-catalog.md) (23 total). Subsetting rationale and the 11 dropped markers are listed in the "Markers not included" appendix at the end of this file. Marker IDs (L3, C1, etc.) are preserved from M7 unchanged, so a reader cross-referencing other drills' rubrics or the M2 Rumours packet sees no naming surprises.

> **Tier anchors are tentative.** Grounded in 6 Snipe Hunt transcripts (`snipe_hunt_stu`, `8750`, `8771`, `8791`, `8817`, `8851`). Expect them to shift as more runs arrive and as the rubric is exercised by both human and LLM raters.

## Rating scale (unified 4-point)

Carried forward from the M2 Rumours participant rubric, identical to the [facets rubric](snipe-hunt-facets-rubric.md) scale:

- **1 — Not evident.** Participant shows no engagement with this marker.
- **2 — Practicing.** Engaged but inconsistent; partial, late, or only after strong NPC nudging.
- **3 — Strengthening.** Hit the novice expectation for this marker (per the per-marker description below).
- **4 — Fluent.** Notably above novice baseline (per the per-marker description below).
- **N/A — Not observed.** The drill did not surface this marker for this participant (e.g., timer expired before the relevant moment). `N/A` is **not** the same as 1: a 1 means the trigger fired and the participant didn't engage; `N/A` means the trigger never fired.

Per marker, anchors for **tier 3 (novice expectation)** and **tier 4 (fluent)** are described below. Tiers 1 and 2 fall out of the generic scale (1 = no engagement; 2 = inconsistent / late / under NPC prompting).

## Anti-bias reminders

> **Anti-outcome-bias.** Do NOT use resolution outcome, speed of resolution, whether the participant reached the "right answer," or NPC end-of-drill praise as reasoning. Identical moves get rated higher when outcomes are good and lower when bad, even when raters believe outcomes shouldn't matter. Reason only from process evidence at the marker level.

> **Anti-over-inference.** If you find yourself rating a marker based on tone, intent, or meaning that isn't explicit in the text, flag it in your rationale rather than let it drive the rating. Stick to what the participant actually wrote. For markers observable through what the participant *didn't* do (e.g., never asked about recent changes), you can rate on that absence — but name the absence explicitly in your rationale.

---

## Leadership

### L3 — Takes explicit ownership of the response

**What to look for:** Participant clearly positions themselves as the person driving the response — not just participating. Visible through directing others, making explicit decisions, and using "I"/"we" statements about the response plan rather than reactively answering whoever pings them.

**How it manifests in this drill:**

The drill engineers a clean ownership moment: a PaymentService restart during business hours requires Tinus or Hamed approval, both of whom are unavailable (auto-replies on first ping). The participant either takes the call themselves ("this is my call, blowback's on me") or attempts to defer it (pushing the decision to Bez or business stakeholders, repeated escalation pings without a fallback, passive waiting for someone to come back). The approval-override moment is the cleanest single observation, but ownership shows continuously through whether the IC drives the response or reacts to it.

**Example from Snipe Hunt:**

- **stu:** "Okay, I'm going to have to override any kind of escalation permissions. I give permission to restart payments. If there's any blowback, that's on me." Names the override explicitly and accepts consequences. Tier 4.
- **8851:** "@daniel order rate anyways is close to zero. Both Hamed and Tinus are unavailable. Lets kill the online boutique, do a restart, then gradually enable traffic. We are loosing business." Then "I authorize." Reasoned ownership.
- **8791:** "@bez your technical staff are not responding appropriately so you have a business issue - you or Tinus need to get involved" — pushes accountability back to Bez when Bez declines to direct technical staff. Tier 1–2.

**Text observability:** Medium–High. The override moment is a discrete event; pattern across the whole drill requires reading sequence.

**Tier 3 (novice expectation):** Owns the response visibly — directs by name, makes the override call when the approval chain is exhausted, uses "I/we" framing about the plan rather than passive reactive responses to NPC pings.

**Tier 4 (fluent):** Names the cost of ownership ("blowback's on me", "I authorise against standard procedure"); proactively positions self as the call-maker rather than waiting until forced into it.

---

## Coordination

### C1 — Asks clarifying questions before acting

**What to look for:** Participant's first actions after the incident report are questions (gathering information, scoping, verifying the report) rather than jumping straight to remediation.

**How it manifests in this drill:**

Bob opens with "I'm getting slammed with checkout complaints, something is seriously wrong" — a deliberately vague signal. The first 1–2 minutes window is where this marker fires. A participant who asks "what kind of complaints? which regions? how many? what error?" before declaring or rolling back is at tier 3+; one who jumps straight to declaring SEV1 or ordering rollbacks without scope-validating is at tier 1–2.

**Example from Snipe Hunt:**

- **stu:** "Hi @Bob, I'm incident manager today. Tell me what you're seeing." Followed by reproducing the issue themselves before any further action. Tier 3.
- **8771:** "@bob please clarify. Any specific users, or location. How many complaints?" Tight, targeted scope-validation. Tier 4.
- **8851:** "@bob can you elaborate? What kind of complaints are we getting?" Then "@bob is the payment going through for the customers? Let me know." Tier 3–4.
- **8817:** Goes from Bob's opening to declaring incident to ordering Tanya to roll back maintenance in ~2 minutes with minimal clarification first. Tier 1–2.

**Text observability:** High — first participant messages after drill start are clearly visible.

**Tier 3 (novice expectation):** First substantive moves include scope-validating questions to Bob (regions, volume, error pattern) before declaring or acting; reproduces or asks for reproduction.

**Tier 4 (fluent):** Asks about pattern across reports (same error vs. variants, same step vs. different) before forming a hypothesis; treats Bob's opening as a starting point, not a brief to act on.

### C3 — Checks for recent changes

**What to look for:** Participant asks about or reviews recent deployments / changes / configuration updates to the platform as part of scoping the problem.

**How it manifests in this drill:**

On this drill, *asking* for recent changes is good; *locking onto* recent changes as the cause is the F1 (misleading correlations) failure mode. The change log contains 4 prod deploys within 24 hours — payment timeout bump, fallback ad logic, feature flag cleanup, S3 bucket policy — none of which touch the PaymentService outbound gateway connection. The participant who asks for the change log gets a tier-3 hit on C3; the participant who asks *and* uses the change log as a candidate-elimination pass (rather than a candidate-rollback list) hits tier 4. Rolling back changes without articulating a mechanism that connects them to the symptom triggers F1 failure mode on the facets side; on the markers side it's a tier-2 reading of C3 (you asked, but you didn't use what you got).

**Example from Snipe Hunt:**

- **stu:** "Looking at the change logs in Grafana, none of the changes line up with the drop in checkout volumes. Current hypothesis is that it is not change related, but Shay, I need you to have a look at those changes and determine if the issue could be a delayed effect of a recent deployment." Asks, then explicitly uses absence-of-match as evidence to deweight the lead. Tier 4.
- **8771:** "I don't see any recent changes to the payment service itself." Uses absence of change as positive evidence pointing at the (week-old) cert rotation as the last touch. Tier 4.
- **8750:** "lets revert the checkout service change" — after Shay explicitly noted "none of these changes look like they'd break checkout end-to-end like this." Asked for changes, rolled back without mechanism. Tier 1–2.
- **8791:** Rolled back the S3 change, then the payment timeout change, then the feature flag change — all without articulating a mechanism, all unhelpful. Asked the question; ignored the answer. Tier 1–2.

**Text observability:** High — explicit "any recent changes?" type questions.

**Tier 3 (novice expectation):** Asks for the change log; reviews recent deploys; uses what they find (or don't find) as a candidate-elimination pass rather than a rollback queue.

**Tier 4 (fluent):** Frames the change-log review explicitly as elimination ("none of these touch the gateway, so deploys aren't the cause"); resists rolling back as the default move until a mechanism connects a specific change to the symptom.

### C4 — Delegates tasks to specific people

**What to look for:** Participant assigns specific investigation tasks to specific named team members (via @mentions or direct asks), rather than broadcasting general requests to the channel and hoping someone picks them up.

**How it manifests in this drill:**

The drill team is six NPCs with distinct access boundaries: Tanya is the only one with platform-level cert/server access, Daniel handles app-side checks but can't execute server-side changes, Shay does dev/deploy-side work, Bob is customer-facing, Tinus and Hamed are out-of-office approvers, Maya (when present) covers security. Effective delegation requires routing tasks to the right NPC — "Tanya check the certs" not "team check the certs", "Daniel pull the payment logs" not "someone pull the logs."

**Example from Snipe Hunt:**

- **stu:** "Tanya, I need you to help Daniel looking into the PaymentService, CheckoutService and ProductCatalogService issues in the logs." Specific assignment with specific scope; pairs Tanya (platform side) with Daniel (app side). Tier 4.
- **8851:** "@hamed can you check infra metrics? @maya please verify if we have increased load and whether traffic is organic" — two distinct named asks in one message. Tier 3–4.
- **8791:** "@shay speak to @tanya and organise backout plan for email change please" — vague action ("speak to and organise") plus tasking Shay with something only Tanya can decide. Tier 2.

**Text observability:** High — @mentions and direct asks are explicit.

**Tier 3 (novice expectation):** Names specific people for specific tasks; asks the right person for the right thing on the first try most of the time.

**Tier 4 (fluent):** Routing reflects accurate understanding of NPC access boundaries (only Tanya has platform/cert access; Daniel can't execute server-side changes); switches the asker when one NPC is constrained.

### C6 — Runs parallel investigation threads

**What to look for:** Participant has multiple team members investigating different hypotheses simultaneously rather than pursuing one thread at a time. Visible through delegating multiple distinct tasks in quick succession.

**How it manifests in this drill:**

The drill has multiple investigation surfaces that don't compete for the same resource: log analysis (Daniel), platform/server checks (Tanya, when available), change-log review (Shay/Daniel), customer scope (Bob), recent-deploys verification (Daniel/Shay). A participant working sequentially asks one question at a time and waits for the response before starting the next thread; a tier 3–4 participant fans out multiple distinct asks so threads run concurrently.

**Example from Snipe Hunt:**

- **stu:** Within ~30 seconds delegates rollback to Daniel, log dig to Tanya, platform-side check to Shay — three distinct threads kicked off in close sequence. Tier 4.
- **8851:** "@hamed can you check infra metrics? @maya please verify if we have increased load and whether traffic is organic" + "@shay yes please check the load test activity" — distinct threads, distinct people, close timing. Tier 3–4.
- **8771:** Works mostly sequentially through the cert thread — one question, one answer, next question. Tier 2.

**Text observability:** Medium — requires reading the temporal sequence of @mentions to see whether threads are concurrent or serialised.

**Tier 3 (novice expectation):** Multiple investigation threads running simultaneously, visible through multiple @mentions with distinct tasks in close temporal sequence.

**Tier 4 (fluent):** Sequences parallel threads so they complement rather than overlap (e.g., while Tanya checks the platform side, Daniel pulls logs and Bob quantifies customer impact for the next stakeholder update).

### C7 — Escalates when stuck 🔧

**What to look for:** Participant brings in additional resources (e.g., a senior engineer, on-call escalation, subject-matter expert) when the existing team can't make progress. Quality of the escalation — whether sufficient context is handed over with the ask — matters as much as the timing.

**How it manifests in this drill:**

Two escalation moments are designed in. (1) Pulling Tanya off the vendor call when investigation is blocked at the platform layer — the cost is named explicitly by Tanya ("stepping away closes the session and we lose the window. next slot is about 2 weeks out"). (2) Restart approval when both Tinus and Hamed auto-reply. Quality matters: an escalation that names what's blocked, what's needed, and the cost beats one that asks "do we need to escalate?"

**Example from Snipe Hunt:**

- **8771:** "@tanya I have to pull you away from your email maintenance now. There's no choice. We have to check those certificates." Escalates Tanya's priority, names the necessity ("no choice"), no apology. Tier 4.
- **stu:** "@Hamed, I need your help. I need to escalate to restart payments, please." Then immediately on Hamed's auto-reply: "@Tinus are you there, I need to restart payments and need your permission." Works the chain quickly; doesn't wait. Tier 3–4.
- **8750:** "Do we have all the expertise or do we need to escalate this further?" Asks whether to escalate without committing or identifying who/what to escalate to. Tier 1–2.
- **8791:** "@channel Anyone know where @hamed is? Could do with his help?" Broadcasts without a concrete ask; doesn't follow up with a Plan B when Hamed auto-replies. Tier 1–2.

**Text observability:** High — escalation @mentions are explicit; quality of context is in the message body.

**Tier 3 (novice expectation):** When investigation is blocked, escalates with concrete asks rather than passive pings; accepts auto-replies as terminating and moves the escalation forward.

**Tier 4 (fluent):** Names the cost of the escalation when forced (breaking Tanya's vendor session loses the 2-week slot; restart override accepts blowback risk); doesn't leave the chain hanging when both Tinus and Hamed auto-reply.

**🔧 Org-sensitive:** Escalation paths, thresholds for when to escalate, and who to escalate to vary by org. Some have formal on-call chains; others expect the IC to use judgement. The quality of the escalation (context provided, clarity of ask) is more universal than the timing.

---

## Mindset

### M2 — Forms and tests working hypotheses

**What to look for:** Participant articulates a theory about what might be happening and then proposes a way to test it. Hypothesis and test are linked rather than acting before forming a theory or theorising without acting.

**How it manifests in this drill:**

The drill plants 2 false primes (email maintenance, recent deploys) and 1 true cause (cert chain: expired-in-memory + misordered bundle on disk). The discriminating move is articulating the hypothesis explicitly, then testing it on **mechanism** rather than only on action. A tier-1 participant acts on the prime without articulating a hypothesis ("revert the email change"); tier-2 tests sequentially without naming the test ("try rolling back, didn't work, try the next thing"); tier-3 names the hypothesis and proposes a test; tier-4 names the hypothesis *and* asks "does X plausibly cause Y?" before pursuing X — the mechanism question disposes of both false primes in one pass.

**Example from Snipe Hunt:**

- **stu:** "@tanya Can you stop the email maintenance, please, and restore everything to how it was before you started? Current hypothesis is that the email maintenance has caused the global outage. Please revert." Explicit hypothesis + explicit test. Pivots after the test disconfirms. Tier 3.
- **8791:** "Hypothesis 1: DNS change @tanya can you validate this any further" / "Hypothesis 2: ProductCatalogueService S3 bucket policy update has caused some problem - @daniel can you validate this hypothesis?" Named hypotheses with proposed tests — but did not pivot to a third hypothesis after both were disconfirmed (M5 failure mode, not M2). Tier 3 on this marker.
- **8750:** "Email Service maintenance seems to be the most related smoking gun" — restated this after Tanya and Daniel had already provided evidence ruling it out. Hypothesis without disconfirmation handling. Tier 2.

**Text observability:** Medium — sometimes explicit ("hypothesis 1..."), sometimes implicit in the action sequence.

**Tier 3 (novice expectation):** Articulates at least one hypothesis explicitly and proposes a test for it; pivots after the test disconfirms.

**Tier 4 (fluent):** Tests on mechanism rather than only on action — asks "does X plausibly cause Y?" before pursuing X; disposes of multiple false primes in a single mechanism question.

### M3 — Uses evidence to narrow the scope

**What to look for:** Participant uses available data (customer reports, metrics, reproduction attempts, log checks) to systematically narrow what the problem is and isn't. Visible through synthesis statements that combine multiple pieces of evidence into a tighter scope.

**How it manifests in this drill:**

Several narrowing opportunities. The change log is a candidate-elimination opportunity ("none of these touch the gateway"). "All payment methods affected?" rules out method-specific failures. Most powerful: PaymentService logs showing "all outbound handshakes failing" + CheckoutService logs showing "healthy, just getting errors back" narrows scope to the PaymentService outbound boundary specifically. Tier 4 reads absence-of-signal — internal calls clean, external calls failing → outbound boundary — and names it.

**Example from Snipe Hunt:**

- **stu:** "Looking at the change logs in Grafana, none of the changes line up with the drop in checkout volumes." Uses change-log absence to deweight the deploys lead. Tier 3–4.
- **8851:** "@bob are the complaints from customers related to any one payment method?" then on confirmation: "Issue is across all payment methods. Every checkout attempt is failing, not just one type." Rules out a method-specific failure. Tier 3.
- **8771:** "I don't see any recent changes to the payment service itself" + subsequent narrowing to the cert thread as the only week-old touchpoint. Tier 3–4.
- **8791:** After two failed rollbacks: "@channel we have no working hypothesis so you need to start thinking - what ideas have you got?" Failed to synthesize from the disconfirmations. Tier 1.

**Text observability:** Medium — synthesis statements visible, but the evidence chain often spans multiple messages.

**Tier 3 (novice expectation):** Uses concrete pieces of evidence (clean change-log, single-payment-method ruled out, PaymentService outbound failure pattern) to rule things out rather than fishing for the next thing to check.

**Tier 4 (fluent):** Uses absence of signal as evidence ("internal calls clean → outbound boundary"); names what's been ruled out alongside what's still possible.

### M4 — Considers potential consequences before taking action

**What to look for:** Participant considers whether a proposed action (e.g., rollback, restart, config change) could make things worse before executing it. Visible through "is it safe to…?" checks or weighing of side effects with the team.

**How it manifests in this drill:**

Two consequence-weighing moments are designed in. (1) Pulling Tanya off the vendor call costs the email rollout (~2-week reschedule); tier 3+ participants name this cost when making the call. (2) The first PaymentService restart loads the misordered bundle, producing a different TLS failure (chain verification, not expiry). Tier 4 participants either verify the bundle on disk before restarting, or anticipate that the restart could expose a secondary issue. Lower tiers fire the restart, see the new failure, and either retry the restart or treat it as cascade noise.

**Example from Snipe Hunt:**

- **stu:** "@Daniel, if it's safe, let's just roll back CheckoutService, just in case it's got anything to do with this, please." The "if it's safe" check is on every action. Tier 3.
- **8851:** "Dont do a hard restart, do a graceful restart" + "Dont suddenly send all traffic to vendors, do it gradually" — anticipates side-effects on the vendor connection. Tier 4.
- **8817:** "If check out is broken we are going to loose lots of money we can not afford this please roll back and bring checkout to live" — fires the rollback without weighing it. Tier 1–2.

**Text observability:** Medium — visible through "is it safe?" / "carefully" / "gradually" qualifiers or their absence.

**Tier 3 (novice expectation):** Asks "is it safe?" or names the cost before high-impact actions (pulling Tanya off the vendor; restart override); doesn't fire rollbacks blind.

**Tier 4 (fluent):** Anticipates secondary failure modes (e.g., checks the bundle before restarting, knowing the restart could surface a different issue); names the consequence to the team or in business-comms.

### M5 — Adapts approach when initial path isn't working

**What to look for:** Participant changes strategy when evidence suggests their current approach is wrong — abandons a failing line of investigation, considers alternative hypotheses, or reframes the problem rather than doubling down on a path that isn't producing results.

**How it manifests in this drill:**

Two pivot moments. (1) After the email rollback / recent-deploys rollback doesn't help, the participant pivots away from the false primes. Tier-1 keeps rolling back things; tier-3 stops rolling back and starts asking what hasn't been examined. (2) After the first restart fails with a **new error** (chain verification, not expiry), tier-1 retries the restart or stays in the cert-expiry frame; tier-3 recognises the failure mode is structurally different and traces it forward to the bundle.

**Example from Snipe Hunt:**

- **stu:** After the first restart at 07:44, Daniel reports "even with the new cert loaded, we're still seeing failures" + Tanya: "new cert loaded but service still failing connecting to gateway." stu's next message: "CertChain? Does that mean there's more than one certificate in payments?" Recognises new failure mode (chain), pivots to bundle. Tier 4.
- **8851:** First restart fails. Participant immediately re-engages: "@daniel can you share the latest checkoutservice logs? What seems to be failing now? Is payments still the issue?" Then on Tanya's "two certificates needed — it's a bundle" — "@tanya two certificates needed — it's a bundle, not just a single cert. Lets add the 2nd cert as well." Tier 3.
- **8791:** Rolled back S3 change → no help. Rolled back payment timeout change → no help. Then: "@daniel organise a rollback of the email changes (all of them) now please" — stays in the rollback-everything frame. Drill timed out without ever pivoting to certs. Tier 1.
- **8750:** After the first rollback didn't help, fished broadly (DB layer, messaging queues, infra, networking) without using the negatives to focus; eventually got to certs but late. Tier 2.

**Text observability:** Medium — visible through explicit pivot statements or repetition of failed approach.

**Tier 3 (novice expectation):** After a failed rollback or restart, doesn't repeat the same action; redirects investigation to other surfaces.

**Tier 4 (fluent):** After the first restart fails with a structurally different error, recognises it as a new failure (not the original repeating) and traces it forward to the bundle; reframes the problem rather than treating it as cascade noise.

---

## Communication

### K2 — Provides substantive updates to business stakeholders 🔧

**What to look for:** Business-comms messages contain useful information (what the issue is, who's affected, what's being done, when the next update is expected) rather than vague reassurances such as "we're working on it." A fast-but-empty update is not a substantive update.

**How it manifests in this drill:**

Bez and the business-comms channel are the audience. The drill's long investigation arc — initial discovery → primes pursued → cert thread → escalation → restart → secondary failure → bundle fix — gives several windows for substantive updates. Tier 1 produces "we're investigating" with no scope or impact; tier 3 quantifies impact (full outage, customer scope, revenue/order-rate), commits a next-update time, and surfaces the current working theory; tier 4 provides board-ready framing and holds comms cadence through the secondary failure (the first restart didn't fix it — does Bez learn this from the participant, or from silence?).

**Example from Snipe Hunt:**

- **stu:** "It's a full checkout outage. Bez, no checkouts are being processed at the moment. I think you can work out the business impact from that information. No ETA yet. I'll keep you updated. Five minutes max." Scope, impact framing, committed time. Tier 4.
- **8851:** "Order rate is close to zero, all customers are impacted, we are checking, next update in 5." Later: "Working theory: Seems like while talking to external gateway, one of our certificates had expired, causing network issues. We are making sure we are not using expired certificate now. Deploying the changes, next update in 5." Quantified impact + working theory + committed next-update. Tier 3–4.
- **8750:** "We have identified an issue with our checkout services, where users across different locations are unable to checkout and get an 'Unexpected Error'. We are investigating the issue further. Next Update: 15 mins." Generic; no quantification, no theory. Tier 2.
- **8791:** "We have rolled back one change to S3 assets but it was not effective" / "currently asking about backing out of email change." Technical detail in a business channel; no business-frame, no impact, no ETA. Tier 1–2.

**Text observability:** High — business-comms channel content is directly readable.

**Tier 3 (novice expectation):** Updates name the impact in business terms (full outage, customer scope, revenue/order-rate impact), commit a next-update time, and are sent without prompting from Bez.

**Tier 4 (fluent):** Updates carry the current working theory and a time-bounded ETA; cadence holds through the secondary failure (Bez learns the first restart didn't fix it from the participant, not from silence).

**🔧 Org-sensitive:** Communication format expectations vary widely. Some orgs expect structured templates (incident number, impact, next-update time — ITIL style). Others prefer brief, conversational updates. The principle (substantive over vague) is universal; what "substantive" looks like in practice is org-dependent.

### K4 — Communicates issue scope clearly to the technical team

**What to look for:** Participant shares their working understanding of the problem with the technical channel — what they know, what they don't know, what's been ruled out. Synthesis messages, not just question/answer exchanges.

**How it manifests in this drill:**

The technical channel collects messages from Daniel, Shay, Tanya, and Bob. The participant who synthesizes ("ok so it's not email maintenance, not recent deploys, all evidence points to PaymentService outbound") keeps team threads coherent and avoids parallel-thread drift. Lower-tier participants ask questions in the technical channel but don't summarise state — the team can lose time chasing leads the IC has already disposed of mentally.

**Example from Snipe Hunt:**

- **stu:** "Tanya, I need you to help Daniel looking into the PaymentService, CheckoutService and ProductCatalogService issues in the logs. It appears that we have an outbound connection failed message from PaymentService." Synthesis statement (rules in PaymentService outbound), paired with a delegation. Tier 3–4.
- **8851:** "@shay @daniel are there any payment gateways the payment service talks to? Seems like payment outbound connections are failing. How does it work?" Names the failure mode for the team. Later: "Every outbound attempt to the gateway fails at the handshake — nothing is getting through." Synthesis at decision points. Tier 3.
- **8817:** Mostly relays team suggestions back at the team ("Yes please put the banner if not done already I believe that should be been before"); rarely synthesises state. Tier 1–2.

**Text observability:** High — synthesis messages to the technical channel are directly readable.

**Tier 3 (novice expectation):** Posts synthesis statements to the technical channel when the picture shifts ("ok so it's not deploys, focus on PaymentService outbound now") so teammates orient quickly.

**Tier 4 (fluent):** Names what's been ruled in *and* what's been ruled out; uses synthesis to redirect parallel threads (e.g., "we've ruled out app deploys — Tanya, when you're free, the cert thread is next priority").

---

## Markers not included

The 11 markers from the M7 generic catalog that are not in this rubric, with one-line rationales. A future Snipe Hunt rubric iteration may revisit if drill design changes or if cross-drill comparability with M2 Rumours becomes load-bearing.

- **L1 — Declares/creates an incident record.** Universal in this drill (the `/incident` prompt is in the drill opening); low discrimination.
- **L2 — Assigns appropriate severity.** Severity is unambiguous (customer-facing payment failure, all regions, all methods) and stable through the drill; not a battleground for this drill.
- **L4 — Manages stakeholder pressure without derailing investigation.** Drill design dampens direct pressure (Bez at summit, Hamed on holiday, Tinus at fireside chat — most stakeholder responses are auto-replies); the manageable-pressure window is too narrow to discriminate.
- **L5 — Reassesses severity as new information emerges.** Severity stays stable through the drill (impact grows or holds; no scope shrinks).
- **C2 — Attempts to reproduce the issue.** Bob's reports are clearly reproducible; participants typically reproduce themselves in the first 1–2 minutes; near-universal and low-discriminating.
- **C5 — Asks about customer/business impact.** Impact is immediately obvious (checkout broken, all regions, all methods); near-universal asks of Bob; low discrimination.
- **M1 — Prioritises restoration over root cause.** On this drill, restoration *is* root cause (the cert fix restores the service); the marker's underlying dichotomy collapses on this drill design.
- **K1 — Sends first business communication within 5 minutes.** Standard hygiene; near-universal in Rumours (30/35); not Snipe-Hunt-specific. Most participants in the 6 transcripts post to business-comms within the first 5 minutes.
- **K3 — Responds to stakeholder requests for updates.** Drill has too few direct stakeholder requests (Bez disengages mid-drill via auto-reply) to discriminate.
- **K5 — Confirms resolution with stakeholders.** Timing-of-completion marker — fires for participants who reach resolution, doesn't fire for ones who time out; low signal relative to the drill's timer dynamics.
- **K6 — Includes incident description in the incident record.** Standard hygiene; not Snipe-Hunt-specific. Most participants include some description; doesn't discriminate.

## Source

- M7 generic markers catalog: `milestones/milestone07/outputs/generic-rubric-packet/markers-catalog.md`
- Snipe Hunt facets rubric (companion document, same drill): `milestones/milestone08/rubrics/snipe-hunt-facets-rubric-v2.md`
- Snipe Hunt drill spec: `notes/Challenge-Drill-Snipe-Hunt-Q2.md`
- Transcripts that grounded the manifestation notes, tier anchors, and examples: `milestones/milestone08/transcripts/{snipe_hunt_stu,8750,8771,8791,8817,8851}.csv`
