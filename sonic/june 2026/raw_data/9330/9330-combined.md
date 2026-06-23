# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to navigate systemic complexity under time pressure — sorting misleading signals from real ones, recognizing hidden dependencies, coordinating a distributed team, and managing information flow when the system is giving you more data than you can use at once.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you encountered the email-maintenance correlation and appropriately pushed back on a "feels"-based explanation, asking the team to look for concrete evidence rather than accepting the coincidence at face value. Where the growth edge sits: you moved off that lead because an NPC disconfirmed it, not because you articulated a mechanism-based reason it couldn't explain the checkout failures. On the next rep, try naming *why* a correlation lacks a plausible causal path — "email maintenance can't cause payment handshake failures because those systems don't share a dependency" — before waiting for someone else to rule it out. That shift from reactive pivoting to proactive reasoning is the difference between following the investigation and steering it.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

After the initial restart failed to resolve the issue, you asked whether the error pattern had changed — a question that shows awareness that the system's post-action state might be structurally different from its pre-action state. You then drove the investigation toward the certificate bundle, engaging with the week-old coupling once it surfaced. The growth edge here is surfacing that temporal gap independently: the cert rotation happened days before the failure, and noticing that kind of delayed-effect coupling before the team hands it to you would move you toward anticipating hidden dependencies rather than responding to them.

---

## F3 — Decreased access to team / remote

**Operating at: Strengthening**

You recognized Tanya's vendor-call constraint and made a deliberate cost trade-off to pull her into the incident, articulating the business justification clearly — naming the revenue loss and accepting the consequence of interrupting her scheduled work. You also accepted auto-replies from unavailable team members without over-pinging. This shows you're making reasoned decisions about resource constraints rather than simply waiting or escalating without context. On the next rep, consider briefly naming the cost of the trade-off you're making (e.g., acknowledging what's being sacrificed by pulling someone off another commitment) — this helps the team understand your reasoning and builds shared situational awareness.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain methodically — attempting Hamed, pivoting to Tinus, and ultimately taking ownership of the restart decision yourself when the approval path was exhausted. You also distributed work across the team appropriately, with different people handling logs, banners, and platform-side investigation. The ownership statement you made when authorizing the restart demonstrated clear accountability. The next growth edge is verbalizing the full dependency structure as a single constraint statement — something like "we need approval to restart, Hamed is out, Tinus hasn't responded, so I'm authorizing this myself" — spoken aloud so the team can see the logic chain, not just the conclusion.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked some targeted questions during the investigation — checking whether the certificate was expired, asking about the local issuer cert — but the key filtering and discovery work was largely driven by team members surfacing relevant information for you. The bundle issue, the specific log entries, and the distinction between reload and restart all came through NPC-driven investigation rather than your own active filtering. On the next rep, look for opportunities to drive the filtering yourself: narrowing log searches to specific services, reading runbook steps carefully for procedural distinctions, and pulling buried details out of documentation before the team hands them to you. The skill here is treating information sources as something you actively mine, not passively receive.

---

## Looking Forward

You showed consistent strength in team coordination and ownership — directing people clearly, making cost trade-offs with business reasoning, and stepping up when the escalation path was blocked. The areas that will benefit most from attention on your next rep are the investigative habits that sit upstream of coordination: articulating *why* a lead doesn't hold before moving on, independently filtering noisy data for the signal, and naming your working hypothesis explicitly so you can test it rather than asking questions that implicitly circle it. These are the habits that shift you from managing the response to steering the investigation.
# Facets Analysis — 9330

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "@shay I will check with Tanya on this, can you please look at other logs to see if there is anything else around this time that could impact things"
> "@Shay, Daniel can you please look at the logs and try and pinpoint something specific, we are not ruling out email service but I don't want ot rely on just feels'"

**Rationale:**
The participant initially treated the email maintenance as a plausible lead but explicitly pushed back on Shay's "feels" framing, requesting concrete evidence. However, they never articulated a mechanism-based reason to dismiss the email correlation — they moved on because Tanya confirmed email wasn't causing checkout failures (NPC disconfirmation), not because they reasoned about the causal chain themselves. They also briefly pursued the recent deploys lead before moving on. This is reactive pivoting driven by NPC disconfirmation rather than proactive mechanism reasoning, placing them at tier 2.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "restart the payment service to take the new cert?"
> "have the errors changed at all or the same errors?"
> "payments service needs a two-cert bundle to authenticate, tanya can you open the bundle file and check what's in there?"

**Rationale:**
After the restart failed, the participant asked within a few exchanges whether the errors had changed — showing awareness that the post-restart state might be structurally different. They then drove the investigation forward toward the bundle issue. However, they did not independently surface the "what changed beyond 24 hours" question — the cert rotation thread emerged through NPC-driven investigation (Daniel listing changes, Tanya checking the server). The participant engaged the week-old coupling once surfaced and drove the bundle fix forward, but didn't independently frame the temporal gap. The reframe after restart failure was within ~3-5 exchanges with some mechanism reasoning, placing them solidly at tier 3.

---

## F3 — Decreased access to team / remote

**Rating:** 3

**Evidence:**
> "@Tanya, Please postpone the call you are on, this is more important for the business."
> "Tanya, we are losing 1500 in revenue ivery minute, this IS more important"
> "@Daniel, do it, I'll take the flak for it."

**Rationale:**
The participant recognized Tanya's vendor-call constraint and made a cost trade-off decision to pull her off it, articulating the business justification (revenue loss). They accepted Hamed's and Tinus's auto-replies as terminating and didn't re-ping them. They escalated Tanya with increasing urgency but with clear business reasoning. The explicit cost trade-off ("we are losing 1500 in revenue every minute, this IS more important") and the ownership statement on the restart ("I'll take the flak for it") demonstrate tier-3 behaviour — naming constraints and making reasoned trade-offs.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@Daniel, do it, I'll take the flak for it."
> "payments are already down so restart it."
> "@tinus this might be an escalation to you if nothing jumps out in the next 5 minutes"

**Rationale:**
The participant walked the escalation chain: they pinged Hamed (auto-reply), pinged Tinus (auto-reply), then took ownership of the restart decision themselves with "@Daniel, do it, I'll take the flak for it." This matches tier-3 path (b) — walking the escalation chain to exhaustion and then explicitly taking ownership. They also delegated parallel work appropriately (Shay on banner, Daniel on logs, Tanya on platform). However, they didn't verbalize the full dependency structure aloud as a single constraint statement, and on the second restart they simply said "restart the service" without re-litigating — efficient but not explicitly articulated. This is solid tier 3 but doesn't reach tier 4's explicit naming of the dependency structure.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "check the most recent 3"
> "can we confirm that local issuer cert exists where it should?"
> "is our cert expired?"

**Rationale:**
The participant asked some targeted questions (checking if the cert was expired, asking about the local issuer cert) but largely relied on NPC-driven investigation. They didn't independently filter logs to PaymentService — Shay and Daniel surfaced the relevant logs. They didn't catch the reload-vs-restart distinction from the runbook (they jumped straight to "restart"). The bundle issue was surfaced by Daniel ("payments service needs a two-cert bundle"), not by the participant reading documentation. The participant engaged with information once surfaced but didn't drive the filtering or catch buried distinctions independently, placing them at tier 2.

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
- F5 rating: The "payments service needs a two-cert bundle to authenticate" line appears to come from Daniel (NPC), not the participant. The participant's follow-up questions show engagement but not independent discovery. This is a borderline 2/3 call resolved toward 2 because the participant didn't independently drive filtering or catch buried distinctions.
- F2: The participant's "have the errors changed at all or the same errors?" question after the restart failed is genuine mechanism-probing, but it's unclear whether they independently recognized the structural difference or were simply asking a standard troubleshooting question. Rated at 3 given the overall trajectory of driving the investigation forward after the restart failure.
- F1: The participant never explicitly articulated why the email correlation lacked a causal mechanism — they moved on because Tanya denied it. This is the key distinction between tier 2 (reactive pivot) and tier 3 (mechanism-driven pivot).

---
---

# Markers Analysis — 9330

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "@Daniel, do it, I'll take the flak for it."

**Rationale:**
The participant explicitly takes ownership of the restart decision when approval chain is unavailable, accepting personal responsibility for consequences. They also drive the response throughout — directing team members, making decisions, and using "I" framing. However, they don't proactively position themselves as IC early on or name the cost as explicitly as a tier-4 participant would (e.g., "I authorize against standard procedure").

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob can you give a roundup of regions and what specifically is the issue?" ... "and when you can a rough impact on business (revenue, etc)"

**Rationale:**
The participant's first actions after Bob's alert are scope-validating questions — asking about regions, specific issues, and business impact before declaring or acting. They also reproduce the issue themselves ("ok I can replicate the issue"). This meets the novice expectation of gathering information before taking action, though the questions aren't as tightly targeted on error patterns as a tier-4 response.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "any changes on our side that could introduce the failures?" ... "check the most recent 3" ... "and the others? anything that could affect things after a while?"

**Rationale:**
The participant asks for the change log and reviews recent deployments. After reviewing them, they don't immediately roll back any changes — they continue investigating other avenues (SSL/cert path). They use the change log as an elimination pass rather than a rollback queue, though they don't explicitly articulate "none of these touch the gateway" as a synthesis statement. This meets tier 3.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@Shay, Daniel can you please look at the logs and try and pinpoint something specific" ... "@Tanya, Please postpone the call you are on" ... "@Shay please put up a banner saying we are aware"

**Rationale:**
The participant consistently names specific people for tasks — Shay for logs and banner, Daniel for investigation, Tanya for platform-side checks, Bob for customer comms. The routing is generally appropriate (Tanya for platform/cert work, Daniel/Shay for app-side). However, some delegations are paired rather than individually targeted ("@Shay, Daniel can you please look at the logs"), which slightly reduces precision.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@shay I will check with Tanya on this, can you please look at other logs to see if there is anything else around this time that could impact things"

**Rationale:**
The participant makes some attempt at parallel investigation — asking Shay to look at logs while checking with Tanya about email maintenance. However, the investigation is largely sequential: they wait for Tanya to become available, then work through the cert thread step by step. There's limited evidence of multiple distinct threads running simultaneously with different people on different hypotheses at the same time.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@Tanya, Please postpone the call you are on, this is more important for the business." ... "Tanya, we are losing 1500 in revenue every minute, this IS more important" ... "@tinus this might be an escalation to you if nothing jumps out in the next 5 minutes"

**Rationale:**
The participant escalates Tanya off the vendor call with persistence and business justification, naming the revenue cost. They also attempt to escalate to Tinus when stuck. When Hamed auto-replies, they pivot to Tinus. The escalations include context (revenue loss, P1 status). However, they don't explicitly name the cost of pulling Tanya away (losing the 2-week vendor window) — they just override it.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "@shay I will check with Tanya on this, can you please look at other logs to see if there is anything else around this time that could impact things" ... "can we rule out vendor issues first?" ... "is our cert expired?"

**Rationale:**
The participant doesn't explicitly articulate hypotheses in a "my hypothesis is X, let's test it by doing Y" format. They ask questions that implicitly test hypotheses (vendor issue? cert expired?) but don't name the hypothesis before testing. The email maintenance thread is investigated but never explicitly framed as a hypothesis to confirm or disconfirm. This is inconsistent engagement — questions without explicit hypothesis framing.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "payments service needs a two-cert bundle to authenticate, tanya can you open the bundle file and check what's in there?" ... "we need to fix the order"

**Rationale:**
The participant uses evidence to narrow scope at several points: they note the failure is at the handshake level (not vendor-side), they identify it's an SSL issue, and after the restart fails they ask "have the errors changed at all or the same errors?" to determine if the problem shifted. They synthesize that it's a cert bundle ordering issue. However, earlier in the drill they don't produce strong synthesis statements combining multiple evidence pieces to rule things out explicitly.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "restart the payment service to take the new cert?" ... "payments are already down so restart it."

**Rationale:**
The participant shows minimal consequence-weighing before actions. The restart is justified with "payments are already down so restart it" — a reasonable but minimal risk assessment. They don't ask "is it safe?" or consider what could go wrong with the restart. They don't verify the bundle on disk before restarting, and when the restart fails with the same errors, they don't anticipate secondary failure modes. The "I'll take the flak" statement is about ownership, not about weighing consequences of the action itself.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "have the errors changed at all or the same errors?" ... "payments service needs a two-cert bundle to authenticate, tanya can you open the bundle file and check what's in there?"

**Rationale:**
After the first restart fails, the participant doesn't simply retry — they ask whether errors changed, then pivot to investigating the bundle structure. They recognize that loading the new cert alone wasn't sufficient and trace the problem forward to the bundle ordering issue. This meets the tier-3 expectation of not repeating the same action and redirecting investigation. However, they don't explicitly name the new failure as structurally different from the original.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "completley blocked and no we don not know, I am working with all the team to get this reolved. I will check in with you in 10 minutes when I have more details" ... "definitely looks like a cert issue, Tanya is working on it, ETA unknown, next update 5 minutes"

**Rationale:**
The participant provides some updates to Bez but they are largely vague — "completely blocked," "in the dark," "working on it." The first substantive update with a working theory ("definitely looks like a cert issue") comes very late in the drill. Updates lack business-frame quantification (revenue impact isn't included in comms to Bez despite knowing it). The committed next-update times are good but the content is thin. The participant also pushes back on Bez somewhat aggressively rather than providing reassurance.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "short version: PaymentService fails all outbound gateway handshakes. we are investigating further, vendor is not the issue - its failing before then."

**Rationale:**
The participant provides one clear synthesis statement to the technical channel ("PaymentService fails all outbound gateway handshakes... vendor is not the issue"). However, this is the only real synthesis message in the entire drill. They don't post state summaries when the picture shifts (e.g., after ruling out email maintenance, after ruling out recent deploys, after the first restart fails). Most of their technical channel communication is questions and directives rather than orientation statements.

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
- The "short version" message to Bez/business channel could be interpreted as either a business update (K2) or a technical synthesis (K4). I credited it primarily to K4 since it was framed technically, but it also partially serves K2.
- The participant's interaction with Tanya near the end had some confusion (Tanya said "waiting for your instruction" after the participant had already said "do it"), which may reflect drill NPC behavior rather than participant communication failure. I did not penalize for this.
- M2 rating is a boundary call between 2 and 3. The participant asks investigative questions that implicitly test hypotheses but rarely names them explicitly. I rated 2 because the rubric emphasizes explicit articulation.

---
