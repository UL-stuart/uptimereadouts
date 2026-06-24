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