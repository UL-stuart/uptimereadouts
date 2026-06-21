---

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