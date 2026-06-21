---

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