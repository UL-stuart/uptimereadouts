# Post-Drill Report — Snipe Hunt

This drill placed you in a live checkout outage with multiple competing signals, limited team availability, and pressure from business stakeholders. It's designed to stress your ability to reason through systemic complexity — tracing causation across services, managing constrained resources, and synthesising noisy information into a coherent investigation path.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you latched onto the email maintenance timing as a leading hypothesis, asking Tanya directly about its potential impact on checkout. When that was disconfirmed, you moved on — but the pivot came because Tanya told you it wasn't relevant, not because you had reasoned through the mechanism yourself. You also pursued the 10:56 UTC deployment timing without articulating why that deployment would cause the specific symptom you were seeing. Your initial clarifying questions about scope and customer impact were strong — you asked about the error, whether it was total or partial, and requested revenue numbers before jumping in. The growth edge here is building the habit of asking "what mechanism connects this correlation to the symptom?" before investing investigation time in a thread. On the next rep, try naming the causal chain you'd expect if a hypothesis were true, then checking whether the evidence matches that chain.

---

## F2 — Hidden coupling

**Operating at: Not yet evident**

You reached the certificate thread — asking whether there had been recent cert stack updates — but didn't engage with the temporal coupling that made it relevant. When Daniel surfaced that a cert rotation happened seven days ago, the key question was *why would a week-old action cause today's failure?* (reload vs. restart, old cert still in memory, expiry timing). Instead, you treated the cert issue as potentially external and asked Tanya to engage the payment gateway provider. The growth edge is recognising when a piece of evidence has a "why now?" question embedded in it. On the next rep, when someone surfaces a past action, practice asking: what changed between then and now that would make this break today?

---

## F3 — Decreased access to team

**Operating at: Practicing**

You walked the escalation chain appropriately — Hamed was out, Tinus was unavailable, and you pulled Tanya into the incident. You recognised the constraint and named it when escalating. However, once Tanya was engaged, you consumed her bandwidth with repeated low-value status requests rather than batching your asks or giving her space to investigate. Each ping ("Any ETA," "We are waiting for your updates") cost attention without advancing the investigation. The growth edge is treating a constrained resource's time as a budget: batch your questions, make each interaction count, and fill the waiting time with work you can do independently or delegate elsewhere.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You recognised that Tanya was the critical path for platform-side investigation and successfully brought her in. But while waiting for her responses, you didn't structure parallel work — Shay and Daniel were available and could have been investigating other threads (reviewing the cert rotation runbook, checking PaymentService configuration, verifying internal vs. external call patterns). Your delegation, when it happened, was often vague ("please support here," "check on the checkoutservice once") rather than scoped to a specific deliverable. The growth edge is sequencing: when one thread is blocked on a person, name two things others can do in parallel, with specific outputs you expect back.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You made good moves asking for filtered logs and narrowing from the broad error spike to PaymentService specifically. You also asked about TLS errors, which showed you were tracking the right signal. However, you accepted NPC summaries at face value without pushing further into the raw evidence — you never asked about the rotation runbook details, never investigated the reload-vs-restart distinction, and never reasoned about what the absence of internal-call failures might tell you. The growth edge is developing the reflex to ask "what's underneath this summary?" When someone gives you a finding, ask what they looked at and what they didn't — that's where buried information hides.

---

## Looking Forward

Across this drill, your instinct to ask questions and walk escalation paths is solid foundation. The consistent growth edge is moving from *reactive* to *generative*: rather than waiting for NPCs to disconfirm a hypothesis or surface the next clue, practice articulating your own causal reasoning out loud, structuring parallel work while you wait, and pushing one layer deeper into the evidence you receive. On your next rep, try naming your working hypothesis explicitly in the channel and assigning at least one parallel investigation thread before you get stuck waiting.
# Facets Analysis — 9380

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." ... Participant asks "@tanya As shay mentioned will there be any impacts because of the email maintains?" ... Later pivots to PaymentService after Shay says "PaymentService is throwing errors consistently, but there hasn't been any change on it for ages."

**Rationale:**
The participant initially pursued the email maintenance correlation by asking Tanya about it, echoing Shay's framing. However, after Tanya explicitly disconfirmed the email lead ("Primary email provider hasn't been touched... this can't be causing checkout failures"), the participant did not persist on that thread and moved toward investigating deployments and downstream services. The pivot was reactive — driven by Tanya's disconfirmation and Shay's PaymentService observation rather than by the participant's own mechanism reasoning. The participant also briefly pursued the deployment correlation ("AT what timestamp checkout failures started? immediately after 10:56 deployment") but moved on. This is tier-2 behaviour: treating coincident factors as leading hypotheses and pivoting reactively to disconfirmation rather than from upstream mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 1

**Evidence:**
> "Was there any recent update on cert stack?" ... Daniel responds: "There was a cert rotation 7 days ago, but Tanya followed the playbook." ... Participant asks "@tanya Any updates on the Cert stack?" and "@tanya Please engage the Payment gateway provider to check the certificates"

**Rationale:**
The participant reached the cert thread but only superficially. When Daniel surfaced the 7-day-old cert rotation, the participant did not engage with the temporal coupling (reload vs. restart, old cert in memory, expiry timing). Instead, they asked Tanya for updates and then suggested engaging the external gateway provider — treating the issue as potentially external rather than tracing the hidden coupling between last week's rotation and today's failure. There is no evidence of the participant connecting "rotated 7 days ago" + "reload not restart" + "expired today" or engaging with the week-old coupling mechanism at all. They treated each piece of evidence as independent rather than building a causal chain. This is tier-1 behaviour: the cert thread surfaced but the participant did not engage with the hidden coupling.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@hamed Can you check is there any abnormal activity from infra side?" [receives auto-reply] ... "@tinus Hamed is off and @tanya is in email maintaince We need support from Platform team" [receives auto-reply] ... "@tanya please support here its P1 issue" ... Multiple pings to Tanya: "We are waiting for your updates" / "Any ETA" / "Got any insites?"

**Rationale:**
The participant did walk the escalation chain (Hamed → Tinus → Tanya) and accepted auto-replies as terminating for Hamed and Tinus. However, they repeatedly pinged Tanya with low-value status requests ("Any ETA," "We are waiting for your updates," "Got any insites?") without batching or economising on her bandwidth. They did not articulate the access constraint pattern in their own words beyond noting "Hamed is off and Tanya is in email maintenance." The participant pulled Tanya off the vendor call appropriately for a P1, but without explicitly naming the cost trade-off. This is tier-2 behaviour: walking the chain without articulating the constraint, and consuming Tanya's bandwidth on repeated low-value queries.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "@tanya please support here its P1 issue" ... "Its might take next couple of minutes @bez. Platform team is looking into it and I'm following up" ... Participant does not delegate parallel work or sequence investigation threads; repeatedly asks Tanya for updates without structuring the work.

**Rationale:**
The participant recognised that Tanya was needed for platform-side investigation and successfully pulled her into the incident. However, they did not sequence work in parallel — while waiting for Tanya, they did not assign Shay or Daniel to investigate other threads (e.g., reviewing the cert rotation runbook, checking PaymentService config). The participant did not name the coordination bottleneck explicitly or own any override decision. They treated the incident as a serial dependency on Tanya's investigation without structuring around it. The restart-approval moment never arose because the participant never identified the specific fix path, but the broader sequencing/parallelism signals show tier-2 behaviour: recognising some bottlenecks but not sequencing around them.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> Participant asks "can we see logs metrics before and after 10:56 UTC?" ... Shay surfaces PaymentService logs showing TLS handshake failures ... Participant asks "Was there any recent update on cert stack?" but does not follow through on the reload-vs-restart distinction or investigate the cert rotation runbook.

**Rationale:**
The participant did ask for filtered logs and narrowed from the broad error spike to PaymentService specifically. They engaged with the cert stack concept once Daniel surfaced the 7-day rotation. However, they did not drive further into the buried information — they never asked about the rotation runbook, never investigated reload vs. restart, and never reasoned about absence of signal (e.g., internal calls clean but external failing). They accepted NPC summaries without further interrogation and did not catch key distinctions in referenced documentation. This is tier-2 behaviour: asking for filtered information but not following through into the raw evidence or catching buried distinctions.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 1 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **1.80** |

---

## Caveats
- The drill timed out before the participant reached the restart-approval moment, limiting F4 evidence to broader sequencing/parallelism signals. The highest-leverage F4 evidence (ownership of override) never fired.
- F2 rating of 1 is a boundary call: the participant did reach the cert thread and asked about it, but never engaged with the temporal coupling mechanism (reload vs. restart, week-old action causing today's failure). Per the rubric, the cert thread surfaced and the participant did not engage with the hidden coupling — this is tier 1, not N/A.
- The participant's repeated low-value pings to Tanya ("Any ETA," "We are waiting for your updates") could be read as either F3 (access constraint) or F4 (coordination bottleneck) evidence; I weighted it in both facets as it manifests differently in each.

---
---

# Markers Analysis — 9380

## L3 — Takes explicit ownership of the response

**Rating:** 2

**Evidence:**
> "Its might take next couple of minutes @bez. Platform team is looking into it and I'm following up"

**Rationale:**
The participant relays information and follows up with NPCs but never explicitly positions themselves as the incident commander driving the response. They never make an override decision (both Tinus and Hamed are unavailable and the participant doesn't self-authorize any action). They act more as a coordinator passing messages than as someone owning the outcome. No "I authorize" or "this is my call" language appears.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob What error customer observed?" ... "How many customers are blocked right now? What's the revenue loss per minute? Is this a total checkout outage or are some orders still going through"

**Rationale:**
The participant's first substantive moves after Bob's alert are clarifying questions about the error, scope, and impact before taking any remediation action. They ask about the error customers see, whether it's total or partial, and request revenue numbers. This is solid scope-validation before acting, meeting the novice expectation.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@shay is there any recent deployment happen?" ... "Full list to see broader view"

**Rationale:**
The participant asks for the deployment list and reviews it. However, they don't use the change log as a candidate-elimination pass. They later ask Daniel what changed in the checkout release and pursue the 10:56 UTC deployment timing correlation without articulating a mechanism connecting it to the symptom. They never explicitly rule out deploys based on the evidence, treating the timing correlation as significant rather than using absence-of-mechanism to deweight it.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "@tanya please support here its P1 issue" ... "@shay can you pull metrics from downstream services like pyaments, currency service..etc" ... "@daniel Can you check on the chekoutservice once"

**Rationale:**
The participant does use @mentions to direct tasks to specific people. However, the asks are often vague ("please support here," "check on the checkoutservice once") rather than specific actionable tasks. They also repeatedly ping Tanya while she's unavailable without redirecting to someone else. The routing shows partial understanding of access boundaries but lacks precision in task definition.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@shay can you pull metrics from downstream services like pyaments, currency service..etc" ... "@hamed Can you check is there any abnormal activity from infra side? n/w metrics"

**Rationale:**
There are a few instances where the participant sends multiple asks in relatively close succession (Shay for metrics, Hamed for infra). However, much of the investigation proceeds sequentially — waiting for one response before asking the next question. The parallel threads are limited and not well-structured as complementary investigations.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "@tinus Hamed is off and @tanya is in email maintaince We need support from Platform team see issue related to networks" ... "@tanya please support here its P1 issue"

**Rationale:**
The participant attempts escalation to Tinus when Hamed is unavailable, which shows awareness of the escalation chain. However, when Tinus auto-replies, the participant doesn't follow up with a Plan B or self-authorize. The escalation to pull Tanya off the vendor call happens only after Daniel explicitly suggests it ("Should we pull Tanya off email maintenance?"). The escalation lacks concrete context and a clear ask.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "@tanya As shay mentioned will there be any impacts because of the email maintains?" ... "External Payment gateway conenction is failing during handshakes please check @tanya"

**Rationale:**
The participant implicitly follows hypotheses (email maintenance, then deployment timing, then gateway connection) but never explicitly articulates them as hypotheses or proposes specific tests. They ask questions that touch on hypotheses but don't frame them as "hypothesis: X, test: Y." The pivot from email maintenance to gateway issues happens largely because NPCs provide the evidence, not because the participant designs a test.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "External Payment gateway conenction is failing during handshakes please check @tanya" ... "Are you seeing any TLS error?"

**Rationale:**
The participant does eventually narrow to the PaymentService outbound connection and TLS handshake failure, but this narrowing is largely driven by NPC-provided evidence (Daniel's logs, Tanya's findings) rather than the participant synthesizing and ruling things out. They never post a synthesis statement like "we've ruled out X, Y, Z — focus is now on W." The narrowing happens passively rather than actively.

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "@tanya please support here its P1 issue"

**Rationale:**
The participant never explicitly weighs consequences before taking action. When pulling Tanya off the vendor call, they don't acknowledge the cost (losing the 2-week rollout window). They don't ask "is it safe?" before any proposed action. No "carefully" or "gradually" qualifiers appear. The absence of consequence-weighing language is notable throughout the transcript.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "Was there any recent update on cert statck?" ... "@tanya Please engage the Payment gateway provider to check the certificates"

**Rationale:**
The participant does move from the email maintenance hypothesis to the deployment timing hypothesis to the gateway/cert area, showing some adaptation. However, the pivots are largely driven by NPC guidance rather than the participant recognizing disconfirmation and redirecting. At the end, when Tanya reports no visible cert issues, the participant's response is to ask Tanya to engage the gateway provider — showing some adaptation but not a strong reframing of the problem.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Payment gateway issue @bez connectivity is failing during the handshake" ... "Its might take next couple of minutes @bez. Platform team is looking into it and I'm following up"

**Rationale:**
The participant does communicate with Bez multiple times, but the updates lack substance. They relay raw information without business framing ("No transactions are going through"), fail to provide revenue numbers despite Bez repeatedly asking, and give vague ETAs ("next couple of minutes") without committing to update cadences. The updates are reactive to Bez's pressure rather than proactive and substantive.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "External Payment gateway conenction is failing during handshakes please check @tanya" ... "What has be ruled out? what is the priority"

**Rationale:**
The participant occasionally relays findings to the team ("External Payment gateway connection is failing during handshakes") but never posts a comprehensive synthesis statement that names what's been ruled in and ruled out. Notably, "What has be ruled out? what is the priority" is the participant *asking* the team rather than *telling* the team — indicating they aren't maintaining a clear mental model to communicate. The team largely self-organizes around the evidence.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 2 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.00** |

---

## Caveats
- The drill ended before the participant reached the cert expiry/bundle resolution, which limits observation of M5 pivot behavior at the second failure point. However, the participant had ample opportunity to demonstrate stronger process behaviors throughout the available time.
- K2 rating could arguably be a 1 given Bez's repeated dissatisfaction, but the participant did provide some directional information (gateway handshake failing, payment gateway issue) even if not in business-framed terms.
- M4 is rated 1 rather than N/A because there were clear moments where consequence-weighing was called for (pulling Tanya off vendor call, any restart/rollback decisions) and the participant did not engage with them.

---