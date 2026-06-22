# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to reason through systemic complexity — separating correlated-but-unrelated signals from actual causes, navigating hidden dependencies, and coordinating a response when key people and information aren't readily available. This report covers what showed up in your run and where the growth edges are for your next rep.

---

## F1 — Misleading correlations

**Operating at: Practicing**

You engaged with the timing of recent changes and asked useful questions about whether email maintenance could explain the symptoms. You also caught a timing discrepancy — noting that a DNS change was too recent to account for complaints that had already been running for twenty minutes. However, when initial hypotheses didn't pan out, your pivot came from failed experiments (rollbacks producing no improvement) rather than from reasoning about *why* a given change couldn't explain the observed failure mode. Tanya flagged that the recent deploys didn't touch the platform or network layer, but rollbacks proceeded anyway.

**Growth edge:** Before acting on a correlation, try articulating the mechanism aloud — "this change could cause handshake failures *because*…" If you can't complete that sentence, treat the correlation as unconfirmed and keep looking rather than testing it through rollback.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the cert rotation surfaced as a candidate cause, you engaged with it meaningfully. When the first restart failed with a different error, you didn't simply retry — you asked what could cause the new symptom and followed the thread to the certificate bundle issue. You connected the "rotated seven days ago" timing with the process not picking up the new cert into a coherent causal chain. The reframe after the failed restart was reasonably quick and showed flexibility in your mental model.

**Growth edge:** The "what changed beyond the last 24 hours" question was surfaced by teammates rather than by you. On the next rep, consider explicitly widening the change window early — especially when recent changes don't mechanistically explain the symptoms.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You handled the unavailability of both approvers cleanly — pinging Hamed, pivoting to Tinus when Hamed auto-replied, and then explicitly taking ownership when neither was reachable. You named the constraint clearly and made the decision to proceed under emergency guidance. You also pulled Tanya off a vendor call appropriately given the severity.

**Growth edge:** When pulling someone off another commitment, explicitly naming the cost trade-off ("I know this interrupts the vendor call — here's why this takes priority") helps the team understand your reasoning and builds trust in your prioritisation. Batching your questions to Tanya before pulling her in could also reduce context-switching overhead.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain in a logical order and delegated work to available team members — routing platform checks to Tanya, application-side tasks to Daniel, and status-page updates to Bob. When the approval blocker emerged, you resolved it by taking ownership rather than stalling. You assigned tasks to specific people with scoped purpose throughout the drill.

**Growth edge:** The approval question only arose when Tanya flagged it. On the next rep, try mapping the full dependency structure early: "to restart, I need X approval; to get X, I need Y person." Naming these chains proactively lets you sequence preparation in parallel — for example, seeking approval readiness while the cert fix is being prepared.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You initially chased the loudest signal — CheckoutService errors and email maintenance timing — rather than filtering toward the specific failing component. Teammates had to surface that PaymentService was the relevant service and that the cert rotation thread was the productive lead. Once the bundle issue was identified by others, you engaged with the documentation reference and connected it to the fix, but the filtering work was largely done for you.

**Growth edge:** When multiple services show errors, ask early: "which service is *originating* the failure versus *reacting* to it?" This helps you cut through noisy dashboards. Similarly, when reviewing change logs, actively cross-reference each change against the specific failure mode rather than treating the list as a rollback queue.

---

## Looking Forward

Your strongest pattern in this run was adaptability after a failed action — you didn't repeat what didn't work, and you engaged with new information when it appeared. The growth edge that cuts across multiple areas is *proactive mechanism reasoning*: before testing a hypothesis through action, articulate why it could explain the specific symptoms you're seeing. This single habit would sharpen your filtering, reduce unnecessary rollbacks, and help you surface hidden causes earlier. Carry that into your next rep.---

# Facets Analysis — 8930

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "@shay exactly when did the DNS changes go live?" ... "@shay why would Tanya's email maintenance has influenced this?" ... "@daniel can we rollback any of those changes?" ... "@daniel lets start by rolling back the checkout service because that is the one with all the errors"

**Rationale:**
The participant initially pursued the email maintenance timing correlation (asking Shay about DNS timing) and then pursued recent deploys as the leading hypothesis, ordering rollbacks of CheckoutService and ProductCatalogueService. However, when Shay admitted "honestly, not sure it would" and when rollbacks produced no improvement, the participant pivoted — asking Tanya about platform-side issues and eventually reaching the cert thread. The pivot was reactive (driven by failed rollback experiments) rather than by mechanism reasoning, placing this squarely in tier 2.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "@tanya the SSL rotation looks very suspicious is there anything in there which could be causing this issue?" ... "Wait — it restarted and it's still down? That shouldn't happen if the cert was the only problem." ... "@tanya what could be the cause of something like that?"

**Rationale:**
The participant engaged with the week-old cert rotation as the root cause once Daniel surfaced it ("only cert-related change is CHG90123... 7 days ago"). After the first restart failed, the participant did not repeat the restart or blame downstream services — instead, within approximately 3-4 exchanges, they asked Tanya about the cause and engaged with the bundle/chain issue. They connected "rotated 7 days ago" + "process didn't pick up new cert" into a causal chain. However, they did not independently surface the "what changed beyond 24 hours" question — Daniel/Shay raised it. The post-restart reframe was reasonably quick but not immediate, placing this at tier 3.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@tanya neither Hamed or Tinus are available right now. I am incident commander and I take responsibility for this major action" ... "Both Hamed and Linus are currently unavailable, is there any way to contact one of them urgently?"

**Rationale:**
The participant accepted auto-replies from Hamed and Tinus as terminating (did not re-ping them after the auto-reply). They named the access constraints explicitly ("Both Hamed and Linus are currently unavailable"). They initially asked Tanya to pause the vendor call appropriately given the severity, and when Tanya noted she couldn't restart without approval, the participant took ownership clearly. However, they did not batch questions to Tanya or articulate the cost trade-off verbally when pulling her off the vendor call — the pull was direct without explicit cost reasoning. This meets tier 3 but not tier 4.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@tanya neither Hamed or Tinus are available right now. I am incident commander and I take responsibility for this major action" ... "I am following emergency guidance and am making all decisions"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), asked about emergency escalation process, then explicitly took ownership and issued the authorisation. This matches tier-3 path (b) cleanly. They also delegated parallel work to available NPCs (Daniel on logs, Tanya on platform investigation, Bob on status page). On the second restart (after bundle fix), they authorised without re-litigating ("Lets kick off another service restart then"). However, they did not name the full dependency structure aloud as a single enumerated constraint or sequence cert fix and approval readiness in parallel — the approval question only arose when Tanya flagged it.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@daniel lets start by rolling back the checkout service because that is the one with all the errors" ... "@tanya can you check if the SSL certs are still valid on checkout service please?" ... "From the docs @tanya the problem is documented"

**Rationale:**
The participant initially chased the loudest signal (CheckoutService errors, email maintenance timing) rather than filtering to PaymentService specifically — Daniel and Tanya had to surface that PaymentService was the failing component. The participant did not independently identify the reload-vs-restart distinction from the runbook, nor did they drive the cert-rotation thread themselves (Daniel/Shay surfaced it). However, once the bundle issue was surfaced by NPCs, the participant engaged with the documentation reference and connected it to the fix. They accepted NPC summaries without much further interrogation. This is consistent with tier 2 — engaged but reliant on NPC filtering.

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
- F1: The participant did ask Shay "why would Tanya's email maintenance has influenced this?" which shows some mechanism-questioning, but this came after already pursuing the DNS timing lead and was followed by ordering rollbacks of recent deploys — the overall pattern is still reactive pivoting rather than mechanism-first reasoning.
- F2: Borderline 2/3. The participant did not surface the "beyond 24 hours" question independently, but their post-restart behaviour (not repeating the restart, engaging with the new error type) was reasonably skilled. Rated 3 based on the post-restart reframe quality.
- F5: The participant's question to Tanya about "SSL certs on checkout service" (rather than payment service) suggests incomplete filtering, though this may have been a naming slip given the context.

------

# Markers Analysis — 8930

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "@tanya neither Hamed or Tinus are available right now. I am incident commander and I take responsibility for this major action"

**Rationale:**
The participant explicitly declares themselves as incident commander and takes responsibility for the restart override when both approvers are unavailable. They also state "I am the incident commander" and "I am in control" earlier. However, they don't proactively position themselves as the decision-maker early on — the ownership declaration comes relatively late and partly in response to the approval blocker rather than being established from the outset.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob what are user's complaining about?" ... "Thanks @bob is there any pattern to the issues?"

**Rationale:**
The participant's first actions after Bob's alert are clarifying questions about what users are experiencing and whether there's a pattern. They gather scope information (regions, volume, pattern) before declaring the incident or taking remediation actions. This meets the novice expectation of scope-validating before acting, though the questions are somewhat generic rather than deeply targeted.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "What else changed recently @shay? Anything apart from email maintenance?" ... "@daniel can I have details on all of those please" ... "We started seeing errors around 07:50 UTC so a few of those changes are in scope"

**Rationale:**
The participant asks for recent changes and reviews them, which is good. However, they then attempt to roll back CheckoutService and ProductCatalogueService without articulating a mechanism connecting those changes to the handshake failures. Tanya explicitly states "None of those changes touch the platform or network layer. They don't explain the handshake failures I'm seeing," yet the participant proceeds with rollbacks anyway. They asked the question but didn't effectively use the answers as an elimination pass.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya please look at the logs for the checkout service and see if you can come up with any theories as to the issue" ... "@daniel please can you put up the maintenance banner please" ... "@daniel can you check the logs again after the restart?"

**Rationale:**
The participant consistently uses @mentions to assign specific tasks to specific people throughout the drill. They route platform-level checks to Tanya and app-side tasks to Daniel appropriately. The delegation is generally well-targeted, though there are a few instances of asking the wrong person initially (e.g., asking Tanya to check "checkout service" logs when the issue is PaymentService platform-side).

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@tanya please pause the email maintenance and help us out with this incident" ... "What else changed recently @shay? Anything apart from email maintenance?" ... "@daniel those logs you posted, do they point to a specific issue?"

**Rationale:**
The participant does engage multiple team members, but the investigation is largely sequential rather than parallel. They ask one question, wait for the response, then ask the next. There are moments where multiple threads are active (Tanya checking platform, Daniel checking logs, Shay reviewing changes), but these emerge organically rather than being deliberately fanned out in close temporal sequence.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@hamed can you join us please. What was your change around permissions related to?" ... "@tinus I need your assistance as @hamed is on holiday. We are trying to understand the change that recently went in"

**Rationale:**
The participant escalates to Hamed, then immediately pivots to Tinus when Hamed auto-replies. They also pull Tanya off the vendor call when needed. When both approvers are unavailable, they accept the situation and take ownership. The escalations include some context about what's needed, though they could be more specific about what's blocked and why.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "We started seeing errors around 07:50 UTC so a few of those changes are in scope" ... "@daniel can we rollback any of those changes?" ... "@tanya can you follow up on any potential impacts from the email maintenance?"

**Rationale:**
The participant doesn't explicitly articulate hypotheses before testing them. They pursue the recent-changes angle and email maintenance angle without naming them as hypotheses or explaining the mechanism by which they could cause the observed symptoms. The rollbacks are attempted without stating "my hypothesis is X, and rolling back will test it." They eventually reach the cert issue through Tanya's investigation rather than through hypothesis-driven reasoning.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "@shay that was only 3 minutes ago, @bob said customers had been seeing issues for 20 minutes"

**Rationale:**
The participant makes one notable narrowing observation — noting the timing discrepancy between the DNS change (3 minutes ago) and the complaints (20 minutes). However, they don't consistently synthesize evidence to narrow scope. Despite Tanya stating "None of those changes touch the platform or network layer," the participant still rolls back changes. They don't produce synthesis statements combining multiple evidence points to rule things out systematically.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "@tanya that is fine, the site is currently down" (in response to Tanya noting brief interruption during restart)

**Rationale:**
The participant shows minimal consequence-weighing before actions. They roll back CheckoutService and ProductCatalogueService without discussing potential side effects. When ordering the restart, they don't ask "is it safe?" or consider what could go wrong. The one instance of consequence acknowledgment is after the bundle fix when they note the site is already down so a restart interruption is acceptable — but this is reactive rather than proactive.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "@tanya what could be the cause of something like that?" ... "Is the new certificate not valid?" ... "From the docs @tanya the problem is documented"

**Rationale:**
After the first restart fails with a new error (cert chain broken vs. expired cert), the participant doesn't simply retry the restart. They ask what could cause the new error, engage the team on the bundle issue, and follow through to the correct fix. They also pivot away from the rollback approach after two failed rollbacks and redirect investigation to the platform/cert side. This meets the novice expectation of not repeating failed actions.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Total outage, I am getting a team together to work through the issue" ... "We still haven't established a root cause yet. I can't give an eta on restore yet I am following emergency guidance and am making all decisions Next update 5 minutes"

**Rationale:**
The participant provides updates to Bez but they are largely vague — "total outage," "working through the issue," "can't give an ETA." They don't quantify revenue impact in business terms (despite Bob providing the numbers), don't share the working theory when they have one, and the updates lack the substance that would help Bez communicate to the board. The "next update in 5 minutes" commitment is good but the content is thin.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "We started seeing errors around 07:50 UTC so a few of those changes are in scope" ... "Thank you, we think we've understood the root cause and I'm preparing remediation actions"

**Rationale:**
The participant rarely posts synthesis statements to the technical team. They don't summarize what's been ruled out or frame the current working understanding for the team. Most of their technical channel messages are questions or action requests rather than state-of-the-world summaries. The team members (Daniel, Tanya, Shay) end up providing more synthesis than the IC does, which is inverted from the expected pattern.

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
- For C3, the participant did ask about changes and review them, but the key discriminator is whether they used the information as elimination evidence or as a rollback queue. They rolled back despite being told the changes didn't explain the failures, which pulls the rating toward tier 2.
- For M5, the participant benefits from NPC guidance (Tanya and Shay providing the bundle diagnosis), but they do engage with the new information and adapt rather than retrying the restart, which supports a tier 3 rating.
- The timing discrepancy observation ("@shay that was only 3 minutes ago, @bob said customers had been seeing issues for 20 minutes") is a strong narrowing move for M3, but it's isolated — the participant doesn't build on it or use it to definitively rule out the DNS/email maintenance hypothesis immediately.

---