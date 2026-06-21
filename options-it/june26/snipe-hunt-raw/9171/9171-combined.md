# Snipe Hunt — Post-Drill Report

This drill puts you in the middle of a live incident with systemic complexity: misleading signals, hidden dependencies between services, constrained team availability, and more information than you can process at once. The facets below capture how you navigated each of those pressures during this run.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you directed team members to investigate the email maintenance change and recent deploys — reasonable starting points. When those were disconfirmed by your teammates, you did eventually shift attention toward the TLS handshake failure, but the pivot came after repeated NPC disconfirmation rather than from your own mechanism reasoning. Later, you circled back to the deploy hypothesis again even after it had been cleared, which extended the time spent on a dead-end lead.

*Growth edge for next rep:* When a hypothesis is disconfirmed, practise naming it aloud as eliminated and articulating *why* you're moving to the next candidate. This makes the pivot deliberate rather than reactive, and reduces the pull to revisit leads that have already been ruled out.

---

## F2 — Hidden coupling

**Operating at: Practicing**

After the first restart failed, you asked whether the error was still cert-related — a reasonable check — but the question reflected confusion rather than recognition that a structurally different failure mode might be in play. The distinction between a single expired certificate and a certificate bundle dependency was surfaced by your teammate rather than independently identified. The reload-vs-restart decision was similarly offered to you rather than read from available documentation.

*Growth edge for next rep:* When a fix doesn't resolve the problem, treat that as a signal that your mental model of the system may be incomplete. Ask "what else is this component connected to?" before re-running the same remediation path.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You walked the escalation chain — reaching out to both unavailable approvers, then asking a peer, and ultimately taking ownership yourself. You also pulled your platform engineer off a vendor call, recognising the priority. However, you didn't explicitly name the access constraints as a pattern early on, and you didn't batch your questions to economise on your engineer's limited bandwidth — instead issuing repeated single-task requests.

*Growth edge for next rep:* When you notice key people are unavailable, try stating the constraint out loud for the team ("we've lost both approvers — here's how we'll handle decisions"). This frames the situation for everyone and lets you move faster when the next bottleneck appears. Also consider batching questions to constrained teammates so each interaction yields maximum information.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You navigated the approval bottleneck effectively: after exhausting the escalation chain, you explicitly took ownership of the restart decision. You also delegated parallel work appropriately — assigning code review and infrastructure checks to different people based on their access. On the second restart, you authorised without re-litigating the approval question, showing you'd internalised the decision authority. Your delegation showed awareness of role boundaries, assigning infrastructure investigation to your platform engineer and code-level review to your developer.

*Growth edge for next rep:* To move further, try naming the full dependency structure before you start walking the chain — "this action requires approval, the approvers are X and Y, both are out, so I'll need to self-authorise or find an alternative." Articulating the structure up front saves time and signals confidence to the team.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked about expired certificates, which showed targeted thinking, but this came after your teammate had already identified the TLS handshake failure — making it confirmatory rather than independently filtering. You asked a teammate to re-review changes that had already been cleared, suggesting difficulty integrating information that had already been surfaced. The narrowing to the specific failing service happened largely through teammate guidance rather than your own synthesis of the available log data.

*Growth edge for next rep:* Practise maintaining a running mental (or written) list of what's been confirmed and eliminated. Before asking someone to check something, ask yourself: "do I already have this answer?" This reduces redundant work and helps you spot the buried signal faster.

---

## Looking Ahead

You showed a consistent willingness to engage — asking questions, delegating, and ultimately stepping into the decision-maker role when the situation demanded it. The pattern across this run is that your pivots and reframes tended to follow teammate input rather than leading it. For your next drill, focus on one thing: after each new piece of information lands, pause briefly to state what it changes about your working picture before issuing the next task. That single habit will strengthen both your hypothesis management and your ability to filter noise from signal.# Facets Analysis — 9171

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Okay @tanya can you please check your email maintenance change, @shay can you also please check if any other changes were made recently on the software side"

**Rationale:**
The participant initially pursued the email maintenance and recent deploys as leading hypotheses, directing Tanya to check her maintenance change and asking Daniel to review changes. When Daniel and Tanya both confirmed their changes were unrelated, the participant eventually pivoted to investigating PaymentService logs and the TLS handshake failure. However, the pivot was reactive — driven by NPC disconfirmation rather than upstream mechanism reasoning. The participant asked "have we checked for expired certs" only after Tanya explicitly identified the SSL certificate verification failure, and later returned to the email/deploy hypothesis again ("can you please also review Tanyas change again"). The pivot latency was extended (many exchanges after initial disconfirmation), placing this in tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "still a cert error?" ... "can you get on the second cert issue please"

**Rationale:**
After the first restart failed, the participant did not independently reframe the problem as structurally different. They asked "still a cert error?" which shows confusion rather than recognition of a new failure mode. Tanya had to surface the bundle issue ("two certificates needed — it's a bundle, not just a single cert") before the participant engaged with it. The participant never independently surfaced the "what changed beyond the last 24 hours" question — the cert rotation was surfaced by NPCs. The reload-vs-restart distinction was offered by Tanya ("so we have two options") rather than read from the runbook by the participant. The pivot after the first restart failing took several exchanges and was NPC-driven, consistent with tier 2.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "As Hamid and Tinus are out, can you please approve this" [to Bez] ... "As Hamid and Tinus are out I will approve the restart"

**Rationale:**
The participant attempted to escalate to Tinus (received auto-reply), then Hamed (received auto-reply), then asked Bez to approve (who declined), and finally took ownership themselves. This shows walking the escalation chain but without articulating the access constraints proactively. The participant also told Tanya "This is more important than maintenance" and pulled her off the vendor call, but without explicitly naming the cost trade-off. The participant did not batch questions to Tanya or economise on her constrained bandwidth — repeatedly saying "now please" and "@tanya this is your priority." The ownership was eventually taken but reasoning was brief ("As Hamid and Tinus are out I will approve the restart") rather than articulating the constraint pattern fully.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "As Hamid and Tinus are out I will approve the restart"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Tinus (auto-reply), pinged Hamed (auto-reply), asked Bez (declined), then explicitly took ownership and issued the authorisation. This matches tier-3 path (b) — walking the escalation chain to exhaustion and then explicitly taking ownership. The participant also delegated parallel work appropriately (Daniel on code review, Tanya on infra, Shay on logs). On the second restart (after bundle fix), the participant authorised without re-litigating ("restart now"), showing learning. However, the participant did not name the dependency structure aloud as a single enumerated constraint statement before the chain was exhausted, which would have been tier-4 behaviour.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "have we checked for expired certs" ... "please review again"

**Rationale:**
The participant asked "have we checked for expired certs" only after Tanya had already identified the TLS handshake failure, showing some targeted thinking but only after NPC filtering. The participant did not independently filter logs to PaymentService — Shay identified it as the anomalous service. The participant asked Daniel to re-review the CheckoutService timeout change twice ("please review again") even after Daniel confirmed it was clean, showing difficulty integrating already-surfaced information. The participant did not catch the reload-vs-restart distinction from the runbook — Tanya offered both options. After the restart failed, the participant did not independently reason about the bundle issue; Tanya surfaced it. The participant accepted NPC summaries without further interrogation and relied heavily on NPCs to filter and surface buried information.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.20** |

---

## Caveats
- F1: The participant did eventually move past the email/deploy hypothesis, but returned to it late in the drill ("can you please also review Tanyas change again" after the restart failed), which reinforces the tier-2 rating rather than tier-3.
- F4: The tier-3 rating is based on path (b) — chain-walk to exhaustion followed by explicit ownership. The second restart authorisation without re-litigation is a positive signal but doesn't elevate to tier 4 given the absence of proactive dependency-structure naming.
- F5: The "have we checked for expired certs" question is a borderline signal — it could indicate proactive thinking, but it came after Tanya had already identified the SSL handshake failure, making it more reactive than proactive.

------

# Markers Analysis — 9171

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "As Hamid and Tinus are out I will approve the restart"

**Rationale:**
The participant eventually takes explicit ownership of the restart decision when both approvers are unavailable, stating they will approve it themselves. However, this comes after first attempting to get Bez to approve ("can you please approve this") and being told it's the incident lead's call. The ownership is real but reactive rather than proactive — they needed the nudge from Bez before stepping up.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "Hi Bob, what is the scope of the impact?" ... "any region in particular?"

**Rationale:**
The participant's first actions are scope-validating questions to Bob about impact and region before taking any remediation action. They ask about scope and region specifics before declaring the incident or ordering changes. This meets the novice expectation of gathering information before acting, though the questions are somewhat basic rather than deeply probing (e.g., they don't ask about error types or specific payment methods).

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "Okay @tanya can you please check your email maintenance change, @shay can you also please check if any other changes were made recently on the software side"

**Rationale:**
The participant asks for recent changes early in the investigation and receives the full change list. Later, after the restart fails, they ask Daniel to confirm "none of these changes would break checkout" and review Tanya's changes. They use the change log as a candidate-elimination pass ("none of the recent changes appear to be the culprit on initial inspection" in the escalation to Tinus). However, they do repeatedly ask Shay and Daniel to re-review changes even after they've been cleared, showing some difficulty fully letting go of the deploys lead.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "Tanya and Daniel can you please check the payments app from your side. Daniel check the code and Tanya the infra"

**Rationale:**
The participant consistently delegates to named individuals with specific tasks — Tanya for infra/platform checks, Daniel for app-side code review, Shay for change review. The delegation to "Daniel check the code and Tanya the infra" shows awareness of access boundaries. However, there are some instances of asking Tanya when she's explicitly said she's mid-maintenance, and asking Shay to check logs when Daniel is the log-puller.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "Okay @tanya can you please check your email maintenance change, @shay can you also please check if any other changes were made recently on the software side"

**Rationale:**
The participant shows some parallel delegation early on (Tanya on email maintenance, Shay on other changes). However, the investigation is largely sequential after that — they wait for one thread to complete before starting the next. After the restart fails, they ask for the change list again and work through it serially rather than fanning out multiple threads simultaneously. The parallelism is limited and inconsistent.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "Hi @tinus, escalating due to the severity of this incident. Customers globally are facing an error at checkout, none of the recent changes appear to be the culprit on initial inspection"

**Rationale:**
The participant escalates to Tinus with reasonable context (severity, global impact, changes ruled out). However, when Tinus auto-replies, they ask the channel "does anyone have the escalation procedure at hand?" rather than immediately working the chain or taking ownership. The escalation to pull Tanya off the vendor call is also hesitant — they say "this is more important" but Tanya initially refuses, and the participant doesn't forcefully pull her until later. The quality of escalation context is decent but the follow-through when blocked is weak.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "have we checked for expired certs"

**Rationale:**
The participant does not explicitly articulate hypotheses with proposed tests. They ask questions that implicitly contain hypotheses (e.g., "have we checked for expired certs") but never frame them as "my hypothesis is X, let's test by doing Y." The cert question comes after Tanya identifies the TLS handshake failure, so it's more reactive than hypothesis-driven. They also repeatedly circle back to the email maintenance and recent changes without explicitly framing these as hypotheses to test and disconfirm.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "appears to be a total checkout outage" ... "Daniel do you agree that none of these changes would break checkout"

**Rationale:**
The participant does some narrowing — they confirm it's a total outage, and they get Daniel to confirm changes aren't the cause. However, they don't produce synthesis statements that combine multiple pieces of evidence. After the restart fails, they ask for the change list again and ask Daniel to re-review changes that were already cleared, suggesting they aren't effectively using prior evidence to narrow scope. The narrowing to PaymentService happens largely through NPC guidance rather than participant synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 3

**Evidence:**
> "whats the impact of the full restart" ... "how long will the graceful reload take" ... "please try that first" ... "with caution"

**Rationale:**
The participant asks about the impact of a full restart and the duration of a graceful reload before choosing the lower-risk option first. They also say "with caution" when approving the restart. This shows consequence-weighing behavior. However, they don't anticipate secondary failure modes (the bundle issue after restart) and don't name the cost of pulling Tanya off the vendor session.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "can you please walk me through the recent change in detail Daniel, focusing on those which took place when the incident started" ... "please review again"

**Rationale:**
After the first restart fails, the participant goes back to reviewing recent changes — asking Daniel to walk through them again and even saying "please review again" after Daniel has already double-checked. This shows difficulty adapting when the initial path isn't working. They don't recognize the new error (chain verification vs. expiry) as structurally different until Tanya explicitly identifies it. They eventually follow the bundle thread but only after NPCs surface it.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "first reported about 20 mins ago, affecting customers globally" ... "appears to be a total checkout outage" ... "no ETA as of yet"

**Rationale:**
The participant provides some information to Bez (global impact, total outage) but the updates lack business framing (no revenue quantification despite Bob providing it), no working theory, and no committed next-update time. When Bez asks for specifics, the participant says "we can work out the revenue details once it is resolved" — deflecting rather than providing what's available. The later update ("We have found an expire cert, however we will need to complete a full restart") is more substantive but comes very late.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "failure is at TLS handshake before data exchange. - can you please check this further @tanya"

**Rationale:**
The participant rarely synthesizes the investigation state for the technical team. They relay information back (quoting Tanya's findings) but don't produce original synthesis statements like "we've ruled out deploys, focus is now on PaymentService outbound." The one instance of scope communication ("failure is at TLS handshake before data exchange") is essentially quoting what Tanya already said. The team is left to piece together the investigation state from the question/answer exchanges rather than receiving clear scope summaries.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 3 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 3 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.42** |

---

## Caveats
- L3 is a borderline 2/3 call. The participant does eventually take ownership of the restart approval, but only after being told by Bez that it's their call. Rated 3 because they do explicitly state "I will approve the restart" rather than continuing to defer.
- M5 is a borderline call — the participant does eventually follow the bundle thread, but only because NPCs surfaced it. The repeated requests to re-review already-cleared changes weigh toward a 2.
- K2 could be argued as a 1 given the deflection of Bez's requests, but the participant does provide some factual information (global, total outage, cert found) so rated 2.

---