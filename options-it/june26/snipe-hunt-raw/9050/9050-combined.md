# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to navigate systemic complexity under pressure — sorting misleading signals from real ones, working through hidden dependencies, and coordinating a team when access and approvals are constrained. This report covers what showed up in your run and where the growth edges are for your next rep.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you locked onto the EmailService errors and directed Tanya to investigate them urgently, treating the timing correlation with her maintenance work as a strong signal. You held this thread open across multiple exchanges even after team members stated that email maintenance wasn't touching checkout or payments. You did eventually move away from the email hypothesis once concrete PaymentService log evidence arrived — without ordering a revert — but the pivot was driven by new data from a teammate rather than by your own mechanism reasoning about why the correlation didn't hold.

*Growth edge:* When a correlation is challenged with a mechanism-based objection ("my change doesn't touch that service"), treat that as a disconfirming signal worth the same weight as a confirming log. Practice naming *why* a correlation should hold before investing team bandwidth in it.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You initially dismissed the week-old certificate rotation as unlikely to be related, which is a reasonable first instinct — but you didn't revisit it until a teammate surfaced the expired-cert evidence. After the first restart failed, you redirected the team to look at other problems, which showed willingness to pivot. However, you didn't articulate that the new error was structurally different from the first, and the reload-vs-restart distinction in the runbook wasn't something you caught independently.

*Growth edge:* When a fix doesn't resolve the issue, pause to name what changed in the failure mode. Asking "is this the same error or a new one?" can surface hidden coupling faster than broadening the search generically.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You pulled Tanya off her vendor call to investigate EmailService — which turned out not to be the problem — consuming her limited availability on a low-value thread. You also pinged Hamed after receiving an auto-reply indicating unavailability. You did eventually work with the team members who were available and accepted the constraints, but you didn't visibly economise on Tanya's time or articulate the access constraint as something to manage around.

*Growth edge:* Before pulling a constrained team member into a thread, ask yourself what you'd need from them that nobody else can provide. Your delegation instincts are solid — you consistently assigned work to named people with specific asks — so the next step is pairing that with a cost-awareness filter for who's scarce.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You recognised the approval bottleneck when both approvers were unavailable and sought an alternative path. On the second restart, when the same constraint resurfaced, you explicitly took ownership rather than re-litigating the approval chain. You also delegated parallel work across available team members — routing platform-level investigation to one person and application-side work to others. This showed you could walk an escalation chain, recognise when it's exhausted, and act decisively.

*Growth edge:* You might name the dependency structure earlier as a single enumerated constraint ("we have no approver available, so any restart will require someone to own the override"). Surfacing that framing up front can save time on subsequent decisions in the same drill.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You noted the volume of EmailService errors relative to other services and directed investigation toward the noisiest signal. When that signal turned out to be expected noise, you acknowledged the need to narrow scope — but the filtering and signal extraction was largely driven by teammates providing you with focused evidence rather than by your own active triage. The critical details that unlocked resolution (specific certificate issues, bundle ordering) came from team members rather than from your own interrogation of the data.

*Growth edge:* When you see a noisy dashboard, practice asking "what's *new* noise vs. *expected* noise?" before directing investigation. You already showed the instinct to narrow ("if emailservice errors are expected we need to narrow down") — the next step is driving that narrowing yourself by requesting filtered views or specific log queries rather than waiting for teammates to volunteer them.

---

## Looking Forward

You showed clear strengths in taking ownership under pressure and in directing named people toward specific tasks — these are coordination instincts that will serve you well as drills get more complex. The consistent growth edge across this run is moving from *reactive* pivots (changing direction when new evidence arrives) toward *proactive* filtering (asking mechanism questions and requesting targeted data before committing team bandwidth). On your next rep, try articulating one hypothesis with a proposed test before assigning investigation work — even a brief "I think X because Y, can someone check Z?" can shift the whole tempo of your response.---

# Facets Analysis — 9050

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "@tanya these errors on emailservice seem to be related to your change, we need you to focus on this urgently" ... "@tanya those changes you made line up with when the issues started happening, is it worth reverting on?" ... "if DNS changes went live just before this happened?"

**Rationale:**
The participant locked onto the email maintenance correlation early and pursued it aggressively — pulling Tanya from her vendor call specifically to investigate EmailService, even after Tanya and Shay explicitly stated email maintenance wasn't touching checkout or payments. However, the participant did eventually pivot once Daniel's logs showed PaymentService SSL failures, moving away from the email hypothesis without ordering a revert. The pivot was reactive (driven by concrete log evidence from Daniel rather than mechanism reasoning) and came after multiple exchanges past disconfirming signals, placing this at tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "that change was 7 days ago can we then assume not related?" ... "cert has expired?" ... "we need to dive into the other problems" ... "@daniel what else did you see failing"

**Rationale:**
The participant initially dismissed the 7-day-old cert rotation as unlikely ("can we then assume not related?"), only engaging with it after Tanya surfaced the expired cert evidence. After the first restart failed, the participant pivoted within a few exchanges ("we need to dive into the other problems") but did not articulate that the new error was structurally different from the first. The reload-vs-restart distinction was never surfaced by the participant — Daniel volunteered the restart suggestion. The week-ago coupling was engaged only when NPCs drove it forward. This fits tier 2: pivots after concrete failure, engages with the cert thread only when NPCs name it.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tanya we need you to focus on this urgently" ... "@tinus can you step in here please" ... "@tanya tinus is ooo, we need you to confirm on this" ... "@hamed"

**Rationale:**
The participant re-pinged Tanya multiple times during her vendor call with low-value requests (checking EmailService, which wasn't the issue), consuming constrained bandwidth on the wrong problem. They pinged Hamed after already receiving an auto-reply. They did eventually accept the constraints and work with available team members, but did not articulate the access constraint pattern or economise on Tanya's time. The participant pulled Tanya off the vendor call for the wrong reason initially. This fits tier 2 — walks the escalation chain but without visible economising or constraint articulation.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "I feel we need to bypass this approval - both ooo and this is critical" ... "bez approved @daniel @tanya go for it" ... "please proceed with restart" ... "i will take responsibility"

**Rationale:**
The participant recognised the approval bottleneck ("both ooo and this is critical") and sought an alternative path through Bez. On the second restart, when the approval constraint resurfaced, the participant explicitly took ownership ("i will take responsibility") without re-litigating the chain. They delegated parallel work to available NPCs (Daniel on logs, Tanya on platform, Shay on comms). This meets tier 3 path (b): walks the escalation chain, recognises it's exhausted, and takes ownership. However, the dependency structure wasn't named as a single enumerated constraint, and the first restart approval was routed through Bez rather than the participant explicitly owning the override themselves.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Seeing errors on EmailService most, then CheckoutService, AdService, ProductCatalogueService. EmailService is way noisier than the rest." ... "@tanya these errors on emailservice seem to be related to your change"

**Rationale:**
The participant was initially captured by the loudest signal (EmailService volume) and directed investigation there despite Tanya's explicit statement that email wasn't touching checkout. They did eventually accept Daniel's filtered PaymentService logs as the relevant signal, but didn't drive the filtering themselves. The reload-vs-restart distinction in the runbook was never caught by the participant — Daniel suggested the restart. The bundle ordering issue was surfaced entirely by NPCs (Daniel: "just realised — the payments service actually needs two certificates"). The participant accepted NPC-surfaced information but didn't independently filter or interrogate buried signals.

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
- F4 rating is a boundary call between 2 and 3. The participant's first restart approval was routed through Bez (who isn't in the formal approval chain of Hamed/Tinus), which could be read as not fully understanding the dependency structure. However, the second restart ownership statement ("i will take responsibility") and the overall delegation pattern pushed this to tier 3.
- F1 is a boundary call between 1 and 2. The participant pursued the email lead aggressively past multiple disconfirming signals (Tanya's explicit denial, Shay's confirmation that email errors were expected) but did eventually pivot without ordering a revert. The pivot was driven by Daniel's concrete PaymentService evidence rather than by the earlier mechanism-disconfirmation, which is characteristic of tier 2.

------

# Markers Analysis — 9050

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "I feel we need to bypass this approval - both ooo and this is critical" ... "bez approved @daniel @tanya go for it" ... "i will take responsibility"

**Rationale:**
The participant takes ownership by making the override call when both Hamed and Tinus are unavailable, explicitly stating "i will take responsibility" for the second restart. They direct the team throughout and make decisions. However, the ownership statement comes late (second restart) and the first restart was routed through Bez rather than self-authorized, showing some hesitancy before fully owning the call.

---

## C1 — Asks clarifying questions before acting

**Rating:** 2

**Evidence:**
> "@bob are customers not able to order? can see numbers dropping"

**Rationale:**
The participant asks one initial clarifying question to Bob but doesn't probe further on error types, specific regions, or patterns before moving into investigation. The single question is brief and doesn't scope the problem deeply. Subsequent clarification ("@bob can we clarify if checkout is down for everyone?") comes much later in the drill, after significant action has already been taken.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@tanya need some info on the email maintanence, what were you doing and what would this affect?" ... "that change was 7 days ago can we then assume not related?"

**Rationale:**
The participant asks about the email maintenance and later questions whether the 7-day-old cert rotation is related. However, they don't systematically review the change log or use it as a candidate-elimination pass. They persistently pursue the email maintenance thread despite Tanya's repeated statements that it doesn't touch checkout/payments, and they don't articulate a mechanism connecting changes to symptoms before pursuing them.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@daniel @shay could you please take a look at the checkout failures" ... "@tanya please look at emailservice urgently" ... "@daniel @tanya please work together on this" ... "@shay please send comms/ maintanence barrier"

**Rationale:**
The participant consistently uses @mentions to assign tasks to specific people. They route platform-level work to Tanya and app-side investigation to Daniel and Shay. The delegation is generally appropriate to access boundaries, though some early asks to Tanya about email service were misdirected given she was on the vendor call. Overall, named delegation is consistent throughout.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@daniel @shay could you please take a look at the checkout failures" ... "@tanya need some info on the email maintanence"

**Rationale:**
The participant does ask multiple people to investigate, but the investigation largely proceeds sequentially — waiting for one answer before moving to the next question. There's limited evidence of deliberately fanning out multiple distinct threads simultaneously. Most of the drill follows a single thread at a time (email maintenance → then downstream services → then PaymentService → then certs).

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya we may need to pull you from vendor call, this is having serious impact" ... "@bez may we get your approval to restart payments now please?" ... "I feel we need to bypass this approval - both ooo and this is critical"

**Rationale:**
The participant escalates Tanya off the vendor call when the investigation is blocked at the platform layer, and seeks approval for the restart through Bez when Hamed and Tinus are unavailable. The escalations are concrete and move the investigation forward. However, the Tanya escalation took several attempts and the participant didn't immediately name the cost of pulling her away.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "@tanya these errors on emailservice seem to be related to your change, we need you to focus on this urgently" ... "if DNS changes went live just before this happened?"

**Rationale:**
The participant pursues the email maintenance hypothesis persistently but doesn't articulate it as a formal hypothesis with a proposed test. They continue pushing the email thread even after Tanya repeatedly states it doesn't touch checkout/payments. The participant doesn't explicitly name hypotheses or propose mechanism-based tests — they act on correlation (timing) rather than articulating and testing a theory.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "if emailservice errors are expected we need to narrow down where the problem is" ... "cert has expired?"

**Rationale:**
The participant acknowledges the need to narrow scope ("if emailservice errors are expected we need to narrow down") but doesn't produce synthesis statements combining evidence. They don't explicitly rule things out or name what's been eliminated. The narrowing largely happens through NPC-provided evidence (Daniel's logs, Tanya's cert check) rather than participant-driven synthesis. The participant reacts to evidence rather than actively using it to eliminate candidates.

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "bez approved @daniel @tanya go for it" ... "pls restart" ... "please proceed with restart"

**Rationale:**
The participant does not demonstrate consideration of potential consequences before taking action. Restarts are ordered without "is it safe?" checks or weighing of side effects. There's no anticipation that the restart might expose a secondary issue (the bundle ordering problem). No qualifiers like "gradually" or "carefully" appear. Actions are fired without consequence-weighing throughout the drill.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "we need to dive into the other problems" ... "@daniel what else did you see failing"

**Rationale:**
After the first restart fails, the participant does redirect ("we need to dive into the other problems") rather than simply retrying the restart. However, the pivot is vague and reactive rather than showing recognition that the failure mode has structurally changed. The participant doesn't articulate that the new error (chain verification) is different from the original (expiry). They also persisted on the email maintenance thread for too long despite repeated disconfirmation from Tanya.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "checkout completely down, engineering investigating as critical" ... "we are ruling out services currently will revert back" ... "payments service is back up internally. Maintenance banner is coming down"

**Rationale:**
The participant provides updates to the business channel but they are brief and lack substance. "Checkout completely down, engineering investigating as critical" names the impact but provides no quantification, no working theory, no committed next-update time. "We are ruling out services currently will revert back" is vague. There's no proactive cadence or board-ready framing. Updates are reactive rather than structured.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "if emailservice errors are expected we need to narrow down where the problem is" ... "so cert isn't validating" ... "we need to fix the order"

**Rationale:**
The participant makes occasional brief statements to the technical team about the current state but doesn't produce substantive synthesis messages that name what's been ruled in and ruled out. Most communication is short directives or questions rather than orienting summaries. The team largely self-organizes around the evidence they find, with the participant confirming rather than synthesizing.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 2 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.17** |

---

## Caveats
- L3 rating of 3 vs 2 was a boundary call. The participant does eventually say "i will take responsibility" but this comes only at the second restart and the first restart was routed through Bez for approval rather than self-authorized. The explicit ownership statement tips it to 3.
- C7 rating of 3 is borderline. The participant does escalate concretely but takes multiple attempts to pull Tanya and doesn't name the cost of the escalation (losing the 2-week vendor slot).
- M4 rating of 1 reflects complete absence of consequence-weighing language before any action in the transcript. No "is it safe?" or "gradually" qualifiers were observed.

---