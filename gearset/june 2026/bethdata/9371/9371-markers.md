---

# Markers Analysis — 9371

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "They are not available. I will need to make that call." ... "They're not available, so I'm taking ownership, please restart"

**Rationale:**
The participant explicitly takes ownership of the restart decision when both approvers are unavailable, using clear "I" framing and directing Tanya to proceed. However, they don't proactively name the cost or blowback risk ("blowback's on me") — they simply state they're taking ownership. They drive the response throughout but the ownership declaration is functional rather than emphatic.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob what are the complaints like?" ... "and how many are coming in?" ... "How many customers are blocked right now? What's the revenue loss per minute? Is this a total checkout outage or just some regions?"

**Rationale:**
The participant's first actions after Bob's alert are clarifying questions about the nature, volume, and scope of complaints. They ask about complaint type, quantity, and regional scope before taking any remediation action. They also ask Bob for revenue impact quantification. This is solid scope-validation before acting.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "Cool, @tanya can you look into this?" [after Shay mentions email maintenance timing] ... "Can you double check if the email maintanence could be causing issues?"

**Rationale:**
The participant does engage with the email maintenance as a recent change and asks about it multiple times. However, they never explicitly ask for a change log or review recent deployments systematically. They fixate on the email maintenance correlation without using evidence to eliminate it — Tanya explicitly states email confirmations are fine and it can't cause checkout failures, yet the participant asks about it again later. They don't use the change log as a candidate-elimination pass.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@daniel can you start with the payment service, and @shay can you start with the product catalogueservice?" ... "@daniel @shay can one of you check the logs of the payment service"

**Rationale:**
The participant consistently uses @mentions to assign specific tasks to specific people. They route log checks to Daniel, platform checks to Tanya, and reproduction to Shay. The routing is mostly appropriate — they correctly pull Tanya in for platform-level cert work. However, some asks are slightly imprecise (e.g., "@daniel @shay can one of you check" rather than naming one person).

---

## C6 — Runs parallel investigation threads

**Rating:** 3

**Evidence:**
> "@daniel can you start with the payment service, and @shay can you start with the product catalogueservice?"

**Rationale:**
The participant explicitly fans out investigation to two people simultaneously — Daniel on PaymentService and Shay on ProductCatalogueService. This is a clear parallel investigation move. Earlier they also ask Shay to reproduce while asking Bob for more details. The parallelism is present but not deeply layered or strategically sequenced throughout the drill.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tinus Hamed is off today, can we get sign off to restart the payment service process? Context is we did a cert rotation but the process hasn't picked up the new one and is still referencing the one that's expired"

**Rationale:**
The participant escalates to Tinus with good context (what's needed, why, what the problem is). When Tinus auto-replies, they accept the situation and take ownership themselves rather than leaving the chain hanging. They also pull Tanya off the vendor call when needed. The escalations include context but don't explicitly name the cost of the escalation (e.g., losing the vendor window).

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Can you double check if the email maintanence could be causing issues?" ... "Okay that makes sense, what could be causing the TLS failures?"

**Rationale:**
The participant doesn't explicitly articulate hypotheses in a structured way. They pursue the email maintenance thread without naming it as a hypothesis to test, and they don't explicitly pivot when Tanya rules it out — they ask about it again later. When the cert issue emerges, they follow the evidence but don't frame it as "hypothesis: expired cert → test: check cert status." The reasoning is reactive rather than hypothesis-driven.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "Okay the running process is using an expired cert it seems" ... "To me the expired cert seems to be the definite issue"

**Rationale:**
The participant does use evidence to narrow scope at key moments. When Daniel reports PaymentService outbound failures and clean logs elsewhere, the participant focuses investigation on PaymentService. They synthesize the cert expiry finding and use it to justify the restart decision. However, they don't produce explicit synthesis statements ruling things out — the narrowing happens more through following NPC guidance than through independent evidence synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "I would say this is probably urgent. What are the issues caused by a payment service restart @shay" ... "What's the runbook to recover those dirty payments?"

**Rationale:**
The participant does ask about risks of the restart and asks about recovery procedures, showing some consequence awareness. However, they don't check the bundle on disk before the first restart, don't ask "is it safe?" before pulling Tanya off the vendor call (they say "It's fine if we lose the rollout slot" without weighing it), and don't anticipate secondary failure modes. The consequence consideration is present but limited.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "@daniel @shay can one of you check the logs of the payment service" [after restart fails] ... "payments service needs a two-cert bundle to authenticate, tanya can you open the bundle file and check what's in there?"

**Rationale:**
After the first restart fails, the participant doesn't retry the same action. They immediately ask for new logs and engage with the new information (certificate chain broken). When Tanya reveals it's a bundle issue, the participant adapts and pursues the bundle ordering fix. They don't get stuck in a loop. However, they don't explicitly name the shift in failure mode — they follow the team's guidance rather than independently recognizing the structural difference.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Seems like the payment service is encountering issues with TLS" ... "Restarting the servcie did not work, but we've identified another issue with the SSL certificate that we're currently fixing" ... "We think the issue is now resolved, things are looking positive"

**Rationale:**
The participant provides some updates to Bez but they are mostly technical and lack business framing. They don't quantify impact in business terms (revenue loss, customer count), don't commit to next-update times, and the updates are brief and reactive rather than proactive. The "TLS" update is technical jargon for a business audience. No committed ETA or cadence is established.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "People can't go through checkout, we're trying to find the RC" ... "ACK @shay but let's look at the other services for nwo"

**Rationale:**
The participant rarely synthesizes the current state of knowledge for the technical team. They don't post summary statements like "we've ruled out X, focusing on Y." Their technical channel communication is mostly questions and acknowledgments rather than synthesis. When they do communicate scope ("People can't go through checkout, we're trying to find the RC"), it's brief and doesn't name what's been ruled in or out.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 3 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 3 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.58** |

---

## Caveats
- For C3, the participant engages with the email maintenance change but never asks for a formal change log or reviews deployments systematically. The rating reflects that they asked about a change but didn't use the information effectively for elimination.
- For M2, the participant's hypothesis work is largely implicit and reactive — following NPC suggestions rather than articulating and testing their own theories. This is a borderline 2/3 call; rated 2 because no explicit hypothesis is named or tested by the participant independently.
- For K2, the participant's updates to Bez are present but lack business framing, quantification, and committed cadence — borderline 1/2, rated 2 because updates do exist and contain some information.
- Anti-outcome-bias note: The successful resolution and NPC praise at the end were not factored into any ratings.

---