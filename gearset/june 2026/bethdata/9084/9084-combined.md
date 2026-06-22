# Snipe Hunt — Post-Drill Report

This drill put you in the middle of a live checkout outage with multiple competing signals, absent key personnel, and documentation that buried critical details. It's designed to stress your ability to reason through systemic complexity — separating noise from signal, navigating coordination constraints, and adapting when your first fix doesn't land.

---

## F1 — Misleading correlations

**Operating at: Strengthening**

Early in the drill, you tested the email maintenance correlation rather than accepting it at face value — you asked whether checkout blocks on the email send, and when the answer was no, you moved on without ordering a rollback. This is exactly the right instinct: checking for a causal mechanism before treating a correlation as actionable. The growth edge here is making that reasoning visible to the team. When you discard a hypothesis, naming *why* out loud ("email is down but checkout doesn't block on it, so this isn't our cause") helps the group stay aligned and avoids someone else circling back to the same dead end.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

After the first restart failed, you stayed composed and redirected investigation toward the certificate bundle rather than retrying the same fix. You caught that the new error was structurally different from the original expiry issue and drove Tanya toward the footnote about bundle ordering. The next-rep growth edge: try to surface the "what changed beyond the obvious" question yourself, earlier. In this run, the connection between the recent change and the coupling emerged through team members rather than from your own framing. Proactively asking "what else shifted in this window that could interact?" before the first fix attempt would give you a head start on hidden dependencies.

---

## F3 — Decreased access to team / remote

**Operating at: Strengthening**

You named the access constraints clearly when you made the authorization call — identifying who was unavailable and why, and noting that Bez was aware. You also worked to pull Tanya off the vendor call by escalating through Bez when you couldn't redirect her directly. For the next rep, consider batching your questions more tightly when working with constrained team members. When someone's availability is limited, front-loading multiple asks in a single message reduces round-trips and keeps momentum.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the approval chain to exhaustion — pinging both Hamed and Tinus, receiving auto-replies, and then explicitly taking ownership of the authorization decision. You delegated appropriately throughout, assigning platform work to Tanya, application-side tasks to Daniel, and setting up Shay as a fallback. The growth edge is articulating the dependency structure proactively — before the approval moment arises, naming "here's who we need, here's who's unavailable, here's what that means for our path" as a single framing statement. This helps the team anticipate bottlenecks rather than discovering them one ping at a time.

---

## F5 — Data overload / buried information

**Operating at: Strengthening**

You filtered effectively through the noise — moving past the email service errors to focus on the payment service, and catching the significance of the footnote in the rotation documentation about bundle ordering. After the restart failed, you directed investigation toward the bundle structure rather than accepting surface-level confirmation. For the next rep, try to drive the initial filtering more proactively — reasoning about what's absent in the data (e.g., which services *aren't* showing errors) can help you narrow scope faster before waiting for others to surface the relevant logs.

---

## Looking Ahead

You're showing consistent, systematic engagement across the core challenges this drill presents — testing mechanisms before acting, adapting when fixes fail, and taking ownership when coordination paths are blocked. The recurring growth edge across your facets is *making your reasoning more visible and proactive*: naming what you've ruled out, articulating constraints before they bite, and surfacing structural questions earlier in the timeline. On the next rep, try narrating your elimination logic to the team as you go — it costs little and compounds quickly.---

# Facets Analysis — 9084

## F1 — Misleading correlations

**Rating:** 3

**Evidence:**
> "@shay does the code block on sending the checkout emails? if so, does the email service being down mean it would entirely freeze?"

**Rationale:**
The participant initially considered the email maintenance correlation but explicitly tested the causal mechanism by asking whether checkout blocks on email send. After Shay confirmed it doesn't, the participant moved on without ordering a rollback or pause of email maintenance. They did not paste NPC framing back as their own conclusion. The mechanism-checking question before acting aligns with tier 3's "explicitly checks whether a causal mechanism exists before acting." They didn't quite reach tier 4 because they didn't articulate the correlation-vs-causation frame explicitly to the team.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "that footnote in the instructions is worrying" ... "@tanya can you examine it more closely? check the ordering" ... "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
After the first restart failed, the participant stayed calm ("let's be calm about this and resolve the issue") and within a few exchanges directed Tanya to check the certificate more closely, referencing the footnote about bundle ordering. They recognized the new error was structurally different from the original expiry issue and drove investigation toward the bundle rather than attempting more restarts. However, they did not independently surface the "what changed beyond 24 hours" question — the cert rotation thread emerged through NPC-driven investigation (Daniel/Shay surfacing CHG90123). The reframe after restart failure happened within approximately 3-5 exchanges, consistent with tier 3.

---

## F3 — Decreased access to team / remote

**Rating:** 3

**Evidence:**
> "Hamed is on leave and Tinus is at the conference. I'll authorize it in their absence. Bez is aware."

**Rationale:**
The participant named the access constraints explicitly when making the authorization decision. They accepted auto-replies from Hamed and Tinus as terminating (only one ping each). They initially tried to redirect Tanya from email maintenance, and when she couldn't leave, they escalated through Bez to pull her off. The authorization statement names the constraint pattern clearly. However, they didn't fully batch questions to Tanya or articulate the vendor-call cost trade-off in their own words — Bez made that call. This places them solidly at tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "Hamed is on leave and Tinus is at the conference. I'll authorize it in their absence. Bez is aware." ... "@daniel can you do that?" ... "@tanya check the payments service certificate"

**Rationale:**
The participant walked the escalation chain (pinged Hamed → auto-reply, pinged Tinus → auto-reply/Bez redirect) and then explicitly took ownership of the authorization decision, naming the constraint. They delegated parallel work appropriately (Daniel on banner, Tanya on cert investigation, Bob on customer comms). On the second restart (after bundle fix), they authorized without re-litigating. This matches tier 3 path (b) — walking the escalation chain to exhaustion then explicitly taking ownership. They didn't quite reach tier 4 because the dependency structure wasn't articulated as a single enumerated constraint statement proactively, and the sequencing wasn't notably ahead of the NPCs' prompting.

---

## F5 — Data overload / buried information

**Rating:** 3

**Evidence:**
> "@tanya can you check that the certificate is correct? that footnote in the instructions is worrying" ... "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
The participant filtered effectively — they moved past the noisy EmailService errors to focus on PaymentService, asked for specific payment logs, and caught the significance of the footnote in the rotation documentation about bundle ordering. After the restart failed, they directed investigation toward the bundle structure rather than accepting surface-level "cert is loaded" confirmation. They read the referenced documentation and caught the key distinction. However, they didn't independently reason about absence of signal (e.g., internal calls clean → external boundary) or drive the initial filtering proactively before NPCs surfaced the payment logs. This places them at tier 3.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 3 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 3 |
| **Mean Facet Score** | **3.00** |

---

## Caveats
- F2 tier 3 vs 4 was a boundary call. The participant reframed after the restart failure within a reasonable window and drove toward the bundle, but they did not independently surface the "what changed beyond 24 hours" question — that came from NPCs (Daniel/Shay). The lack of independent surfacing of the week-old coupling keeps this at tier 3.
- F4 tier 3 vs 4 was close. The participant named constraints when authorizing but didn't proactively enumerate the dependency structure before the approval moment arose. The second restart authorization was clean and fast, which is a tier-4 signal, but overall the pattern fits tier 3 more cleanly.
- F1 could arguably be tier 4 given the early mechanism-testing question, but the participant didn't explicitly name the correlation-as-prime framing to the team, which is the load-bearing tier-4 signal.

------

# Markers Analysis — 9084

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "Hamed is on leave and Tinus is at the conference. I'll authorize it in their absence. Bez is aware."

**Rationale:**
The participant takes explicit ownership of the restart authorization when both approvers are unavailable, making the call themselves and noting Bez's awareness. They also drive the response throughout — directing Tanya, Daniel, and Shay by name. However, they don't explicitly name the personal cost/blowback risk of the override, which would elevate to tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "What are the complaints about Bob?" ... "Is this a total checkout outage? How many customers are blocked and what's the revenue loss per minute right now?"

**Rationale:**
The participant's first action after Bob's alert is a clarifying question about the nature of the complaints. They follow up with scope-validating questions about whether it's a total outage, customer count, and revenue impact before taking action. They also ask about recent changes. This represents solid scope-validation before acting, meeting the tier 3 expectation.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "can we line this up with any recent changes? @shay ?"

**Rationale:**
The participant explicitly asks for recent changes early in the investigation. When Shay and Daniel provide the change log, the participant doesn't immediately jump to rolling back those changes. They move on to investigating logs and other causes. However, they don't explicitly articulate the elimination logic ("none of these touch the gateway") — the deweighting is implicit rather than stated. This places them at tier 3.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya check the payment service. it's failing outbound gateway handshakes" ... "@daniel can you do that?" ... "@shay could you do the above if Daniel is not available?"

**Rationale:**
The participant consistently delegates to specific named individuals with specific tasks — Tanya for platform/cert checks, Daniel for logs and banner, Shay as backup. They route platform-level work to Tanya and app-side work to Daniel appropriately. The fallback delegation to Shay when Daniel might be unavailable shows awareness of access boundaries, approaching tier 4 but not consistently demonstrating deep boundary knowledge throughout.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "can we line this up with any recent changes? @shay ?" ... "Can someone check the logs on the checkout service?"

**Rationale:**
The participant does kick off a change-log review and log checks in relatively close succession. However, much of the investigation proceeds sequentially — waiting for Daniel's log results before moving to the next step, then waiting for Tanya's findings. The "@here can everyone mob on this one?" is a broadcast rather than structured parallel delegation. The investigation is mostly serial rather than deliberately fanned out.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya the payment service is failing outbound gateway handshakes. that seems infrastructure. can someone else take over the email vendor hand holding for you?" ... "Hamed is on leave and Tinus is at the conference. I'll authorize it in their absence."

**Rationale:**
The participant escalates Tanya's priority by trying to pull her off the vendor call, providing concrete context about why (outbound handshake failures). When both Tinus and Hamed are unavailable for the restart approval, they don't leave the chain hanging — they authorize it themselves. However, they don't explicitly name the cost of pulling Tanya off the vendor session (the 2-week slot loss), which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 3

**Evidence:**
> "@shay does the code block on sending the checkout emails? if so, does the email service being down mean it would entirely freeze?" ... "maybe they changed their ssl cert and we don't have the public one trusted?"

**Rationale:**
The participant forms testable hypotheses — first about email maintenance blocking checkout (tested via Shay's response that checkout doesn't block on email), then about ClearBank's cert changing. They pivot when hypotheses are disconfirmed. The email hypothesis is explicitly articulated and tested on mechanism ("does the code block on sending?"). This meets tier 3 expectations of naming hypotheses and proposing tests.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "Ok, so do any of the other service logs show an issue or is it just the email service" ... "@tanya the payment service is failing outbound gateway handshakes. that seems infrastructure."

**Rationale:**
The participant uses Daniel's log findings to narrow from "checkout broken" to "PaymentService outbound handshake failure" and correctly identifies this as infrastructure territory. They use Shay's confirmation that checkout doesn't block on email to eliminate that hypothesis. However, they don't produce explicit synthesis statements naming what's been ruled out alongside what remains, which would push to tier 4.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "@tanya do it" ... "@tanya restart the service"

**Rationale:**
The participant issues restart commands without explicit consideration of potential consequences. They don't ask "is it safe?" before the first restart, nor do they anticipate that the restart could expose a secondary issue (the misordered bundle). They don't check the bundle on disk before restarting. The absence of consequence-weighing language ("if it's safe," "gradually," "what could go wrong") places this at tier 2.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "@tanya can you check that the certificate is correct? that footnote in the instructions is worrying." ... "@tanya can we examine it more closely? check the ordering"

**Rationale:**
After the first restart fails, the participant doesn't simply retry the restart. They redirect investigation to the certificate itself, referencing the footnote about bundle ordering. They then ask Tanya to examine the bundle more closely and check the ordering, which leads to discovering the misordered chain. This demonstrates clear adaptation when the initial fix didn't work, meeting tier 3. They don't quite reach tier 4 because they don't explicitly name the new failure as structurally different from the original.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "we've not located the exact source of the failure yet. we'll update again in 5 minutes." ... "10 minutes" ... "our certificate isn't correct. we're going to generate a new one and rotate that in"

**Rationale:**
The participant's business communications are mostly thin. The first update to Bez ("we've not located the exact source") lacks impact quantification or working theory. The "10 minutes" ETA is given without context. Later updates improve slightly ("our certificate isn't correct") but still lack business framing (revenue impact, customer scope). They don't proactively update Bez after the first restart fails. This is inconsistent and below the tier 3 expectation of quantified impact and committed next-update times.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 3

**Evidence:**
> "@tanya the payment service is failing outbound gateway handshakes. that seems infrastructure. can someone else take over the email vendor hand holding for you?" ... "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
The participant shares working understanding with the team at key moments — identifying the failure as infrastructure-level outbound handshake failures, and later directing attention to the bundle structure. They synthesize Daniel's findings into actionable direction for Tanya. However, they don't produce comprehensive "here's what we've ruled out" synthesis statements, which would push to tier 4.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 3 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 3 |
| M3 — Uses evidence to narrow the scope | 3 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 3 |
| **Mean Marker Score** | **2.75** |

---

## Caveats
- L3: The authorization statement "I'll authorize it in their absence. Bez is aware." is clear ownership but doesn't explicitly name personal risk/blowback. This is a borderline 3/4 call; rated 3 because the cost-naming language is absent.
- K2: Bez's aggressive questioning ("Not good enough") may have pressured the participant into terse responses, but the rubric evaluates the substance of what was communicated regardless of pressure context.
- M4: The absence of consequence-weighing is rated on what the participant *didn't* say before issuing restart commands. No "is it safe?" or "what could go wrong?" language appears anywhere in the transcript before high-impact actions.

---