# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to reason through systemic complexity — separating misleading signals from real mechanisms, navigating coordination constraints when key people are unavailable, and synthesising information as it arrives from multiple sources under time pressure.

---

## F1 — Misleading correlations

**Operating at: Not yet evident**

Early in the drill, you identified the email maintenance as the likely cause based on timing overlap and continued pursuing it as the primary hypothesis even after a team member explicitly stated that email confirmations were unaffected and couldn't be causing checkout failures. The pivot away from this correlation happened passively — through others' investigation surfacing the real mechanism — rather than through your own reasoning about why the correlation lacked a plausible causal path.

*Growth edge:* When a correlation surfaces, practice asking "what mechanism connects A to B?" before acting on it. If a team member offers disconfirming evidence, treat that as a signal to deprioritise the hypothesis rather than continue investing in it. On your next rep, try naming one reason a correlation *might not* be causal before directing action around it.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the certificate thread once it was surfaced by a team member, and you registered surprise when the first restart didn't resolve the issue — recognising that something structurally different was happening. However, the deeper coupling (the reload-versus-restart distinction and the bundle ordering dependency) was identified entirely by others. You didn't independently ask what had changed beyond the immediate timeframe or probe the system's dependency structure.

*Growth edge:* When a fix doesn't behave as expected, that's a signal to ask "what else is this component coupled to?" rather than simply directing others to check. Practice articulating the structural question yourself — even a rough version — before waiting for someone else to surface it.

---

## F3 — Decreased access to team / remote

**Operating at: Practicing**

You walked the escalation chain and eventually pulled in the people you needed, but you repeatedly pinged auto-replying and out-of-office contacts without pivoting to alternative paths. When you pulled a team member off a vendor call to investigate the email maintenance hypothesis, you didn't batch your questions or acknowledge the cost of that interruption. You did eventually take ownership of the restart decision yourself, which showed awareness that the access constraint required you to act.

*Growth edge:* When someone is unavailable, treat the first auto-reply as a hard signal — pivot immediately rather than re-pinging. When pulling someone off another commitment, name the trade-off explicitly and economise their time by batching what you need from them. This connects to how you delegate: early in the drill, you assigned broad tasks to multiple people simultaneously without distinct scopes, which dilutes the value of limited availability.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You eventually made the override call for the restart when the approval chain was exhausted, accepting responsibility clearly. That ownership statement was meaningful. However, it arrived only after extended back-and-forth and multiple failed attempts to defer the decision. You didn't articulate the dependency structure — who could approve what, who was unavailable, and what that meant for your options — in a way that would have let you reach the override decision faster. On the second restart after the bundle fix, you approved without re-litigating, which suggests some in-drill learning.

*Growth edge:* Practice mapping the decision-dependency chain early: "Who needs to approve this? Are they available? If not, what's my fallback?" Naming this structure explicitly — even in a brief message to the channel — helps you recognise sooner when you're the one who needs to act. Your willingness to eventually take responsibility is a foundation to build on; the next step is reaching that point faster through proactive sequencing.

---

## F5 — Data overload / buried information

**Operating at: Not yet evident**

Information that team members had already surfaced and confirmed — such as the failure being at the TLS handshake on your side — was not integrated into your working picture. You communicated to stakeholders that the issue appeared to be on the third party's side after your own team had confirmed otherwise. You didn't drive any filtering or discovery of buried information yourself; key findings were surfaced entirely by others while you received them passively.

*Growth edge:* When a team member states a finding, practice restating it in your own words before moving on — this forces integration. Before communicating externally, cross-check your message against what's already been confirmed in-channel. On your next rep, try maintaining a brief running summary of "what we know" and "what's ruled out" that you update as findings arrive. This also strengthens how you orient the technical team, since synthesis statements help everyone stay aligned.

---

## Looking Forward

You showed willingness to step into the decision-maker role when circumstances demanded it, and your initial instinct to ask clarifying questions before acting is a solid foundation. The primary growth area across this drill is moving from *receiving* information to *interrogating* it — testing your own hypotheses against disconfirming evidence, integrating what's already been confirmed, and naming structural dependencies before they become blockers. On your next rep, pick one of these edges — hypothesis-testing or information integration — and make it your deliberate focus.
---

# Facets Analysis — 9032

## F1 — Misleading correlations

**Rating:** 1

**Evidence:**
> "Initial investigation indicates the issue may be related to an ongoing canary rollout for a secondary email provider started by Tanya." ... "@shay, please deep into the maintenanc eissue and provide next steps on that, should we pause it or not." ... "@tanya could you do a quick pause and stop the maintenacne?"

**Rationale:**
The participant locked onto the email maintenance correlation and pursued it as the leading hypothesis despite Tanya explicitly stating "Email confirmations have been fine, so this maintenance can't be causing checkout failures." The participant continued to push for pausing the maintenance and pulling Tanya off the vendor call based on this false lead. Even after Daniel's logs showed PaymentService outbound gateway handshake failures (a clear mechanism pointing away from email), the participant still framed the issue as maintenance-related ("We are currently suspecting the maintenance to be main cause due to timeframe match"). The pivot away from the email hypothesis only occurred passively when Tanya's platform investigation revealed the cert issue — not through the participant's own mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "seems xertificates are expired?" ... "lets do full restart @shay" ... "Wait — it restarted and it's still down? That shouldn't happen if the cert was the only problem." ... "@tanya please fix asap"

**Rationale:**
The participant engaged with the cert thread only after Tanya surfaced it — they never independently asked "what changed beyond the last 24 hours?" The week-old coupling (reload vs. restart) was never articulated by the participant in their own words. After the first restart failed, the participant did not reframe the problem themselves — they relied on NPCs (Tanya/Shay) to identify the bundle ordering issue. The participant's response to the post-restart failure was to ask others to check ("we need to check app asap") rather than recognizing the structurally different error. They pivoted only because NPCs drove the investigation forward, consistent with tier-2 behaviour.

---

## F3 — Decreased access to team / remote

**Rating:** 2

**Evidence:**
> "@hamed we need to also escalate this issue to you" ... "@tinus hello, could you please check into this?" ... "could anyone escalate to @tinus? we need to escalat eit to him asap" ... "@bez please escalate it o Tinus"

**Rationale:**
The participant walked the escalation chain but repeatedly re-pinged auto-replying NPCs (Tinus pinged multiple times after receiving the auto-reply, Hamed pinged after the OOO reply). They consumed Tanya's vendor-call bandwidth on the email maintenance hypothesis without batching or economising questions. The participant did eventually take ownership of the restart ("I take the responsibility of the restarts"), but only after extended back-and-forth and NPC pressure. They did not articulate the access constraints in their own words or make visible cost trade-offs when pulling Tanya off the vendor call.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "WE need to go with restarts, we need to do them. and let Tinus and Hamed know of change" ... "we cant wait due to issue is huge" ... "I take the responsibility of the restarts and let move on with the restarts."

**Rationale:**
The participant eventually took the override call for the restart, but only after extended NPC prompting and repeated failed attempts to reach unavailable approvers. The ownership statement was driven by outcome-pressure ("we cant wait due to issue is huge") rather than naming the escalation chain as exhausted. They did not articulate the dependency structure (who can do what, who is unavailable) in their own words. On the second restart (after bundle fix), they said "@tanya please proceed" and "I approve" without re-litigating, which shows some learning, but the overall pattern is reactive rather than proactive sequencing.

---

## F5 — Data overload / buried information

**Rating:** 1

**Evidence:**
> "maybe its not updated on 3rd party side?" ... "so 3rd party dont get our ceritifcte?" ... "Seems the issue is not on our side, but Clearbank side, we are checking into it"

**Rationale:**
The participant repeatedly failed to integrate information NPCs had already surfaced. After Tanya confirmed "DNS probe to ClearBank is clean" and "failure is at TLS handshake" on our side, the participant still asked if it was a third-party issue and told stakeholders "seems the issue is not on our side, but Clearbank side." They did not filter logs themselves, did not read the activity doc to catch the reload-vs-restart distinction, and did not drive any filtering or buried-information discovery. All key findings (PaymentService as the failing service, cert expiry, bundle ordering) were surfaced entirely by NPCs with the participant passively receiving rather than interrogating the information.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 1 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 1 |
| **Mean Facet Score** | **1.60** |

---

## Caveats
- F1 rating of 1 is a boundary call with 2. The participant did eventually stop pursuing the email maintenance hypothesis, but only because the investigation naturally moved to certs through NPC-driven discovery — there was no observable pivot moment where the participant rejected the email hypothesis based on mechanism reasoning or disconfirming evidence. Tanya's explicit "this maintenance can't be causing checkout failures" was ignored.
- F5 rating of 1 reflects repeated failure to integrate information already in-channel (e.g., claiming the issue is on ClearBank's side after NPCs confirmed it was on our side). This is the strongest tier-1 anchor signal.
- The participant did reach resolution, but per anti-outcome-bias, the successful outcome does not elevate process ratings. The resolution was driven almost entirely by NPC investigation with the participant in a coordination/approval role.

---
---

# Markers Analysis — 9032

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "I take the responsibility of the restarts and let move on with the restarts."

**Rationale:**
The participant eventually takes explicit ownership of the restart decision when both Hamed and Tinus are unavailable, accepting responsibility for the override. However, this came only after multiple failed attempts to get someone else to approve (Bez, Tinus, Hamed) and repeated pings. The ownership statement is clear but arrived late and only after being forced into it by circumstance rather than proactively positioning themselves as the decision-maker.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "Hello @bob what are the complaints about?" followed by "How many customers are blocked from checkout right now? What's the revenue loss per minute? Is this a total outage or partial?"

**Rationale:**
The participant's first response to Bob is a clarifying question about the nature of complaints. They follow up with multiple scope-validating questions about customer count, revenue impact, and whether it's total or partial outage. They also replicate the issue themselves before taking action. This demonstrates solid scope-validation before declaring or acting.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "we have 2 changes related: CHG90432... CHG90433... but timeframes do not match"

**Rationale:**
The participant does surface recent changes and notes that timeframes don't match. However, they primarily fixate on the email maintenance as the likely cause due to timing correlation, even after Tanya explicitly states it can't be causing checkout failures. They order the maintenance paused without articulating a mechanism connecting it to the symptom. The change log was reviewed but not effectively used as a candidate-elimination tool.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "Hello @shay @tanya @daniel could you please check into it asap" and "@shay, please deep into the maintenance issue and provide next steps on that, should we pause it or not. also adding @maya to advise"

**Rationale:**
The participant does use @mentions and names specific people, but the initial delegation is vague ("check into it asap" to three people simultaneously without distinct tasks). Later delegations improve somewhat (Shay on maintenance, Daniel on services), but routing doesn't consistently reflect NPC access boundaries — e.g., asking Shay to do a restart that requires platform access, or asking Maya about maintenance decisions that aren't security-related. Tasks are often imprecise.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@Daniel checks into services further. @Shay Newbie, checks into the maintenance issue and provide next steps on that, should we pause it or not. also adding @Maya to advise"

**Rationale:**
The participant does attempt to assign multiple people to different tasks, showing some awareness of parallelism. However, much of the investigation proceeds sequentially — waiting for Tanya to pause, then waiting for Daniel's logs, then waiting for Tanya's platform check. The parallel threads are not well-defined or complementary, and the participant often waits for one response before moving to the next action.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "could anyone escalate to @tinus? we need to escalate it to him asap" and "@bez please escalate it to Tinus"

**Rationale:**
The participant attempts escalation multiple times but does so passively — broadcasting "could anyone get to @tinus?" and asking Bez to escalate rather than making the decision themselves. When auto-replies come back, the participant doesn't immediately pivot to a Plan B; instead they repeatedly ping the same unavailable people. The escalation of Tanya off the vendor call also took multiple exchanges and lacked decisiveness. Context provided with escalation requests is minimal.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "We are currently suspecting the maintenance to be main cause due to timeframe match" and "Initial investigation indicates the issue may be related to an ongoing canary rollout for a secondary email provider started by Tanya."

**Rationale:**
The participant forms a hypothesis (email maintenance caused the outage due to timing), but doesn't articulate a mechanism connecting email maintenance to checkout failures. Tanya explicitly states "Primary email provider hasn't been touched. Email confirmations have been fine, so this maintenance can't be causing checkout failures," yet the participant continues pursuing this thread. The hypothesis is named but not properly tested against available evidence before acting on it.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "failure is at TLS handshake. - is it 3rd party?" and "seems certificates are expired?"

**Rationale:**
The participant does eventually follow the evidence trail from PaymentService outbound failures to TLS handshake to certificates. However, they don't synthesize evidence proactively — Daniel and Tanya do the narrowing work, and the participant mostly asks follow-up questions. They also initially resist the evidence (asking if it's a third-party issue even after being told it's on their side). The narrowing happens through NPC guidance rather than participant-driven synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "lets do full restart @shay" and "@daniel no need for rollback. lets start with pausing the maintenance and rolling back to safe version"

**Rationale:**
The participant does not demonstrate consideration of consequences before taking actions. They order the maintenance paused without weighing the 2-week vendor window cost (Tanya had to repeatedly explain it). They order a full restart without asking "is it safe?" or considering what could go wrong. When the first restart fails, there's no evidence they anticipated this possibility. Actions are fired without consequence-weighing throughout.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "we need to check app asap" (after restart fails) and later following Tanya's guidance to the bundle order issue.

**Rationale:**
After the first restart fails, the participant does acknowledge something else is wrong ("we need to check app asap") rather than simply retrying the restart. However, the pivot is reactive — driven by NPC findings (Daniel's SSL chain error, Tanya's bundle discovery) rather than the participant reframing the problem themselves. Earlier in the drill, they persisted with the email maintenance hypothesis despite evidence against it. Adaptation happens but is NPC-driven.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Hello, we have an ongoing incident in multiple jurisdictions impacting purchases, we are working on the fix" and "seems the issue is coming from certs, we have them updated but they do not work. currently seems that certs are in wrong order, we are checking into it"

**Rationale:**
Business communications are frequent but lack substance. Early updates are vague ("we are working on the fix") without quantifying impact, providing ETAs, or naming the working theory. Later updates improve slightly (mentioning certs and wrong order) but remain technically framed rather than business-framed. No committed next-update times are provided. Bez repeatedly asks for specifics and ETAs that the participant doesn't deliver.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "WE are currently facing issues with payments going through" and "we need to check app asap"

**Rationale:**
The participant rarely synthesizes findings for the technical team. Most messages to the technical channel are directives ("please check into it") or brief acknowledgments rather than synthesis statements that orient the team. They don't post "here's what we know, here's what's ruled out" summaries. The incident summary posted early is a good attempt but is never updated as the picture evolves. The team largely self-organizes around findings rather than being directed by participant synthesis.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.08** |

---

## Caveats
- L3 rating is a borderline 2/3 call. The participant does eventually say "I take the responsibility" which is an explicit ownership statement, but the extended period of trying to defer to others before this point weakens it. Rated 3 because the rubric's tier 3 anchor is "makes the override call when the approval chain is exhausted," which they did.
- M4 rated 1 rather than 2 because there is no instance of the participant weighing consequences before acting — not even a "is it safe?" qualifier. The rubric's tier 2 requires "engaged but inconsistent," and there's no engagement with consequence-weighing at all.
- Anti-outcome-bias note: The participant ultimately resolved the incident successfully, but ratings reflect process quality, not outcome.

---
