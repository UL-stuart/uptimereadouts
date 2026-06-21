---

# Markers Analysis — 9046

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "@bez - can i get your approval for a prod reboot please. Tinus and Hamed out of office. This is needed to likely resolve the issue"

**Rationale:**
The participant drives the response throughout — declaring the incident, directing team members, making the call to pull Tanya off the vendor session, and seeking restart approval when the chain is exhausted. They secure Bez's approval and authorize the restart. However, they don't explicitly name personal accountability ("blowback's on me") — they route through Bez rather than self-authorizing, which is reasonable but stops short of tier 4 ownership language.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob - could you elaborate please? What complaints, when did they start and where from?"

**Rationale:**
The participant's very first message after Bob's alert is a clarifying question asking for specifics on the complaints, timing, and geography. This is a textbook scope-validation move before any action is taken. They gather information from Bob before declaring the incident or ordering any changes, meeting the novice expectation cleanly.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "Can i get a list of changes please?" ... [later] "Was anyone working on anything that isnt documented in Shays change list?"

**Rationale:**
The participant explicitly requests the change list and reviews it. They also ask whether anything undocumented was done. When Shay notes "none of these changes look like they'd break checkout end-to-end," the participant doesn't blindly roll back — they continue investigating other angles. They don't explicitly articulate elimination logic ("none of these touch the gateway"), but they do move past the changes without rolling them back, which meets tier 3.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@daniel - Looping you in here, we're seeing users unable to checkout. Could you please take a look at the logs from this error message please?" ... "@tanya - looping you in here- Users having issues with checking out. Can i please have an infrastructure check please?"

**Rationale:**
The participant consistently delegates to specific named individuals with specific tasks — Daniel for logs, Tanya for infrastructure, Bob for the banner, Shay for change details, Maya for security. The routing is generally appropriate (Tanya for platform, Daniel for app-side). They occasionally ask the wrong person first (Hamed for infrastructure when he's OOO), but overall delegation is targeted and named.

---

## C6 — Runs parallel investigation threads

**Rating:** 3

**Evidence:**
> "@tanya - looping you in here- Users having issues with checking out. Can i please have an infrastructure check please?" [while Daniel is already investigating logs] ... "@maya - can we please get you looped in here to check for anything abnormal also from a sec standpoint?"

**Rationale:**
The participant runs multiple threads concurrently — Daniel on logs, Tanya on infrastructure, Maya on security, Shay on change details. These are distinct investigation surfaces assigned to different people in relatively close temporal proximity. This meets the tier 3 expectation of multiple simultaneous threads, though the sequencing isn't as tightly orchestrated as a tier 4 performance.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tinus - looping you in here. We have a Global P1, expired certificate on the payment server. Need approval to reboot" ... [auto-reply received] "@bez - can i get your approval for a prod reboot please. Tinus and Hamed out of office."

**Rationale:**
When the restart approval chain is blocked (Hamed OOO, Tinus OOO), the participant escalates to Bez with a concrete ask and context ("Global P1, expired certificate, need approval"). They don't leave the chain hanging — they move to Bez promptly after the auto-replies. The escalation includes sufficient context. They also pulled Tanya off the vendor call when needed. However, they don't explicitly name the cost of the escalation (losing the 2-week vendor window) in their own words, which keeps this at tier 3.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "What is the error we're getting from the payments app?" ... "@daniel - please confirm what is the error?"

**Rationale:**
The participant does not explicitly articulate hypotheses at any point in the transcript. They follow the investigation thread reactively — asking questions and following up on what the team reports — rather than stating "my hypothesis is X, let's test it by doing Y." They do pursue the payment service thread once evidence points there, but this is reactive following of evidence rather than explicit hypothesis formation and testing. The absence of any explicit hypothesis statement places this at tier 2.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "Okay lets move onto whats next. Whats the error messages now @shay?" [after restart failed, pivoting to new evidence]

**Rationale:**
The participant uses evidence to narrow scope at several points: they accept that infrastructure is fine (Tanya's check), that recent changes don't explain the failure (Shay's assessment), and focus on PaymentService when logs point there. They don't explicitly synthesize ruled-out candidates in a single statement, but they do progressively narrow from "checkout broken" to "PaymentService handshake failure" to "expired cert" to "bundle order." This meets tier 3 but lacks the explicit absence-of-signal reasoning of tier 4.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "Lets do a full restart please" ... [no safety check or consequence consideration mentioned]

**Rationale:**
The participant does not demonstrate explicit consequence-weighing before high-impact actions. They order the restart without asking "is it safe?" or considering what could go wrong. When pulling Tanya off the vendor call, they acknowledge the 2-week cost only after Tanya raises it ("Thats fine" / "Please drop- orders are at Zero") — they don't proactively name the trade-off. The absence of "is it safe?" qualifiers or anticipation of secondary failures places this at tier 2.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Okay lets move onto whats next. Whats the error messages now @shay?" ... "Can we get a second certificate please Tanya" ... "Can we change this around please and reapply?"

**Rationale:**
After the first restart fails, the participant doesn't retry the same action — they immediately ask for the new error messages and pivot to investigating the cert chain issue. When told it's a bundle problem with wrong ordering, they adapt again and request the reorder. This demonstrates clear adaptation when the initial path (restart with new cert) doesn't work, meeting tier 3. They don't independently recognize the structural difference in the error (Shay and Tanya identify it), which keeps this from tier 4.

---

## M5 — Adapts approach when initial path isn't working

*Already scored above.*

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Incident description: Checkout issues occurring globally. Zero customer orders. Status: Banner up on site, expired certificate on the payment server- team reviewing. Next update in 5 minutes"

**Rationale:**
The participant provides several updates, and the later ones include some specifics (zero orders, expired certificate). However, the updates lack business-framing of revenue impact, don't include a working theory until late, and are mostly posted to the incident channel rather than directly addressing Bez with business-relevant language. When Bez asks "What's the revenue loss per minute? Have you found the cause yet?" the participant responds only with "@bez - the customer orders per minute is at 0 currently" without fuller context. The updates are present but not substantive enough for tier 3.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Incident description: Checkout issues occurring globally. Zero customer orders. Status: Banner up on site, infrastructure looks fine on checks. Appears to be an issue with PaymentService fails. Next update in 5 minutes"

**Rationale:**
The participant posts incident status updates but does not provide synthesis statements to the technical team that name what's been ruled out and what's still in scope. They don't post messages like "it's not deploys, not infra, focus on PaymentService outbound" — instead, the team members (Shay, Daniel, Tanya) drive the synthesis themselves. The participant asks questions and delegates but rarely synthesizes the current state of knowledge for the team's benefit.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 3 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 3 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 3 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.67** |

---

## Caveats
- **K2 boundary call:** The participant does provide updates with some specifics (zero orders, expired cert), but they lack the business-framing and proactive cadence expected at tier 3. Bez has to ask for scope/revenue information rather than receiving it proactively. Rated 2 rather than 3 on this basis.
- **M2 boundary call:** The participant never uses the word "hypothesis" or explicitly frames a theory-then-test sequence. Their investigation is reactive (following team findings) rather than hypothesis-driven. This could arguably be a low 3 if one interprets their focus on PaymentService as an implicit hypothesis, but the rubric emphasizes explicit articulation.
- **L3 boundary call:** The participant secures approval through Bez rather than self-authorizing. This is a reasonable organizational move but stops short of the "blowback's on me" tier-4 framing. Rated 3 as they clearly drive the response and make the override decision (routing through Bez for sign-off).

---