# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to navigate systemic complexity under time pressure — sorting misleading signals from root causes, coordinating a constrained team, and making decisions when the usual approval paths aren't available. This report walks through what showed up in your run and where the growth edges are for your next rep.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you flagged the timing overlap between email maintenance and the checkout failures and pulled Tanya in to investigate on that basis. When Tanya explicitly disconfirmed the email theory, you pivoted away from it — which is the right move. The growth edge here is making that pivot *before* an NPC hands it to you: asking yourself "what's the actual mechanism that would connect these two?" before committing investigative resources to a coincidence. On the next rep, try articulating the causal chain out loud before treating a correlation as a lead.

---

## F2 — Hidden coupling

**Operating at: Practicing**

The deeper structural issue — a certificate rotation from days earlier interacting with a service restart — was surfaced by your teammates rather than by your own questioning. After the first restart failed and a new error appeared, you moved to cache-clearing questions rather than reframing the problem as structurally different. The growth edge is recognising when a failure mode *changes shape* after an action: that's a signal to pause and ask "what assumption just broke?" rather than continuing down the same path. Building the habit of asking "what changed beyond the obvious window?" early in an incident will help you catch hidden coupling sooner.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You walked the approval chain — Hamed's auto-reply led you to Tinus, then to Bez — which shows awareness that you needed to find someone with authority. However, pulling Tanya off her vendor call happened without visible acknowledgement of the trade-off, and the questions you sent her weren't batched or scoped to minimise her context-switching. The growth edge is treating constrained availability as a design problem: when someone is expensive to interrupt, front-load your asks into a single, well-structured message so you get maximum value from minimum disruption.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

When both approvers were unavailable, you initially tried to route the sign-off decision to a business stakeholder who couldn't grant it. You did eventually take ownership of the call — and did so again on the second restart — but this happened after explicit prompting rather than from your own recognition that the escalation chain was exhausted. Your delegation throughout tended toward serial, one-at-a-time requests rather than parallel tasking. The growth edge is naming the bottleneck explicitly ("approval chain is exhausted, I'm taking the call") and sequencing work so that multiple threads can progress simultaneously rather than waiting on each answer before asking the next question.

---

## F5 — Data overload / buried information

**Operating at: Not yet evident**

Several moments in the drill showed information being available in-channel but not integrated into your decision-making. A deployment list was interpreted as a failure list, leading to an inaccurate scope statement. The maintenance banner was toggled without a clear read on system state, and a premature claim of resolution was made while checkout was still broken. Investigative filtering — identifying which service was actually failing, reading the rotation runbook for the reload-vs-restart distinction — was largely performed by teammates rather than by you. The growth edge here is foundational: before synthesising for others, pause to confirm what you're actually seeing. Read the data yourself, name what's ruled out, and resist the pull to declare resolution until you've verified it against the original symptom.

---

## Looking Ahead

Two things to carry into your next rep. First, practice *pausing before acting*: when you're about to authorise an action or broadcast a status, take five seconds to ask "what could go wrong?" and "is this accurate based on what I actually know?" Second, work on owning the investigative thread yourself — forming a hypothesis, naming what would confirm or disconfirm it, and using NPC findings as inputs to *your* reasoning rather than as the reasoning itself. These habits will compound quickly across reps.
# Facets Analysis — 9150

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "hey — not trying to distract from this, but tanya kicked off the email maintenance right before the complaints started. probably nothing, but the timing is a bit close." ... "@tanya we have p1 issue. there is revenue loss. could you please check this on priority"

**Rationale:**
The participant initially pulled Tanya off her vendor call based on the timing correlation between email maintenance and checkout failures, treating it as a leading hypothesis. However, they did not persist on the email theory after Tanya stated email wasn't causing checkout failures. They pivoted reactively — moving to investigate downstream services and deployments — but this pivot was driven by Tanya's explicit disconfirmation rather than by the participant's own mechanism reasoning. They never articulated "correlation isn't causation" or questioned the causal chain independently. This fits tier 2: pursued the coincident factor, then pivoted after NPC disconfirmation.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "looks like something is expired @tanya can you fix it?" ... "@tanya is there any cache that we need to clear"

**Rationale:**
The participant never independently surfaced the "what changed beyond the last 24 hours?" question — Daniel/Shay found the cert rotation from 7 days ago. After the first restart failed, the participant did not recognise the new error as structurally different. They asked about cache clearing and seemed confused ("@tanya site is not coming only. did you check TLS time?") rather than reframing. It took multiple NPC messages (Shay noting "SSL chain broken errors" and "two certificates needed — it's a bundle") before the participant engaged with the bundle issue. Pivot latency was well beyond 5 exchanges after the restart failed, and the reframing was NPC-driven rather than participant-driven.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tanya we have p1 issue. there is revenue loss. could you please check this on priority" ... "@tinus could you please give signoff" ... "@bez Infra team need signoff for loading new certificate from tinus or hameed. both are not available at the moment. could you please give singoff"

**Rationale:**
The participant pulled Tanya off her vendor call without visible economising or acknowledging the trade-off cost. They pinged Tinus after Hamed's auto-reply, which shows walking the chain, but they then asked Bez for sign-off (which Bez cannot give). They never articulated the access constraints in their own words or batched questions for Tanya. The escalation chain was walked but without reasoning about the constraint pattern. This fits tier 2: walks the escalation chain in order but does not articulate the constraint pattern or economise on constrained channels.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "@bez Infra team need signoff for loading new certificate from tinus or hameed. both are not available at the moment. could you please give singoff" ... "@tanya i am giving you signoff to do so. since there is revenue impact"

**Rationale:**
The participant attempted to route the approval decision to Bez (who explicitly cannot approve technical actions), showing incomplete understanding of the dependency structure. They eventually took ownership but only after Bez refused and Tanya explicitly prompted them ("Just say the word that you're taking or owning the outcome of restart"). The reasoning was outcome-pressure-based ("since there is revenue impact") rather than naming the escalation chain as exhausted. They did not sequence parallel work effectively — much of the investigation was serial with repeated "could you please check" messages. On the second restart (after bundle fix), they authorised more quickly. This fits tier 2: takes the override call after explicit NPC prompting, without first cleanly walking the escalation chain or naming the bottleneck.

---

## F5 — Data overload / buried information

**Rating:** 1

**Evidence:**
> "all this services are failing @tanya" ... "Issue summary is all this servies are not working any throwing error" ... "@shay remove the maintaince banner" ... "@bob I am able to place order"

**Rationale:**
The participant repeatedly misread the situation — listing all deployed services as "failing" when only PaymentService was the issue, claiming they could place an order when checkout was still broken, and toggling the maintenance banner on and off without understanding the state. They did not filter logs to the relevant service themselves (Daniel/Shay did this), did not read the rotation runbook to catch the reload-vs-restart distinction, and did not engage with the bundle/chain issue until NPCs explicitly surfaced it. The participant delegated nearly all investigative filtering to NPCs and failed to integrate information already in-channel (e.g., asking Tanya about cache when she'd already said a restart was needed). This represents failure to filter or integrate available information.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 1 |
| **Mean Facet Score** | **1.80** |

---

## Caveats
- F5 rating of 1 is a boundary call with 2. The participant did eventually direct investigation toward PaymentService and third-party connections, but this was largely NPC-driven. The maintenance banner confusion and the false claim of being able to place an order weigh toward tier 1 as evidence of not integrating available information.
- F4 tier-2 vs tier-3 boundary: the participant did walk Hamed → Tinus → (Bez, incorrectly) before taking ownership, but the Bez detour and the need for explicit NPC prompting ("Just say the word") place this firmly in tier 2 rather than tier 3.

---
---

# Markers Analysis — 9150

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "@tanya since both are not avaialble and since we have prod issue. I am giving you signoff to load the new certificate"

**Rationale:**
The participant takes the override decision when both Tinus and Hamed are unavailable, giving Tanya sign-off to proceed. They do this twice (for the reload and later for the restart). However, they don't explicitly name the personal cost or blowback ("that's on me") — Bez had to prompt them that "Whoever's running this incident needs to take responsibility for the call" before they acted. This places them at tier 3 rather than 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 2

**Evidence:**
> "what is it @bob"

**Rationale:**
The participant's first response is a brief "what is it @bob" which is a clarifying question, but it's extremely generic. They don't ask about specific regions, error types, or patterns. Their next substantive moves are to ask Daniel and Shay to check logs and ask about deployments — action-oriented rather than scope-validating. They do later ask "@bob do we have any success order at the moment?" which is useful, but the initial scoping is minimal and non-specific.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@shay @daniel can you check what all deployed today."

**Rationale:**
The participant does ask about recent deployments, and Shay provides the list. However, there is no evidence the participant used this information to eliminate candidates or reason about mechanisms. They never synthesized "none of these touch PaymentService" or articulated why the deploys were or weren't relevant. The change log was requested but not meaningfully used as an elimination tool.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "@daniel @shay could you please check the logs" ... "@hamed @tanya do you any issue from infra side?" ... "@maya do you see any issue from security side?"

**Rationale:**
The participant does name specific people, but the tasks are vague ("check the logs," "any issue from infra side," "could you please investigate"). They rarely give specific, scoped tasks that match NPC access boundaries. Many messages are broadcast-style ("@daniel @tanya @shay @maya") without differentiated asks. The delegation is present but imprecise and often repetitive.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@daniel @shay could you please check the logs" ... "@hamed @tanya do you any issue from infra side?" ... "@maya do you see any issue from security side?"

**Rationale:**
The participant does ping multiple people in quick succession early on (Daniel/Shay for logs, Tanya/Hamed for infra, Maya for security), which shows some parallel intent. However, the asks are so vague that they don't constitute distinct investigation threads. The investigation largely proceeds sequentially after the initial burst, with the participant waiting for one answer before asking the next question.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "@bez Infra team need signoff for loading new certificate from tinus or hameed. both are not available at the moment. could you please give singoff"

**Rationale:**
The participant does escalate to Bez when Tinus and Hamed are unavailable, which shows awareness of the need to escalate. However, they initially try to push the approval decision to Bez (a business stakeholder who can't approve technical actions), and only take ownership after Bez explicitly refuses. The escalation lacks the quality of naming what's blocked and why, and the participant needed prompting to take the call themselves.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "looks like something is expired @tanya can you fix it?"

**Rationale:**
The participant never explicitly articulates a hypothesis in a structured way. They don't say "my hypothesis is X, let's test it by doing Y." When the expired cert is surfaced by Tanya, they react to it ("looks like something is expired") rather than having formed and tested the hypothesis themselves. The investigation is largely reactive — following NPC findings rather than driving hypothesis formation and testing.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "@bob do we have any success order at the moment?" ... "Issue summary is all this servies are not working any throwing error. customer are not ablet to place order in any region"

**Rationale:**
The participant asks Bob about successful orders (useful narrowing) and confirms zero orders are going through. However, they misinterpret the deployment list as meaning "all this services are failing" when it's actually a deployment log, not a failure list. They don't synthesize evidence to narrow scope — they don't articulate what's been ruled out or use absence of signal as evidence. Most narrowing is done by NPCs (Daniel identifying PaymentService outbound failures).

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "its ok @tanya we need to fix the PROD first. that is priority" ... "restart it @tanya I am giving signoff"

**Rationale:**
The participant pulls Tanya off the vendor call without acknowledging the 2-week cost. They authorize restarts without asking "is it safe?" or considering what could go wrong. When the first restart fails, there's no evidence they anticipated this possibility. Actions are fired without consequence-weighing qualifiers throughout the drill.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "@tanya is there any cache that we need to clear" ... "Could you please investigate further with team"

**Rationale:**
After the first restart fails, the participant does not immediately recognize the new failure mode (chain verification vs. expiry). They ask about cache clearing and make vague requests to investigate further. Eventually the NPCs (Shay and Tanya) surface the bundle issue, and the participant follows their lead. The adaptation happens, but it's NPC-driven rather than participant-driven. The participant doesn't reframe the problem themselves.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "@bez we have issue in PROD customer are not able to compelte there orders. Team is investigating. will let you the updates in next 5 minutes" ... "@bez issue is ssl certificate is expired. Infra team is working on it"

**Rationale:**
The participant does provide updates to Bez and commits to 5-minute update windows. However, the updates lack quantified business impact (revenue numbers, customer count), lack ETAs, and are often vague ("team is investigating," "Infra team is working on it"). The certificate update is the most substantive, but it's technical rather than business-framed. Bez repeatedly asks for specifics that aren't provided.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 1

**Evidence:**
> "Issue summary is all this servies are not working any throwing error. customer are not ablet to place order in any region"

**Rationale:**
The participant's synthesis to the technical team is inaccurate (conflating a deployment list with a failure list) and vague. They never post a clear "here's what we know, here's what's ruled out" message. The technical team receives repetitive requests ("could you please check," "could you please investigate") without orientation on what's already been established. No evidence of synthesis statements that help the team orient.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 2 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 1 |
| **Mean Marker Score** | **1.92** |

---

## Caveats
- L3 is a borderline 2/3 call. The participant does eventually give sign-off, but only after Bez explicitly tells them to take responsibility. Rated 3 because they do ultimately own the decision (twice), but it's a weak 3.
- C6 is borderline — the initial burst of pings to multiple people could be read as parallel threads, but the vagueness of the asks and subsequent sequential behavior pulls it toward 2.
- M5 rated 2 rather than 1 because the participant does eventually follow the bundle thread, but the pivot is NPC-driven rather than self-initiated.

---