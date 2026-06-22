---

# Markers Analysis — 9084

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "Hamed is on leave and Tinus is at the conference. I'll authorize it in their absence. Bez is aware."

**Rationale:**
The participant takes explicit ownership of the restart authorization when both approvers are unavailable, making the call themselves and noting Bez's awareness. They also drive the response throughout — directing Tanya, Daniel, and Shay by name. However, they don't explicitly name the personal cost/blowback risk of the override, which would elevate to tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "What are the complaints about Bob?" ... "Is this a total checkout outage? How many customers are blocked and what's the revenue loss per minute right now?"

**Rationale:**
The participant's first action after Bob's alert is a clarifying question about the nature of the complaints. They follow up with scope-validating questions about whether it's a total outage, customer count, and revenue impact before taking action. They also ask about recent changes. This represents solid scope-validation before acting, meeting the tier 3 expectation.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "can we line this up with any recent changes? @shay ?"

**Rationale:**
The participant explicitly asks for recent changes early in the investigation. When Shay and Daniel provide the change log, the participant doesn't immediately jump to rolling back those changes. They move on to investigating logs and other causes. However, they don't explicitly articulate the elimination logic ("none of these touch the gateway") — the deweighting is implicit rather than stated. This places them at tier 3.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya check the payment service. it's failing outbound gateway handshakes" ... "@daniel can you do that?" ... "@shay could you do the above if Daniel is not available?"

**Rationale:**
The participant consistently delegates to specific named individuals with specific tasks — Tanya for platform/cert checks, Daniel for logs and banner, Shay as backup. They route platform-level work to Tanya and app-side work to Daniel appropriately. The fallback delegation to Shay when Daniel might be unavailable shows awareness of access boundaries, approaching tier 4 but not consistently demonstrating deep boundary knowledge throughout.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "can we line this up with any recent changes? @shay ?" ... "Can someone check the logs on the checkout service?"

**Rationale:**
The participant does kick off a change-log review and log checks in relatively close succession. However, much of the investigation proceeds sequentially — waiting for Daniel's log results before moving to the next step, then waiting for Tanya's findings. The "@here can everyone mob on this one?" is a broadcast rather than structured parallel delegation. The investigation is mostly serial rather than deliberately fanned out.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya the payment service is failing outbound gateway handshakes. that seems infrastructure. can someone else take over the email vendor hand holding for you?" ... "Hamed is on leave and Tinus is at the conference. I'll authorize it in their absence."

**Rationale:**
The participant escalates Tanya's priority by trying to pull her off the vendor call, providing concrete context about why (outbound handshake failures). When both Tinus and Hamed are unavailable for the restart approval, they don't leave the chain hanging — they authorize it themselves. However, they don't explicitly name the cost of pulling Tanya off the vendor session (the 2-week slot loss), which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 3

**Evidence:**
> "@shay does the code block on sending the checkout emails? if so, does the email service being down mean it would entirely freeze?" ... "maybe they changed their ssl cert and we don't have the public one trusted?"

**Rationale:**
The participant forms testable hypotheses — first about email maintenance blocking checkout (tested via Shay's response that checkout doesn't block on email), then about ClearBank's cert changing. They pivot when hypotheses are disconfirmed. The email hypothesis is explicitly articulated and tested on mechanism ("does the code block on sending?"). This meets tier 3 expectations of naming hypotheses and proposing tests.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "Ok, so do any of the other service logs show an issue or is it just the email service" ... "@tanya the payment service is failing outbound gateway handshakes. that seems infrastructure."

**Rationale:**
The participant uses Daniel's log findings to narrow from "checkout broken" to "PaymentService outbound handshake failure" and correctly identifies this as infrastructure territory. They use Shay's confirmation that checkout doesn't block on email to eliminate that hypothesis. However, they don't produce explicit synthesis statements naming what's been ruled out alongside what remains, which would push to tier 4.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "@tanya do it" ... "@tanya restart the service"

**Rationale:**
The participant issues restart commands without explicit consideration of potential consequences. They don't ask "is it safe?" before the first restart, nor do they anticipate that the restart could expose a secondary issue (the misordered bundle). They don't check the bundle on disk before restarting. The absence of consequence-weighing language ("if it's safe," "gradually," "what could go wrong") places this at tier 2.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "@tanya can you check that the certificate is correct? that footnote in the instructions is worrying." ... "@tanya can we examine it more closely? check the ordering"

**Rationale:**
After the first restart fails, the participant doesn't simply retry the restart. They redirect investigation to the certificate itself, referencing the footnote about bundle ordering. They then ask Tanya to examine the bundle more closely and check the ordering, which leads to discovering the misordered chain. This demonstrates clear adaptation when the initial fix didn't work, meeting tier 3. They don't quite reach tier 4 because they don't explicitly name the new failure as structurally different from the original.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "we've not located the exact source of the failure yet. we'll update again in 5 minutes." ... "10 minutes" ... "our certificate isn't correct. we're going to generate a new one and rotate that in"

**Rationale:**
The participant's business communications are mostly thin. The first update to Bez ("we've not located the exact source") lacks impact quantification or working theory. The "10 minutes" ETA is given without context. Later updates improve slightly ("our certificate isn't correct") but still lack business framing (revenue impact, customer scope). They don't proactively update Bez after the first restart fails. This is inconsistent and below the tier 3 expectation of quantified impact and committed next-update times.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 3

**Evidence:**
> "@tanya the payment service is failing outbound gateway handshakes. that seems infrastructure. can someone else take over the email vendor hand holding for you?" ... "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
The participant shares working understanding with the team at key moments — identifying the failure as infrastructure-level outbound handshake failures, and later directing attention to the bundle structure. They synthesize Daniel's findings into actionable direction for Tanya. However, they don't produce comprehensive "here's what we've ruled out" synthesis statements, which would push to tier 4.

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
| K4 — Communicates issue scope clearly to the technical team | 3 |
| **Mean Marker Score** | **2.75** |

---

## Caveats
- L3: The authorization statement "I'll authorize it in their absence. Bez is aware." is clear ownership but doesn't explicitly name personal risk/blowback. This is a borderline 3/4 call; rated 3 because the cost-naming language is absent.
- K2: Bez's aggressive questioning ("Not good enough") may have pressured the participant into terse responses, but the rubric evaluates the substance of what was communicated regardless of pressure context.
- M4: The absence of consequence-weighing is rated on what the participant *didn't* say before issuing restart commands. No "is it safe?" or "what could go wrong?" language appears anywhere in the transcript before high-impact actions.

---