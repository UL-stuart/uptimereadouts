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