# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, hidden system dependencies, constrained team availability, and a volume of technical detail that needed active filtering. The observations below reflect how you engaged with each of these dimensions during the run.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill you explored the email maintenance timing as a possible cause, asking team members whether it was related. You moved away from this thread once concrete log evidence pointed elsewhere — specifically when PaymentService handshake failures surfaced. The pivot was driven by what others brought you rather than by your own reasoning about whether the email maintenance *could* mechanistically affect payment handshakes. On the next rep, try pausing when a coincidence surfaces and asking yourself: "What would the causal chain have to look like for this to be the cause?" If you can't sketch one, you can deprioritise it earlier and preserve investigation bandwidth.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

After the first restart failed to resolve the issue, you moved quickly to investigate the new error rather than retrying the same action. You engaged with the structural difference — asking what the "unable to get local issuer certificate" error meant — and followed the thread toward the certificate bundle fix. This showed recognition that the situation had changed and that a different failure mode was now in play. The growth edge here is surfacing the "what changed beyond the obvious?" question yourself rather than waiting for a team member to volunteer it. Asking "why would a fresh cert still fail?" before someone else explains it would move you toward independently tracing hidden dependencies.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You encountered multiple unavailable team members (auto-replies from Hamed and Tinus) and worked through the escalation chain to unblock the restart. You also pulled Tanya off a vendor call when the situation demanded it. However, you didn't name the constraint pattern aloud — articulating something like "we've lost access to the two people who normally approve this, so here's how I'm going to handle it." You also didn't visibly batch or economise your asks to Tanya, who was your most constrained resource. On the next rep, try explicitly naming access constraints when they appear: who's unavailable, what that blocks, and how you'll route around it. This makes your reasoning visible and helps the team anticipate bottlenecks.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You navigated the approval dependency for the restart by working through available contacts, and on the second restart you authorised without re-litigating — showing some learning within the drill. The growth area is in how you take override decisions. Rather than routing the decision through an indirect claim of someone else's approval, owning the call explicitly ("I'm authorising this; here's why") makes the decision structure clear to the team and creates an auditable record. You delegated well to available people — assigning platform investigation, log review, and security checks to the right individuals — which supported parallel progress. The next step is naming the dependency structure itself: "We're blocked on X, the normal approver is unavailable, I'm unblocking us by doing Y."

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You made targeted asks — requesting PaymentService logs specifically, asking about downstream service errors — which shows awareness that you need to filter. However, when information came back (cert comparisons, bundle output), you tended to ask "what's the issue now?" rather than interpreting the data yourself. You relied on team members to surface and explain key signals rather than driving the filter independently. On the next rep, when a team member presents output, try stating what you see before asking what it means: "I see the in-memory cert is expired but the on-disk cert is valid — so the service didn't pick up the new cert?" This builds your own interpretive muscle and keeps you in the driver's seat.

---

## Looking Forward

Across this drill, your strongest process was recognising when the situation changed after a failed remediation and redirecting investigation rather than repeating the same approach. You also fanned out work to multiple people early, which kept threads moving in parallel. The consistent growth edge is moving from reactive to proactive: naming constraints before they block you, articulating hypotheses before evidence forces a pivot, and interpreting data before asking others to summarise it. On your next rep, pick one of these — perhaps stating your working hypothesis aloud before asking someone to check it — and see how it changes the shape of the investigation.# Facets Analysis — 9502

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Tanya are email maintenance any how related?" ... "Shay what did email maintenance doing?" ... Later, after Daniel identifies PaymentService errors: participant shifts focus to PaymentService and pulls Tanya off vendor call to investigate platform-side TLS issue.

**Rationale:**
The participant initially entertained the email maintenance correlation, asking Tanya about it and engaging with Shay's repeated nudges about the timing. However, once Daniel surfaced PaymentService logs showing handshake failures and Shay noted "This failure is at the connection layer, that's Tanya's domain," the participant pivoted to the cert/TLS investigation. The pivot was reactive — driven by concrete log evidence rather than upstream mechanism reasoning ("does email plausibly break payment handshakes?"). The participant never explicitly dismissed the email correlation on mechanism grounds, but did move on once disconfirming evidence accumulated. This fits tier 2: pursued the coincident factor as a leading hypothesis, pivoted reactively after concrete evidence rather than from mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> After restart fails: "Tanya whats the log saying now? is it still same?" ... Tanya reports "ssl errors in logs, cert chain broken" and "new cert loaded but service still failing connecting to gateway" ... Participant asks "Tanya what does 'error 20 at 0 depth lookup: unable to get local issuer certificate' mean?"

**Rationale:**
After the first restart failed, the participant did not repeat the restart or blame downstream services. Within a few exchanges, they asked Tanya about the new error message, indicating recognition that the situation had changed. They engaged with the structural difference (chain verification vs. expiry) by asking what the error meant and then driving toward the bundle fix. However, the participant did not independently surface the "what changed beyond 24 hours" question — Daniel volunteered the cert rotation history. The participant also didn't articulate "this is a different failure" explicitly but did pursue the new error thread promptly. This fits tier 3: reframes within ~5 exchanges of the restart failing, recognises the new error is structurally different, and traces forward to the bundle with NPC assistance.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "Hamed can you get me the logs?" [receives auto-reply] ... "Tinus can you allow Tanya to restart the payment service" [receives auto-reply] ... "Bez can you allow Tanya to restart the payment service" ... "I've talked to Bez and its fine to do so"

**Rationale:**
The participant pinged Hamed for logs despite Hamed being on holiday (receiving an auto-reply), then later pinged Tinus (also unavailable) and Bez for restart approval. The participant did not articulate the access constraints in their own words at any point. They pulled Tanya off the vendor call decisively ("Yes Tanya this is important, its fine to miss the slot") but without explicitly naming the cost trade-off. The claim "I've talked to Bez and its fine to do so" appears to fabricate approval rather than owning the override decision. There's no visible batching of questions to Tanya or economising on constrained channels. This fits tier 2: walks the escalation chain but doesn't articulate the constraint pattern or make reasoned trade-off statements.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "Tanya just go ahead" ... "I can't proceed, the restart needs approval from Hamed or Tinus" ... "I've talked to Bez and its fine to do so" ... For the second restart after bundle fix: "restart the service" — no re-litigation of approval.

**Rationale:**
The participant attempted to get approval from Tinus (auto-reply) and Bez, then claimed Bez had approved rather than explicitly owning the override decision themselves. They did not name the dependency structure aloud or articulate that the escalation chain was exhausted. The override was taken under pressure from the situation rather than through a reasoned statement of authority. However, on the second restart, the participant authorized without re-litigating, showing some learning. The participant delegated work to available NPCs (Daniel on logs, Tanya on platform) but didn't proactively surface blockers in business-comms. This fits tier 2: takes the override call without clearly walking the escalation chain to exhaustion or naming the bottleneck structure.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Daniel can you tell me what downstream services is showing error" ... After Daniel surfaces PaymentService logs: "Daniel PaymentService? whats the log saying" ... "can be SSL certificate expired? Daniel check" ... After bundle output shown: "so whats the issue now?"

**Rationale:**
The participant asked for filtered information (PaymentService logs specifically, downstream service errors) which shows some targeting. However, they relied heavily on NPCs to surface and interpret key signals. When Tanya showed the cert comparison (expired in-memory vs. valid on disk), the participant asked "whats the fix here?" rather than reasoning about the reload-vs-restart distinction themselves. After the bundle order output was displayed, the participant asked "so whats the issue now?" despite the information being clearly presented. They did not independently catch the reload-vs-restart distinction from the runbook or reason about absence of signal. This fits tier 2: asks for filtered logs but accepts NPC summaries without further interrogation; engages with key concepts once NPCs surface them but doesn't drive the filter.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.20** |

---

## Caveats
- F3/F4 boundary call: The participant's claim "I've talked to Bez and its fine to do so" is ambiguous — it could be interpreted as a creative workaround to unblock Tanya or as fabricating approval. I rated it as not constituting genuine ownership of the override decision, which kept both F3 and F4 at tier 2 rather than tier 3.
- F2 tier 3 vs tier 4: The participant did not independently surface the "what changed beyond 24 hours" question (Daniel volunteered it), which is a key tier-4 differentiator. The reframe after restart failure was prompt but NPC-assisted, placing this solidly at tier 3.
- Anti-outcome-bias note: The participant successfully resolved the incident, but ratings are based on process evidence (how they engaged with each facet) rather than the resolution outcome.

------

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