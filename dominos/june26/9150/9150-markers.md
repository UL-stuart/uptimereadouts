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