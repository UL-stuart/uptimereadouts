---

# Markers Analysis — 9190

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "With both absent I authorise the change"

**Rationale:**
The participant takes ownership of the response by making the override decision when both Tinus and Hamed are unavailable. They also drive the investigation throughout, directing team members and making decisions. However, they don't explicitly name the cost or consequences of the override ("blowback's on me" style), which would elevate to tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "What reports are you seeing Bob?" ... "Are you saying its every region affected? Was it five minutes ago the first report of this?" ... "Also Bob, what error message are they seeing?"

**Rationale:**
The participant's first actions are scope-validating questions to Bob — asking about the nature of reports, regions affected, timing, and error messages before declaring the incident or taking remediation action. They gather information systematically before acting, meeting the novice expectation. They don't quite reach tier 4 as they don't probe for pattern differentiation across reports.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "Is this your change Tanya CHG90436?" ... "Would that change affected anything CHG90436 @tanya?"

**Rationale:**
The participant does ask about recent changes, specifically querying Tanya about CHG90436 and whether it could have affected checkout. However, they don't systematically review the change log as a candidate-elimination pass. They also spend significant time pursuing Tanya's email maintenance as a potential cause without articulating a clear mechanism connecting it to the symptom. The change-log review is reactive rather than systematic.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya Can you elaborate on what change you made..." / "If you can Daniel please, thanks" / "@bob can you please ring tinus until he picks up" / "@shay / @daniel please reach out to Tinus"

**Rationale:**
The participant delegates tasks to specific named individuals throughout the drill — asking Daniel for logs, Tanya for platform investigation, Bob for customer communication, and Shay/Daniel for the maintenance banner. Most delegations are appropriately routed to the right person. However, some asks are slightly misrouted (asking Bob to ring Tinus, asking Hamed to contact the payment provider when he's OOO), which prevents a tier 4 rating.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@tanya Can you elaborate on what change you made that Shay is referring to?" ... "If you can Daniel please, thanks" [in response to Daniel offering to pull logs]

**Rationale:**
The participant does have multiple people working at different points, but the investigation is largely sequential. They focus on Tanya's email maintenance first, then move to logs with Daniel, then back to Tanya for platform checks. There's limited evidence of deliberately fanning out multiple distinct investigation threads simultaneously. Most parallel activity happens reactively rather than through deliberate concurrent delegation.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "This is more important than the secondary email rollout" ... "Pause It" ... "With both absent I authorise the change"

**Rationale:**
The participant escalates effectively by pulling Tanya off the vendor call when investigation is blocked at the platform layer, and makes the override decision when both Tinus and Hamed are unavailable. They accept the auto-replies as terminating and move forward. However, they don't explicitly name the cost of pulling Tanya off the vendor call (the 2-week window loss), which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "I believe the issue may be related to an expired certificate, confirming with the platform team now"

**Rationale:**
The participant does eventually arrive at the cert hypothesis, but they don't explicitly articulate and test hypotheses throughout the investigation. The email maintenance lead is pursued without a clear mechanism test — they ask Tanya to check her changes but don't articulate "hypothesis: email maintenance caused checkout failure because X." The cert hypothesis is stated only after Tanya's investigation reveals it. The participant is more reactive to NPC findings than proactively forming and testing theories.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "Looks like the first one has expired?" ... "Lets get that second cert on asap please @tanya"

**Rationale:**
The participant does use evidence at key moments — recognizing the expired cert from Tanya's output and understanding the bundle order issue. However, they don't produce synthesis statements that combine multiple pieces of evidence to narrow scope. They don't explicitly rule things out or name what's been eliminated. Much of the narrowing is done by NPCs (Daniel and Tanya) with the participant acknowledging rather than synthesizing.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "Can we reload it asap? Or if that doesn't work restart? As long as there are no other dependencies"

**Rationale:**
The participant shows some awareness of consequences with the "as long as there are no other dependencies" qualifier before the restart. However, they don't anticipate the secondary failure mode (bundle order issue) or check the bundle before restarting. They also don't explicitly name the cost of pulling Tanya off the vendor call. The consequence consideration is present but minimal and inconsistent.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Can we check the logs to see where it's failing now @tanya?" ... "Can you please go over the steps in the cert documentation to ensure they were all followed?"

**Rationale:**
After the first restart fails, the participant doesn't simply retry — they ask to check logs for the new failure mode and request verification against the cert documentation. This leads to discovering the bundle order issue. They adapt from "restart should fix it" to "something else is wrong, let's investigate further." This meets the novice expectation of not repeating the same failed action and redirecting investigation.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "We're investigating now, I will update you in 5 minutes" ... "I believe the issue may be related to an expired certificate, confirming with the platform team now" ... "We are making a change in the next 2 minutes, we hope this will fix it"

**Rationale:**
The participant provides some updates to Bez but they are largely vague — "investigating with highest priority," "can't give a specific ETA." The cert-related update is more substantive but comes late. They don't quantify business impact in their comms to Bez (despite having the data from Bob), and the updates lack the structure of scope + impact + theory + next-update time. The "5 minutes" commitment is good but the content is thin.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Bob is reporting that we are losing £1,000 to £1,500 a minute at peak, all users affected, 34 reports of it so far"

**Rationale:**
The participant shares Bob's impact data with the technical channel, which is useful context. However, they rarely produce synthesis statements that summarize what's been ruled in or out for the team. They don't post messages like "it's not email maintenance, not recent deploys, focus on PaymentService outbound." Most of their technical channel messages are questions or acknowledgments rather than state-of-the-world summaries that orient the team.

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
- L3: The participant says "With both absent I authorise the change" which is a clear ownership moment, but it lacks the explicit cost-naming that would push to tier 4. Borderline 3/4 call resolved toward 3.
- C3: The participant asks about changes but doesn't systematically use the change log as an elimination tool. They pursue the email maintenance lead without clear mechanism reasoning, which is more of an M2 issue but also reflects on how they used the change information.
- M5: The post-restart pivot is clean (asking for new logs, checking documentation), but the participant doesn't explicitly name the new failure as structurally different from the original, which keeps this at tier 3 rather than 4.
- K2: The update to Bez about the cert issue ("I believe the issue may be related to an expired certificate") is the most substantive business update, but it comes without quantified impact framing or committed next-update time in the same message.

---