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