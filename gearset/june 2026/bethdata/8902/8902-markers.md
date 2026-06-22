---

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