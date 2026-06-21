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