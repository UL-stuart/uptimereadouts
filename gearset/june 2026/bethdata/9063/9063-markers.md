---

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