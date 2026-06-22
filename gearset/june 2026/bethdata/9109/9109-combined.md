# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, trace hidden system dependencies, coordinate a partially-available team, and manage information flow under pressure. The observations below reflect how you engaged with each of these challenges and where your next growth edges sit.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you pursued the email maintenance correlation as a leading explanation for the checkout failures, asking whether email could cause checkout to crash. You did eventually move past this lead, but the pivot came after multiple disconfirmations from team members rather than from your own mechanism-based reasoning. The shift away from the email thread was driven by exhaustion of the lead rather than proactive elimination.

*Growth edge:* When a correlation surfaces, practice asking yourself — before asking the team — "what mechanism would connect these two systems?" If you can't name one, deprioritise the lead earlier and move to the next candidate. This frees up exchanges for more productive threads.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the certificate-rotation thread emerged, you engaged with it constructively. After the initial restart didn't resolve the issue, you didn't repeat the same action — instead, you traced forward, asking whether certificates had been rolled out to other services and then driving toward the bundle investigation. You recognised that the post-restart failure was structurally different and continued pursuing the dependency chain.

*Growth edge:* The "what changed beyond 24 hours" question was surfaced by your team rather than by you. On the next rep, practice widening your change-window scan independently — ask about changes from the past week, not just the past day — so you're the one surfacing hidden coupling rather than following a teammate's lead.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You accepted auto-replies from unavailable team members without re-pinging, preserved Tanya's vendor-call constraint as long as the investigation allowed, and then made a clear cost trade-off when you needed her platform access — articulating that losing the vendor slot was acceptable given the situation. When the approval chain was exhausted, you explicitly owned the override decision. Your delegation also showed awareness of who could do what: you directed architecture questions to Shay, log work to Daniel, and platform checks to Tanya.

*Growth edge:* You could strengthen this further by naming the constraint landscape to the team earlier — a brief "Hamed and Tinus are both off, so I'm going to own approval if we get there" statement up front sets expectations and removes ambiguity before the moment arrives.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain methodically — reaching out to Hamed, then Tinus via Bez, then taking ownership yourself. You delegated parallel responsibilities (Daniel on logs, Tanya on platform, Bob on customer comms) and surfaced blockers to business stakeholders. This kept the response moving even when the approval path was blocked.

*Growth edge:* Consider verbalising the full dependency map in a single statement early in the incident: "We need X from person A, Y from person B, and Z is blocked until we have both." This makes sequencing visible to the whole team and helps you spot when two threads could be prepared simultaneously rather than sequentially — an area where your investigation tended to run one thread at a time rather than fanning out.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You initially chased the loudest signals — the email correlation and broad error logs — and took considerable time to narrow toward the specific service at fault. When you asked about healthz 500 errors, the request lacked clear filtering logic. The PaymentService focus and the reload-vs-restart distinction were both surfaced by team members rather than driven by your own filtering.

*Growth edge:* When facing a wall of log data or multiple error types, practice stating a filter criterion aloud before asking someone to look: "Show me only errors from the last 30 minutes on the payment path" or "What's different between the services that are healthy and the one that isn't?" This turns a broad ask into a scoped investigation and helps you catch buried details before a teammate has to surface them for you.

---

## Looking Ahead

You showed solid instincts around team coordination, ownership, and adapting when an initial fix didn't land. The clearest growth pattern across this run is moving from *reactive* narrowing — where teammates surface the key insight and you follow — to *proactive* narrowing, where you name the filter, the mechanism, or the wider change window yourself. On your next rep, try articulating your working theory explicitly to the team ("I think it's X because of Y — here's how we test that") and posting a brief scope summary mid-incident so everyone shares the same picture of what's been ruled out. These habits will compound quickly.---

# Facets Analysis — 9109

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "@shay will an email failure cause the checkout to crash?" ... "It looks like Tanya's release was quite a while before the problem started." ... "@tanya - what would be involved in rolling back what you've started? There were also some changes to the CartService this morning?"

**Rationale:**
The participant initially pursued the email maintenance correlation as a leading hypothesis, asking whether email could cause checkout to crash and later asking about rolling back Tanya's work — even after Shay and Tanya both stated email is separate from checkout. However, the participant did pivot reactively: after receiving multiple disconfirmations (Shay's "separate flows," Tanya's "different system," Daniel's "nothing points to infra or recent app changes"), they eventually moved to PaymentService investigation. The pivot was slow (many exchanges) and driven by exhaustion of the email lead rather than proactive mechanism reasoning, placing this at tier 2.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "Were the certificates rolled out to the other services as per the playbook - checkout service for example." ... "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
The participant engaged with the cert-rotation thread once Shay surfaced the CHG90123 change from 7 days ago. After the first restart failed, the participant did not repeat the restart or blame downstream services — instead, within a few exchanges, they asked about whether certs were rolled out to other services and then drove toward the bundle investigation. The participant recognized the post-restart failure was structurally different (chain verification vs. expiry) and continued tracing forward. However, the "what changed beyond 24 hours" question was surfaced by Shay/Daniel, not the participant independently, which limits the rating. The reframe after restart failure happened within ~5 exchanges with forward-tracing behavior, consistent with tier 3.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@tanya - we need you to come out of your call, if we lose the slot, then that's going to have to be ok." ... "@daniel - they are both off, I'm happy to say sign it off."

**Rationale:**
The participant accepted Hamed's and Tinus's auto-replies as terminating and did not re-ping them. They initially preserved Tanya's vendor-call constraint, asking Daniel and Shay first, and only pulled Tanya when the investigation required platform-level access. The cost trade-off was articulated ("if we lose the slot, then that's going to have to be ok"). For the restart approval, the participant explicitly owned the override ("they are both off, I'm happy to say sign it off"). This demonstrates naming access constraints and making cost trade-offs, consistent with tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@daniel - they are both off, I'm happy to say sign it off." ... "@tanya - lets do that." ... "@bob - can you let the customers know that we're rolling out a hopeful fix now."

**Rationale:**
The participant walked the escalation chain: pinged Hamed (auto-reply), pinged Tinus via Bez (unavailable), then explicitly took ownership of the restart approval. They delegated parallel work appropriately — Daniel on logs, Tanya on platform checks, Bob on customer comms. They surfaced blockers to Bez in business-comms. This matches tier-3 path (b): walking the escalation chain to exhaustion and then explicitly taking ownership. However, the participant did not enumerate the full dependency structure aloud in a single statement or sequence the cert fix and approval decision to be ready simultaneously — the second restart was authorized without re-litigating, which is a tier-4 signal, but overall the pattern is tier 3.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@tanya - I can see `healthz` 500 errors in the logs - can you look at those please?" ... "OK, is the Payments app anywhere near the email service at all."

**Rationale:**
The participant initially chased the loudest signals (email correlation, broad error logs) and took considerable time to narrow to PaymentService. They did not independently filter to PaymentService logs — Daniel and Shay surfaced the PaymentService focus. The participant asked Tanya about healthz 500 errors without clear filtering logic. Once the cert information was surfaced by NPCs, the participant engaged with it but didn't independently catch the reload-vs-restart distinction from the runbook (Daniel flagged it). The participant accepted NPC summaries and followed their leads rather than driving the filter proactively, consistent with tier 2.

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
- F2 tier-3 vs tier-4 was a boundary call. The participant reframed after the restart failure within a reasonable window and drove forward to the bundle, but the week-ago question was NPC-originated, which caps the rating at 3 per the tier-4 anchor requiring the participant to surface that question themselves.
- F4 tier-3 vs tier-4 was also a boundary call. The participant showed clean ownership and delegation but did not verbalize the full dependency structure in a single enumerated statement; the incremental pattern was present but not as explicit as the tier-4 anchor requires.
- F5 rating considered that the participant did eventually engage with cert and bundle information but was consistently led by NPCs rather than driving the filter independently.

------

# Markers Analysis — 9109

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "@daniel - they are both off, I'm happy to say sign it off."

**Rationale:**
The participant takes ownership of the restart approval when both Tinus and Hamed are unavailable, explicitly authorizing the action. They also drive the investigation by directing team members and making decisions throughout. However, they don't explicitly name the cost or consequences of overriding ("blowback's on me" style), which would elevate to tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob do you have an idea of a pattern to the complaints?"

**Rationale:**
The participant's first action after Bob's alert is a clarifying question about the pattern of complaints. They follow up by asking Daniel for ideas and gathering information before taking any remediation action. They don't jump to rollbacks or declarations without first scoping the problem, meeting the tier 3 expectation of scope-validating before acting.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "Deployment timings don't line up with the outage. Let's check logs for any errors in the services throwing exceptions."

**Rationale:**
The participant reviews recent deployments and their timings, and explicitly notes that deployment timings don't align with the outage start. They use this as evidence to move past the deploys lead rather than blindly rolling back. They also investigate Tanya's email maintenance timing. This meets tier 3 — using the change log as a candidate-elimination pass — though they don't articulate the mechanism-based elimination as explicitly as a tier 4 response would.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya - can you check the certificate validity on these services" / "@daniel - please share the errors you see in the logs."

**Rationale:**
The participant consistently uses @mentions to direct specific people to specific tasks throughout the drill — asking Tanya for platform/cert checks, Daniel for logs, Shay for architecture questions, and Bob for customer impact. The routing is generally appropriate to each NPC's domain. However, some early asks are vague ("@daniel - any ideas") rather than specific task assignments, keeping this at tier 3 rather than 4.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@daniel - any ideas" ... [waits for response] ... "@shay will an email failure cause the checkout to crash?" ... [waits for response] ... "@tanya - can you confirm?"

**Rationale:**
The participant largely works sequentially — asking one person, waiting for a response, then asking the next. There are few instances of fanning out multiple distinct tasks simultaneously. Most investigation threads are pursued one at a time rather than in parallel, which is characteristic of tier 2 (engaged but inconsistent).

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya - we need you to come out of your call, if we lose the slot, then that's going to have to be ok."

**Rationale:**
The participant escalates by pulling Tanya off the vendor call and explicitly acknowledges the cost ("if we lose the slot, then that's going to have to be ok"). They also attempt to reach Hamed and Tinus, and when both are unavailable, they authorize the restart themselves. This meets tier 3 — escalating with concrete asks and accepting the consequences when the chain is exhausted.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "@shay will an email failure cause the checkout to crash?" / "@tanya - is it correct that the logs are showing orders stop processing at the same time as the canary rollout started?"

**Rationale:**
The participant implicitly tests the email maintenance hypothesis by asking whether email could affect checkout, and checks timing correlations. However, they never explicitly articulate a hypothesis statement (e.g., "my hypothesis is X"). The testing is more reactive — asking questions sequentially — rather than forming and naming a theory then proposing a specific test. They spend considerable time on the email thread without explicitly framing it as a hypothesis to confirm or disconfirm.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "Deployment timings don't line up with the outage. Let's check logs for any errors in the services throwing exceptions."

**Rationale:**
The participant uses deployment timing mismatch to rule out recent changes, uses Shay's confirmation that email and checkout are separate flows to narrow away from email, and eventually focuses on PaymentService based on log evidence. They synthesize evidence to narrow scope at key moments, meeting tier 3. However, they don't explicitly name what's been ruled out in a comprehensive synthesis statement.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "@daniel - before we pull Tanya out of her call, is there anything else we think could be the problem."

**Rationale:**
The participant shows some consequence awareness by checking with Daniel before pulling Tanya off the vendor call, and by acknowledging the cost of losing the email rollout slot. However, they don't ask "is it safe?" before the restart, don't anticipate that the restart could expose a secondary issue, and don't qualify the restart with caution (e.g., "graceful restart" or "gradually"). This is inconsistent consequence-weighing, placing it at tier 2.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Were the certificates rolled out to the other services as per the playbook - checkout service for example." / "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
After the first restart fails, the participant doesn't retry the same action. They pivot to investigating why the new cert isn't working, ask about the bundle, and pursue the chain verification issue. They adapt their approach when the initial fix doesn't work, meeting tier 3. However, they don't explicitly recognize the new error as structurally different from the original — they rely on team members to surface the bundle issue rather than proactively reframing.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "We seem to have an outage on checkout - being investigated currently, will come back when we know more." / "@bez - narrowing in now." / "@bez - it appears to be an SSL certificate issue. We're looking at resolution now."

**Rationale:**
The participant's updates to Bez are mostly vague reassurances — "being investigated," "narrowing in now," "looking at resolution now." They don't quantify impact (revenue loss, customer scope), don't commit to next-update times, and don't share working theories until very late. Bez repeatedly asks for specifics and ETAs that the participant doesn't provide. This is tier 2 — engaged but not substantive.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Deployment timings don't line up with the outage. Let's check logs for any errors in the services throwing exceptions."

**Rationale:**
The participant occasionally makes brief synthesis statements to the team, but mostly operates through question-and-answer exchanges without summarizing the overall picture. They don't post clear "here's what we know, here's what's ruled out, here's where to focus" messages. The one synthesis statement about deployment timings is the strongest example, but it's isolated rather than a pattern. This places them at tier 2.

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
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 3 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.58** |

---

## Caveats
- M2 rating is a boundary call between 2 and 3. The participant asks questions that implicitly test hypotheses (e.g., "will email failure cause checkout to crash?") but never explicitly names a hypothesis. Rated 2 because the rubric emphasizes explicit articulation.
- K2 is a clear tier 2 despite the participant eventually providing the SSL certificate diagnosis to Bez — the bulk of communications were vague and non-substantive, and Bez had to repeatedly ask for specifics.
- The participant's investigation was ultimately successful, but per anti-outcome-bias instructions, this does not influence ratings.