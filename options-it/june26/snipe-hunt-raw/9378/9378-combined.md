# Snipe Hunt — Post-Drill Developmental Report

This drill puts you in the middle of a live outage where multiple signals compete for attention, familiar fixes don't resolve the problem, and the people who normally approve high-risk actions aren't available. It's designed to stress your ability to reason through misleading data, navigate coordination constraints, and adapt when your initial read doesn't hold up.

---

## F1 — Misleading correlations

**Operating at: Not yet evident**

Early in the drill, you latched onto the email-maintenance timing correlation and held onto it even after a team member explicitly stated that email confirmations were working and that the email system was separate from the payment path. You ordered a DNS revert on that basis despite the disconfirmation. The growth edge here is building a habit of pausing when someone with system knowledge names a mechanism break — treating that as a signal to release the hypothesis rather than push through it. On your next rep, practice naming the correlation aloud ("I notice X happened right before Y") and then asking "what's the mechanism?" before acting on it.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You did eventually engage with the certificate thread — asking whether the SSL cert had expired and following up when the restart didn't resolve the issue. That pivot showed willingness to move into unfamiliar territory. However, the investigation into the cert was surfaced by teammates rather than by your own questioning, and when the restart produced a different error, you didn't reframe the problem as structurally new (e.g., a chain or bundle issue versus a simple expiry). The next-rep growth edge is noticing when a fix changes the error signature and treating that as a new diagnostic moment rather than continuing with the same mental model.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You handled the access constraints well. When your first escalation attempt returned an auto-reply, you moved to the next person, accepted that result, tried a third path, and ultimately took personal accountability for the restart decision. You also pulled a team member off a vendor call to redirect their effort. The growth edge is making those constraints visible to the rest of the team — stating aloud that approvers are unavailable and naming the trade-off you're making ("I'm pulling Tanya off the vendor call because the global outage outweighs the vendor window"). That explicit framing helps the team understand your reasoning and builds shared situational awareness.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain to exhaustion in a clear sequence and then issued the authorisation yourself as a distinct decision. You also delegated parallel work — routing platform checks to one person and service investigation to another. The growth edge is compressing the time between recognising the bottleneck and acting on it. You spent extended back-and-forth trying to find someone else to approve before taking ownership. On the next rep, practice setting yourself a mental timer: if the chain doesn't yield an approver within a short window, name the constraint and act.

---

## F5 — Data overload / buried information

**Operating at: Not yet evident**

The loudest signal in the logs — EmailService errors — captured your attention and became your declared root cause, even as teammates surfaced payment-specific evidence (TLS handshake failures) that pointed elsewhere. You didn't independently filter or interrogate the competing signals, and when a teammate offered both a reload and a restart option, you chose without engaging the distinction between them. The growth edge is building a triage step before declaring cause: when logs show multiple error types, ask "which of these is on the critical path to the symptom?" and use that to rank signals rather than defaulting to the loudest one.

---

## Looking Ahead

Two patterns stand out as high-leverage for your next rep. First, practice releasing a hypothesis when someone with direct system knowledge names a mechanism break — that single habit would have changed the trajectory of this drill significantly. Second, when a fix changes the error rather than resolving it, treat that as a fresh diagnostic moment: name the new error, ask what's different, and resist continuing with the prior frame. Your escalation and coordination instincts are solid foundations to build on.# Facets Analysis — 9378

## F1 — Misleading correlations

**Rating:** 1

**Evidence:**
> "ok, this does look like it's realted to @tanya ongoing maintenance per the logs @shay has provided. @daniel or @shay, can you revert CHG90431?"
> ...
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." → "@tanya - what was the exact DNS change and can you revert it?"

**Rationale:**
The participant repeatedly committed to the email/DNS correlation as causal even after multiple NPCs explicitly disconfirmed the mechanism. After Tanya stated "Email provider is up, and email confirmations are working. This isn't connected to the checkout issue," the participant continued insisting the email logs showed the cause. Later, after Shay re-pitched the DNS timing correlation, the participant ordered a revert of email DNS changes despite Tanya explicitly stating "it won't affect the payments issue since they're separate systems." This is tier-1 behaviour: ordering rollbacks in the face of explicit NPC mechanism-disconfirmation and staying locked into the prime.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "has the SSL certificate expired? @tanya"
> ...
> "even after a restart @tanya?" ... "can you delete the old certifcate?"

**Rationale:**
The participant eventually engaged with the cert thread but only after NPCs (Shay, Daniel) surfaced the cert rotation and TLS handshake failure. The participant asked about cert expiry but did not independently surface the "what changed beyond 24 hours" question — that came from NPC investigation. After the restart failed to fix the issue, the participant did not reframe the error as structurally different (bundle/chain issue); instead they tried removing the old cert file from disk, treating it as a continuation of the same problem rather than recognising a new failure mode. The pivot to cert work was NPC-driven, and post-restart reframing did not occur, placing this at tier 2.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@hamed or @tinus - we are hard down here..." → receives auto-reply → "@tinus - we are hard down here..." → receives auto-reply → "ok. with both tinus and hamed out I will seek approval from @bez"
> ...
> "i will take the accountability, do the restart"

**Rationale:**
The participant walked the escalation chain methodically (Hamed → auto-reply, Tinus → auto-reply, then Bez, then Tanya), accepted auto-replies as terminating, and eventually took personal accountability for the restart. They also pulled Tanya off the vendor call with a clear directive. However, the participant did not explicitly articulate the access constraints as a pattern to the team or in business-comms, and the decision to pull Tanya off the vendor call lacked a stated cost trade-off ("global outage outweighs vendor window"). This meets tier 3 — names constraints implicitly through actions, accepts auto-replies, escalates appropriately — but lacks the explicit verbalisation of tier 4.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@hamed or @tinus - we are hard down here..." → auto-reply → "@tinus..." → auto-reply → "ok. with both tinus and hamed out I will seek approval from @bez" → "with @tanya the only platform team member available, we will have to revert to her" → "i will take the accountability, do the restart"

**Rationale:**
The participant walked the escalation chain to exhaustion in observable order — pinging Hamed (auto-reply), Tinus (auto-reply), Bez (told Bez can't approve), Tanya (told she can't approve without sign-off), then explicitly took ownership. This matches tier-3 path (b): walks the escalation chain to exhaustion and then issues the authorisation as a distinct message. The participant also delegated parallel work (Daniel on frontend, Shay on PaymentService). However, they did not name the dependency structure aloud as a constraint statement, and the override came only after extended back-and-forth rather than within a short window of chain exhaustion, preventing a tier-4 rating.

---

## F5 — Data overload / buried information

**Rating:** 1

**Evidence:**
> "well we can see from these logs that the EmailService is failing. @tanya can you check the emailservice?"
> ...
> "the reason the checkout failures are happening is because our email provider is unavailable. according to logs provided by @shay"

**Rationale:**
The participant was captured by the loudest signal — EmailService errors in the logs — and declared them the root cause despite Tanya explicitly stating email was unrelated. When Shay provided payment logs showing TLS handshake failures, the participant did not independently filter or interrogate the signal; NPCs drove the investigation to the cert issue. The participant did not read the rotation runbook to catch the reload-vs-restart distinction (Tanya offered both options and the participant chose without engaging the distinction). After the restart failed, the participant did not reason about the new error's structure or investigate the bundle. This is tier-1 behaviour: captured by noise, failing to integrate information NPCs surfaced.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 1 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 1 |
| **Mean Facet Score** | **2.00** |

---

## Caveats
- F1 rating is a clear tier 1: the participant ordered the email DNS revert *after* Tanya explicitly stated it wouldn't help, and said "please do it anyway" — this is commitment to the prime in the face of named disconfirmation.
- F2 could be argued as borderline 1/2. The participant did engage with the cert thread (asked "has the SSL certificate expired?") but only after NPCs surfaced it. Post-restart, they did not reframe the new error. I rated 2 because they did pivot away from the deploy/email hypotheses to cert work, even if NPC-driven.
- F3 and F4 both benefit from the escalation-chain walk, which was well-executed. The boundary between 3 and 4 on both facets turns on explicit verbalisation of constraints, which was largely absent.
- The drill ended before the bundle-ordering issue could be fully explored, limiting F2 and F5 evidence on the deepening layers.

------

# Markers Analysis — 9378

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "i will take the accountability, do the restart"

**Rationale:**
The participant eventually takes explicit ownership of the restart decision when both approvers are unavailable, accepting personal accountability. However, this came only after extended back-and-forth with Tanya and multiple attempts to find someone else to approve. They did drive the response throughout but the ownership moment was late and forced rather than proactive.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "How many customers are blocked from checkout right now? What's the revenue loss per minute?" ... "what complaints are you getting @bob ?"

**Rationale:**
The participant's first messages after Bob's alert are clarifying questions about scope, volume, and nature of complaints. They ask about revenue impact and the type of complaints before taking action. This demonstrates scope-validation before acting, meeting the novice expectation.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@daniel - can see you pushed this to prod earlier: CHG90433... it looks like it was a change to the checkout service where users are having issues. Can this be reverted?"

**Rationale:**
The participant identified a recent change and immediately ordered a rollback without articulating a mechanism connecting it to the symptom. They asked about changes but used the change log as a rollback queue rather than a candidate-elimination pass. They also later attempted to revert CHG90431 based on log correlation without mechanism reasoning. This is the classic tier-2 pattern: asked the question but didn't use the answer analytically.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya - can you please approve?" ... "@shay can you review the PaymentService please?" ... "@daniel & @shay can one of you check when the maintenance ended?"

**Rationale:**
The participant consistently uses @mentions to assign tasks to specific people. They route platform checks to Tanya, log investigation to Daniel, and service checks to Shay. While not always perfectly matched to access boundaries (e.g., asking Shay to check PaymentService when Daniel had the logs), they generally name specific people for specific tasks.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@daniel & @shay can one of you check when the maintenance ended?" ... "ok thanks @tanya - @shay can you review the PaymentService please?"

**Rationale:**
The participant mostly works sequentially — pursuing one thread at a time (rollback CHG90433, then CHG90431, then email maintenance, then PaymentService). There is limited evidence of multiple concurrent investigation threads. Tasks are assigned one at a time with waiting for results before moving to the next action.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@hamed or @tinus - we are hard down here and seeking the fastest route to get us back online. Could you please approve the restart to load a new cert?" ... "ok. with both tinus and hamed out I will seek approval from @bez"

**Rationale:**
When the restart was blocked, the participant escalated to Hamed, then Tinus, then attempted Bez, then tried Tanya. They worked the chain and didn't give up after the first auto-reply. The escalation messages include context (hard down, seeking fastest route). However, they spent considerable time trying alternatives before ultimately taking ownership themselves, showing some hesitation.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "ok, this does look like it's realted to @tanya ongoing maintenance per the logs @shay has provided. @daniel or @shay, can you revert CHG90431?"

**Rationale:**
The participant forms implicit hypotheses (checkout change caused it, email maintenance caused it) but doesn't articulate them explicitly as hypotheses to test. They act on correlations without naming the mechanism. When the email maintenance hypothesis was disconfirmed by Tanya multiple times, the participant persisted ("I keep coming back to the email maintenance"). They eventually followed the cert thread but didn't explicitly frame hypothesis-test cycles.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "the CheckoutService can't reach the PaymentService. @tanya can you check that?"

**Rationale:**
The participant does some narrowing — moving from checkout broadly to PaymentService specifically after logs were provided. However, they don't synthesize evidence into elimination statements. After Tanya repeatedly confirmed email maintenance was unrelated, the participant still pursued that thread ("I keep coming back to the email maintenance"). They didn't use disconfirmations effectively to narrow scope.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "what would happen with a full restart? what could users not access?"

**Rationale:**
The participant asks about consequences of the restart before proceeding, which shows some consideration. However, they ordered the CHG90433 rollback without weighing consequences, and when they finally got to the restart, they didn't consider what could go wrong (e.g., the bundle issue). The single "what would happen" question is a partial engagement with this marker.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing."

**Rationale:**
The participant shows difficulty adapting. After the CHG90433 rollback failed, they moved to CHG90431 (another rollback). After Tanya repeatedly said email wasn't related, the participant still pursued email DNS changes. They eventually followed the cert thread but returned to the email hypothesis even after it was disconfirmed. After the restart didn't fully resolve the issue, they asked to clear Redis cache and delete old certs — somewhat scattershot rather than adapting based on the new error pattern.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "confirmed the roll back does not work. we are now investigating an SSL certificate issue. We are confirming if the certificate has expired or not. Updates to follow."

**Rationale:**
The participant provides some updates to the business channel but they are mostly technical and lack business framing. Early updates ("we are investigating") are vague. The later update about the SSL certificate is more substantive but doesn't quantify business impact, provide an ETA, or commit to a next-update time. No proactive cadence of updates is maintained.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "the reason the checkout failures are happening is because our email provider is unavailable. according to logs provided by @shay"

**Rationale:**
The participant makes some scope statements to the technical team but they are often incorrect (claiming email provider is the cause when it wasn't). They don't provide clear synthesis statements that name what's been ruled in and out. The team receives directives but not a coherent picture of the investigation state. The participant rarely summarizes findings for the team's benefit.

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
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.33** |

---

## Caveats
- L3 rating of 3 is a borderline call. The participant did eventually take accountability explicitly ("i will take the accountability, do the restart"), which is the key ownership moment. However, it came only after exhausting all other options and extended back-and-forth, which could argue for a 2. Rated 3 because the explicit acceptance of personal accountability is present.
- M5 is a borderline 1-2 call. The participant did eventually follow the cert thread, but the persistent return to the email hypothesis after multiple disconfirmations and the lack of adaptation after the restart produced a different error pattern argue for a low rating. Rated 2 because they did eventually move off the rollback approach.
- The drill ended with partial resolution (orders coming in at 72-78/min) but the bundle issue was never identified or resolved. Per anti-outcome-bias, this does not affect ratings.

---