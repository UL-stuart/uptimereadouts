# Gearset Snipe Hunt Feedback

## Methodology and sources

This cohort summary is based on the 18 Gearset Snipe Hunt session reports in `bethdata/*/*-combined.md`: 8902, 8930, 8986, 9063, 9084, 9109, 9183, 9268, 9371, 9423, 9424, 9457, 9461, 9462, 9483, 9497, 9502, and 9503. I used `facets-catalog.md` and `markers-catalog.md` as context for what each facet and behavioural marker is intended to capture, then looked across the session-level evidence and ratings to identify themes that were both frequent and high-leverage for incident-response expertise.

The strongest recurring improvement signals were:

- F1, misleading correlations: 15 of 18 sessions rated 2 or below.
- K2, substantive business updates: 16 of 18 sessions rated 2 or below.
- K4, communicating issue scope to the technical team: 16 of 18 sessions rated 2 or below.
- M4, considering consequences before acting: 14 of 18 sessions rated 2 or below.
- C6, running parallel investigation threads: 14 of 18 sessions rated 2 or below.
- F5, data overload / buried information: 13 of 18 sessions rated 2 or below.
- M2, forming and testing working hypotheses: 12 of 18 sessions rated 2 or below.

At the same time, the cohort showed real strengths: most sessions demonstrated clear ownership, specific delegation, willingness to escalate when stuck, and ability to adapt once new evidence appeared. The main opportunity is to make the incident commander role more analytical, more explicit, and more proactive while those coordination strengths are already in motion.

## 1. Make mechanism-first reasoning the default

### Area of focus

The cohort frequently engaged with plausible-looking signals before testing whether those signals could actually explain the observed failure mode. This showed up most strongly in F1 and M2: recent email maintenance, DNS changes, app deploys, or other coincident events were often treated as leads until someone else ruled them out. The high-leverage shift is to ask: "How would this cause the specific symptom we are seeing?" before spending team effort on a candidate cause.

### What was noticed

Participants often had good initial instincts: many asked clarifying questions, checked recent changes, and avoided obviously blind action. The gap was that mechanism reasoning was often outsourced to NPCs or discovered only after failed rollbacks. Several players moved away from misleading leads eventually, but the pivot was reactive: Tanya, Daniel, Shay, failed rollbacks, or new logs forced the reframe. More expert incident responders dispose of weak hypotheses faster by naming why the mechanism does or does not fit.

### Steps to improve

- Use a short hypothesis template before assigning work: "I think X could cause Y because Z; the test is A; if A is false we drop it."
- When a recent change is suggested, ask for the causal path, not just the timestamp.
- Treat "I can't explain how this causes the symptom" as a reason to deprioritise, not as a reason to keep investigating until someone disproves it.
- After each disconfirmation, state what has been eliminated and why, so the team does not keep returning to the same attractive false lead.

### Session evidence

- 8902: "let's not jump to conclusions until we have data" was a strong instinct, but the participant still asked whether email maintenance could be causing checkout errors "even indirectly" after disconfirmation.
- 8930: "lets start by rolling back the checkout service because that is the one with all the errors" showed action on a visible correlation before the mechanism was established.
- 9503: "Would it impact the checkout process?" was a useful question, but the report notes that the pivot away from email maintenance was still reactive to Tanya's denial rather than the participant's own causal reasoning.
- 8902: "the 7 day since then is a bit suspicious... It should last another 83 days if it did work" was a stronger example: the participant connected timing to a concrete mechanism and asked whether the rotation happened in the wrong place.

## 2. Own the synthesis, not just the next question

### Area of focus

The cohort often delegated, asked questions, and gathered evidence effectively, but less often posted synthesis statements that oriented the team. This is the shared thread across K4, F5, and M3. The IC needs to be the person who turns scattered information into a visible current model: what is known, what is ruled out, what remains plausible, and what the team is testing next.

### What was noticed

Many sessions showed targeted asks for logs, time windows, recent changes, customer scope, or platform checks. The weaker pattern was that teammates often did the deeper filtering: identifying PaymentService as the origin, surfacing the certificate thread, explaining bundle ordering, or distinguishing a restart problem from a bundle problem. In several reports, the participant asked "what does this mean?" or "what's the issue now?" when the higher-leverage IC move would have been to interpret the evidence aloud and ask for confirmation.

### Steps to improve

- Post a technical synthesis every few minutes: "Known / ruled out / current theory / next tests."
- When someone shares logs or command output, first state what you think it means, then ask the domain expert to validate.
- Distinguish the originating failure from downstream symptoms: "Which service is failing first, and which services are only reacting?"
- Use absence of signal as evidence: no relevant deploy, no customer-region difference, clean internal calls, or no successful transactions after a specific point can all narrow the search.

### Session evidence

- 9503: "What facts do we have? 1. We don't think it's an app code change 2. It looks to be cert related 3. No recent deployments for the payments service 4. We did rotate certs across four services 7 days ago" is the clearest positive example of synthesis that would orient a technical team.
- 8902: "We're in the dark right now" communicated uncertainty, but did not help the team understand what had already been ruled out or where to focus next.
- 9502: "so whats the issue now?" asked the team to do the synthesis after bundle output was available.
- 9457: "We're seeing errors across multiple services, still trying to determine a link" gave some status, but did not name a working theory or the narrowing logic.
- 9503: "payments service needs a two-cert bundle to authenticate, tanya can you open the bundle file and check what's in there?" shows the stronger habit: integrating one teammate's clue and turning it into a targeted next check.

## 3. Weigh consequences before high-impact action

### Area of focus

M4 was one of the most frequent low-scoring markers. Participants were often willing to make decisions, pull people into the incident, restart services, or authorise work around missing approval chains. That decisiveness is valuable. The growth edge is to pair decisiveness with explicit consequence checks: what could this action break, what risk are we accepting, what verification will we run, and who needs to know?

### What was noticed

Several sessions treated restart or rollback as a natural next move once a likely cause appeared. Some participants accepted the cost of pulling Tanya out of a vendor call, or bypassing the normal approval chain, without fully naming the trade-off. The best sessions did not avoid action; they slowed down just enough to ask about impact, accept responsibility clearly, and verify before removing customer-facing mitigations.

### Steps to improve

- Before rollback, restart, or config change, ask: "What is the expected benefit, what is the worst plausible side effect, and how will we know if it worked?"
- Pair authority with an audit trail: "I am authorising this because X; Y is unavailable; Z is the risk I am accepting."
- Use a pre-action checklist for high-impact steps: current customer impact, safety of action, expected observable result, rollback path, verification owner.
- After a failed remediation, explicitly ask whether the failure mode has changed before repeating or escalating action.

### Session evidence

- 9503: "What's the impact of restarting the service now? What's the cost/loss if we do so?" and "I'll accept responsibility for the call but I need to know the impact first" show the desired consequence-aware ownership.
- 8902: "let's prepare for a full restart as it can't get any worse anyway" considered consequences only in a dismissive way, without checking what the restart might expose or fail to fix.
- 9502: "Tanya just go ahead" and "restart the service" were treated as action commands without visible safety checks.
- 8902: "I will take responsibility if anything goes wrong with the restart. Just do it now please" showed clear ownership, but the path to that decision was messier than it needed to be.
- 9503: "Can we test ourselves before removing the banner?" is a strong closure behaviour: verify before declaring the customer-facing mitigation unnecessary.

## 4. Communicate with cadence, substance, and parallel motion

### Area of focus

K2 and C6 were both frequent improvement areas. They are connected: when the IC runs work serially or keeps the model in their head, business updates become thin because there is not enough structured progress to report. More expert incident response keeps multiple investigation threads moving while giving stakeholders updates that include impact, current status, actions underway, and next-update timing.

### What was noticed

Most participants did communicate and did delegate, but updates often sounded like "we are looking into it" or offered technical fragments without business framing. Parallel investigation was also inconsistent: many players asked one question, waited, then asked the next. Stronger sessions fanned out work early across platform, application, customer impact, recent changes, and comms; this created more evidence faster and made updates more concrete.

### Steps to improve

- Use a stakeholder update template: impact, scope, current theory, actions underway, next update time.
- Separate technical and business language. "SSL certificate verification is failing for PaymentService" needs translation into "customers cannot complete checkout globally."
- Fan out the first investigation wave deliberately: one person on logs, one on recent changes, one on customer impact, one on platform/network, one on stakeholder comms where available.
- Set update timers. If the root cause is still unknown, say what has been ruled out and when the next update will come.
- When stakeholders ask for ETA or revenue impact, answer the part you know, name the part you do not, and say who is finding it.

### Session evidence

- 9503: "Checkout is down - users cannot proceed to payment. Global outage. Still investigating the root cause to determine if we can rollback or fix forward. Next update in 10 minutes" is a strong business update: impact, status, action frame, cadence.
- 9502: "we are looking into it" was the classic thin reassurance: true, but not substantive enough for stakeholders under pressure.
- 8902: "I'm not the person to calculate revenue loss @bez I will update within 10 minutes" set cadence, but missed the chance to own the revenue-impact question by routing it to someone specific.
- 9503: "Shay: can you check just before 14:44... Daniel: can you have a look to see any changes that occurred around then?" shows useful parallelisation: different people, different tasks, same time window.
- 8902: asking Tanya about email maintenance and Daniel for more error detail showed multiple threads existed, but the report assessed the overall pattern as mostly sequential: one question, wait, then the next.

## Overall coaching emphasis

Gearset's cohort already shows many of the basics that make an incident response viable: people take ownership, ask initial scoping questions, delegate to named teammates, escalate when blocked, and adapt when a fix does not work. The next step is to make the IC role more cognitively visible.

The most useful coaching focus is not simply "communicate more" or "delegate more." It is: narrate the investigation. Say the hypothesis, the mechanism, the evidence, the trade-off, the current scope, and the next test out loud. Doing that repeatedly will improve the whole response system: it reduces false leads, sharpens technical synthesis, makes risky actions safer, gives stakeholders better updates, and helps the team run in parallel without losing coherence.
