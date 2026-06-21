# Post-Drill Developmental Report

This drill placed you in the middle of a live checkout outage requiring you to coordinate a distributed team, navigate misleading signals, and make decisions under time pressure with limited access to senior engineers. The complexity here is systemic — multiple services, layered dependencies, and information that doesn't point cleanly in one direction.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you identified the email maintenance window as a potential cause based on timing overlap with the outage. You pursued this lead persistently — asking Tanya to roll back changes — even after she clarified that her work was paused before anything reached production and that the email system is architecturally separate from checkout. You did eventually pivot once payment logs surfaced TLS handshake failures, which showed responsiveness to concrete disconfirmation.

The growth edge here is building the habit of asking *how* a candidate cause could produce the observed symptom before investing investigation time in it. When a correlation surfaces, naming the mechanism ("if email maintenance caused this, the path would be…") helps you test it faster and release it sooner when the mechanism doesn't hold.

---

## F2 — Hidden coupling

**Operating at: Practicing**

The deeper structural issue — that a cert rotation from days earlier interacted with the payment gateway's bundle requirements — was surfaced by your teammates rather than through your own questioning. After the restart failed to resolve the outage, you did request a bundle verification, which shows engagement with the coupling. However, you didn't independently reframe the problem when the restart didn't work — the shift came after NPC guidance about the two-cert bundle requirement.

On the next rep, practice asking "what changed beyond the obvious window?" earlier, and when a fix doesn't hold, treat that as a signal that the problem has a different shape than you assumed. The restart failure was structurally informative — it told you the issue wasn't just an expired cert.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You walked the escalation chain from Hamed to Tinus, which is appropriate. When both were unavailable, you re-pinged them rather than immediately adapting to the constraint. You did eventually accept the situation and take ownership of the restart approval yourself. When working with Tanya — your primary available engineer — you directed her toward tasks without explicitly acknowledging her bandwidth limitations or batching your requests to economise her time.

The growth edge is recognising access constraints as a *design input* rather than an obstacle to push against. When a key person is unavailable, the next move is "what can I do with who I have?" rather than repeated attempts to reach the unavailable person.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You took the restart approval decision after learning both approvers were out of hours, which was the right call. The decision came after Tanya explicitly flagged the approval requirement and asked who would take responsibility. You didn't proactively identify the approval bottleneck or sequence work to avoid it. Earlier in the drill, time was spent on the email hypothesis while cert investigation could have been running in parallel — this represents a missed opportunity to manage dependencies by keeping multiple paths active.

For the next rep, look for moments where you can name the dependency structure aloud: "We need approval, both approvers are out, so I'm taking this." That framing — even briefly — signals to the team that you see the bottleneck and are actively managing it. Your delegation also tended toward vague asks rather than scoped, actionable tasks matched to each person's access and expertise.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

The path from checkout errors to PaymentService to TLS failures to the cert issue was largely navigated by your teammates surfacing filtered logs and drawing conclusions. You followed the evidence trail once it was presented, asking reactive questions like whether the rotation could be the issue. You didn't independently drive filtering or use absence of signal as a narrowing tool.

The growth edge is taking a more active role in directing *what* gets looked at and *why*. Rather than asking the team to "see the logs" broadly, try specifying what you're looking for: "Show me outbound connections from PaymentService — I want to know if it's failing to reach the gateway."

---

## Looking Forward

Across this drill, the consistent pattern is reactive engagement — you followed leads and accepted direction from teammates, and you did eventually arrive at productive actions. The next developmental step is moving from reactive to directive: naming your working theory aloud, specifying what evidence would change your mind, and treating constraints (unavailable people, failed fixes) as information that reshapes your approach rather than obstacles to retry. Carry that into your next rep — the goal isn't to know the answer faster, but to *drive the investigation* rather than follow it.
---

# Facets Analysis — 9058

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Looking at the arctichetire there is email service which is connected to checkout.. it may have caused this issue" ... "as the issue started at same time" ... "@tanya - Can we not rollback the changes"

**Rationale:**
The participant committed heavily to the email maintenance correlation, repeatedly asking Tanya to roll back her changes and explicitly citing the timing coincidence as evidence of causation. Tanya directly stated "Email work was paused before anything went live on prod" and "This isn't related to checkout—totally separate system," yet the participant continued pursuing this lead for several more exchanges. However, the participant did eventually pivot away from the email hypothesis once payment logs showed TLS handshake failures, moving to the cert investigation. This reactive pivot after concrete disconfirmation (not mechanism reasoning) places the participant at tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "Wait — it restarted and it's still down? That shouldn't happen if the cert was the only problem." ... "Please checek the bundle - penssl verify -CAfile /etc/ssl/certs/ca-bundle.crt payment-gateway.crt"

**Rationale:**
The participant did not independently surface the "what changed beyond the last 24 hours" question — it was Shay/Daniel who identified the cert rotation from 7 days ago. After the restart failed, the participant showed some confusion ("Hopefully this shud bring the server up") but then asked Tanya to check the bundle within a few exchanges. The participant did not articulate that the post-restart failure was structurally different from the original expiry issue. The bundle check request came after NPC prompting ("payments service needs a two-cert bundle to authenticate"), placing this at tier 2 — reactive engagement with the coupling after NPC direction rather than independent reframing.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@hamed - What wud you suggest please" ... "@tinus - In absense of Hamed .. wud you be able to suggest further" ... "@tinus @hamed - Need escalation as we arent able to get the direction form available technical resouces"

**Rationale:**
The participant walked the escalation chain (Hamed → Tinus) but then re-pinged both after receiving auto-replies, which is a tier-1 signal. However, the participant did eventually accept the constraint and take ownership of the restart approval. The participant pulled Tanya off the vendor call without articulating the cost trade-off explicitly — simply asking her to roll back changes rather than framing it as a deliberate decision. There's no visible batching of questions or economising on Tanya's constrained bandwidth. The participant shows partial adaptation but without articulating constraints.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "They both are oOH and i approve" ... "I aprrove please prceed"

**Rationale:**
The participant did take the restart approval decision after Tanya flagged the requirement, but only after Tanya explicitly stated "I can't restart payments without approval from Hamed or Tinus." The participant's ownership statement was brief ("They both are OOH and I approve") without naming the escalation chain as exhausted or articulating the dependency structure. The participant did not sequence parallel work effectively — much time was spent on the email red herring while cert investigation could have been pursued. The override was taken after NPC prompting rather than proactive recognition of the bottleneck, placing this at tier 2.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Payemnt serice is hsowing no outbound cinnection?" ... "can the rotation be a issue?" ... "WHy does it says expired ??"

**Rationale:**
The participant did eventually focus on PaymentService after seeing the payment logs, but this was largely NPC-driven (Daniel and Shay surfaced the filtered logs and the cert rotation history). The participant asked reactive questions ("can the rotation be a issue?") rather than driving the filter proactively. The reload-vs-restart distinction was presented by Tanya as options rather than discovered by the participant in the runbook. The participant did not independently reason about absence of signal or catch the bundle ordering issue — Shay identified it. The participant accepted NPC summaries and followed their direction without deeper interrogation.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.00** |

---

## Caveats
- F3 rating is a boundary call between 1 and 2. The participant re-pinged auto-replied NPCs (tier-1 behavior) but did eventually accept constraints and take ownership (tier-2 behavior). Weighted toward tier 2 per the anti-first-impression-lock reminder and the trajectory of the full session.
- F2 rating could arguably be lower given the participant did not independently surface the week-ago question and showed limited reframing after the restart failed. However, the participant did engage with the cert thread and eventually requested the bundle check, which prevents a tier-1 rating.
- The drill ended before the second restart could be authorized (after bundle fix), limiting the highest-leverage F4 evidence for the second restart decision.

---
---

# Markers Analysis — 9058

## L3 — Takes explicit ownership of the response

**Rating:** 2

**Evidence:**
> "Let me take command of this incidnet" ... "i will be incidnet commander" ... "and i approve" ... "I aprrove please prceed"

**Rationale:**
The participant declares themselves IC and eventually authorizes the restart, but ownership is inconsistent. They repeatedly defer to unavailable stakeholders (Hamed, Tinus) before acting, and much of the response is reactive rather than directive. The approval comes only after being told both approvers are out and being prompted by Tanya about who takes responsibility. They never explicitly accept consequences ("blowback's on me").

---

## C1 — Asks clarifying questions before acting

**Rating:** 2

**Evidence:**
> "@bob - do you know more" ... "How many customers are blocked from checkout right now? What's the revenue loss per minute? Is this a total outage or just some users?"

**Rationale:**
The participant does ask Bob for more information and later asks about revenue loss. However, the initial question ("do you know more") is vague rather than targeted, and the more specific scoping questions come after the participant has already declared the incident and begun directing actions. The clarifying questions are present but not well-sequenced before action.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "Ok thank @shay - Have a look at changes also and @tanya - can you please explain on the maintence you had" ... "@daniel - Have you reviewed all the Prod changes done today"

**Rationale:**
The participant asks about recent changes and reviews them with Daniel and Shay. However, they don't use the change log as a candidate-elimination tool. Despite Shay noting "none of these changes look like they'd break checkout end-to-end," the participant still orders rollbacks of CheckoutService changes and repeatedly pushes Tanya to roll back email maintenance without articulating a mechanism connecting those changes to the symptom.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "Ok thank @shay - Have a look at changes also and @tanya - can you please explain on the maintence you had" ... "@daniel @shay - Please see the logs .. what errors you are seieng"

**Rationale:**
The participant does use @mentions and names specific people, but delegation is often vague ("have a look at changes," "please look into this further and suggest") rather than giving specific, actionable tasks. They also repeatedly ask Tanya to do things she's already done or can't do (e.g., rolling back changes that were never applied). Routing doesn't consistently reflect understanding of access boundaries.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "Ok thank @shay - Have a look at changes also and @tanya - can you please explain on the maintence you had" ... "@daniel @shay - Please see the logs .. what errors you are seieng"

**Rationale:**
There are moments where the participant asks multiple people to do things in close succession (Shay for changes, Tanya for maintenance explanation). However, much of the investigation is sequential — waiting for one response before moving to the next question. The participant doesn't clearly fan out distinct complementary threads running concurrently.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "@tinus @hamed - Need escalation as we arent able to get the direction form available technical resouces" ... "Hi @hamed - What wud you suggest please"

**Rationale:**
The participant attempts escalation to Hamed and Tinus multiple times, but the escalation quality is low — vague asks ("What wud you suggest please," "Need escalation as we arent able to get the direction") without concrete context about what's blocked or what's needed. When both auto-reply, the participant doesn't immediately pivot to a Plan B; they eventually authorize the restart themselves but only after significant delay and prompting from Tanya.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "@tanya - Looking at the arctichetire there is email service which is connected to checkout.. it may have caused this issue" ... "as the issue started at same time"

**Rationale:**
The participant forms an implicit hypothesis about email maintenance causing the issue based on timing correlation, but never explicitly names it as a hypothesis to test. They don't articulate a mechanism connecting email maintenance to checkout failure. When evidence disconfirms (Tanya says email changes weren't applied to prod), the participant continues pushing that thread. The cert hypothesis emerges from NPC guidance rather than participant reasoning.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "Payemnt serice is hsowing no outbound cinnection ?" ... "see we see lot of payment errors" ... "TLS handshare failures ? who can help here ? @tanya"

**Rationale:**
The participant does eventually follow the evidence trail from checkout → PaymentService → outbound handshake → TLS, but this narrowing is largely driven by Daniel and Tanya providing the evidence and explicitly stating conclusions. The participant rarely synthesizes evidence independently or uses absence of signal to rule things out. They don't produce synthesis statements combining multiple data points.

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "can we please roll then back ?" ... "Ok can you please start the failover" ... "go for full restart"

**Rationale:**
The participant orders rollbacks, failovers, and restarts without asking "is it safe?" or considering potential side effects. They don't weigh the cost of pulling Tanya off the vendor call (asking "If you dont rollout what is the impact?" is about the email rollout impact, not about the incident action's consequences). They order a full restart without checking the bundle on disk first. No "gradually" or "carefully" qualifiers appear.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "Please checek the bundle - penssl verify -CAfile /etc/ssl/certs/ca-bundle.crt payment-gateway.crt"

**Rationale:**
After the restart fails to fix the issue, the participant does pivot to checking the bundle, which is a meaningful adaptation. However, earlier in the drill they repeatedly pursue the same failing approach (rolling back changes that NPCs have already said are unrelated). The bundle check comes relatively quickly after the restart failure, suggesting some adaptability, but the earlier pattern of repeated rollbacks without pivoting keeps this at tier 2.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 1

**Evidence:**
> "We do not know the caused yet , but no orders are placed" ... "All customers ar eimpacted globally" ... "I am checek ing with tean" ... "we dont know the cause"

**Rationale:**
Updates to Bez are minimal and reactive (only in response to Bez's questions). They contain no working theory, no committed next-update time, no ETA, and no business-framed impact quantification beyond "all customers impacted." The participant never proactively updates Bez and provides only vague reassurances when pressed. Later updates ("We are trying to restart the system") are technical without business framing.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 1

**Evidence:**
> "We are not trading so @tanya please look into this firther and suggest" ... "@daniel @shay - Please see the logs .. what errors you are seieng"

**Rationale:**
The participant rarely synthesizes the current state of knowledge for the technical team. They don't post summary statements about what's been ruled out or what the current working theory is. Instructions to the team are vague ("look into this further and suggest," "see the logs"). The team members (Daniel, Shay, Tanya) end up driving the investigation narrative themselves rather than being oriented by the IC.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 2 |
| C1 — Asks clarifying questions before acting | 2 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 1 |
| K4 — Communicates issue scope clearly to the technical team | 1 |
| **Mean Marker Score** | **1.75** |

---

## Caveats
- The participant's messages contain many typos, which makes intent harder to parse in some cases. I rated based on what was actually communicated rather than inferring intended meaning.
- The bundle check near the end ("Please checek the bundle") could be interpreted as tier 3 on M5 if weighted heavily, but the earlier pattern of repeated rollbacks without adaptation anchors the overall rating at 2.
- For M4, the question "If you dont rollout what is the impact?" was about understanding Tanya's email maintenance stakes rather than weighing consequences of an incident action, so it was not counted as consequence-weighing for incident response actions.

---