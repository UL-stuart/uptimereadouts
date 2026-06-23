---

# Markers Analysis — 9159

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "Hey Bob. I'll take lead here. Can you get more details from customers on what's happening?" ... "Hamed and Tinus are out. Bez has handed me authority. Restart payments, Tanya and get the cert working."

**Rationale:**
The participant takes lead immediately and drives the response throughout. They make the restart override call when both approvers are unavailable, claiming Bez handed them authority. However, they don't explicitly name personal accountability or consequences ("blowback's on me") — they needed prompting from Shay ("own it and move forward... tell team that you're taking responsibility") before proceeding. This places them at tier 3 rather than 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "Is this impacting all customers or just a subset? How much revenue are we losing per minute right now?" ... "Is checkout fully blocked or are some transactions still going through? I need to know the scale of the impact."

**Rationale:**
The participant's early moves include scope-validating questions about customer impact, regional scope, and whether checkout is fully blocked. They also ask Shay to replicate the issue. These are substantive clarifying questions before taking remediation action. They don't deeply probe the error pattern (same error vs. variants, same step vs. different), which would push to tier 4.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "Daniel and Hamed, please start looking into the changelogs for pushes your teams have done. See if there's anything that looks like a smoking gun." ... "a rollback of all the changes that occurred after the incident, as well as any changes up to an hour before the first reported issue"

**Rationale:**
The participant asks for changelogs, which is good. However, when the team reports nothing obvious ("None of the PROD deployment timings line up exactly"), the participant orders a blanket rollback of all six PROD changes without articulating a mechanism connecting any specific change to the symptom. They asked the question but didn't use the answer as an elimination pass — they used it as a rollback queue. This is the tier 1–2 pattern described in the rubric.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "Daniel and Hamed, please start looking into the changelogs..." ... "Tanya, look at changelogs and see if there's anything suspect to this issue." ... "Shay, you can work that theory on payment timeout bump..."

**Rationale:**
The participant consistently names specific people for specific tasks throughout the drill. They route platform-side work to Tanya, log/app work to Daniel, and theory-testing to Shay. Some routing is slightly off (asking Hamed who is OOO, initially asking Tanya to fill Hamed's shoes when she's on a vendor call), but overall delegation is named and directed. Not quite tier 4 because of some misrouting early on.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "Shay, you can work that theory on payment timeout bump from 10s to 12s... Find any changelogs related and see how to rollback if needed." ... "Tanya, follow up on Shay's thought on the cert chain."

**Rationale:**
The participant mostly works sequentially — asking for changelogs, waiting, then ordering blanket rollbacks, waiting for those to complete, then asking "ideas, anyone?" Only after the rollbacks fail do they begin to fan out. The Shay/Tanya parallel assignment comes late in the drill. For most of the investigation, the participant pursued one thread at a time (changelogs → rollbacks → deep dive), which is a tier 2 pattern.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "Ok Tanya, I'm authorizing you to push that vendor call to lower priority. Move to investigating this P1 outage." ... "Hamed and Tinus are out. Bez has handed me authority. Restart payments, Tanya and get the cert working."

**Rationale:**
The participant escalates Tanya off the vendor call (though somewhat delayed) and works the approval chain for the restart. When Hamed auto-replies, they go to Bez, and when Bez declines technical sign-off, they take the call themselves. The escalations are concrete and move the investigation forward. However, they don't explicitly name the cost of pulling Tanya off the vendor call (the 2-week delay), which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Roll the email maintenance back anyway, if you can at all." ... "a rollback of all the changes that occurred after the incident, as well as any changes up to an hour before the first reported issue"

**Rationale:**
The participant does not explicitly articulate hypotheses before acting. They pursue the email maintenance angle despite Tanya repeatedly stating it's unrelated, and order blanket rollbacks without naming a mechanism. They don't frame actions as hypothesis tests ("if X is the cause, then rolling back X should fix it"). The cert thread emerges from team investigation rather than participant-driven hypothesis formation. This is a tier 2 pattern — acting without naming the theory.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "Ok. Site is still broke. Ideas, anyone?" ... "Thoughts, anyone?"

**Rationale:**
The participant struggles to synthesize evidence into scope-narrowing conclusions. When told "None of the PROD deployment timings line up exactly" and "PaymentService is throwing errors consistently — but there's been no change on it for a long time," they still order blanket rollbacks rather than narrowing to PaymentService. After rollbacks fail, they ask the team for ideas rather than synthesizing what's been ruled out. The narrowing to the cert issue is driven by Daniel and Tanya's investigation, not participant synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "What are the implications of the restart?" ... "Do we have a backend site testing method that gets around the banner? Also, I thought the banner was an actual banner. Not a frontpage."

**Rationale:**
The participant asks about restart implications, which shows some consequence awareness. However, they order blanket rollbacks of six PROD changes without weighing consequences, and the maintenance banner deployment catches them off guard (they didn't realize it would block the entire site). They don't anticipate secondary failure modes after the first restart fails. The single "what are the implications" question earns tier 2 but not tier 3.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Ok. Site is still broke. Ideas, anyone?" ... "Daniel, yes do so." [re: deep dive into downstream service] ... "Tanya, follow up on Shay's thought on the cert chain."

**Rationale:**
After the blanket rollbacks fail, the participant does pivot — they stop rolling back and redirect to deep-diving the specific failing service. When the first restart fails, they don't retry the same action but instead follow the team's suggestion about the cert chain. The pivots happen, though they're somewhat passive (asking "ideas, anyone?" rather than driving the reframe). This meets tier 3 — doesn't repeat failed actions, redirects investigation.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Still scoping the issue. Will update you in 5 or 10mins." ... "Purchases can't be completed. Seems to be multiple regions." ... "Not yet. We paused some maintenance work and we're working on rolling back any changes that could be at all related."

**Rationale:**
The participant's business communications to Bez are largely vague and reactive. They don't quantify revenue impact (despite Bob providing the numbers), don't share working theories, and don't commit firm next-update times. Updates like "Still working on that" and "Team still in dark - I'm scrounging SMEs" lack substance. The later update "restart did not fix. Cert issue with ordering of cert chain. Fixing. ETA 2mins" is better but comes very late. Overall tier 2 — engaged but inconsistent.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Ok. Site is still broke. Ideas, anyone?" ... "Thoughts, anyone?" ... "Let's all put out the other theories we have. Please format list for readability."

**Rationale:**
The participant rarely synthesizes the current state of knowledge for the technical team. They don't post messages like "we've ruled out deploys, focus on PaymentService outbound now." Instead, they ask open-ended questions ("Ideas, anyone?") without framing what's been eliminated. The team drives its own narrowing (Daniel identifies PaymentService, Shay suggests cert chain) without synthesis from the IC. This is a tier 1–2 pattern.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.42** |

---

## Caveats
- L3 is a borderline 3/4 call. The participant does take the override decision, but only after Shay explicitly prompts them to "own it." Rated 3 because the ownership was reactive to prompting rather than proactive.
- M5 is a borderline 2/3 call. The participant does pivot after rollbacks fail, but the pivot is somewhat passive ("ideas, anyone?"). Rated 3 because they don't repeat the failed approach and do redirect when the team offers alternatives.
- K4 rated 2 rather than 1 because the participant does occasionally relay information (e.g., forwarding Bob's revenue numbers to Bez channel), but doesn't synthesize for the technical team specifically.

---