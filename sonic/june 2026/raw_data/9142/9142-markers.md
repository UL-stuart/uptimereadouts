

# Markers Analysis — 9142

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "I am authorizing a restart of the Payment System. @tanya let's restart Payments."

**Rationale:**
The participant takes explicit ownership at the critical approval-override moment, authorizing the restart when both Hamed and Tinus are unavailable. They also direct the response throughout (declaring the incident, setting update cadence with Bez, delegating tasks). However, they don't explicitly name the cost/blowback of the override decision, which would elevate to tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob is there any pattern to the complaints? are they global or regional?" ... "@bob can you give me an example of what is wrong?"

**Rationale:**
The participant's first two actions after Bob's alert are clarifying questions — asking about geographic pattern and the nature of the failure. They gather scope information before declaring the incident or taking remediation action. This meets the tier 3 expectation of scope-validating before acting, though the questions are somewhat basic rather than deeply probing (e.g., didn't ask about error types, payment methods, or volume).

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "@daniel can you pull up the most recent changes to the checkout service?" ... "Increasing the payment timeout shouldn't have make it worse - not sure about the feature flags."

**Rationale:**
The participant asks Daniel for recent changes and reviews them. They reason about whether the timeout bump could be causal ("shouldn't have made it worse") and engage with the feature flag cleanup. They use the change log as part of their investigation rather than immediately rolling back. However, they don't explicitly frame the absence of PaymentService changes as elimination evidence — that insight comes from Daniel/Shay rather than the participant synthesizing it.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@daniel @shay I need you both to jump in - we need to figure out why payments are broken." ... "@tanya I need you to look at our outbound payment gateway."

**Rationale:**
The participant consistently uses @mentions to delegate to specific people. They route platform-level work to Tanya and app-side checks to Daniel and Shay. The initial delegation to Daniel and Hamed is slightly off (Hamed is unavailable), but they quickly adjust. Tasks are named but sometimes broad ("figure out why payments are broken") rather than precisely scoped.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@daniel @hamed I need you to start looking at the payment system" ... "@tanya I need your help - payments system is broken."

**Rationale:**
The participant attempts to engage multiple people early, but the investigation largely proceeds sequentially — they wait for Tanya's response, then wait for Daniel's logs, then wait for the cert check. There's limited evidence of distinct parallel threads running simultaneously with different hypotheses. Most of the investigation follows a single thread at a time rather than fanning out multiple concurrent lines of inquiry.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya I need you here now. This is more imporant." ... "@tinus you here? Hamed is out and Tanya is dealing with a vendor. We need a platform expert now."

**Rationale:**
The participant escalates effectively when blocked. They pull Tanya off the vendor call when the investigation requires platform expertise, and they work through the approval chain (Hamed → Tinus → self-authorization) when the restart is blocked. They don't leave the chain hanging. However, they don't explicitly name the cost of pulling Tanya off the vendor call (the 2-week window loss), which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 3

**Evidence:**
> "Increasing the payment timeout shouldn't have make it worse - not sure about the feature flags." ... "Let's review the playbook steps - did the new certificate get installed? Did the payment service get restarted?"

**Rationale:**
The participant engages with hypotheses — they consider the timeout change, feature flags, and then focus on the certificate rotation as the likely cause. They propose tests (reviewing the playbook steps, checking the bundle order). They pivot when the first restart doesn't work. However, hypotheses are somewhat implicit rather than explicitly stated and named, which keeps this at tier 3 rather than 4.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "We've narrowed down issues to failures in the outbound payments gateway - still investigating other causes while are working on fixing that issue."

**Rationale:**
The participant synthesizes evidence to narrow scope — from "payments broken" to "outbound gateway handshake failure" to "certificate issue." They use Daniel's log findings to rule out app-side issues and focus on the platform/TLS layer. They communicate this narrowing to Bez. However, the narrowing is largely driven by NPC findings rather than the participant actively synthesizing multiple data points themselves.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "Is there anything special involved with the sign-off of restarting the payment service, or do we just need senior approval?"

**Rationale:**
The participant shows some awareness of consequences by asking about the restart process requirements. However, they don't explicitly weigh the cost of pulling Tanya off the vendor call, don't ask "is it safe?" before the restart, and don't anticipate that the restart could expose a secondary issue (the bundle ordering problem). The consequence consideration is minimal and reactive rather than proactive.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "What are the errors looking like on payments now? Did anything change?" ... "I see from error logs that there are 2 types of bundles - When we restart, are we sure we checked the right bundles are loaded"

**Rationale:**
When the first restart fails, the participant doesn't simply retry it. They ask what the new errors look like, recognize the bundle issue as a distinct problem from the expired cert, and redirect the investigation toward the bundle ordering. They adapt their approach based on the new evidence. However, the pivot is somewhat guided by NPCs (Shay's "two certificates needed — it's a bundle") rather than being fully self-driven.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 3

**Evidence:**
> "@bez this is impacting all regions. No one can make payments. I am bringing in the whole team and will be posting updates every 5 minutes." ... "This is on our side - issue with certificate for the Payment Service. Working on fix now."

**Rationale:**
The participant provides substantive updates to Bez — naming the scope (all regions, no payments), committing to a cadence (every 5 minutes), and later identifying the cause (certificate issue) and confirming it's on their side. They update through the secondary failure. However, they don't quantify revenue impact or provide precise ETAs, and some updates are somewhat thin ("We have not found the cause yet").

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 3

**Evidence:**
> "We've narrowed down issues to failures in the outbound payments gateway - still investigating other causes while are working on fixing that issue." ... "As mentioned in Tanya's message above- we have to restart with both bundles loaded- Payments need 2 certificate updates"

**Rationale:**
The participant posts synthesis statements to the technical channel at key decision points — narrowing to the outbound gateway, identifying the certificate issue, and directing the bundle fix. They communicate what's been found and what the next step is. However, they don't explicitly name what's been ruled out (e.g., "not deploys, not email maintenance") in a single synthesis message for the team.

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
| K2 — Provides substantive updates to business stakeholders | 3 |
| K4 — Communicates issue scope clearly to the technical team | 3 |
| **Mean Marker Score** | **2.83** |

---

## Caveats
- The participant's bundle-check request ("@tanya can you please check the bundle carefully one more time") before the restart shows some awareness of potential issues, but it's ambiguous whether this reflects consequence-anticipation (M4) or simply thoroughness. I rated M4 conservatively at 2 because the participant never explicitly articulates what could go wrong.
- For M5, the participant's recognition of the bundle issue is partially self-driven ("I see from error logs that there are 2 types of bundles") and partially NPC-driven. I gave tier 3 because they do redirect the investigation rather than retrying the same action.
- C6 is a borderline 2/3 call. The participant engages multiple people but the investigation proceeds largely sequentially. I rated 2 because there's limited evidence of truly concurrent distinct threads.

---