# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident with systemic complexity: misleading signals, constrained team availability, layered technical dependencies, and a volume of information that required active filtering. The observations below reflect how you navigated that complexity across five dimensions the drill is designed to surface.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you kept the email maintenance thread alive as a possible cause even after a teammate explicitly stated it couldn't be responsible for checkout failures. Your eventual pivot away from it was driven by concrete log evidence pointing to the payment gateway rather than by reasoning through *why* the correlation couldn't hold mechanistically. On your next rep, notice when a teammate offers a clear elimination statement — that's a cue to close the thread and redirect attention rather than holding it open as background noise. Building the habit of asking "what mechanism would connect these?" can help you shed distractors faster.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the certificate rotation thread surfaced, you engaged productively — asking to review the playbook steps, checking whether the service had been restarted, and then reframing the problem after the restart failed. You recognized that the issue shifted from "expired cert" to "bundle ordering," which is a meaningful conceptual pivot. The growth edge here is surfacing the deeper-time question yourself: the cert rotation happened a week earlier, and the "what changed beyond the obvious window" question came from teammates rather than from you. On the next rep, try explicitly asking what changed in the days *before* the incident window — not just the hours.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You handled constrained availability well. You accepted auto-replies without stalling, pulled a teammate off a vendor call with a clear priority statement, and eventually took ownership of the restart authorization when the approval chain was exhausted. You also directed that teammate to specific tasks once she was available, economizing on her time. The next growth edge is articulating the trade-off explicitly when you make a priority call — naming what you're pulling someone away from and why the current situation outweighs it. That reasoning, stated aloud, helps the team trust the call and reduces friction.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain in a visible, deliberate order and ultimately self-authorized the restart when the chain was exhausted. You also delegated parallel work appropriately — routing platform-level investigation to the right person and app-side checks to others. On the second restart attempt, you authorized without re-litigating the approval chain, which shows growing fluency with the dependency structure. The growth edge is naming the constraint *before* you hit it: stating something like "we need senior approval for a restart, and our two approvers are currently unavailable — here's how I'm going to handle that" as a single framing statement rather than discovering it step by step.

---

## F5 — Data overload / buried information

**Operating at: Strengthening**

You asked targeted questions about the playbook (reload vs. restart), directed investigation to the payment service once logs pointed there, and engaged with the bundle concept after the restart failed. You integrated information across multiple teammates — connecting certificate output, the bundle ordering suggestion, and the verification failure. The growth edge is driving the filtering yourself rather than waiting for teammates to surface the key signal. On the next rep, try actively reasoning about what's *absent* from the data — what you'd expect to see if a hypothesis were true — as a way to narrow scope before someone else does it for you.

---

## Looking Ahead

Across this drill, you showed consistent ability to engage with complexity once it was surfaced — following threads, reframing when evidence shifted, and managing coordination constraints. The pattern to carry into your next rep is moving from *reactive engagement* to *proactive framing*: closing dead-end hypotheses on mechanism rather than waiting for contradicting evidence, naming constraints and trade-offs aloud before they become blockers, and asking the "what's missing" question before a teammate hands you the answer. You have the coordination and synthesis instincts — the next step is exercising them earlier in the timeline.
# Facets Analysis — 9142

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "The email maintenance started right when checkout issues began. Still feels worth keeping an eye on — that timing hasn't gone away." ... "We haven't officially ruled out the email maintenance yet. Still an open thread."

**Rationale:**
The participant initially accepted the email maintenance correlation as a live hypothesis. Tanya explicitly stated "this maintenance can't be causing checkout failures" early on, yet the participant (via Shay's framing) kept the email thread open. However, the participant did pivot reactively once logs showed PaymentService outbound gateway failures, moving investigation to the platform/cert layer without ordering an email rollback. The pivot was driven by concrete log evidence rather than mechanism reasoning about why email couldn't cause checkout failures, placing this at tier 2.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "yes, I handled that rotation. I followed the playbook in this activity doc" ... "not sure why the process isn't picking up the new certificate" ... "I see from error logs that there are 2 types of bundles - When we restart, are we sure we checked the right bundles are loaded"

**Rationale:**
The participant engaged with the week-old cert rotation thread once Daniel surfaced it, asking to review the playbook steps and whether the service was restarted. After the restart failed, the participant recognized within a few exchanges that the problem was structurally different — shifting from "expired cert" to "bundle order" — referencing the earlier suggestion about bundle ordering. The participant didn't independently surface the "what changed beyond 24 hours" question (Daniel/Shay raised it), but drove the investigation forward once the cert thread was active and reframed after the restart failure within approximately 3-5 exchanges, consistent with tier 3.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@tanya I need you here now. This is more important." ... "No other approvers are available" ... "I am authorizing a restart of the Payment System."

**Rationale:**
The participant recognized access constraints: accepted Hamed's auto-reply and moved to Tinus, accepted Tinus's auto-reply, then pulled Tanya off the vendor call with a clear priority statement. The participant economized on Tanya's time by directing her to specific tasks. The participant eventually took ownership of the restart authorization after exhausting the approval chain. However, the participant did ping Tanya multiple times while she was on the vendor call before making the priority call, and didn't explicitly articulate the cost trade-off verbally when pulling her off ("this is more important" is brief rather than reasoned). This places the participant solidly at tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "Okay, we need @tinus to sign off on a restart of the Payments service then - Hamed is completely unavailable." ... "I am authorizing a restart of the Payment System. @tanya let's restart Payments."

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), then explicitly took ownership and issued the authorization as a distinct message. This matches tier-3 path (b). The participant also delegated parallel work appropriately (Daniel on logs, Shay on investigation, Tanya on platform). On the second restart (after bundle fix), the participant authorized without re-litigating the approval chain, which is a tier-4 signal. However, the participant didn't name the dependency structure aloud as a single constraint statement before the chain was exhausted, keeping this at tier 3 rather than 4.

---

## F5 — Data overload / buried information

**Rating:** 3

**Evidence:**
> "Let's review the playbook steps - did the new certificate get installed? Did the payment service get restarted?" ... "I see from error logs that there are 2 types of bundles - When we restart, are we sure we checked the right bundles are loaded as suggested by @Joe?"

**Rationale:**
The participant asked targeted questions about the playbook (reload vs. restart distinction), directed investigation to PaymentService specifically once logs pointed there, and engaged with the bundle concept after the restart failed. The participant integrated information across NPC channels — connecting Tanya's cert output, the earlier bundle ordering suggestion, and the verification failure. However, the participant didn't independently drive the filtering to PaymentService (Shay/Daniel surfaced it) and didn't reason about absence of signal proactively. The participant caught key distinctions in referenced docs when directed, consistent with tier 3.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 3 |
| **Mean Facet Score** | **2.80** |

---

## Caveats
- F2 tier-3 vs tier-4 was a boundary call. The participant reframed after the restart failure within a reasonable window and engaged with the bundle concept, but the "what changed beyond 24 hours" question was NPC-surfaced rather than participant-driven, which is the key differentiator keeping this at tier 3.
- F4 tier-3 vs tier-4 was also a boundary call. The second restart authorization without re-litigating is a tier-4 signal, but the absence of an explicit dependency-structure statement before the chain was exhausted keeps this at tier 3.
- Some NPC messages (particularly Shay's) appear to echo or reinforce the email prime, making it difficult to distinguish participant framing from NPC framing in the early stages of F1.

---


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
