# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, absent team members, hidden system dependencies, and dense operational information — all while coordinating a distributed team under time pressure. The observations below reflect how you engaged with each of these challenges.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you latched onto Tanya's email maintenance change as the leading cause of checkout failures. Even after Tanya explicitly stated that email confirmations were unrelated to the checkout path, you continued pursuing that thread for several more exchanges before pivoting. The pivot eventually came once Daniel's logs surfaced concrete disconfirming evidence (TLS handshake failures pointing to PaymentService), rather than from your own mechanism reasoning about why email maintenance couldn't cause the observed symptoms.

*Growth edge:* When a team member offers a clear disconfirmation, practise pausing to ask yourself "what mechanism would connect this change to the symptom I'm seeing?" If you can't articulate one, move on sooner. The goal is to let mechanism reasoning — not just new evidence from elsewhere — drive your pivots.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once Daniel surfaced the 7-day-old cert rotation (CHG90123), you engaged with the cert thread and asked relevant questions about expiry. When the first restart didn't resolve the issue, you redirected within a few exchanges — asking for fresh logs and requesting a review of the cert documentation rather than proposing another restart. You followed the chain from cert rotation through to the bundle ordering issue with NPC assistance, connecting the layers of the problem as they emerged.

*Growth edge:* You didn't independently surface the "what changed beyond 24 hours" question — Daniel found the older change. On your next rep, try broadening your change-window scan earlier. Asking "what changed in the last week, not just today?" can surface hidden coupling before a teammate happens to find it.

---

## F3 — Decreased access to team / remote

**Operating at: Strengthening**

You handled the absence of Hamed and Tinus by accepting their auto-replies and moving forward. You made an explicit ownership statement when authorising the restart, and you made a clear cost trade-off by pulling Tanya off the vendor call — escalating from "pause" to "postpone altogether" when the situation demanded it. You also routed delegation appropriately given who was available, assigning Daniel to logs and Tanya to platform investigation.

There was some inefficiency: you continued attempting to reach Tinus through Bob and Daniel even after already receiving auto-replies and having already authorised the change yourself. This created noise without adding decision-making value.

*Growth edge:* Once you've taken ownership and made the call, trust your own authority. Continuing to chase an absent approver after you've already acted can signal uncertainty to the team and consume coordination bandwidth.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain in a visible, logical order — attempting Hamed, then Tinus, then explicitly taking ownership when both were unavailable. On the second restart (after the bundle fix), you authorised without re-litigating the approval chain, which showed you'd internalised the decision authority. You also delegated parallel work appropriately, with Daniel on logs and Shay/Daniel on the customer-facing banner.

*Growth edge:* Consider articulating the full dependency structure in a single statement early in the incident — something like "we need platform access, approval authority, and vendor coordination; here's who owns each." Naming the structure aloud helps the team see bottlenecks before they bite, and positions you to act faster when one path closes.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You showed awareness of the cert documentation by asking the team to review it, but you didn't independently catch the key distinctions within it (reload vs. restart, bundle ordering). The log filtering that pointed to PaymentService was driven by Daniel, and the bundle issue was surfaced by Tanya. You accepted NPC summaries without further interrogation, and your engagement with buried details came after teammates had already extracted them.

*Growth edge:* When a teammate surfaces a finding, try asking one layer deeper before accepting it — "what else is in that log section?" or "what does the runbook say about failure modes after a restart?" Practising active interrogation of data sources, rather than waiting for filtered summaries, builds the muscle for catching buried signals yourself.

---

## Looking Forward

You showed clear strengths in taking ownership under pressure and adapting your approach when the first fix didn't work — you didn't simply retry the restart, you redirected investigation. Carry that adaptiveness into your next rep, and pair it with earlier mechanism reasoning when evaluating candidate causes. The combination of decisive authority (which you demonstrated) and independent evidence interrogation (your next growth area) will strengthen your overall incident command.# Facets Analysis — 9190

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Are you saying its every region affected? Was it five minutes ago the first report of this?" ... "@tanya Can you elaborate on what change you made that Shay is reffering to? Email maintenance? Does the change affect anything else?" ... "This is more important than the secondary email rollout"

**Rationale:**
The participant initially treated Tanya's email maintenance as the leading hypothesis, pulling Tanya off the vendor call to investigate her changes. Tanya explicitly stated "Email confirmations have been fine, so this maintenance can't be causing checkout failures," yet the participant continued pursuing this thread for several more exchanges. The participant did eventually pivot away from the email hypothesis once Daniel's logs pointed to PaymentService SSL failures, but this pivot was driven by concrete disconfirming evidence (the logs showing TLS handshake failures) rather than upstream mechanism reasoning. The pivot latency from Tanya's disconfirmation was substantial (many exchanges), placing this in tier 2 territory.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "No certs have expired have they?" ... "Can we please redirect it to point to the new cert asap please?" ... "Can we reload it asap? Or if that doesn't work restart?" ... "Can we check the logs to see where it's failing now @tanya?"

**Rationale:**
The participant engaged with the cert thread once Daniel surfaced CHG90123 (the 7-day-old cert rotation). After the first restart failed, the participant pivoted within approximately 3-4 exchanges — asking to check logs, and then engaging with the bundle/chain issue once Tanya surfaced the verification failure. The participant did not independently surface the "what changed beyond 24 hours" question (Daniel found CHG90123), but once the restart failed, the participant reframed relatively quickly by asking for new logs rather than proposing another restart. The participant connected the cert rotation → reload-vs-restart → bundle ordering chain with NPC assistance, meeting tier 3 criteria.

---

## F3 — Decreased access to team / remote

**Rating:** 3

**Evidence:**
> "With both absent I authorise the change" ... "@hamed Can you please reach out to the payment service provider..." [receives auto-reply] ... "@tinus Can you please reach out..." [receives auto-reply] ... "Pause It" ... "Please don't pause the vendor window, postpone it all together"

**Rationale:**
The participant accepted auto-replies from Hamed and Tinus and moved on after one cycle each. They made the cost trade-off with Tanya explicitly — pulling her off the vendor call and later escalating from "pause" to "postpone." They named the access constraint when authorising the restart ("With both absent I authorise the change"). However, there was some inefficiency — they continued pinging Tinus via Bob and Daniel even after receiving auto-replies multiple times, and the initial handling of Tanya's vendor-call constraint required multiple exchanges before being decisive. This places the participant solidly at tier 3 with some tier-2 elements.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "With both absent I authorise the change" ... "I dont think we need any further approvals from Tinus or Hamed since you're at command here in the incident" [NPC affirming participant's earlier decision] ... "Please restart @tanya"

**Rationale:**
The participant walked the escalation chain in observable order — pinged Hamed (auto-reply), pinged Tinus (auto-reply), then explicitly took ownership and authorised the restart. This matches tier-3 path (b). They delegated parallel work appropriately (Daniel on logs, Shay/Daniel on banner). On the second restart (after bundle fix), the participant authorised without re-litigating the approval chain ("Please restart @tanya"). However, they did not articulate the full dependency structure aloud in a single enumerated statement, and continued attempting to reach Tinus even after the first authorisation, which slightly undermines the tier-4 case.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Can we please go over the steps in the cert documentation to ensure they were all followed?" ... "Can we reload it asap? Or if that doesn't work restart?" ... "Lets get that second cert on asap please @tanya"

**Rationale:**
The participant did not independently filter logs to PaymentService — Daniel drove that investigation. The participant did not independently surface the reload-vs-restart distinction from the runbook; Tanya surfaced the cert status and the bundle issue. The participant's request to "go over the steps in the cert documentation" shows awareness of the doc but they didn't catch the key distinctions themselves. They accepted NPC summaries without further interrogation and engaged with key concepts (bundle, chain order) only once NPCs surfaced them. This matches tier 2: asks for filtered information but doesn't drive the filter or catch buried distinctions independently.

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
- F1 rating is a boundary call between 1 and 2. The participant pursued the email hypothesis persistently despite Tanya's explicit disconfirmation, but did eventually pivot once logs pointed elsewhere. Rated 2 because the pivot occurred (driven by concrete evidence from Daniel's logs) rather than the participant staying locked on the email hypothesis through the entire drill.
- F3 rating is a boundary call between 2 and 3. The participant's repeated attempts to reach Tinus (via Bob, Daniel) after already receiving auto-replies and already having authorised the change themselves is a tier-2 signal, but the explicit ownership statement and the decisive Tanya trade-off push toward tier 3.
- Anti-outcome-bias note: The successful resolution and NPC praise at the end are not factored into ratings. The participant reached resolution largely through NPC-driven investigation (Daniel finding logs, Tanya identifying cert issues and bundle problems).

------

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