# Post-Drill Developmental Report

This drill placed you in a live incident requiring you to navigate misleading signals, coordinate a distributed team under access constraints, and drive toward root cause while managing stakeholder communication. The observations below reflect how you engaged with each of these dimensions and where your next growth edges sit.

## F1 — Misleading correlations

**Operating at: Practicing**

You engaged with the initial correlations the drill surfaced — investigating the email maintenance timing and exploring whether Daniel's deploy at 08:55 UTC aligned with the complaint window. When Tanya denied the email connection, you moved on, which shows willingness to release a lead. The growth edge here is *why* you release it: your pivot came because an NPC told you the correlation didn't hold, rather than because you reasoned through the causal mechanism yourself. On your next rep, try articulating *how* a correlation would need to work before accepting or discarding it — "for email maintenance to cause checkout failures, it would need to touch X" — so your pivots are driven by your own reasoning rather than waiting for someone else to close the door.

## F2 — Hidden coupling

**Operating at: Practicing**

When the first restart failed, your initial response treated it as a timing issue rather than a signal that the problem was structurally different. The deeper coupling — a cert rotation from a week prior — was surfaced entirely by your team rather than by your own investigation. The growth edge is recognising restart failure as a *reframe trigger*: when a standard remediation doesn't work, that's the moment to widen your change window and ask "what changed beyond the last 24 hours?" Practise treating failed fixes as new data points that demand a different question, not just patience.

## F3 — Decreased access to team

**Operating at: Strengthening**

You walked the escalation chain methodically — reaching out to Hamed, then Tinus, then pulling Tanya off her vendor call with a clear rationale that this was a Sev 1. You accepted auto-replies as terminating signals and made the cost trade-off explicitly. This sequencing shows solid awareness of access constraints and appropriate escalation logic. Your next growth edge is speed of recognition: you can tighten the loop by setting a mental threshold for how many cycles you'll attempt before escalating, so the decision to pull someone off another commitment comes a beat earlier.

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the approval chain to exhaustion and then explicitly took ownership of the restart decision, stating you'd take it on your shoulders. You also delegated parallel responsibilities — Tanya on platform checks, Daniel on logs, Shay on change records — and when the second restart was needed after the bundle fix, you authorised it without re-litigating. The growth edge is making the dependency structure *visible* to the team: try naming the full constraint aloud ("we need approval, Hamed and Tinus are both unreachable, so I'm authorising") as a single enumerated statement. This helps the team understand the landscape, not just the decision.

## F5 — Data overload / buried information

**Operating at: Practicing**

You directed team members to investigate logs and asked targeted questions about whether the issue was isolated to payments. However, the critical findings — PaymentService as the anomaly, the cert expiry, the bundle ordering issue — were all surfaced by your team rather than through your own data interrogation. You asked Tanya about the playbook but didn't catch the reload-vs-restart distinction yourself. The growth edge is moving from *delegating data retrieval* to *driving data interpretation*: when logs come back, try synthesising what they show before asking the team what to do next. Ask yourself what signal is *absent* as well as what's present — that's often where buried information hides.

---

## Looking Forward

Across this drill, your coordination instincts — escalation sequencing, delegation, taking ownership when the chain is exhausted — are working well and forming a reliable foundation. The consistent growth edge is shifting from *reactive* to *generative* in your diagnostic reasoning: articulating hypotheses before testing them, treating failed remediations as reframe signals, and synthesising data yourself rather than waiting for the team to surface findings. On your next rep, try verbalising one explicit hypothesis early and naming what would confirm or disconfirm it — that single habit will pull several of these facets forward together.
# Facets Analysis — 9196

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "@shay email maintenance has no relation to this?" ... "@shay lets have a look at the change records and pinpooint when it started" ... "ok so lets focus on checkout @everyone"

**Rationale:**
The participant initially engaged with the email maintenance correlation, asking Shay to pull change records and investigating the timing. However, they did pivot away from the email lead after Tanya explicitly stated email maintenance wasn't causing checkout failures. The pivot was reactive rather than mechanism-driven — they moved on because Tanya denied the connection, not because they reasoned about the causal chain. They also spent significant time on the "recent deploys" correlation (asking Daniel about his changes, correlating 08:55 UTC with complaints at 09:00 UTC) before eventually narrowing to PaymentService through NPC-driven log investigation. Pivot latency was moderate — several exchanges after disconfirming signals.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "do we have to give this a few minutes to restart?" ... "ok @daniel , @tanya next steps? Do we see a success with the cert errors though?"

**Rationale:**
After the first restart failed, the participant did not immediately reframe the problem as structurally different. Their first response was "do we have to give this a few minutes to restart?" — treating it as a timing issue rather than recognizing a new failure mode. They then asked NPCs for next steps rather than driving the investigation themselves. The week-ago coupling (cert rotation 7 days prior) was surfaced entirely by NPCs (Shay found CHG90123, Tanya identified the expired cert). The participant never independently asked "what changed beyond the last 24 hours?" The post-restart reframe came only after NPCs (Tanya and Daniel) identified the bundle issue. Pivot latency from the restart-failing event was >5 exchanges, and the reframe was NPC-driven.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@hamed can you look into this in tanyas absence?" ... "@tinus we will need you here please, Hammad is not availble" ... "@tanya this is more important, unless @ hammad can deputize instead?"

**Rationale:**
The participant walked the escalation chain methodically — tried Hamed (got auto-reply), tried Tinus (got auto-reply), then pulled Tanya off the vendor call. They accepted auto-replies as terminating after one cycle (did not re-ping Hamed or Tinus repeatedly after the initial auto-replies, with one exception for Tinus). They made the cost trade-off when pulling Tanya: "this is more important" and later "this is a sev 1." They named the access constraint implicitly ("both I cant reach, who can approve"). However, they did re-ping Tinus once more after already receiving the auto-reply, which is a minor tier-2 signal. Overall, the pattern shows awareness of constraints and appropriate escalation sequencing.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@daniel both I cant reach, who can approve, I will happily take this on my shoulders" ... "On it.. restarting the payments service now."

**Rationale:**
The participant walked the escalation chain to exhaustion — pinged Hamed (auto-reply), pinged Tinus (auto-reply), then explicitly took ownership of the restart decision ("I will happily take this on my shoulders"). This matches tier-3 path (b): walking the escalation chain in observable order and then explicitly taking ownership. They also delegated parallel work appropriately (Tanya on platform checks, Daniel on logs, Shay on change records). For the second restart (after bundle fix), they authorized without re-litigating ("@tanya can you restart ut? or @daniel"). However, they did not name the full dependency structure aloud as a single enumerated constraint statement, and the ownership reasoning was brief rather than articulating the escalation as exhausted, which keeps this at tier 3 rather than 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@daniel and the next steps to focus on with regard to the cirtical errors, whats the runbook on that?" ... "@tanya can you be specific on what you were looking at and what part of the playbook you mean please?"

**Rationale:**
The participant asked for logs and directed team members to investigate, but largely relied on NPCs to filter and interpret the data. They did not independently filter logs to PaymentService — Shay surfaced that PaymentService was the anomaly. They asked Tanya about the playbook but did not read the referenced documentation themselves or catch the reload-vs-restart distinction. The cert expiry, the bundle issue, and the chain-verification failure were all surfaced by NPCs (Tanya, Daniel, Shay). The participant asked targeted questions ("is it failed payments alone, or anything else mentioned?") which shows some filtering intent, but they consistently delegated the actual data interrogation rather than driving it. They did not reason about absence of signal or spot buried distinctions independently.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.40** |

---

## Caveats
- F1 rating is a boundary call between 1 and 2. The participant did eventually move off the email lead, but spent considerable time on the "recent deploys" correlation (asking about 08:55 UTC timing) which is also a false lead. They pivoted reactively when NPCs narrowed to PaymentService, not from mechanism reasoning. Rated 2 because they did move on after disconfirmation rather than staying locked.
- F3 rating is a boundary call between 2 and 3. The participant re-pinged Tinus once after the auto-reply, which is a minor tier-1/2 signal, but overall the escalation pattern was clean and they made the cost trade-off verbally when pulling Tanya.
- F4: The second restart authorization without re-litigating is a positive signal that supports tier 3 but doesn't quite reach tier 4 given the absence of explicit dependency-structure enumeration.

---
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