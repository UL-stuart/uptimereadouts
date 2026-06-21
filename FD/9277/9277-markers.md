---

# Markers Analysis — 9277

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "cool, I will make the call (will be approving my end in Tinus absense FYI)" ... "Tinus is away folks, ive informed business I will make a call on restart approval. @Daniel please take this as my approval and go aheaf"

**Rationale:**
The participant takes explicit ownership of the restart approval decision when both Tinus and Hamed are unavailable, communicating this to both the business and technical teams. They also direct the investigation throughout (asking for banner, escalating to Daniel, pulling Tanya off maintenance). However, they don't explicitly name the personal cost/blowback of the override decision, which would elevate to tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "what sort of complaints Bob" ... "Can we see anything these customers have in common in terms of region etc"

**Rationale:**
The participant's first substantive move after Bob's alert is asking what kind of complaints are being received. They follow up by asking about regional patterns. They gather scope information before declaring the incident or ordering remediation actions. This meets the novice expectation of scope-validating before acting, though the questions aren't as tightly targeted as tier 4 (e.g., asking about specific error types or payment methods).

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "also what all changes were deployed since initial reported issue" ... "ok Shay, if zero impact in rolling back lets try that to rule it out considering criticality of this issue - has anyone any objections before Shay rolls back?"

**Rationale:**
The participant explicitly asks for the change log and reviews recent deployments. They use the DNS rollback as a candidate-elimination test ("to rule it out"), which shows intent to use changes as a diagnostic tool rather than blindly rolling back everything. However, after the DNS rollback failed, they didn't explicitly articulate why the remaining changes were unlikely causes (no mechanism-based elimination), which would be tier 4.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@shay - any theories why that may have an impact" ... "Shay - please escalate to Daniel immediatly" ... "@Daniel - can we action a restart?" ... "Tanya - please commit to this due to criticality" ... "@Tanya please remove banner and confirm here once done"

**Rationale:**
The participant consistently names specific people for specific tasks throughout the drill — Shay for change investigation, Daniel for app-side logs and restarts, Tanya for platform/cert work, Bob for customer impact. The routing is generally appropriate to each NPC's domain. Some early delegation is slightly imprecise (asking Shay to "escalate to Daniel" rather than directly tasking Daniel), but overall meets tier 3.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "also what all changes were deployed since initial reported issue" [asked while DNS rollback discussion ongoing] ... "@Maya - any chance this could be a security issue" [asked while Tanya investigating certs]

**Rationale:**
The participant mostly works sequentially — pursuing the DNS/email maintenance thread, then waiting for results, then moving to logs, then to certs. The Maya security check is a brief parallel thread but doesn't represent sustained parallel investigation. There's limited evidence of fanning out multiple distinct investigation tasks to different people simultaneously in the early critical phase.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "Shay - please escalate to Daniel immediatly as we need this up within 15 mins" ... "Tanya - please commit to this due to criticality" ... "@Tinus - can we get approval for a restart on payements here as this is top criticality"

**Rationale:**
The participant escalates to Daniel when initial investigation stalls, pulls Tanya off her vendor session when platform-level access is needed, and works the approval chain (Hamed → Tinus → self-approval). When both approvers are unavailable, they don't leave the chain hanging — they make the call themselves. The escalations include context about criticality. However, they don't explicitly name the cost of pulling Tanya off (the 2-week delay), which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 3

**Evidence:**
> "ok Shay, if zero impact in rolling back lets try that to rule it out considering criticality of this issue" ... "is there anyway it could have a delayed impact? Please thoroughly review deployement"

**Rationale:**
The participant forms an implicit hypothesis around the email maintenance timing correlation and proposes a test (rollback to rule it out). After the rollback fails, they pivot to investigating the cert rotation as a potential delayed-impact cause. The hypotheses are somewhat implicit rather than explicitly named ("hypothesis 1..."), but the test-and-pivot pattern is present. They don't explicitly ask "does X plausibly cause Y?" before pursuing leads, which would be tier 4.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "last order was exactly 15:50, what all events happened in our architexture percisely at that time" ... "are all checkouts failing or just a portion?"

**Rationale:**
The participant uses timing correlation (last successful order at 15:50) to narrow the investigation window, asks about scope (all checkouts vs. portion), and uses the DNS rollback failure as elimination evidence to move on. They also use Bob's confirmation that all regions are affected to rule out region-specific causes. This meets tier 3 — using concrete evidence to rule things out — though they don't produce explicit synthesis statements naming what's been ruled out alongside what remains.

---

## M4 — Considers potential consequences before acting

**Rating:** 3

**Evidence:**
> "@shay re the DNS changes, what is the impact of rolling them back" ... "what is the impact of cancelling email maintenance" ... "and what is impact of pushing migration back?"

**Rationale:**
The participant consistently asks about impact before taking actions — checking the impact of DNS rollback, the impact of cancelling email maintenance, and the impact of pushing the migration back. They only proceed after confirming low/no impact. This "is it safe?" pattern meets tier 3. However, they don't anticipate secondary failure modes (e.g., checking the bundle before the first restart), which would be tier 4.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> After DNS rollback: "last order was exactly 15:50, what all events happened in our architexture percisely at that time" ... After first restart fails: "@Daniel - any other ideas on what we can try here"

**Rationale:**
After the DNS rollback doesn't fix the issue, the participant pivots to investigating timing and logs rather than rolling back more changes. After the first restart fails, they ask for new ideas and engage with the cert chain/bundle thread when it surfaces. They don't repeat failed actions or stay stuck in one frame. However, the pivot after the first restart is somewhat passive ("any other ideas?") rather than actively reframing the problem themselves, which keeps this at tier 3 rather than 4.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 3

**Evidence:**
> "ETA for rollback of DNS changes is 2 minutes, along with testing ETA 5 minutes. However that may not be the solution. ETA TBC, if must go with 15 minutes..." ... "Engineering has identified a potential root cause related to certificate bundle configuration... remediation should be relatively targeted..."

**Rationale:**
The participant provides multiple substantive updates to the business channel that include scope (all checkouts affected), impact quantification (20-30 orders/minute, thousands in revenue), ETAs, and working theories. The updates are proactive and contain useful information. However, some updates are overly verbose/templated and the cadence could be tighter — the update after the first restart failure is somewhat delayed. Meets tier 3 with elements of tier 4.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "this issue is widespread in terms of region, we are rolling back email maintenance DNS changes as the timing is aligned with failures" ... "ok who can update to correct the order"

**Rationale:**
The participant provides some scope communication to the technical team but rarely posts explicit synthesis statements that name what's been ruled in and out. Most technical channel communication is question-and-answer or delegation rather than state summaries. They don't produce clear "here's where we are" messages that orient the team (e.g., "we've ruled out DNS, deploys, and security — focus is now on cert chain"). The team largely drives the investigation findings while the participant directs traffic.

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
| M4 — Considers potential consequences before acting | 3 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 3 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.83** |

---

## Caveats
- L3: The participant takes the override decision clearly but doesn't explicitly name personal risk/blowback in the way the tier 4 anchor describes. Borderline 3/4, rated 3.
- K2: The business updates are substantive but some are quite long and template-like. The participant does provide ETAs and working theories, which pushes toward tier 3-4, but cadence through the secondary failure could be tighter.
- C6: This was a borderline 2/3 call. The participant does occasionally have overlapping threads (e.g., asking Maya about security while Tanya investigates certs), but the dominant pattern is sequential investigation. Rated 2.
- Anti-outcome-bias note: The successful resolution and NPC praise at the end were not factored into ratings.

---