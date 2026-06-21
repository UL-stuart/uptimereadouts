---

# Markers Analysis — 9311

## L3 — Takes explicit ownership of the response

**Rating:** 2

**Evidence:**
> "Let me create a incident" / "i approve" / "pease go ahead"

**Rationale:**
The participant creates the incident and eventually approves the restart, but does so only after being prompted by Tanya asking "Do you want me to go ahead?" The participant never explicitly positions themselves as the decision-maker driving the response — they react to NPC prompts rather than proactively owning the call. The "i approve" is late and lacks any framing of cost or accountability.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "How many customers are blocked from checkout right now? What's the revenue loss per minute? Is this a total outage or partial?"

**Rationale:**
The participant asks scope-validating questions early — about the number of affected customers, revenue impact, and whether it's total or partial. They also reproduce the error themselves ("Yes i can validate and see the error in checkout"). These questions come before major remediation actions, meeting the novice expectation for this marker.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@daniel @shay @tanya - Can you please look into this and look for changes in the system"

**Rationale:**
The participant asks for recent changes early and receives the change log. However, they then order rollbacks of CheckoutService changes, Shipping, and CartService without articulating a mechanism connecting those changes to the symptom. They asked the question but used the answers as a rollback queue rather than a candidate-elimination pass, fitting the tier 2 description.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "@daniel @shay @tanya - Can you please look into this and look for changes in the system" / "@tanya - can you please verify the steps you have followed"

**Rationale:**
The participant uses @mentions frequently but often broadcasts to multiple people simultaneously without distinct tasks ("look into this"). Many delegations to Tanya are repetitive requests for the same information (runbook steps, changes made). The participant rarely routes tasks based on NPC access boundaries — repeatedly asking Tanya for application-level information rather than leveraging Daniel for app-side and Tanya for platform-side work.

---

## C6 — Runs parallel investigation threads

**Rating:** 1

**Evidence:**
> Repeated sequential questions to @tanya about the same topics (runbook, changes, Redis pool) without concurrent threads to other team members.

**Rationale:**
The participant works almost entirely sequentially, spending the majority of the drill asking Tanya the same questions repeatedly. There is no evidence of multiple distinct investigation threads running concurrently — Daniel and Shay are largely idle until Daniel eventually surfaces the payment logs. The participant does not fan out distinct tasks to different people in parallel.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "@hamed - can you please help here" / Then after Hamed's auto-reply, no follow-up to Tinus or alternative escalation path.

**Rationale:**
The participant pings Hamed but receives an auto-reply directing them to Tinus for approvals. The participant does not follow up with Tinus or articulate a Plan B. Later, when Tanya says she can't restart without approval, the participant simply says "i approve" without naming authority or cost. The escalation lacks context and follow-through.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Can you pleas eupdate" / "Can you please rollback those changes @tanya" / repeated requests for Tanya's runbook steps without articulating why.

**Rationale:**
The participant never explicitly articulates a hypothesis. They order rollbacks (CheckoutService, Shipping, CartService) without stating what they believe is causing the issue or how the rollback would test that belief. The closest to hypothesis-testing is the implicit assumption that recent changes caused the issue, but this is never stated or tested on mechanism. Actions are taken without linked reasoning.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "@bob - this is the global issue right?" / "yes its isolated to checkout only"

**Rationale:**
The participant confirms the issue is global and isolated to checkout, which provides some narrowing. However, after rollbacks fail, the participant does not synthesize the negative results to narrow scope further. They spend extensive time re-asking Tanya about changes already confirmed as unrelated. The eventual narrowing to PaymentService outbound happens largely through Daniel's initiative, not the participant's synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "Can you please rollback those changes @tanya" / "do the restart" / "pease go ahead"

**Rationale:**
The participant orders rollbacks and restarts without any "is it safe?" checks or consideration of side effects. When pulling Tanya off the vendor call, there's no acknowledgment of the 2-week cost. The restart is ordered without verifying the bundle state first. No evidence of consequence-weighing before any action throughout the drill.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> After multiple failed rollbacks, the participant eventually asks "ok, @shay @daniel - any more suggestions?" and agrees to deep-dive into the specific downstream service.

**Rationale:**
The participant does eventually shift away from rollbacks, but only after multiple failures and largely at the NPCs' suggestion ("Want us to deep dive into that service specifically?"). The pivot is reactive rather than proactive — the participant asks the team for suggestions rather than synthesizing the failed rollbacks into a new direction themselves. This is inconsistent adaptation driven by NPC nudging, fitting tier 2.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "@bez - its a global outage and revenue is £1000/min" / "not yet, we are tried to rollback changes we have deployed" / "We are woking on this Bez. Looking at the changes today"

**Rationale:**
The participant provides some quantification (revenue loss) early on, which is positive. However, subsequent updates to Bez are vague ("we are working on this," "not yet") without a working theory, next-update commitment, or concrete ETA. The updates lack the substance expected at tier 3 — no current hypothesis, no committed timeline, no structured business framing.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 1

**Evidence:**
> No synthesis statements to the technical channel summarizing what's been ruled out or what the current working picture is.

**Rationale:**
The participant never posts a synthesis message to the team summarizing the state of the investigation. They ask individual questions but never consolidate findings ("rollbacks didn't help, so it's not recent deploys; focus on X"). The team receives no orientation from the participant about what's been eliminated or what the current focus should be. Daniel and Shay eventually self-direct to the payment logs without IC guidance.

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
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 1 |
| **Mean Marker Score** | **1.83** |

---

## Caveats
- The participant's repeated requests to Tanya for the same runbook information (asked 5+ times) consumed significant drill time and made it difficult to assess whether the participant had a mental model they were testing or was simply stuck in a loop. I rated M2 conservatively at 2 rather than 1 because the rollback actions do imply an implicit (if unarticulated) hypothesis.
- The participant did reach resolution (cert bundle fix + restart), but per anti-outcome-bias instructions, this outcome did not influence ratings. The resolution was largely driven by NPC initiative (Daniel surfacing payment logs, Shay identifying the bundle order issue).
- C7 is a borderline 1/2 — the participant did ping Hamed, which is more than zero escalation effort, but the lack of follow-through to Tinus and the absence of context in the escalation keeps it at 2.

---