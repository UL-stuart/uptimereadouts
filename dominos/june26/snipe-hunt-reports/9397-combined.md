# Snipe Hunt — Post-Drill Developmental Report

This drill puts you in the middle of a live incident where multiple systems interact in non-obvious ways, team availability is constrained, and the information environment is noisy. It's designed to stress your ability to reason through misleading signals, coordinate under pressure, and drive investigation when easy answers don't hold up.

---

## F1 — Misleading correlations

**Operating at: Practicing**

You noticed the timing overlap between the email maintenance window and the checkout failures, and you kept it in view as a possible factor. When you pursued the CheckoutService rollback and it produced no change, you moved away from the deployment hypothesis — but the pivot came from the rollback failing rather than from reasoning about *why* the deployment couldn't explain outbound gateway handshake errors. The email-maintenance lead similarly faded from attention without an explicit dismissal.

*Growth edge:* Before committing to a remediation action (like a rollback), practice stating the mechanism you expect: "If the deployment caused this, I'd expect the rollback to resolve handshake failures because…" That framing makes disconfirmation faster and more deliberate when the action doesn't work.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the certificate thread once the team surfaced it — asking about updating the new certificate and later proposing manual removal of the old one. However, the critical insight (expired cert still loaded in memory despite a new cert on disk) was driven by NPC investigation rather than your own questioning. The distinction between a config reload and a full service restart — which the runbook describes — didn't surface in your reasoning until Tanya explained it.

*Growth edge:* When a "fix" (like a cert rotation) appears to already be in place but the problem persists, ask what layer the fix lives at versus what layer the running service is using. That question — "is the running process actually using the new state?" — is the unlock for this class of coupling.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You reached out to both Hamed and Tinus after receiving auto-replies, and you escalated to Tanya with increasing urgency. The escalation chain eventually worked. What was missing was an explicit acknowledgement of the cost: pulling Tanya off the vendor call has consequences, and naming that trade-off ("I'm pulling you because revenue loss exceeds the risk of delaying the vendor migration") would have made the decision visible to the team and to stakeholders.

*Growth edge:* When you need to pull someone off another commitment, state the trade-off out loud in the channel. This isn't just politeness — it creates a decision record and signals to the team that you're weighing constraints, not just reacting to urgency.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You identified that Hamed was unavailable and Tanya was occupied, stating it once in-channel. That's a useful observation. The next step — sequencing work around those constraints — didn't follow. You waited for Tanya to become available rather than preparing investigation threads that could run without her, or identifying what you could pre-stage (logs, runbook steps, approval context) so her time would be used efficiently once she joined.

*Growth edge:* When you name a bottleneck, follow it immediately with "what can I do *before* this person is free?" Even gathering and posting a summary of what's been tried so far saves time when the constrained resource arrives. Your initial clarifying questions to Bob showed good instinct for scoping before acting — apply that same instinct to preparing for constrained teammates.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked Shay for filtered information about specific service deployments, which is a good instinct for managing the information flow. Once Daniel and Shay surfaced the payment-layer evidence and the cert rotation finding, you engaged with it. The pattern, though, was reactive: the critical filtering (narrowing to PaymentService, identifying the cert-in-memory issue) was done by teammates rather than driven by your own interrogation of the data.

*Growth edge:* When a teammate surfaces a finding, practice asking "what else in the logs would confirm or contradict this?" before accepting it as the working theory. Driving the filter — rather than receiving filtered results — builds the muscle for incidents where your team is smaller or less experienced.

---

## Looking Forward

Across this drill, you showed consistent willingness to engage: asking questions, reaching out to teammates, and following up when actions didn't produce results. The recurring growth theme is moving from *reactive* engagement to *proactive* framing — stating mechanisms before testing them, naming trade-offs before making them, and driving the information filter rather than waiting for teammates to surface the critical evidence. On your next rep, pick one of these edges (mechanism-stating, trade-off-naming, or filter-driving) and make it deliberate. One at a time is enough.
# Facets Analysis — 9397

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "also, the email maintenance started right when the checkout failures began. still feels worth keeping an eye on — that timing hasn't gone away." ... "dont you think if we rollback the deployements on checkout service will resolve this issue"

**Rationale:**
The participant pursued both the email maintenance and recent deployments as leading hypotheses. They ordered a CheckoutService rollback, and when it failed ("No change in error pattern"), they pivoted away from the deployment hypothesis and moved toward platform-side investigation. However, they never articulated a mechanism-based reason for dismissing the email lead — they pivoted reactively after the rollback failed rather than from upstream reasoning. The pivot latency was moderate (several exchanges after disconfirmation), consistent with tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "Oh ok, What could be the reason for it. And can you update the new certificate immediately" ... "Can we remove old certificate manually and run the reload?"

**Rationale:**
The participant engaged with the cert thread only after NPCs surfaced it (Shay found the 7-day-old rotation, Tanya investigated). They did not independently ask "what changed beyond the last 24 hours?" — that question was effectively answered by NPC investigation. When the reload failed, the participant proposed removing the old cert manually rather than recognizing the reload-vs-restart distinction from the runbook. They showed partial engagement with the coupling (expired cert in memory vs. new cert on disk) but took NPC framing rather than driving it themselves. The drill ended before a restart could be attempted, limiting deeper F2 evidence.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "Hi @hamed could you please look into this" ... "Hi @tinus we could see logs of this issue stating that errors on outbound gateway handshakes, we want have a look if this is caused due to email maintenance."

**Rationale:**
The participant pinged both Hamed and Tinus after receiving auto-replies, though they did not re-ping after the auto-replies fired. They repeatedly asked Tanya for help during her vendor call without batching or economising questions, eventually pulling her off with "Need help from platform team" and "Please prioritize this one." They never explicitly named the access constraints in their own words or articulated the cost trade-off of pulling Tanya off the vendor call. This pattern — walking the escalation chain without articulating the constraint — aligns with tier 2.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "We need to check this issue from platform side, Hamed is off today and Tanya is busy with Vendor call on email maintenance." ... "Will restarting impact anything?"

**Rationale:**
The participant did identify that Hamed was unavailable and Tanya was busy, stating this once in-channel. However, they did not proactively sequence work around these constraints — they waited passively for Tanya to become available rather than preparing parallel investigation threads. When the restart question arose, they asked "Will restarting impact anything?" but the drill ended before they could take ownership of the approval decision. They recognized some bottlenecks but didn't sequence around them or own the override, consistent with tier 2.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Yes @shay need information on checkout and shipping service deployments, can very the logs of the issue and let me know if it is causing due to the deployments" ... "Is it causing the issue now ? Can you verify it ?"

**Rationale:**
The participant asked for filtered information (checkout and shipping deployments specifically) and engaged with the payment logs when Daniel surfaced them. However, they did not independently drive filtering to PaymentService — Daniel and Shay surfaced the critical log evidence. They did not catch the reload-vs-restart distinction from the runbook (Tanya had to explain it). They accepted NPC summaries without further interrogation and relied on NPCs to surface the cert rotation and the expired-cert-in-memory finding. This pattern of engaging with information once surfaced but not driving the filter aligns with tier 2.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.00** |

---

## Caveats
- The drill ended before the participant could attempt the restart or face the post-restart bundle-order failure, limiting the depth of evidence available for F2 and F4.
- F4 rating is a borderline 2/3 call: the participant did state "Hamed is off today and Tanya is busy" once, which partially meets tier-3(a) criteria for naming the bottleneck. However, this was a reactive observation rather than a proactive coordination statement, and they did not sequence work around it or take ownership of the override, keeping the rating at 2.
- F1 pivot latency was moderate — the participant moved on from the deployment hypothesis after rollback failure but never explicitly dismissed the email hypothesis with mechanism reasoning; it simply faded from their attention once Tanya joined.

---
---

# Markers Analysis — 9397

## L3 — Takes explicit ownership of the response

**Rating:** 2

**Evidence:**
> "We are working on it Bez, cause of the issue is still unclear." / "It is the global outage, we are figuring out the resolution Bez"

**Rationale:**
The participant responds to stakeholder queries but never explicitly positions themselves as the decision-maker driving the response. They ask questions and relay information but don't use "I" statements about owning the plan. The drill ended before the restart approval moment could fully play out — the participant asked "Will restarting impact anything?" but never made the override call themselves. No explicit ownership language or acceptance of consequences is visible.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "Hi @bob What are the complaints about and how many customers impacted"

**Rationale:**
The participant's very first message after Bob's alert is a scope-validating question asking about the nature of complaints and customer impact. This precedes any declarations or remediation actions. They gather information before declaring the incident or ordering rollbacks, meeting the novice expectation for this marker.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@shay did we deployed any new changes today ?" / "Need full list @shay" / "dont you think if we rollback the deployements on checkout service will resolve this issue"

**Rationale:**
The participant asks for the change log and reviews recent deployments — good. However, they then propose rolling back the CheckoutService deployment without articulating a mechanism connecting it to the outbound gateway handshake failure. Daniel and Shay had already identified the failure was at the connection layer (Tanya's domain), yet the participant still pursued the rollback. They asked the question but didn't use the answer as an elimination pass.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "@shay @daniel dont you think if we rollback the deployements on checkout service will resolve this issue" / "@tanya we could see errors on outbound gateway handshakes, could you please have a look"

**Rationale:**
The participant does use @mentions to direct tasks to specific people. However, many asks are vague ("could you please look into it") or addressed to pairs without clear role differentiation. The participant also asks Hamed for help despite Hamed having no clear role in the investigation, and repeatedly pings Tanya without a concrete fallback plan. Delegation is present but imprecise.

---

## C6 — Runs parallel investigation threads

**Rating:** 1

**Evidence:**
> Sequential pattern: asks Shay for changes → waits → asks for details → waits → proposes rollback → waits for result → then moves to platform side

**Rationale:**
The participant works almost entirely sequentially throughout the drill. They pursue one thread at a time: first the change log, then the rollback, then trying to get Tanya involved. There is no evidence of multiple investigation threads running simultaneously with different team members assigned distinct concurrent tasks.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "Hi @hamed could you please look into this" / "Hi @tinus we could see logs of this issue stating that errors on outbound gateway handshakes... Could you please help us on this" / "Hi @tanya we need you to look into the issue as it is impacting the revenue. Please prioritize this one"

**Rationale:**
The participant does attempt escalation by pinging Hamed, then Tinus when Hamed auto-replies. However, the escalation to Tinus is vague ("Could you please help us on this") rather than a concrete ask for approval or action. When both are unavailable, the participant doesn't take ownership of the decision or form a Plan B — they repeatedly ping Tanya with increasing urgency but without naming the cost trade-off. The escalation eventually works but lacks quality context.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "@shay @daniel dont you think if we rollback the deployements on checkout service will resolve this issue" / "Is it causing the issue now ? Can you verify it ?"

**Rationale:**
The participant proposes the rollback as a test but doesn't articulate an explicit hypothesis connecting the checkout deployment to outbound gateway handshake failures. When the cert rotation is surfaced, they ask "Is it causing the issue now?" which is a test request but without articulating the mechanism. Hypotheses are implicit rather than explicitly stated and tested — the participant acts on suggestions from NPCs rather than forming their own theories.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "We could see some disks are using expired certificates even though the new certificate is present. Tanya is running the reloading"

**Rationale:**
The participant does relay findings (e.g., the expired certificate discovery) but rarely synthesizes multiple pieces of evidence to narrow scope. They don't use the failed rollback as elimination evidence, don't synthesize Daniel's "failure is at connection layer" with the change log to rule out app deploys, and don't name what's been ruled out. Most narrowing is done by NPCs (Daniel, Tanya) rather than the participant.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "Will restarting impact anything ?"

**Rationale:**
The participant does ask about restart consequences before executing, which shows some awareness. However, this is the only instance of consequence-weighing in the entire drill. They didn't consider consequences before rolling back CheckoutService, didn't weigh the cost of pulling Tanya off the vendor call (Tanya volunteered after repeated pings), and didn't ask "is it safe?" on any earlier action. The single instance at the end is insufficient for tier 3.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "We need to check this issue from platform side, Hamed is off today and Tanya is busy with Vendor call on email maintenance."

**Rationale:**
After the rollback fails, the participant does recognize they need to shift to the platform side, which shows some adaptation. However, the pivot is slow and largely driven by NPC suggestions (Daniel: "we need Tanya to check from the platform side"). The participant doesn't independently reframe the problem or propose alternative hypotheses — they follow the team's lead rather than driving the pivot. After the cert reload fails, they suggest removing the old cert, which shows some adaptation but the drill ended before full resolution.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Hi @bez No one can check out right now. Zero successful transactions since this started. We're losing about £1,000 to £1,500 every minute." / "We are working on it Bez, cause of the issue is still unclear."

**Rationale:**
The first update to Bez includes impact numbers (relayed from Bob) but no working theory, no ETA, and no committed next-update time. The second update ("working on it, cause unclear") is a vague reassurance. When Bez asks for a concrete ETA, the participant doesn't provide one. The later cert-related update to Bez mentions disks and certificates but is technical rather than business-framed. No committed cadence is maintained.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 1

**Evidence:**
> "We could see the logs are pointing out at connection issues. errors on outbound gateway handshakes, could you please look into it"

**Rationale:**
The participant rarely synthesizes findings for the technical team. They don't post summary statements about what's been ruled out or what the current working theory is. Most of their messages to the technical channel are questions or requests rather than synthesis. The one instance of scope communication ("errors on outbound gateway handshakes") is a relay of what Daniel already reported, not an independent synthesis that orients the team.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 2 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 1 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 1 |
| **Mean Marker Score** | **1.92** |

---

## Caveats
- The drill ended abruptly ("Drill Wrap-Up") just as the participant was exploring the restart path. The participant asked "Will restarting impact anything?" but never got to make the restart decision. This truncation means L3 (ownership override moment) and M5 (adaptation after restart failure) could not fully manifest. However, based on the pattern up to that point, the ratings reflect what was observed rather than what might have happened.
- K2 rating is a boundary call between 1 and 2. The participant did relay Bob's impact numbers to Bez (which is more than "we're investigating"), but never provided a working theory, ETA, or committed next-update time, and the second update was vague. Rated 2 for partial engagement.
- C7 is also a boundary call. The participant did work through the escalation chain (Hamed → Tinus → repeated Tanya pings), but the quality of escalation context was low and they never formed a Plan B or made an override decision themselves.

---