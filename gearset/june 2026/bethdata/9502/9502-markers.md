---

# Markers Analysis — 9502

## L3 — Takes explicit ownership of the response

**Rating:** 2

**Evidence:**
> "Tanya just go ahead" / "I've talked to Bez and its fine to do so"

**Rationale:**
The participant attempts to authorize the restart but does so indirectly — claiming Bez approved it (Bez never explicitly did) rather than taking personal ownership ("this is my call, blowback's on me"). Throughout the drill, the participant directs tasks but never explicitly positions themselves as the decision-maker accepting consequences. They try to pass the approval through others rather than owning the override.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "How many customers are blocked from checking out? What's the revenue loss per minute right now?" / "Bob how many people affected? regions?" / "Is checkout totally down for all users or are any transactions getting through at all?"

**Rationale:**
The participant's first substantive moves include multiple scope-validating questions to Bob (volume, regions, revenue impact, partial vs. total outage) before taking remediation actions. They also ask about the nature of the failure pattern. This meets the novice expectation of gathering information before acting.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "Daniel can you look into recent commits that may have caused this?" / "Daniel list of changes since this issue arrised" / "Daniel what was last CheckoutService change?"

**Rationale:**
The participant asks for the change log and reviews recent deployments. However, after receiving the list and Shay's note that "none of these changes look like they'd break checkout end-to-end," the participant doesn't explicitly use this as elimination evidence. They continue to entertain the email maintenance correlation without articulating why changes are or aren't connected mechanistically. They asked but didn't synthesize the answer into a narrowing statement.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "Tanya we have lost all the orders per min, what is the platform looking like? investigate this please" / "Daniel can you look into recent commits that may have caused this?" / "Maya we have dropped all the checkout, can you check if we have any security issue?"

**Rationale:**
The participant consistently names specific people for specific tasks throughout the drill — Tanya for platform, Daniel for logs/changes, Shay for investigation, Maya for security, Bob for the banner. Most assignments are appropriately routed to the right person. This meets the novice expectation of naming specific people for specific tasks.

---

## C6 — Runs parallel investigation threads

**Rating:** 3

**Evidence:**
> "Tanya we have lost all the orders per min, what is the platform looking like?" / "Daniel can you look into recent commits that may have caused this?" / "Bob how many people affected? regions?"

**Rationale:**
Early in the drill, the participant fans out multiple asks in close temporal sequence — Tanya on platform, Daniel on changes, Bob on scope. Later they also task Maya on security while Daniel and Tanya work the payment logs. Multiple threads run concurrently rather than purely sequentially, meeting the novice expectation.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "Tinus can you allow Tanya to restart the payment service" / "Bez can you allow Tanya to restart the payment service, so it can pick up the certificate changes" / "Tanya just go ahead"

**Rationale:**
The participant works through the escalation chain (Hamed auto-reply → Tinus auto-reply → Bez), which shows awareness of the need to escalate. However, the escalation to Bez lacks context about why it's urgent or what the cost is, and Bez never explicitly approves. The participant then tells Tanya "I've talked to Bez and its fine" — which is inaccurate. The escalation is attempted but lacks quality context and clear resolution.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Tanya are email maintenance any how related?" / "can be SSL certificate expired? Daniel check"

**Rationale:**
The participant entertains hypotheses (email maintenance, SSL certificate expiry) but rarely articulates them explicitly as testable theories. The email maintenance hypothesis is raised as a question rather than a named hypothesis with a proposed test. The cert hypothesis ("can be SSL certificate expired?") is closer to a named hypothesis with a test, but it comes late and only after Daniel's logs pointed directly there. The participant mostly follows NPC leads rather than forming and testing their own hypotheses.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "SSL certificate verification is failing for payment service" / "Is checkout totally down for all users or are any transactions getting through at all?"

**Rationale:**
The participant asks good scoping questions early (all users? all regions?) but rarely synthesizes evidence into narrowing statements. They don't explicitly rule things out — the email maintenance thread lingers without being formally eliminated. When Daniel and Tanya provide evidence pointing to PaymentService outbound failures, the participant acknowledges it but doesn't produce synthesis statements combining multiple evidence points. Most narrowing is done by NPCs, not the participant.

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "Yes Tanya this is important, its fine to miss the slot" / "Tanya just go ahead" / "restart the service"

**Rationale:**
The participant acknowledges the cost of pulling Tanya off the vendor call ("its fine to miss the slot") but doesn't weigh it or name the trade-off explicitly. For the restart, there's no "is it safe?" check, no consideration of what could go wrong, and no anticipation that the restart might expose a secondary issue. Actions are fired without consequence-weighing throughout the drill.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Tanya whats the log saying now? is it still same?" / "Tanya what does 'error 20 at 0 depth lookup: unable to get local issuer certificate' mean?" / "so whats the issue now?"

**Rationale:**
After the first restart fails, the participant doesn't retry the same action or give up. They ask what's different now, engage with the new error message, and follow the cert chain thread to the bundle ordering issue. While the participant relies heavily on NPCs to explain the new failure mode, they do redirect investigation rather than repeating the failed approach. This meets the novice expectation of not repeating the same action after failure.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "customer unable to checkout" / "we are looking into it" / "30 mins" / "SSL certificate verification is failing for payment service"

**Rationale:**
Updates to Bez are sparse and lack substance. "We are looking into it" is the classic vague reassurance the rubric flags. "30 mins" is an ETA without context. "SSL certificate verification is failing for payment service" is technical detail without business framing. The participant never quantifies impact in business terms for Bez, never commits a next-update time, and doesn't proactively update when the first restart fails.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Tanya telling me why the outbound gateway handshakes failing for payments service" / "so whats the issue now?" / "we need to fix the order"

**Rationale:**
The participant rarely posts synthesis statements to the technical channel. They ask questions and relay information back as questions rather than summarizing state for the team. "So whats the issue now?" is asking the team to synthesize rather than doing it themselves. The brief "we need to fix the order" is a synthesis moment but comes only after Tanya and Daniel have already explained it. The team is mostly self-organizing around the participant's questions rather than being oriented by synthesis.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 2 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 3 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.25** |

---

## Caveats
- L3 rating is a boundary call between 2 and 3. The participant does direct the response and makes the restart call, but the ownership is indirect (claiming Bez approved when Bez didn't explicitly do so) rather than explicit personal ownership. Rated 2 because the override is achieved through misrepresentation rather than explicit self-authorization.
- C7 is also a boundary call. The participant does work the chain (Hamed → Tinus → Bez → self-authorize), but the quality of escalation context is low and the resolution is questionable (Bez never explicitly approved).
- M4 rating of 1: The participant does say "its fine to miss the slot" which acknowledges a consequence, but this is more of a dismissal than a weighing. Considered rating 2 but the absence of any "is it safe?" or consequence-weighing on the restart actions (the higher-stakes moments) kept it at 1.

---