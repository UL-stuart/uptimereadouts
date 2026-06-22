# Snipe Hunt — Post-Drill Report

This drill placed you in a live incident with layered complexity: misleading surface signals, constrained team availability, hidden system coupling, and an approval chain that required navigation under pressure. The observations below reflect how you engaged with each of these dimensions.

---

## F1 — Misleading correlations

**Operating at: Strengthening**

You engaged critically with the email maintenance correlation rather than treating it as a ready-made explanation. When the timing overlap was raised, you challenged it on mechanism — asking why a failure to send an email would produce a checkout error, and pressing for a causal hypothesis beyond coincidence. You held the correlation as a data point without ordering a rollback or pausing the maintenance based on it alone.

Your growth edge here is moving from *challenging* a misleading correlation to *explicitly naming and parking it* for the team. Stating something like "we're noting the timing overlap but not acting on it until we have a mechanism" would sharpen the signal for others and reduce the chance of the team drifting back to it.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the week-old certificate rotation was surfaced, you connected it to the current failure and moved through the investigation — from reload attempt to recognising the bundle ordering issue needed a fix. When the reload didn't resolve the handshake errors, you pivoted cleanly to rebuilding the certificate in the correct order.

The growth edge is in *surfacing* hidden coupling yourself rather than receiving it from a teammate. The "what changed beyond the last 24 hours?" question came from someone else. On your next rep, consider building that question into your early investigation routine — actively asking about changes outside the obvious window.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You accepted unavailability signals without over-pursuing them — moving past Hamed's auto-reply quickly and preserving Tanya's vendor-call time until it became clear she was the only path to platform-level investigation. When you did pull her in, you sent targeted questions rather than open-ended requests. You also explicitly named the constraint when taking ownership of the restart decision.

For your next rep, consider economising even further on constrained team members. You asked Tanya several questions while she was still on the vendor call before making the pull decision. Batching those into a single, scoped ask — or deciding earlier whether to pull her — would reduce the drag on both her and the investigation timeline.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the approval chain methodically — Hamed, then Tinus, then Bez — and when each path terminated, you moved to the next without stalling. When the chain was exhausted, you explicitly took ownership and authorised the restart yourself, naming the accountability clearly. You also delegated parallel work appropriately, routing platform tasks to Tanya and application-layer tasks to Daniel.

The growth edge is anticipating the dependency structure earlier. Rather than discovering each blocker sequentially, consider mapping the approval and access dependencies at the start of an incident — who can approve what, who has platform access — so you can sequence requests to arrive in parallel rather than in series.

---

## F5 — Data overload / buried information

**Operating at: Strengthening**

You filtered effectively past the loudest signal (EmailService errors) to focus on PaymentService connection failures, asking targeted questions about what the service was connecting to and what the handshake error indicated. You engaged with the certificate chain details and caught the bundle ordering discrepancy by referencing the runbook path.

Your growth edge is in proactively driving the "what's buried?" question rather than following the thread once surfaced. You narrowed well once pointed in the right direction, but the initial pivot toward the cert rotation came from a teammate. On your next rep, consider explicitly asking "what are we not seeing?" or scanning for signals outside the immediate noise earlier in the investigation.

---

## Communication as a growth area

Across the drill, your investigation and decision-making were systematic, but your communication to both business stakeholders and the technical team lagged behind your thinking. Business updates were initially generic rather than quantified, and you didn't consolidate findings into synthesis statements for the technical channel. Your teammates ended up providing their own summaries of the investigation state. On your next rep, consider posting brief "here's where we are" messages — both to business stakeholders (with impact and ETA) and to the technical team (with what's been ruled out and what's being pursued). This keeps everyone aligned without requiring them to reconstruct your reasoning from your questions.

---

## Looking forward

You demonstrated consistent mechanism-based reasoning and a willingness to hold uncertainty rather than act prematurely on convenient explanations. The patterns that will serve you well on the next drill are your targeted questioning and your clean pivots when a path doesn't work. The areas to stretch into are earlier self-initiated surfacing of hidden factors, parallel sequencing of dependencies, and real-time synthesis communication that keeps the team and stakeholders inside your decision loop.---

# Facets Analysis — 9063

## F1 — Misleading correlations

**Rating:** 3

**Evidence:**
> "do you have a hypothesis on why the email change would be responsible, shay?" "other than timing"

**Rationale:**
The participant initially engaged with the email maintenance correlation but critically challenged it by asking Shay for a causal mechanism beyond timing. They also asked "why would failing to send an email throw an error on the system?" — showing mechanism reasoning before acting. They never ordered a rollback of email changes or a pause of Tanya's maintenance based solely on the correlation. While they did ask Tanya about pausing early on, they ultimately held the hypothesis without acting on it and pivoted to investigating PaymentService logs. This demonstrates systematic engagement with the correlation-vs-causation distinction, meeting tier 3.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "not sure why the process isn't picking up the new certificate" ... "let's reload first just to confirm, then we can fix the certificate if necessary"

**Rationale:**
The participant engaged with the week-old cert rotation thread once Shay surfaced it, asking Tanya for details and connecting the expired cert to the current failure. They did not independently surface the "what changed beyond 24 hours?" question — that came from Shay. After the reload failed (Daniel: "No change — same handshake errors"), the participant pivoted within ~1-2 exchanges to fixing the bundle order ("okay, @tanya go ahead and rebuild the certificate in the correct order"), showing they recognized the reload alone was insufficient. However, they didn't articulate that this was a structurally different failure — they moved forward pragmatically rather than with explicit mechanism reasoning about why reload failed. The week-ago coupling was engaged via NPC prompting, and the post-restart pivot was clean but not explicitly framed. This fits tier 3.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "Linus and Hamed are away, let's proceed anyway and I will take accountability"

**Rationale:**
The participant accepted Hamed's auto-reply and moved on after one attempt. They preserved Tanya's vendor-call constraint for a substantial period, only pulling her off when it became clear she was the only one with platform access. They named the access constraints implicitly through their actions — escalating to Tinus only when restart approval was needed, and explicitly stating the constraint when taking ownership. They sent Tanya targeted questions rather than vague requests. However, they did ask Tanya multiple questions while she was on the vendor call before making the pull decision, showing some but not maximal economising. This meets tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@tinus are you able to approve restarting the payments service to pick up a rotated certificate? the service is already unavailable" ... "Linus and Hamed are away, let's proceed anyway and I will take accountability"

**Rationale:**
The participant walked the escalation chain in observable order: attempted Hamed (auto-reply), attempted Tinus (auto-reply), asked Bez (declined), then explicitly took ownership. This matches tier 3 path (b) — walking the escalation chain to exhaustion and then issuing the authorisation as a distinct message. They also delegated parallel work appropriately (Daniel on logs, Tanya on platform investigation). They did not enumerate the full dependency structure aloud in advance or sequence the cert fix and approval decision to be ready simultaneously, which would indicate tier 4.

---

## F5 — Data overload / buried information

**Rating:** 3

**Evidence:**
> "@daniel what is the payment service trying to connect to" ... "do you have details on the certificate change Shay?"

**Rationale:**
The participant moved past the noisy EmailService errors to focus on PaymentService connection failures, asking targeted questions about what the service was connecting to. They engaged with the cert rotation information once surfaced and asked Tanya to verify the certificate chain and check the bundle. They caught the bundle ordering issue (with Tanya's help) and referenced the runbook path discrepancy ("in the doc it says /etc/paymentservice/certs/payment-gateway.crt"). They filtered signal from noise by not chasing EmailService despite it being the loudest. However, they didn't independently surface the cert rotation thread or drive the "beyond 24 hours" question — that came from Shay. They also didn't reason explicitly about absence of signal. This fits tier 3.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 3 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 3 |
| **Mean Facet Score** | **3.00** |

---

## Caveats
- F1: The participant's early questions to Tanya about pausing could be read as pursuing the email lead, but they never ordered a rollback and explicitly challenged the mechanism, which distinguishes this from tier 2 behaviour.
- F2: The "what changed beyond 24 hours?" question was NPC-initiated (Shay), which is the key differentiator between tier 3 and tier 4 on this facet. The post-reload pivot was clean but lacked explicit mechanism articulation.
- F4: The participant asked Bez to approve or ask "Linux" (Tinus), showing slight confusion about the approval structure, but ultimately walked the chain correctly and took ownership cleanly.

------

# Markers Analysis — 9063

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "Linus and Hamed are away, let's proceed anyway and I will take accountability"

**Rationale:**
The participant explicitly takes ownership of the restart decision when both approvers are unavailable, stating they will take accountability. Throughout the drill they direct the investigation and make decisions, though the ownership moment comes relatively late and only after exhausting the approval chain. They use "let's" framing and direct team members, but the explicit ownership statement is a single moment rather than a sustained posture from the start.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "can you give us more detail Bob?" ... "what are people reporting?"

**Rationale:**
The participant's first two messages after Bob's alert are clarifying questions — asking for more detail and what people are reporting. They gather scope information (regions, error pattern, timing) before declaring severity or taking action. This is solid scope-validation before acting, meeting the novice expectation of asking questions before jumping to remediation.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "have we made any other changes recently?" ... "do you have a list of recent changes?"

**Rationale:**
The participant asks about recent changes and reviews the change log. When Shay provides the list and notes "none of these changes look like they'd break checkout end-to-end like this," the participant doesn't rush to roll back any of them. They ask Shay to walk through the checkout service change specifically, and later ask Shay for a hypothesis on the email change beyond timing. They use the change log as information rather than a rollback queue, meeting tier 3.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@daniel are you available?" ... "@tanya can you check on the connection logs and see if there's issue connection from the payment service" ... "@bob can you remove the banner please"

**Rationale:**
The participant delegates specific tasks to specific named people throughout — Daniel for logs, Tanya for platform/connection investigation, Bob for the banner. They route platform-level tasks to Tanya and app-side tasks to Daniel appropriately. However, early in the drill they ping Hamed (who is unavailable) and take some time to identify who can help, showing slight inefficiency in routing.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "yes please" [to Daniel pulling logs] ... "@tanya were any DNS changes made as part of that change?"

**Rationale:**
The participant works mostly sequentially through the investigation. They ask Daniel to pull logs, then separately ask Tanya questions, but these aren't clearly parallel threads running simultaneously. There's no moment where multiple distinct tasks are fanned out to different people in close succession. The investigation proceeds one question at a time, waiting for responses before moving to the next thread.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "sounds like no, okay @tanya can you pause the email rollout and help investigate?" ... "@tinus are you able to approve restarting the payments service to pick up a rotated certificate? the service is already unavailable"

**Rationale:**
The participant escalates Tanya off the vendor call when investigation is blocked at the platform layer, and works the approval chain (Hamed → Tinus → Bez → self-authorization) when the restart is needed. They accept auto-replies as terminating and move forward. However, they don't explicitly name the cost of pulling Tanya off the vendor call, and the escalation to Bez is somewhat confused ("would you be able to ask Linux or approve yourself"). Meets tier 3 but not tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 3

**Evidence:**
> "why would failing to send an email throw an error on the system?" ... "do you have a hypothesis on why the email change would be responsible, shay? other than timing"

**Rationale:**
The participant challenges the email maintenance hypothesis by asking about mechanism — "why would failing to send an email throw an error on the system?" and later asks Shay for a hypothesis beyond timing. This is testing on mechanism rather than just action. They don't explicitly name their own hypothesis in a "Current hypothesis is X" format, but they implicitly test and discard the email maintenance lead through mechanism questioning before pivoting to the connection-layer investigation.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "I would like to establish what's happening before taking action Shay" ... "@daniel what is the payment service trying to connect to?"

**Rationale:**
The participant uses evidence to narrow scope progressively: from broad checkout failure → to PaymentService outbound connection failure → to TLS handshake → to expired cert → to misordered bundle. They resist Shay's repeated suggestions to act on the email maintenance correlation without mechanism. They ask targeted questions that narrow the scope (what is it connecting to, what's the handshake error). They meet tier 3 by using evidence to rule things out rather than fishing broadly.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "can anyone else investigate connection layer problems? I'm conscious that abandoning the email rollout might make the situation worse" ... "let's reload first just to confirm, then we can fix the certificate if necessary"

**Rationale:**
The participant shows some consequence awareness — they hesitate to pull Tanya off the vendor call ("might make the situation worse") and choose to reload before fixing the bundle order as a less invasive first step. However, they don't explicitly ask "is it safe?" before the reload, and when Tanya warns about restart disruption, the participant dismisses it ("we're already down") rather than weighing it. The consequence consideration is present but inconsistent.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "okay, @tanya go ahead and rebuild the certificate in the correct order"

**Rationale:**
After the reload doesn't fix the issue (Daniel reports "No change — same handshake errors"), the participant immediately pivots to fixing the bundle order rather than retrying the reload or reverting to other hypotheses. Earlier, they also pivot away from the email maintenance hypothesis when mechanism doesn't support it, and move to the connection-layer investigation. They adapt when paths don't work, meeting tier 3. However, they don't explicitly name the structural difference in the failure after reload (they had already identified the bundle order issue beforehand via Tanya's investigation).

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "we're seeing an issue with checkout on the platform, all users appear to be impacted - we are investigating and will update in 10 minutes" ... "we're unsure of the root cause - still investigating, we are unable to take orders at the moment so revenue will be down"

**Rationale:**
The participant's early business updates are generic — "investigating," "will update in 10 minutes" — without quantifying impact or providing a working theory. Bez repeatedly asks for numbers and ETAs that the participant doesn't provide. The later update ("root cause on a TLS certificate issue, attempting to fix now, ETA 5 minutes") is more substantive but comes very late in the drill. The participant doesn't proactively provide revenue impact numbers despite Bez asking multiple times.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "I would like to establish what's happening before taking action Shay"

**Rationale:**
The participant asks good questions of the technical team but rarely posts synthesis statements that summarize the current state of knowledge for the team. They don't explicitly say things like "we've ruled out deploys, focus is now on PaymentService outbound connections." The team members (Daniel, Shay) end up providing their own synthesis ("Logs checked. PaymentService fails all outbound gateway handshakes. Checkout is healthy, just getting errors.") rather than the participant framing the picture. The one statement about establishing what's happening is a process comment, not a scope synthesis.

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
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.67** |

---

## Caveats
- **M2 rating boundary call:** The participant's mechanism questioning ("why would failing to send an email throw an error?") is implicit hypothesis testing rather than explicit "my hypothesis is X." Rated at 3 because the mechanism question effectively tests and disposes of the email prime, which is the core tier-3 behavior.
- **K4 rating:** The participant's lack of synthesis statements is an absence-based rating. They ask good questions but don't consolidate findings for the team. This is rated on what they didn't do (no "here's where we are" messages to the technical channel).
- **M5:** The participant had already identified the bundle order issue before the reload failed, so the "pivot" after reload failure was pre-planned rather than a reactive adaptation. Still rated 3 because the overall pattern shows adaptation (away from email maintenance, toward certs, toward bundle fix).

---