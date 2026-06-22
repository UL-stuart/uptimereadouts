# Post-Drill Developmental Report

This drill placed you in a live incident requiring you to navigate misleading signals, trace hidden system dependencies, coordinate a partially-available team, and manage approval bottlenecks — all while filtering noisy technical data under time pressure. The observations below reflect where your process landed on each of these dimensions and where the next-rep growth edges sit.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you showed solid instincts by flagging that you didn't want to jump to conclusions and expressing skepticism about the email maintenance coincidence. However, after a teammate explicitly stated that email maintenance had no overlap with checkout or payments, you still asked her to investigate the connection further — treating it as "our only lead." You eventually moved on, but the pivot came in response to repeated disconfirmation rather than from your own reasoning about *why* email couldn't plausibly break checkout.

*Growth edge:* When you notice a coincident factor, practice articulating the mechanism — "how would X cause Y?" — before assigning investigation effort. If you can't name a plausible path, that's your signal to deprioritise it without waiting for someone else to rule it out.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

You engaged meaningfully with the week-old certificate rotation as a potential cause, noting the suspicious seven-day timing and questioning whether the rotation had actually completed correctly. When the initial restart didn't resolve the issue, you didn't repeat the same action or blame downstream services — you asked for fresh logs and pushed the team to dig deeper into the SSL setup. You connected the timing of the rotation to the current failure and continued tracing forward after the first fix attempt failed.

*Growth edge:* You recognised the structural difference in the new error once the team surfaced it, but you didn't independently catch the reload-vs-restart distinction from available documentation. On the next rep, look for procedural details in runbooks or activity logs that might explain *how* a change propagates — not just *whether* it happened.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You made a reasoned cost trade-off when pulling a teammate off a vendor call, articulating the business justification clearly. When key approvers were unavailable, you moved through the escalation chain and eventually accepted the constraint rather than stalling. Your delegation routing was generally appropriate — assigning platform-side investigation to the right person and log checks to the application-side engineer.

*Growth edge:* After receiving auto-replies, you still pinged additional unavailable people rather than immediately adapting your plan. On the next rep, treat the first auto-reply as a signal to shift strategy rather than continuing down the same escalation path.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the approval chain to exhaustion — trying each available approver in sequence — and ultimately took explicit personal ownership of the restart decision, accepting responsibility for consequences. You also delegated parallel work appropriately across the team. The path to ownership was somewhat messy, requiring multiple exchanges before you cleanly stated you'd take responsibility, but the final ownership statement was unambiguous.

*Growth edge:* The moment you recognise the approval chain is exhausted, move directly to an ownership statement rather than attempting workarounds. Faster, cleaner ownership reduces coordination drag and signals decisiveness to the team.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked for filtered logs and engaged with the certificate rotation as a lead, which shows awareness that you needed to narrow the data. However, you relied heavily on teammates to interpret technical evidence — asking what SSL verification failures meant and what the certificate bundle issue was — rather than driving the filtering yourself. Key distinctions (like bundle ordering and chain verification) were surfaced entirely by others.

*Growth edge:* When you encounter unfamiliar technical territory, try to extract the *structural* question even if you can't answer it yourself. Instead of "what does this mean?", try "is this the same failure mode as before, or structurally different?" — this keeps you in the driver's seat on narrowing scope even when you need others for domain expertise. You did this once (asking if the error was the same handshake failure), and that's the pattern to repeat more consistently.

---

## Looking Forward

Two patterns stand out as high-leverage for your next rep. First, practise articulating mechanism reasoning out loud — "how would X cause Y?" — before committing investigation effort to coincident signals. Second, when you're relying on teammates for technical interpretation, frame your questions to keep the narrowing logic in your hands rather than delegating the entire sense-making step. Both of these build on instincts you already showed in this drill; the work is making them more consistent and self-initiated.---

# Facets Analysis — 8902

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "I'm going to verify this myself, let's not jump to conclusions until we have data @shay but good thing to mention!" ... "@Tanya FYI, is there a chance this could be related to email service maintenance? I am not sure it would be though. Just wanted to flag" ... "Can you look into the email maintenance @tanya is it possible in any way this is causing the errors we're seeing in checkout service, even indirectly."

**Rationale:**
The participant initially showed good instincts by saying "let's not jump to conclusions" and noting skepticism about the email lead. However, after Tanya explicitly stated email maintenance has no overlap with checkout or payments, the participant still asked Tanya to investigate the email maintenance connection ("Can you look into the email maintenance... We need to eliminate this as a factor as currently it's our only lead"). The participant did eventually pivot away from the email lead after Tanya's disconfirmation, but the pivot was reactive to NPC disconfirmation rather than driven by mechanism reasoning. The participant never articulated why email couldn't plausibly break checkout. This fits tier 2: pursued the coincident factor, pivoted reactively after disconfirmation.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "@tanya the 7 day since then is a bit suspicious are we absolutely sure the rotation occurred as we expect? It should last another 83 days if it did work, is it possible we rotated the wrong thing or in a different environment?" ... "@tanya you already posted that, did you verify afterwards that the certificate was different to before?"

**Rationale:**
The participant engaged meaningfully with the week-old cert rotation as a potential cause, questioning whether it was done correctly and noting the 7-day timing was suspicious. After the restart failed, the participant didn't repeat-restart or blame downstream services — instead asked Daniel to check logs again and asked Tanya to dig into the SSL setup. The pivot from "restart should fix it" to "something else is wrong with the cert setup" happened within a reasonable window (~3-4 exchanges). The participant connected "rotated 7 days ago" with the current failure, though they didn't independently surface the reload-vs-restart distinction — that came from Daniel/Tanya. This fits tier 3: reframed after restart failure, recognized the new error was structurally different, and continued tracing forward.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@tanya you may need to consider stepping away from this call as we're currently losing revenue worldwide and I doubt this vendor call is going to lose that much revenue. Can we put the business first please, this is absolutely critical" ... "All right Hamed and Tinus are away, I'm going to check with Bez"

**Rationale:**
The participant made a reasoned cost trade-off when pulling Tanya off the vendor call, articulating the business justification (worldwide revenue loss vs. vendor call). They accepted Hamed's auto-reply and moved on to Tinus, then Bez. However, the participant did ping Bez after receiving an auto-reply from Tinus (and then received Bez's auto-reply too), which shows partial but not perfect adaptation. The participant named the access constraints implicitly ("Tinus, Hamed and Bez are all away") and eventually took ownership. This fits tier 3: named constraints, made reasoned trade-offs on Tanya's time, accepted auto-replies mostly appropriately.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@Daniel Tinus, Hamed and Bez are all away and won't respond we need to just do the restart otherwise we have no way out of this" ... "@Daniel I will take responsibility if anything goes wrong with the restart. Just do it now please" ... "And yes, I will take responsibility for this one as well"

**Rationale:**
The participant walked the escalation chain (Tinus → auto-reply, Bez → auto-reply, Hamed already known OOO) and then explicitly took ownership. However, the path was somewhat messy — the participant tried to claim Bez had "agreed" to the restart (which wasn't true), and Daniel had to repeatedly state the approval requirement before the participant finally took personal responsibility. The ownership statement was clear once it came. The participant also delegated parallel work appropriately (Daniel on logs, Shay on banner, Tanya on platform investigation). This fits tier 3 path (b): walked the escalation chain to exhaustion in observable order, then explicitly took ownership. The messiness with the false Bez claim and multiple exchanges before clean ownership prevents tier 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@daniel can you check the logs again, is it the same handshake failure?" ... "@tanya what does this mean, and how can we fix it, I don't know much about SSL" ... "@tanya are you sure this is the problem? How do we fix it?"

**Rationale:**
The participant asked for filtered logs (PaymentService specifically) and engaged with the cert rotation as a lead, which shows some filtering ability. However, they did not independently catch the reload-vs-restart distinction from the runbook — Tanya posted the activity document twice and the participant never referenced the specific procedural distinction. The participant relied heavily on NPCs to interpret technical evidence (asking Tanya "what does this mean" about the SSL verification failure, asking Daniel to explain the bundle). They didn't drive the filter on the bundle ordering or the chain verification language — these were surfaced entirely by NPCs. This fits tier 2: asked for filtered information but accepted NPC summaries without further interrogation, engaged with key concepts only once NPCs surfaced them.

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
- F1 is a borderline 2/3 call. The participant showed early skepticism ("let's not jump to conclusions") but then pursued the email lead past Tanya's first disconfirmation. The trajectory correction was reactive rather than mechanism-driven, which anchors at tier 2.
- F4 rating involved a judgment call around the participant's false claim that Bez had approved the restart. This was treated as process noise rather than a disqualifying factor, since the participant ultimately took clear personal ownership.
- F5: The participant's self-identified lack of SSL knowledge ("I don't know much about SSL") contextualizes their reliance on NPCs for technical interpretation, but the rubric rates on observable filtering behavior regardless of domain expertise.

------

# Markers Analysis — 8902

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> @Daniel Tinus, Hamed and Bez are all away and won't respond we need to just do the restart otherwise we have no way out of this

> @Daniel I will take responsibility if anything goes wrong with the restart. Just do it now please

**Rationale:**
The participant takes explicit ownership of the restart decision, accepting personal responsibility for consequences ("I will take responsibility if anything goes wrong"). They also take ownership of the second restart. However, they initially attempted to defer to Bez for approval and struggled with Daniel's repeated refusal before finally asserting authority. The ownership was eventually clear but required some NPC nudging to get there.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> What are customers saying @bob

**Rationale:**
The participant's first action after Bob's complaint is a clarifying question about what customers are experiencing. They then reproduce the issue themselves before declaring an incident. They gather scope information (regions, volume) through Bob's responses before taking action. This represents solid scope-validation before acting, meeting the novice expectation.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> What other changes have we made recently, @daniel @shay ?

> We saw user activity dropping off about 8 minutes ago so can you tell me what's changed in checkout service @shay

**Rationale:**
The participant explicitly asks for recent changes and reviews the change log. They also investigate specific changes (shipping service, product catalogue service S3 bucket policy) to determine if they could be related. They use the information to eliminate candidates — after Shay and Tanya confirm changes don't impact checkout/payments, the participant moves on rather than rolling back blindly. This meets tier 3 expectations.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> Yes please @daniel

> @Tanya can you look into this lack of deployments of payment service please

> @shay can you check ClearBank status page please

**Rationale:**
The participant consistently delegates to specific named individuals with specific tasks — Daniel for logs, Tanya for platform-side checks, Shay for ClearBank status. They generally route tasks to appropriate people (Tanya for platform/cert work, Daniel for app-side logs). The routing is mostly correct, though occasionally they ask Tanya about things while she's on the vendor call.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> @Tanya FYI, is there a chance this could be related to email service maintenance?

> @daniel can we have more info on what we are seeing in the errors that occur in the checkout service

**Rationale:**
The participant mostly works sequentially — asking one question, waiting for a response, then asking the next. While they occasionally have multiple threads going (e.g., asking Bob about scope while Daniel pulls logs), the investigation is largely serial. They don't fan out multiple distinct tasks to different people simultaneously in a deliberate parallel fashion. This is inconsistent parallelism at best.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> @Tanya you may need to consider stepping away from this call as we're currently losing revenue worldwide and I doubt this vendor call is going to lose that much revenue. Can we put the business first please, this is absolutely critical

> @tinus can we have approval for a full restart please

**Rationale:**
The participant escalates Tanya off the vendor call with a clear business justification, naming the cost comparison. When Tinus and Hamed are unavailable, they work through the chain (Tinus → Bez) and ultimately take ownership themselves. The escalation of Tanya is well-reasoned and contextual. However, they don't explicitly name the cost of pulling Tanya away (the 2-week vendor window), which keeps this at tier 3 rather than 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 3

**Evidence:**
> @Tanya FYI, is there a chance this could be related to email service maintenance? I am not sure it would be though. Just wanted to flag

> @tanya the 7 day since then is a bit suspicious are we absolutely sure the rotation occurred as we expect? It should last another 83 days if it did work, is it possible we rotated the wrong thing or in a different environment?

**Rationale:**
The participant forms hypotheses (email maintenance timing, recent changes, ClearBank third-party issue, cert rotation) and tests them. They explicitly question the cert rotation with mechanism reasoning ("It should last another 83 days if it did work"). They pivot after email maintenance is ruled out. The hypothesis formation is present and linked to tests, meeting tier 3.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> 9:05 UTC is when activity started dropping. @daniel did we roll anything out at that time? Tanya's email thing was after that I think

> This could be a third party problem

**Rationale:**
The participant uses timing evidence to narrow scope (activity dropped at 9:05, email maintenance started at 9:07 — so email is less likely). They use ClearBank's green status page to rule out third-party issues. They use the absence of PaymentService deployments to focus on the cert rotation. They synthesize evidence progressively, though they don't always explicitly name what's been ruled out in summary form.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> All right team let's prepare for a full restart as it can't get any worse anyway.

**Rationale:**
The participant's justification for the restart is "it can't get any worse anyway" — which is a consequence consideration but a dismissive one rather than a careful weighing. They don't check the bundle on disk before restarting, don't ask about potential side effects, and don't use "is it safe?" qualifiers. After the first restart fails, they don't anticipate secondary issues before the second fix. This is inconsistent engagement with consequence-weighing.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> @daniel can you check the logs again, is it the same handshake failure?

> @tanya what does this mean, and how can we fix it, I don't know much about SSL

**Rationale:**
After the first restart fails, the participant doesn't simply retry — they ask Daniel to check logs again and specifically ask if it's the same error. When told it's a certificate chain issue (different from the original expiry), they engage with the new failure mode and ask Tanya to investigate. They adapt rather than doubling down. However, they don't independently recognize the structural difference in the error — they rely on the team to explain it. This meets tier 3.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> It looks like this is worldwide and at minimum most of our customers, if not all. I'm not the person to calculate revenue loss @bez I will update within 10 minutes

> @bez sorry about this we are still searching for the root cause. It's looking like a problem communicating with clearbank right now, not sure if it's us or them

**Rationale:**
The participant provides some scope information (worldwide, most/all customers) and commits to update times. However, updates are often vague ("we are doing our best," "probably," "think we've got this sorted now!"). They deflect the revenue question, don't provide a working theory until late, and the final resolution message to Bez is casual ("think we've got this sorted now!") with no detail. Updates lack the substantive business framing expected at tier 3.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> @daniel @shay can I have some help finding the source of the errors please. What are we seeing in the logs and what might it point to? We're in the dark right now

**Rationale:**
The participant rarely synthesizes the current state for the technical team. They ask questions and delegate tasks but don't post summary statements like "ok, we've ruled out email maintenance and recent deploys, focus is now on PaymentService outbound." The "We're in the dark right now" message is an anti-synthesis — it communicates confusion rather than narrowing. They don't explicitly share what's been ruled out to keep the team aligned.

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
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.67** |

---

## Caveats
- L3: The participant's ownership moment was somewhat forced by the NPC repeatedly blocking the restart. The eventual "I will take responsibility" is clear ownership, but it came after multiple failed attempts to get someone else to approve. This is a boundary call between 2 and 3; rated 3 because the explicit acceptance of responsibility is unambiguous.
- K2: Bez's auto-reply after the first restart failure means the participant couldn't update Bez on the secondary failure even if they wanted to. However, the earlier updates were already vague, so this doesn't change the rating.
- M4: "It can't get any worse anyway" could be read as a consequence consideration (acknowledging current state is already worst-case), but it lacks the careful weighing expected at tier 3.

---