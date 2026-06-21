# Snipe Hunt — Post-Drill Developmental Report

This drill puts you in the middle of a live checkout outage with multiple possible causes, limited team availability, and pressure to coordinate across technical and business layers simultaneously. It's designed to stress your ability to reason through misleading signals, surface hidden system relationships, and manage coordination under constraint.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, when the email maintenance timing was raised as a possible cause, you directed Tanya to investigate it. Once she reported back that email confirmations were unaffected, you moved on — which is the right outcome. The growth edge here is in *how* you moved on: the pivot came because Tanya told you it wasn't the cause, rather than because you reasoned through whether email could plausibly break payment at all. On your next rep, try articulating the mechanism before assigning someone to investigate — "could this change reach the failing component?" If the answer is no, you save time and team bandwidth without needing someone else to rule it out for you.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the certificate thread once it was surfaced by your team, and you recognised the expired-cert evidence when it appeared. The gap is in who drove the discovery: the connection between a week-old cert rotation and today's failure was identified by NPCs, and after the first restart failed, you asked for ideas rather than reframing why a restart might not resolve a cert-loading issue. The next growth edge is noticing when a fix fails and asking yourself *what structural assumption did I just invalidate?* — that's the moment where hidden coupling becomes visible, and it's worth pausing to reason through rather than immediately asking others what to try next.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You walked the escalation chain — pinging Hamed, Tinus, and eventually pulling Tanya off her vendor call. The pattern that emerged, though, was multiple individual pings to people who had already signalled unavailability, and several separate requests to Tanya rather than a single batched ask. On your next rep, try naming the constraint pattern to yourself early: "Who is actually available right now, and what can each person uniquely do?" That framing helps you economise attention — both yours and theirs — and makes the decision to pull someone off another task more deliberate rather than incremental.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

This was your strongest facet in this run. You walked the approval chain to exhaustion — checking whether Hamed or Tinus could sign off, confirming both were out, asking if anyone else could authorise, and then explicitly stating you would own the risk. You also delegated parallel work appropriately, assigning Shay to the customer-facing banner while the technical investigation continued. The growth edge toward the next level is naming the dependency structure *before* you hit it — verbalising something like "restart needs sign-off, and both approvers are OOO, so I need to decide now whether I'm willing to own this" as a single constraint statement rather than discovering it through sequential attempts.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

When evidence appeared — logs, cert status, error messages — you engaged with it. But the filtering and interpretation work was largely done by your team members, with you asking follow-up questions after they'd already synthesised. You asked "how do we fix the chain?" only after the chain verification failure had been identified for you. The growth edge is in actively reading the available documentation and evidence yourself, looking for distinctions (like reload-vs-restart) before asking others to interpret. Even a quick scan of an activity doc or error output, with a "what's different here from what I expected?" lens, can surface critical information earlier.

---

## Looking Forward

Across this drill, your coordination instincts — pulling people in, escalating when blocked, taking ownership of risk — are developing well and gave you a solid foundation to work from. The consistent growth edge is in *driving your own reasoning* earlier in the sequence: articulating mechanisms before investigating, reframing when a fix fails, and synthesising evidence yourself rather than waiting for team members to interpret it for you. On your next rep, try narrating your current understanding to the team channel — even a brief "here's what we know and don't know" statement can sharpen your own thinking and keep the investigation coherent.# Facets Analysis — 9173

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "hey — not trying to distract from this, but tanya kicked off the email maintenance right before the complaints started. probably nothing, but the timing is a bit close." ... "thanks Daniel @tanya can you look into your email maintenance change" ... "@tanya please can you leave the maintenace and help investigate urgently"

**Rationale:**
The participant initially pursued the email maintenance lead after Shay raised it, asking Tanya to investigate her email changes. However, after Tanya explicitly stated "Primary email provider is untouched. Email confirmations have been sending fine, so this maintenance isn't causing checkout failures," the participant did not continue pursuing email as the cause. They pivoted reactively — Tanya's disconfirmation was concrete and the participant moved on, but they never articulated mechanism reasoning ("does email plausibly break payment?"). The pivot was reactive to NPC disconfirmation rather than driven by upstream reasoning, placing this at tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "So is this a certificate error? 'Certificate on disk (not loaded by process):'" ... "can we restart the process?" ... "@tanya any other ideas?" [after restart failed]

**Rationale:**
The participant did not surface the "what changed beyond the last 24 hours?" question themselves — it was Tanya who volunteered the cert rotation information. After the first restart failed, the participant did not reframe the failure as structurally different; instead they asked "@tanya any other ideas?" and waited for NPCs to drive the investigation forward. They did not articulate the reload-vs-restart distinction or connect the week-old rotation to today's failure in their own words. The pivot after the failed restart was passive — they relied on Daniel and Tanya to identify the chain verification issue. This matches tier 2: engages with the cert thread only when NPCs name it, partial connection of timestamps, and the reload-vs-restart distinction taken on NPC framing.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tinus do you think we should pull Tanya" [after Tinus already sent auto-reply] ... "@hamed is there anything else we can check in the meanwhile" [after Hamed's auto-reply] ... "please step away and help us review" [third ping to Tanya during vendor call]

**Rationale:**
The participant pinged Hamed after receiving the auto-reply, and pinged Tinus after already knowing he was at the summit. They sent multiple messages to Tanya during the vendor call without batching or economising, requiring three separate requests before making the call to pull her. They did not articulate the access constraints in their own words or make a cost trade-off statement when pulling Tanya. This matches tier 2: walks the escalation chain but without articulating the constraint pattern, and consumes Tanya's bandwidth without visible economising.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "Hamad and Tinus are OOO" ... "Can anyone else sign off?" ... "As they are both out I will own the risk. Please restart the process"

**Rationale:**
The participant walked the escalation chain to exhaustion in observable order: asked Tanya about restart, learned sign-off was needed from Hamed or Tinus, acknowledged both were OOO, asked if anyone else could sign off, then explicitly took ownership ("As they are both out I will own the risk"). This matches tier 3 path (b) — walks the escalation chain to exhaustion and then explicitly takes ownership. They also delegated parallel work appropriately (Shay on banner, Daniel on logs). On the second restart (after bundle fix), they authorised without re-litigating. However, they did not name the dependency structure aloud as a single constraint statement or verbalise it proactively before the moment arose, which would be needed for tier 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "So is this a certificate error? 'Certificate on disk (not loaded by process):'" ... "how do we fix the chain?" ... "Can you restart the process"

**Rationale:**
The participant noticed the expired certificate information when Tanya surfaced it but did not drive the filtering themselves — they relied on Daniel to pull PaymentService logs and on Tanya to identify the TLS handshake failure. They did not read the activity doc or catch the reload-vs-restart distinction. After the restart failed, they asked "@tanya any other ideas?" rather than engaging with the structural difference in the error. They asked "how do we fix the chain?" only after Daniel and Tanya surfaced the chain verification failure. This matches tier 2: engages with key concepts once NPCs surface them but doesn't drive the filter or read docs to catch distinctions.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.20** |

---

## Caveats
- F1 is a borderline 2/3 call. The participant did not explicitly pursue the email lead after Tanya's first disconfirmation, which could suggest mechanism reasoning. However, they never articulated *why* email couldn't cause checkout failures — the pivot appears reactive to Tanya's authority rather than to mechanism reasoning. Rated 2 on the basis that no mechanism reasoning is observable in the text.
- F4 is a clean tier 3 via path (b). The participant did not verbalise the dependency structure proactively or name it as a constraint statement, which would be needed for tier 4.
- The participant reached resolution, but per anti-outcome-bias, this does not influence ratings.

------

# Markers Analysis — 9173

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "As they are both out I will own the risk. Please restart the process"

**Rationale:**
The participant explicitly takes ownership of the restart decision when both approvers are unavailable, stating they will "own the risk." However, this came only after multiple back-and-forth exchanges where they asked others if they could sign off and seemed to need prompting from NPCs about who would need to take responsibility. The ownership statement is clear but arrived late in the sequence rather than proactively.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "What are customers complaing about?" ... "How many customers are blocked from checkout right now? What's the revenue loss per minute? Is this a total outage or are some still getting through?"

**Rationale:**
The participant's first response to Bob's complaint is a clarifying question about what customers are experiencing. They follow up with scope-quantifying questions about how many are affected and whether it's total or partial. These questions precede any remediation actions, showing a clear information-gathering-first approach before declaring the incident.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "can I see the recent changes" ... "can you investigate this further whther this could be causing the issues?"

**Rationale:**
The participant asks for the change log, which is good. However, when Shay notes "none of these changes look like they'd break checkout end-to-end like this," the participant doesn't use this as elimination evidence. Instead, they ask "so we think its one of the checkout changes that could have caused this?" — suggesting they didn't process the absence-of-mechanism signal. They asked the question but didn't effectively use the answer for candidate elimination.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "Hi @daniel , @hamed please can you take a look customers are unable to check out" ... "@tanya please can you leave the maintenace and help investigate urgently" ... "@shay can you help Tanya at all"

**Rationale:**
The participant does use @mentions to direct tasks to specific people. However, the initial delegation to Daniel and Hamed is vague ("take a look"), and Hamed is OOO. The ask to Shay to "help Tanya" is imprecise — Shay can't do platform work. The participant routes tasks to named people but often without specific scope or awareness of access boundaries.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@shay @daniel @hamed is there anything else we can check in the meanwhile"

**Rationale:**
The participant mostly works sequentially — asking Tanya to check email maintenance, then waiting, then asking Daniel for logs, then waiting for Tanya to check certs. The one attempt at parallelism ("is there anything else we can check in the meanwhile") is a vague broadcast rather than distinct tasks assigned to distinct people. The investigation proceeds largely as a single thread at a time.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya yes please pause" ... "@tinus do you think we should pull Tanya"

**Rationale:**
The participant escalates by pulling Tanya off the vendor call when the investigation is blocked at the platform layer. They first try Tinus for approval (who auto-replies), then make the call themselves. The escalation is concrete — they tell Tanya to pause and help investigate. However, they initially asked Tinus whether to pull Tanya rather than making the call directly, showing some hesitation before committing.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "so we think its one of the checkout changes that could have caused this?" ... "So is this a certificate error?"

**Rationale:**
The participant rarely articulates explicit hypotheses. They ask questions that imply hypotheses (checkout changes? email maintenance? certificates?) but don't frame them as testable theories. The closest to hypothesis formation is asking about the certificate error after seeing the evidence, but this is more reactive observation than proactive hypothesis-test pairing. They follow NPC leads rather than forming and testing their own theories.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "So is this a certificate error? 'Certificate on disk (not loaded by process):'"

**Rationale:**
The participant does eventually recognize the certificate issue from the evidence Tanya presents, but they don't actively synthesize evidence to narrow scope. When Daniel reports "PaymentService fails all outbound gateway handshakes. Checkout is healthy, just getting errors," the participant doesn't use this to explicitly narrow the problem. They rely heavily on NPCs to interpret evidence rather than performing their own synthesis and elimination.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "What do we think the risks are to restart the payment process?"

**Rationale:**
The participant does ask about risks before the restart, which shows some consequence consideration. However, this is a single instance, and they don't consider consequences before other actions (pulling Tanya off the vendor call without weighing the 2-week cost, or considering what might happen if the restart doesn't fix the issue). The risk question about the restart is good but isolated.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "@tanya any other ideas?" ... "@daniel can you check app side" ... "how do we fix the chain?"

**Rationale:**
After the first restart fails, the participant doesn't simply retry the same action. They ask for new ideas and direct Daniel to check the app side, which surfaces the cert chain issue. When Tanya identifies the bundle problem, they move forward with the fix. The pivot isn't deeply analytical (they ask others for ideas rather than reframing themselves), but they do adapt rather than repeating the failed approach.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "We are checking the payment gateway connection from the server side now" ... "No ETA yet, will update ASAP" ... "Correcting the cert chain bundle order now, 2 mins ETA"

**Rationale:**
The participant provides some updates to Bez but they lack business framing. "We are checking the payment gateway connection from the server side" is technical, not business-oriented. They don't quantify impact in business terms (despite having the data — 90% order drop), don't provide a working theory in accessible language, and their updates are reactive to Bez's questions rather than proactive. The ETA commitment is vague ("ASAP") until the very end.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 1

**Evidence:**
> "here are some logs that daniel pulled, failure is at the connection layer" ... "can we restart the process?"

**Rationale:**
The participant rarely synthesizes the current state of understanding for the technical team. They relay information between NPCs ("here are some logs that daniel pulled") but don't post synthesis statements like "we've ruled out deploys and email maintenance, focus is now on PaymentService outbound TLS." The team receives questions and directives but not a coherent picture of what's known and unknown.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 1 |
| **Mean Marker Score** | **2.25** |

---

## Caveats
- L3 rating is a borderline 2/3 call. The participant does eventually make the ownership statement clearly, but it required multiple NPC prompts about who would need to take responsibility. Rated 3 because the statement itself is unambiguous.
- M5 is a borderline 2/3. The participant adapts by asking others for ideas rather than reframing the problem themselves, but they do move forward rather than repeating the failed restart.
- K4 at tier 1 reflects a complete absence of synthesis statements to the technical channel throughout the drill. The participant asks questions and relays information but never posts a "here's where we are" summary.

---