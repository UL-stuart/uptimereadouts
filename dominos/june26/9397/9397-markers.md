---

# Markers Analysis — 9397

## L3 — Takes explicit ownership of the response

**Rating:** 2

**Evidence:**
> "We are working on it Bez, cause of the issue is still unclear." / "It is the global outage, we are figuring out the resolution Bez"

**Rationale:**
The participant responds to stakeholder queries but never explicitly positions themselves as the decision-maker driving the response. They ask questions and relay information but don't use "I" statements about owning the plan. The drill ended before the restart approval moment could fully play out — the participant asked "Will restarting impact anything?" but never made the override call themselves. No explicit ownership language or acceptance of consequences is visible.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "Hi @bob What are the complaints about and how many customers impacted"

**Rationale:**
The participant's very first message after Bob's alert is a scope-validating question asking about the nature of complaints and customer impact. This precedes any declarations or remediation actions. They gather information before declaring the incident or ordering rollbacks, meeting the novice expectation for this marker.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@shay did we deployed any new changes today ?" / "Need full list @shay" / "dont you think if we rollback the deployements on checkout service will resolve this issue"

**Rationale:**
The participant asks for the change log and reviews recent deployments — good. However, they then propose rolling back the CheckoutService deployment without articulating a mechanism connecting it to the outbound gateway handshake failure. Daniel and Shay had already identified the failure was at the connection layer (Tanya's domain), yet the participant still pursued the rollback. They asked the question but didn't use the answer as an elimination pass.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "@shay @daniel dont you think if we rollback the deployements on checkout service will resolve this issue" / "@tanya we could see errors on outbound gateway handshakes, could you please have a look"

**Rationale:**
The participant does use @mentions to direct tasks to specific people. However, many asks are vague ("could you please look into it") or addressed to pairs without clear role differentiation. The participant also asks Hamed for help despite Hamed having no clear role in the investigation, and repeatedly pings Tanya without a concrete fallback plan. Delegation is present but imprecise.

---

## C6 — Runs parallel investigation threads

**Rating:** 1

**Evidence:**
> Sequential pattern: asks Shay for changes → waits → asks for details → waits → proposes rollback → waits for result → then moves to platform side

**Rationale:**
The participant works almost entirely sequentially throughout the drill. They pursue one thread at a time: first the change log, then the rollback, then trying to get Tanya involved. There is no evidence of multiple investigation threads running simultaneously with different team members assigned distinct concurrent tasks.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "Hi @hamed could you please look into this" / "Hi @tinus we could see logs of this issue stating that errors on outbound gateway handshakes... Could you please help us on this" / "Hi @tanya we need you to look into the issue as it is impacting the revenue. Please prioritize this one"

**Rationale:**
The participant does attempt escalation by pinging Hamed, then Tinus when Hamed auto-replies. However, the escalation to Tinus is vague ("Could you please help us on this") rather than a concrete ask for approval or action. When both are unavailable, the participant doesn't take ownership of the decision or form a Plan B — they repeatedly ping Tanya with increasing urgency but without naming the cost trade-off. The escalation eventually works but lacks quality context.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "@shay @daniel dont you think if we rollback the deployements on checkout service will resolve this issue" / "Is it causing the issue now ? Can you verify it ?"

**Rationale:**
The participant proposes the rollback as a test but doesn't articulate an explicit hypothesis connecting the checkout deployment to outbound gateway handshake failures. When the cert rotation is surfaced, they ask "Is it causing the issue now?" which is a test request but without articulating the mechanism. Hypotheses are implicit rather than explicitly stated and tested — the participant acts on suggestions from NPCs rather than forming their own theories.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "We could see some disks are using expired certificates even though the new certificate is present. Tanya is running the reloading"

**Rationale:**
The participant does relay findings (e.g., the expired certificate discovery) but rarely synthesizes multiple pieces of evidence to narrow scope. They don't use the failed rollback as elimination evidence, don't synthesize Daniel's "failure is at connection layer" with the change log to rule out app deploys, and don't name what's been ruled out. Most narrowing is done by NPCs (Daniel, Tanya) rather than the participant.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "Will restarting impact anything ?"

**Rationale:**
The participant does ask about restart consequences before executing, which shows some awareness. However, this is the only instance of consequence-weighing in the entire drill. They didn't consider consequences before rolling back CheckoutService, didn't weigh the cost of pulling Tanya off the vendor call (Tanya volunteered after repeated pings), and didn't ask "is it safe?" on any earlier action. The single instance at the end is insufficient for tier 3.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "We need to check this issue from platform side, Hamed is off today and Tanya is busy with Vendor call on email maintenance."

**Rationale:**
After the rollback fails, the participant does recognize they need to shift to the platform side, which shows some adaptation. However, the pivot is slow and largely driven by NPC suggestions (Daniel: "we need Tanya to check from the platform side"). The participant doesn't independently reframe the problem or propose alternative hypotheses — they follow the team's lead rather than driving the pivot. After the cert reload fails, they suggest removing the old cert, which shows some adaptation but the drill ended before full resolution.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Hi @bez No one can check out right now. Zero successful transactions since this started. We're losing about £1,000 to £1,500 every minute." / "We are working on it Bez, cause of the issue is still unclear."

**Rationale:**
The first update to Bez includes impact numbers (relayed from Bob) but no working theory, no ETA, and no committed next-update time. The second update ("working on it, cause unclear") is a vague reassurance. When Bez asks for a concrete ETA, the participant doesn't provide one. The later cert-related update to Bez mentions disks and certificates but is technical rather than business-framed. No committed cadence is maintained.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 1

**Evidence:**
> "We could see the logs are pointing out at connection issues. errors on outbound gateway handshakes, could you please look into it"

**Rationale:**
The participant rarely synthesizes findings for the technical team. They don't post summary statements about what's been ruled out or what the current working theory is. Most of their messages to the technical channel are questions or requests rather than synthesis. The one instance of scope communication ("errors on outbound gateway handshakes") is a relay of what Daniel already reported, not an independent synthesis that orients the team.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 2 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 1 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 1 |
| **Mean Marker Score** | **1.92** |

---

## Caveats
- The drill ended abruptly ("Drill Wrap-Up") just as the participant was exploring the restart path. The participant asked "Will restarting impact anything?" but never got to make the restart decision. This truncation means L3 (ownership override moment) and M5 (adaptation after restart failure) could not fully manifest. However, based on the pattern up to that point, the ratings reflect what was observed rather than what might have happened.
- K2 rating is a boundary call between 1 and 2. The participant did relay Bob's impact numbers to Bez (which is more than "we're investigating"), but never provided a working theory, ETA, or committed next-update time, and the second update was vague. Rated 2 for partial engagement.
- C7 is also a boundary call. The participant did work through the escalation chain (Hamed → Tinus → repeated Tanya pings), but the quality of escalation context was low and they never formed a Plan B or made an override decision themselves.

---