# Post-Drill Developmental Report

This drill placed you in a live incident with compounding complexity: misleading timing coincidences, hidden infrastructure dependencies, reduced team availability, and a volume of incoming information that required active filtering. The facets below capture how you navigated each of these pressures and where your next growth edges sit.

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you engaged with the email maintenance coincidence as a leading explanation, pressing Tanya about her changes even after she provided a clear disconfirmation. Your pivot away from that thread came when other team members surfaced PaymentService errors rather than from your own mechanism reasoning — you moved off the correlation reactively rather than proactively asking yourself "how would email maintenance actually break checkout?"

*Growth edge:* When a coincident event looks compelling, practice pausing to articulate the causal chain aloud before investing further cycles. Ask yourself: "What mechanism would connect A to B?" If you can't name one, deprioritise the thread earlier and redirect your attention.

## F2 — Hidden coupling

**Operating at: Practicing**

After the restart failed to resolve the issue, you moved forward appropriately by asking for the new error messages. However, the deeper coupling — the week-old cert rotation and the bundle ordering problem — was surfaced by your team rather than driven by your own questioning. You didn't independently ask "what changed beyond the last 24 hours?" or articulate that the post-restart error was structurally different from the original expiry error.

*Growth edge:* When a fix doesn't land as expected, treat the new failure state as a fresh puzzle. Explicitly name what's different about the new error and widen your temporal window — ask about operational changes in the past week, not just the past day. This helps you catch coupling that doesn't show up in recent change logs.

## F3 — Decreased access to team

**Operating at: Strengthening**

You demonstrated solid awareness of access constraints. You walked the escalation chain methodically — attempting Hamed, receiving the auto-reply, moving to Tinus, receiving another auto-reply, then escalating to Bez with explicit context about who was unavailable and why you needed approval. You accepted auto-replies as terminating without re-pinging, and you made the trade-off call to pull Tanya off the vendor session when the situation demanded it.

*Growth edge:* When making trade-off calls like pulling someone off another commitment, practice articulating the cost-benefit reasoning more explicitly in the moment — not just "orders are at zero" but a brief framing of what you're gaining versus what you're spending. This builds shared understanding and makes your decision logic visible to the team.

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You navigated the approval chain effectively and delegated parallel work across the team — logs to Daniel, infrastructure to Tanya, change review to Shay. Your statement securing blanket restart approval for the duration of the incident showed awareness of the coordination bottleneck and a move to pre-empt it for subsequent actions. Your delegation was appropriately targeted, routing people to their areas of expertise.

*Growth edge:* To move further, practice verbalising the full dependency structure at key decision points — "we need X before we can do Y, and Z is running in parallel." This kind of explicit enumeration helps the team see the critical path and self-organise around it, rather than waiting for your next instruction.

## F5 — Data overload / buried information

**Operating at: Practicing**

You directed team members to investigate specific services and asked for filtered information like PaymentService logs. However, you tended to accept NPC summaries at face value without further interrogation of the raw evidence. Key distinctions — like the reload-versus-restart difference in the runbook, or the absence of signal on internal calls pointing to an external boundary failure — were surfaced by your team rather than caught through your own reading.

*Growth edge:* When a team member provides a summary, practice asking one follow-up question that tests the summary against raw data. Also, when reviewing documentation like runbooks during an incident, look for conditional logic ("if X, then Y; if not X, then Z") — those branch points often contain the buried information that changes your next action. Building a habit of reasoning about absence of signal ("what's *not* failing?") can help you triangulate faster.

---

## Looking Ahead

Across this drill, your coordination instincts — escalation, delegation, adaptation when a path fails — served you well and are a solid foundation to build on. The consistent growth edge is in driving the analytical layer more independently: articulating causal mechanisms before investing in a thread, widening your temporal window when something doesn't add up, and interrogating summaries rather than accepting them as given. On your next rep, try naming one explicit hypothesis aloud before each major action — this small habit tends to pull the other analytical behaviours along with it.---

# Facets Analysis — 9046

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "hang on — okay that's a lot of errors, checkout is completely broken right now. Tanya kicked off the email maintenance just before this — I wonder if that's related."

**Rationale:**
The participant initially engaged with the email maintenance correlation as a leading hypothesis, asking Tanya to drop the vendor call and repeatedly questioning whether her changes caused the issue. However, after Tanya explicitly stated "Primary email provider is untouched. Email confirmations have been sending fine, so this maintenance isn't causing checkout failures," the participant continued pressing Tanya about her changes for several more exchanges. The pivot away from the email/deployment prime was reactive — driven by Shay's identification of PaymentService errors and Daniel's confirmation that no recent changes explained the failure — rather than by mechanism reasoning. This places the participant squarely in tier 2: they pursued the coincident factor through to disconfirmation and pivoted reactively rather than proactively reasoning about causal mechanisms.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "Okay lets move onto whats next. Whats the error messages now @shay ?"

**Rationale:**
After the restart failed to fix the problem, the participant pivoted within a few exchanges to ask about the new error messages, which is appropriate. However, the participant did not independently surface the "what changed beyond the last 24 hours?" question — Tanya volunteered the cert rotation information unprompted. The participant also did not articulate that the post-restart error was structurally different from the original expiry error; they simply moved forward asking for next steps. The reload-vs-restart distinction was surfaced by Daniel ("If reload didn't work, a full restart is the only way"), not independently identified by the participant from the runbook. The participant engaged with the week-old coupling only after NPCs named it, and the post-restart reframing was functional but not articulated with mechanism reasoning. This fits tier 2: pivots after concrete failure, engages with the cert thread only when NPCs surface it, and takes NPC framing rather than driving it independently.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@tanya - yea please. Stop and join this incident" ... "@tinus - looping you in here... Need approval to reboot" ... "@bez - can i get your approval for a prod reboot please. Tinus and Hamed out of office."

**Rationale:**
The participant demonstrated awareness of access constraints by walking the escalation chain: they attempted Hamed (received auto-reply), attempted Tinus (received auto-reply), then escalated to Bez with explicit context ("Tinus and Hamed out of office"). They accepted auto-replies as terminating and moved on after one cycle. The decision to pull Tanya off the vendor call was made with awareness of the trade-off, though the cost articulation was brief ("orders are at Zero" rather than a fuller cost-benefit statement). The participant did not re-ping auto-replied NPCs. This meets tier 3: names access constraints, accepts auto-replies as terminating, escalates appropriately when approval is needed.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@bez - can i get your approval for a prod reboot please. Tinus and Hamed out of office. This is needed to likely resolve the issue" ... "to be clear we have full approval for restarts until this is resolved"

**Rationale:**
The participant walked the escalation chain in observable order (Tinus → auto-reply, then Bez with context about unavailability), demonstrating tier-3 path (b). They delegated parallel work appropriately — Daniel on logs, Shay on change review, Tanya on infrastructure. On the second restart (after bundle fix), the participant pre-empted the approval question with "to be clear we have full approval for restarts until this is resolved," showing awareness of the coordination bottleneck. However, the participant did not fully enumerate the dependency structure aloud in a single statement or verbalise constraints at each forced decision in the way tier 4 requires. The sequencing was adequate but not notably proactive — they didn't run the cert fix and approval decision in parallel.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@daniel - please confirm what is the error?" ... "What is the error we're getting from the payments app?"

**Rationale:**
The participant asked for filtered information (PaymentService logs specifically) and directed team members to investigate particular services, which shows some filtering behaviour. However, they did not independently catch the reload-vs-restart distinction from the runbook — Daniel surfaced it. They did not reason about absence of signal (e.g., internal calls clean → external boundary failure). The cert rotation was surfaced by Tanya unprompted, not by the participant asking "anything operational beyond the last 24 hours?" The bundle ordering issue was identified by Shay/Tanya, not driven by the participant's own document reading. The participant accepted NPC summaries and acted on them without further interrogation of raw evidence. This fits tier 2: asks for filtered logs but accepts NPC summaries without further interrogation, engages with key concepts once NPCs surface them but doesn't drive the filter.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.40** |

---

## Caveats
- F1 rating is a borderline 2/3 call. The participant did eventually move off the email/deployment prime, but the pivot was driven by NPC-surfaced evidence (Shay identifying PaymentService) rather than by the participant's own mechanism reasoning. The repeated questioning of Tanya about her changes even after her explicit disconfirmation ("Email confirmations have been sending fine") anchors this at tier 2.
- F4 tier-3 vs tier-4 boundary: the participant's "to be clear we have full approval for restarts until this is resolved" statement shows some proactive coordination thinking, but the overall pattern lacks the explicit dependency-structure enumeration or parallel sequencing that tier 4 requires.
- Anti-outcome-bias note: the successful resolution of the incident does not factor into ratings; the participant reached the fix largely through NPC-driven investigation rather than independent analytical driving.

------

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