# Post-Drill Developmental Report

This drill placed you in a live incident with compounding complexity: misleading signals, unavailable team members, layered system dependencies, and a volume of information that required active filtering. The facets below capture how you navigated each of those pressures and where your next growth edges sit.

---

## F1 — Misleading correlations

**Operating at: Practicing**

You pursued the email maintenance and recent deploy hypotheses with energy, rolling back multiple changes before shifting your attention elsewhere. The pivot away from those threads came after concrete experiment failures — the rollbacks didn't resolve the issue — rather than from reasoning about whether a plausible mechanism connected those changes to the symptom. Disconfirming information from teammates (explicit statements that email wouldn't affect checkout) was available well before you moved on.

*Growth edge:* When a correlation looks compelling, practise asking "what mechanism would connect this cause to this symptom?" before committing to a remediation action. If you can't articulate the mechanism, treat the correlation as unconfirmed and keep other threads alive.

---

## F2 — Hidden coupling

**Operating at: Practicing**

When the first service restart didn't resolve the problem, your instinct was to restart additional services rather than reframe the failure as structurally different from what you'd assumed. The cert-bundle dependency — the idea that a single restart wouldn't suffice because two certificates were needed — was surfaced by a teammate rather than through your own investigation of why the post-restart behaviour differed from the pre-restart behaviour.

*Growth edge:* After a remediation attempt fails, pause and ask "is the error I'm seeing now the *same* error or a *different* one?" That reframing question is often the fastest route to uncovering hidden coupling between components.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You named the access constraints early — noting that key approvers were offline — and accepted auto-replies as terminating rather than spinning on unavailable people indefinitely. You escalated to an alternative authority for restart approval and eventually made the cost trade-off to pull a teammate off a vendor call. Your delegation throughout the drill was directed at named individuals with specific tasks, which helped keep work moving despite reduced availability.

*Growth edge:* When pulling someone into the response who has competing obligations, batch your questions before interrupting them. Repeated single-question pings to a constrained teammate can erode cooperation and slow the overall response.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain in a visible, logical order — attempting standard approvers, recognising they were unavailable, then escalating to a senior leader for authorisation. You delegated parallel tasks to available teammates and used the approval you obtained to unblock the restart without re-litigating it later. The sequencing was sound.

*Growth edge:* Try naming the dependency structure aloud as a single statement early in the incident ("we need restart approval; Hamed and Tinus are out; I'm going to Bez now"). Making the constraint explicit — rather than discovering it step by step — lets you pre-position decisions alongside investigation work rather than sequencing them reactively.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You were captured by the loudest signal — the email maintenance window — for an extended stretch, and you repeated requests for email-related information even after teammates explicitly confirmed it was unrelated to checkout. Once the cert thread was surfaced by others, you engaged with it effectively, but the filtering work was largely NPC-driven rather than self-initiated.

*Growth edge:* When a teammate gives you a clear "that's unrelated" statement, treat it as a data point that closes a thread rather than one that needs re-verification. Keeping a short written list of ruled-out causes can help you avoid revisiting closed threads under pressure.

---

## Looking Ahead

Two patterns stand out as high-leverage for your next rep. First, building the habit of articulating a mechanism before acting on a correlation — even a single sentence ("I think X caused Y because Z") — will sharpen your filtering and reduce time spent on dead-end rollbacks. Second, when a remediation fails, treating the post-failure state as new diagnostic information (rather than a prompt to repeat the same class of action) will help you surface hidden coupling faster. Your ownership instincts and escalation sequencing are solid foundations to build on.---

# Facets Analysis — 8936

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." [Shay's repeated nudge, which the participant pursued] ... "lets roll back CHG90433 as well please" ... "handshake error suggests a cert issue. have we reviewed all certs to ensure nothing is expired"

**Rationale:**
The participant pursued the email maintenance and recent deploy hypotheses extensively, rolling back CHG90439, CHG90440, and CHG90433 before pivoting. The pivot came only after concrete experiment failures (rollbacks didn't help) rather than from upstream mechanism reasoning. The participant did eventually move to cert investigation after multiple failed rollbacks, but never articulated "correlation needs a mechanism" reasoning. Pivot latency was well beyond 5 exchanges from disconfirming evidence (Tanya's explicit "email won't affect checkout" statements were repeated multiple times before the participant moved on). This fits tier 2: reactive pivot after failed experiments.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "can we restart the other services in the chain please?" ... "restart please? if we are hard down, it could help" ... "lets restart all of these in turn"

**Rationale:**
After the first restart failed to fix the problem, the participant's response was to restart additional services rather than reframe the failure as structurally different. The participant did not independently surface the "what changed beyond 24 hours" question — the cert rotation was surfaced by NPCs (Daniel/Tanya). After the restart failed, the participant spent multiple exchanges requesting restarts of other services before Shay identified the bundle issue ("two certificates needed — it's a bundle, not just a single cert"). The participant did not articulate that the post-restart error was different from the pre-restart error. This matches tier 2: pivots only after concrete failure of a "more of the same" reflex, with NPC redirection needed.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "struggling to escalate as @hamed and @tinus are both offline" ... "please pause given we have other members out / unavailable" ... "we have approval from Bez" ... "i will own the response"

**Rationale:**
The participant named the access constraints ("struggling to escalate as @hamed and @tinus are both offline"), accepted auto-replies as terminating after the second cycle (though did re-ping Hamed once), and eventually made the cost trade-off to pull Tanya off the vendor call. The participant escalated to Bez for restart approval when the standard approvers were unavailable. However, the participant repeatedly asked Tanya for information while she was on the vendor call without batching questions efficiently, and the interaction with Tanya was somewhat adversarial ("can you list the changes so far? please cooperate" / "CAN YOU LIST THE CHANGES YOU MADE SO FAR?"). This shows awareness of constraints but imperfect economising, fitting tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "struggling to escalate as @hamed and @tinus are both offline" ... "we have approval from Bez" ... "engineers are refusing to restart the service with out tinus or hamed approval"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), then escalated to Bez for approval and issued the restart authorisation. This matches tier 3 path (b) — walking the escalation chain to exhaustion and then taking ownership. The participant also delegated parallel work to available NPCs (Daniel on rollbacks, Tanya on cert checks, Shay on log review). However, the participant did not name the dependency structure aloud as a single enumerated constraint statement, and the second restart (after bundle fix) proceeded without re-litigating approval, which is a positive signal. The sequencing was somewhat reactive rather than proactive — the participant didn't pre-position the approval decision alongside the cert investigation.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "can we review the failures around email service?" [asked after Daniel already identified PaymentService as the failing component] ... "list all changes made re: email so far" [repeated 3 times after Tanya confirmed email is unrelated]

**Rationale:**
The participant was captured by the loudest signal (email maintenance) for an extended period and repeatedly asked Tanya to list email changes even after she explicitly stated email was unrelated to checkout. The participant did eventually ask for PaymentService-specific logs and identified the cert issue from the handshake errors, but this was largely NPC-driven. The participant did not independently catch the reload-vs-restart distinction from the runbook, and the bundle issue was surfaced entirely by Shay. The repeated requests for already-answered information ("list all changes made re: email so far" asked three times) and pursuing EmailService after it was disconfirmed indicate difficulty filtering signal from noise. This fits tier 2: accepts NPC summaries, engages with key concepts once surfaced by others, but doesn't drive the filter.

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
- F1 rating is a borderline 1/2 call. The participant did eventually pivot away from the email/deploy hypotheses, but only after multiple failed rollbacks and repeated NPC disconfirmation. The pivot was clearly reactive rather than mechanism-driven, but it did occur, placing this in tier 2 territory.
- F3 rating could be argued as a 2/3 boundary. The participant named constraints but the repeated adversarial interactions with Tanya and failure to batch questions efficiently pull toward 2. Rated 3 because the participant did ultimately make the cost trade-off explicitly and accepted auto-replies as terminating.
- F5 rating is solidly tier 2 — the repeated requests for email-related information after explicit disconfirmation is a notable signal of difficulty filtering, but the participant did eventually engage with the cert thread once NPCs surfaced it.

------

# Markers Analysis — 8936

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "I am incident manager" ... "i will own the response"

**Rationale:**
The participant explicitly declares themselves as incident manager early on and later restates ownership ("i will own the response") when Bez challenges accountability. They direct the team throughout, make the restart override call using Bez's backing, and drive the response. However, they don't explicitly name personal consequences or accept blowback risk in the way a tier-4 participant would — they rely on Bez's approval rather than self-authorizing.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "looking into it Bob. can you give me more info on the nature of the complaints?" ... "what are customers reporting exactly?" ... "How many customers are blocked from checkout? What's the revenue loss per minute right now?"

**Rationale:**
The participant's first actions are clarifying questions to Bob about the nature of complaints, scope, and impact before declaring the incident or taking remediation steps. They also reproduce the issue themselves. This aligns with tier-3 behavior — scope-validating questions before acting. They don't quite reach tier-4 as they don't deeply probe patterns across reports before forming hypotheses.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "can all engineers please confirm the nature of their changes in last 12 hours?" ... "lets roll back CHG90433 as well please"

**Rationale:**
The participant asks for the change log and reviews recent changes, which is positive. However, they then proceed to roll back CHG90439 and CHG90433 without articulating a mechanism connecting those changes to the symptom — even after Shay noted "none of these changes look like they'd break checkout end-to-end like this." They asked the question but used the change log as a rollback queue rather than an elimination pass, fitting tier 2.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@hamed @tanya please review the logs and let me know what you see also" ... "@daniel lets look at rolling back CHG90439" ... "@tanya please review server side certs" ... "@shay please review the payment services logs"

**Rationale:**
The participant consistently uses @mentions to assign specific tasks to specific people. They route cert/platform checks to Tanya and app-side work to Daniel and Shay. Some early delegation is slightly misrouted (asking Hamed who is OOO), but overall they demonstrate clear named delegation throughout the drill. The routing generally reflects understanding of access boundaries.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@hamed @tanya please review the logs and let me know what you see also" ... "can all engineers please confirm the nature of their changes in last 12 hours?"

**Rationale:**
The participant mostly works sequentially — rolling back one change, waiting for results, then rolling back another. While they occasionally ask multiple people for input, the investigation threads are largely serial rather than parallel. They don't fan out multiple distinct investigation tasks simultaneously in the way tier-3+ participants do. The approach is predominantly one-thread-at-a-time.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@bez could you try and reach @hamed? we need him to confirm if he pushed an s3 bucket change" ... "engineers are refusing to restart the service with out tinus or hamed approval" ... "we have approval from Bez"

**Rationale:**
When both Hamed and Tinus are unavailable and the restart is blocked, the participant escalates to Bez and uses Bez's backing to authorize the restart. They don't leave the chain hanging — they find an alternative path. However, they don't explicitly name the cost of the escalation or self-authorize with personal accountability, which would push to tier 4. The escalation is concrete and effective.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "hold, I get an out of office from @hamed, yet he pushed a change at 10:48? can we drill into this?" ... "can we please get ready to roll back this change. I am seeing errors in the logs re: payment service"

**Rationale:**
The participant pursues leads (Hamed's S3 change, checkout service rollbacks) but rarely articulates explicit hypotheses before acting. They don't state "my hypothesis is X, let's test it by doing Y." The rollbacks are executed without a stated mechanism connecting the change to the symptom. They eventually reach the cert hypothesis through evidence accumulation rather than explicit hypothesis-test cycles. This is inconsistent/implicit hypothesis work — tier 2.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "handshake error suggests a cert issue. have we reviewed all certs to ensure nothing is expired" ... "the cert has expired on the payment service"

**Rationale:**
The participant does use evidence to narrow scope at key moments — noting the handshake errors suggest a cert issue, recognizing that PaymentService outbound connections are failing, and connecting the TLS errors to an expired certificate. They also note "looks like almost full, but not quite" early on. However, they spend significant time on false leads (S3 change, multiple rollbacks) before narrowing effectively. The eventual narrowing to certs via log evidence earns tier 3.

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "lets roll back CHG90433 as well please" ... "now please" [restart order] ... "can we restart the other services in the chain please?"

**Rationale:**
The participant consistently fires rollbacks and restarts without weighing potential consequences. They don't ask "is it safe?" before rollbacks, don't consider what might happen if the restart doesn't work, and order restarts of other services without articulating why it might help or what could go wrong. When pulling Tanya off the vendor call, they don't acknowledge the 2-week cost until Tanya forces the confirmation. No evidence of consequence-weighing behavior.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "handshake error suggests a cert issue. have we reviewed all certs to ensure nothing is expired" ... "can we apply the second cert please"

**Rationale:**
After the rollbacks of CHG90439 and CHG90440 fail, the participant does eventually pivot away from the rollback approach and toward investigating PaymentService specifically. After the first restart fails, they don't simply retry the same action — they ask for logs and when told "two certificates needed — it's a bundle," they immediately pivot to applying the second cert. The adaptation after the first restart failure is appropriate, though the initial rollback phase shows some repetition before pivoting.

---

## M5 — Adapts approach when initial path isn't working

*Already scored above.*

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "@bez we are reviewing recent changes. From Bob, this is the current impact: We're losing around £1,000 to £1,500 every minute this keeps up." ... "rollback completed. issue persists. update in 3-5 mins" ... "issue appears to be down to an expired ssl certificate on payment service. this is being worked on"

**Rationale:**
The participant provides some updates to Bez/business-comms, including revenue impact and committed update times. However, most updates are brief and lack business framing — "rollback completed. issue persists" and "restart done. issue persists" are status updates without scope, theory, or ETA. The cert identification update is substantive but comes late. Updates don't consistently include what's being done, when the next update is expected, or business-frame the impact. This is inconsistent — tier 2.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "the cert has expired on the payment service" ... "further cert issue identified, being remedied now"

**Rationale:**
The participant rarely posts synthesis statements to the technical team. They ask questions and give orders but don't summarize the state of the investigation ("we've ruled out deploys, focus is now on PaymentService outbound"). The team members (Shay, Daniel) often provide synthesis that the participant doesn't. The participant's technical communications are mostly directives rather than scope-framing statements. Limited evidence of keeping the team oriented on what's been ruled in/out.

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
| M3 — Uses evidence to narrow the scope | 3 |
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.42** |

---

## Caveats
- L3 is a borderline 3/4 call. The participant does declare ownership explicitly ("i will own the response") but relies on Bez's authority for the restart rather than self-authorizing with personal accountability. Rated 3.
- M5 is a borderline 2/3 call. The participant does eventually pivot from rollbacks to cert investigation, and adapts after the first restart failure, but the initial rollback phase shows some repetitive behavior (rolling back multiple changes sequentially without mechanism). Rated 3 because the post-restart pivot is clean.
- K2 could be argued as borderline 2/3 — the participant does commit update times and provides some impact data, but the majority of updates lack the substance expected at tier 3 (working theory, business-framed impact, consistent cadence through the secondary failure).

---