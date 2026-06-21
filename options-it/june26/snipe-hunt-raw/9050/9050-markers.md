---

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