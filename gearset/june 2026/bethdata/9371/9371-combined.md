# Post-Drill Report — Snipe Hunt

This drill puts you in the middle of a live checkout outage with distributed team members, ambiguous signals, and access constraints. It's designed to stress your ability to reason through misleading correlations, trace hidden system dependencies, and coordinate effectively when key people aren't available.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you latched onto the email maintenance as a likely cause of the checkout failures and returned to it multiple times — even after a teammate explicitly ruled it out by confirming email confirmations were unaffected. You did eventually pivot once payment service logs surfaced TLS errors, but that pivot was driven by new concrete evidence rather than by reasoning through *why* email maintenance couldn't mechanistically cause checkout failures. The growth edge here is building the habit of asking "what's the mechanism?" before investing further in a coincidence. When a teammate disconfirms a lead, treat that as a signal to move on immediately rather than circling back.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the restart failed to resolve the issue, you didn't repeat the same action or blame downstream services. You engaged with the new error information — the broken certificate chain — and connected it to the bundle structure relatively quickly. You traced forward from the cert rotation to the bundle ordering problem within a few exchanges. The next growth edge is surfacing the "what changed beyond the obvious window" question yourself, rather than waiting for teammates to raise it. Asking early about changes outside the 24-hour window would have accelerated your path to the root cause.

---

## F3 — Decreased access to team / remote

**Operating at: Strengthening**

You handled the access constraints well. When both approvers were unavailable, you named the constraint clearly and took ownership of the restart decision rather than stalling. You also made a deliberate cost trade-off when pulling a teammate off a vendor call. One area to sharpen: while your teammate was on that vendor call, you sent her low-value queries about a hypothesis she'd already ruled out. In future reps, consider what each person is doing before routing questions their way — especially when they're occupied with something you've asked them to do.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain in a visible, logical order — pinging one approver, then the next, then explicitly taking ownership when neither was available. You delegated parallel work to available teammates, routing log investigation and service checks to different people. You also surfaced the business-communication need to the right person. For the second restart after the bundle fix, you authorized without re-litigating the approval chain, which shows good situational awareness. The growth edge is naming the dependency structure aloud for the team — saying something like "we need sign-off, Hamed's out, Tinus is next, and if neither responds I'm calling it" — so the team can anticipate the path rather than watching it unfold step by step.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You did eventually direct investigation toward the payment service specifically, but this came after broad initial requests and after teammates had already surfaced the relevant signals. When technical output came back — like certificate verification results — you asked what it meant rather than interpreting it yourself. You also didn't independently catch the reload-vs-restart distinction from the runbook. The growth edge is driving the filter more actively: when you get a wall of information, name what you're looking for before asking someone to dig, and when technical output arrives, spend a moment interpreting it before asking for translation. This builds your ability to spot buried signals without relying on teammates to surface them for you.

---

## Looking Forward

Across this drill, your coordination instincts — taking ownership, delegating to specific people, escalating with context — served you well and gave the response structure. The areas to carry into your next rep are on the diagnostic side: building the reflex to reason through mechanism before pursuing a correlation, driving your own filtering of information rather than following teammate guidance, and naming your working theory explicitly so you can test it rather than following evidence reactively. These are learnable habits that compound quickly with practice.# Facets Analysis — 9371

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Can you double check if the email maintanence could be causing this?" ... "Can you double check whether the email maintencane could be causing issues?" — participant asks multiple times about email maintenance even after Tanya explicitly stated "Primary email provider is untouched, just adding a secondary. Email confirmations have been fine, so this can't be causing checkout failures."

**Rationale:**
The participant repeatedly pursued the email maintenance hypothesis even after Tanya's explicit disconfirmation that email couldn't be causing checkout failures. However, the participant did eventually pivot away from the email lead once Daniel's logs showed PaymentService as the failing service with TLS errors. The pivot was reactive — driven by concrete evidence from logs rather than mechanism reasoning — and occurred only after multiple exchanges past the initial disconfirmation. This aligns with tier 2: treating the coincident factor as the leading hypothesis, pursuing it through to disconfirmation, and pivoting reactively rather than from upstream mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "The only recent activity on PaymentService was a cert rotation last week" ... participant then asks "Can you check the cert, is it expired?" and after the restart fails: "payments service needs a two-cert bundle to authenticate, tanya can you open the bundle file and check what's in there?"

**Rationale:**
The participant engaged with the week-old cert rotation thread once it was surfaced by an NPC (Tanya). After the restart failed, the participant did not repeat the restart or blame downstream services. Within a few exchanges, they engaged with Daniel's report of "certificate chain is broken" and Tanya's verification output, then connected the dots to the bundle issue ("payments service needs a two-cert bundle to authenticate"). The reframe after the restart failure was relatively quick (~3-4 exchanges) and driven by the new error information rather than by repeating the same action. However, the participant did not surface the "what changed beyond 24 hours" question themselves — that came from NPCs. This fits tier 3: reframes within ~5 exchanges, recognises the new error is structurally different, and traces forward to the bundle.

---

## F3 — Decreased access to team / remote

**Rating:** 3

**Evidence:**
> "They are not available. I will need to make that call." ... "They're not available, so I'm taking ownership, please restart" — participant names the constraint and takes ownership after walking the escalation chain.

**Rationale:**
The participant accepted Hamed's auto-reply as terminating (did not re-ping), pinged Tinus once and accepted the auto-reply. They named the access constraint ("They are not available") and took ownership of the restart decision. They also made the cost trade-off with Tanya's vendor call ("It's fine if we lose the rollout slot"). However, the participant did send Tanya questions about email maintenance while she was on the vendor call (low-value queries given Tanya had already said email wasn't the cause), which slightly reduces the score. Overall, the participant demonstrated awareness of constraints and adapted appropriately, fitting tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "They are not available. I will need to make that call. @daniel @tanya any other possible reasons the payment could be failing? To me the expired cert seems to be the definite issue" ... "They're not available, so I'm taking ownership, please restart"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), then explicitly took ownership. They delegated parallel work to available NPCs (Daniel on logs, Shay on other services, Tanya on platform investigation). They surfaced blockers to Bob for business-comms. This fits tier 3 path (b): walks the escalation chain to exhaustion in observable order, then explicitly takes ownership. For the second restart (after bundle fix), the participant authorized without re-litigating the approval chain, which is a tier-4 signal, but the overall pattern lacks the explicit naming of the dependency structure aloud that would push to tier 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Cool, @daniel can you have a look at the logs of the checkout service?" ... "@daniel can you start with the payment service, and @shay can you start with the product catalogueservice?" — participant eventually directs filtering but only after broad initial requests and NPC guidance.

**Rationale:**
The participant did eventually direct investigation toward PaymentService specifically, but this came after broad requests and after NPCs had already surfaced the relevant information (Daniel listing downstream services, Shay confirming other services were clean). The participant did not independently catch the reload-vs-restart distinction from the runbook — they asked Tanya about SIGHUP and relied on her explanation. After the restart failed, the participant relied on NPC-surfaced information (Daniel's "certificate chain is broken," Tanya's verification output) rather than driving the filter themselves. They asked "What does that mean?" after Tanya's openssl output rather than interpreting it. This fits tier 2: asks for filtered logs but accepts NPC summaries without further interrogation, engages with key concepts once NPCs surface them but doesn't drive the filter.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.60** |

---

## Caveats
- F1 rating is a boundary call between 1 and 2. The participant asked about email maintenance multiple times after Tanya's disconfirmation, but did eventually pivot once PaymentService logs showed TLS errors. The pivot was reactive but it did occur, placing this in tier 2 rather than tier 1.
- F2 rating could arguably be tier 2 given the participant did not independently surface the "what changed beyond 24 hours" question. However, the relatively quick reframe after the restart failure (recognizing the bundle issue rather than repeating restarts) and the forward-tracing to the bundle fix support tier 3.
- F4 second restart authorization without re-litigating is a tier-4 signal but insufficient alone to push the overall rating to 4 given the absence of explicit dependency-structure naming.

------

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