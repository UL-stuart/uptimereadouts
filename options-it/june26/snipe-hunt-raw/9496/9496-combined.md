# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, coordinate a partially unavailable team, and locate a root cause buried beneath layers of recent changes and system complexity. The observations below reflect how you engaged with each of these challenges and where your next growth edges sit.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you pursued the email-maintenance correlation and committed to a systematic rollback strategy across multiple services. When a team member explicitly disconfirmed the email link, you continued down that path before eventually accepting the disconfirmation — but the pivot came because rollbacks concretely failed, not because you reasoned through *why* the correlation didn't hold mechanistically. On your next rep, practise pausing when a teammate offers a clear disconfirmation: ask yourself what mechanism would need to be true for the correlation to hold, and let that reasoning — not just the failure of alternatives — drive your pivot.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the week-old certificate rotation as the root cause, but only after team members surfaced the timeline and connected the dots for you. The question "if it was done last week, why are we only experiencing this now?" is exactly the right instinct — next time, try asking it earlier and independently, before the team hands you the answer. The reload-versus-restart distinction also came from a teammate's reading of the runbook rather than your own interrogation of the documentation. Growth edge: when a fix fails, treat that failure as a structural clue — ask what kind of problem would survive a restart — rather than broadening the search outward to network or external providers.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You pulled a key team member off a vendor session decisively, and you eventually walked the escalation chain to reach an approver. However, you pinged unavailable colleagues multiple times after receiving auto-replies without articulating the constraint pattern aloud or adjusting your plan around it. On your next rep, try naming the access constraint explicitly — "Hamed is out, Tinus is unreachable, so my options are X and Y" — and use that framing to move faster toward alternatives rather than re-attempting blocked paths.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

This was your strongest facet in this run. You walked the approval chain methodically — attempting Hamed, then Tinus, then escalating to Bez — and when prompted to make the call yourself, you took explicit ownership of the restart decision and its consequences. You also kept multiple team members working in parallel, routing platform-level investigation to the right person and log analysis to another. Your delegation was purposeful and appropriately scoped throughout. The growth edge here is proactiveness: try naming the full dependency structure as a single constraint statement *before* you're forced into it by exhausting options, so you can compress the escalation timeline.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked for logs and accepted deep-dive summaries from your team, but you didn't drive the filtering yourself — the critical signals (the cert chain failure, the bundle requirement, the reload step in the runbook) were all surfaced by teammates rather than caught through your own interrogation of the data. On your next rep, practise reasoning about *absence* of signal: if internal service calls are clean but external-facing calls fail, what does that boundary tell you? Use that kind of structural reasoning to direct where your team looks, rather than waiting for them to surface the answer.

---

## Looking Forward

You showed clear strengths in taking ownership under pressure and in routing work to the right people with clear asks. The consistent growth edge across this run is moving from *reactive* to *proactive* reasoning: using disconfirmations, failed fixes, and access constraints as active information rather than waiting for alternatives to exhaust themselves. On your next drill, try treating each negative result as a narrowing tool — name what it rules out, say it aloud to the team, and let that shape your next move.# Facets Analysis — 9496

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Thanks @daniel - please can we roll back Tanya's most recent change? I want to roll back change systematically"

**Rationale:**
The participant initially pursued the email maintenance/DNS correlation and systematically rolled back multiple changes (shipping, product catalogue, checkout services) before pivoting. After Tanya explicitly stated "Primary email provider is untouched. Email confirmations have been sending fine, so this maintenance isn't causing checkout failures," the participant still pulled Tanya off the vendor call to roll back. Later, after multiple failed rollbacks and Shay's repeated nudging about email, the participant eventually accepted Tanya's disconfirmation ("For the clarity, I'm 100% sure that email maintenance is not causing this issue"). The pivot was reactive — driven by concrete failure of rollbacks rather than mechanism reasoning — placing this squarely at tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "If it was done last week, why are we only experiencing this issue now?" ... "So what you are telling me, is the new certs were applied but weren't applied correctly so that payment service has continuously been using the old certs until the day of expiry (today) and now the new certs won't work?"

**Rationale:**
The participant engaged with the week-old coupling only after NPCs surfaced the cert rotation history and explicitly connected the dots. The participant did not independently ask "what changed beyond the last 24 hours?" — that came from Shay/Tanya's investigation. After the first restart failed, the participant did not immediately reframe the failure as structurally different; instead they asked about external providers, network, firewalls, and ClearBank IPs before eventually returning to the cert chain issue when Tanya surfaced the verification failure. The reload-vs-restart distinction was taken from NPC framing ("Step 3 in the doc is to reload"). Pivot latency after the restart failure was well beyond 5 exchanges. This matches tier 2: engages with the week-ago question only when NPCs name it, partial connection of timestamps, reload-vs-restart taken on NPC framing.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tanya please drop from vendor session, this is business impacting and a SEV-1 incident" ... "@tanya please can you call @hamed personal number, tell him we have a SEV-1 and require his input"

**Rationale:**
The participant pulled Tanya off the vendor call without articulating the cost trade-off or economising on her bandwidth. They repeatedly pinged Hamed after receiving the auto-reply (at least 3 times), and pinged Tinus multiple times after receiving his auto-reply. There is no statement of the access constraint pattern in the participant's own words — they never articulated "Hamed is OOO, Tinus is at the summit" as a constraint to work around. They did eventually escalate to Bez for approval, which shows some chain-walking, but the repeated re-pinging of unavailable NPCs and lack of constraint articulation places this at tier 2 rather than tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@bez can we please get your approval given Tinus and Hamed are unreachable right now? Thanks" ... "Restart the payments please. I will take the balme if anything goes wrong"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), escalated to Bez, and when Bez said "make the call and own it," the participant explicitly took ownership ("I will take the blame if anything goes wrong"). This matches tier 3 path (b) — walking the escalation chain to exhaustion and then explicitly taking ownership. They also delegated parallel work to available NPCs (Tanya on platform, Daniel/Shay on logs). However, they did not name the dependency structure aloud as a single constraint statement before being forced into it, and on the second restart (after bundle fix) they simply said "restart the service please" without re-litigating — which is appropriate. The lack of proactive constraint enumeration and the need for Bez's explicit prompt keeps this at tier 3 rather than 4.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Yes please, deep dive" ... "The Activity doc says Step 3 is to reload the server. That might get the process to pick up the new cert."

**Rationale:**
The participant did not drive filtering proactively — they asked Daniel to pull logs but accepted NPC summaries without further interrogation. The reload-vs-restart distinction from the runbook was surfaced by Shay, not caught by the participant reading the doc themselves. The participant did not reason about absence of signal (e.g., internal calls clean → external boundary failure). They eventually engaged with the cert chain/bundle concept but only after Tanya ran the openssl verify and Shay stated "two certificates needed, it's a bundle." The participant relied heavily on NPCs to surface and interpret buried information rather than driving the filter themselves, placing this at tier 2.

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
- F3 rating was a boundary call between 1 and 2. The repeated re-pinging of auto-replied NPCs (Hamed pinged 3+ times, Tinus pinged 2+ times) is a tier-1 anchor behaviour, but the participant did eventually walk the escalation chain and reach Bez, which is tier-2 territory. Weighted toward tier 2 based on the anti-first-impression-lock reminder and the eventual chain-walking behaviour.
- F4 tier-3 vs tier-4 boundary: the participant took ownership clearly but only after Bez explicitly said "make the call and own it" — this NPC prompting is noted in the tier-2 anchor but the chain-walking behaviour preceding it elevates to tier 3 via path (b).
- The participant gave a "firm estimate" of 10 minutes ETA early in the incident with no basis, which is not directly scored by any facet but contextualises the overall approach.

------

# Markers Analysis — 9496

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "Restart the payments please. I will take the balme if anything goes wrong"

**Rationale:**
The participant explicitly takes ownership of the restart decision when both Tinus and Hamed are unavailable, accepting personal accountability for consequences. They also drive the response throughout — declaring the incident, directing rollbacks, pulling Tanya off the vendor session. However, the ownership statement comes only after Bez prompts them to "make the call and own it," which slightly reduces the proactiveness compared to tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "What are the complaints @bob ? Please expand. I need to know where these customers are based and numbers. Thanks"

**Rationale:**
The participant's first response to Bob's vague complaint is a clarifying question asking for specifics about the nature of complaints, customer locations, and numbers. They also attempt to reproduce the issue themselves before taking action. This demonstrates scope-validation before declaring or acting, meeting the tier 3 expectation.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "Ok thanks, please can I have an overview of all changes?" ... "Thanks @daniel - please can we roll back Tanya's most recent change? I want to roll back change systematically"

**Rationale:**
The participant asks for the change log, which is good. However, they then proceed to roll back changes systematically without articulating a mechanism connecting any specific change to the symptom. They roll back shipping, product catalogue, and checkout changes sequentially without using the change log as a candidate-elimination tool. This is the "asked the question but used it as a rollback queue" pattern described as tier 1–2 in the rubric.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya please take a look from your side re: handshake failure thanks" ... "@maya anything on your end in terms of security?" ... "@bob how many customers do we have on the site right now?"

**Rationale:**
The participant consistently uses @mentions to assign specific tasks to specific people — Tanya for platform/cert checks, Daniel for logs, Bob for customer numbers, Maya for security. They route platform-level cert work to Tanya appropriately. Some early delegation is slightly misrouted (asking Daniel to roll back Tanya's change), but overall the pattern is solid and meets tier 3.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@maya anything on your end in terms of security?" ... "@bob how are we looking, please give me an update on numbers"

**Rationale:**
The participant does occasionally fan out to multiple people (Maya for security, Bob for numbers), but the overall investigation pattern is largely sequential — roll back one change, wait for result, roll back next change, wait for result. The security check to Maya is a parallel thread, but the core investigation proceeds one step at a time rather than running multiple distinct hypothesis threads concurrently.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya please drop from vendor session, this is business impacting and a SEV-1 incident" ... "Please drop now and roll back"

**Rationale:**
The participant escalates Tanya off the vendor session decisively when investigation is blocked, overriding her initial refusal. They also attempt to reach Hamed and Tinus multiple times, and when both are unavailable, they escalate to Bez for restart approval. The escalations include context (SEV-1, business impact). However, they don't explicitly name the cost of pulling Tanya (the 2-week vendor slot loss), which keeps this at tier 3 rather than 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "Thanks @daniel - please can we roll back Tanya's most recent change? I want to roll back change systematically"

**Rationale:**
The participant does not explicitly articulate hypotheses before acting. Their approach is to "roll back changes systematically" rather than forming a theory about what might be causing the issue and testing it. They don't name a mechanism connecting any specific change to the symptom. Later, when the cert issue is identified, they engage with it, but the early investigation lacks explicit hypothesis formation and testing.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "So what you are telling me, is the new certs were applied but weren't applied correctly so that payment service has continuously been using the old certs until the day of expiry (today) and now the new certs won't work?"

**Rationale:**
The participant does eventually synthesize the cert situation into a coherent understanding. However, during the early investigation, they don't use failed rollbacks as elimination evidence to narrow scope. They roll back multiple changes without synthesizing the negatives. The narrowing largely happens through NPC guidance (Daniel identifying PaymentService errors, Tanya finding the cert) rather than participant-driven evidence synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "I would no like to roll back Daniel's change. The error being seen relates to paymentservice that links directly from CheckoutService."

**Rationale:**
The participant shows some reasoning about why to roll back specific changes (connecting PaymentService to CheckoutService), but generally fires rollbacks without asking "is it safe?" or considering side effects. They don't anticipate that the restart could expose a secondary issue, and they don't name costs when pulling Tanya off the vendor session. The "I will take the blame" statement addresses accountability but not technical consequences of the restart itself.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "I think by now we should be looking into the logs to understand the root failure, which is not surfacing on either our dashboards or in the alerts"

**Rationale:**
After multiple failed rollbacks, the participant recognizes the rollback approach isn't working and pivots to log analysis. This is a clear adaptation. After the first restart fails, they also adapt — checking with the vendor, investigating network, and eventually pulling logs again to discover the bundle issue. They don't stay stuck in the rollback frame indefinitely, meeting tier 3.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Hello! Major incident. No successful checkouts coming through on our side. Zero successful transactions since this started @ 5.18pm. Affecting customers globally." ... "ETA to resolution: 10 mins" ... "Firm estimate"

**Rationale:**
The initial business update names the scope (zero transactions, global) which is good. However, the "ETA to resolution: 10 mins" and "Firm estimate" are unfounded — the participant has no basis for this claim at that point. Later updates are thin: "We have rolled back a number of changes to no avail" and "the team are doing great" — which Bez explicitly rejects. No working theory is shared with business stakeholders, and the cadence drops during the secondary failure.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "The logs are showing checkout errors across multiple services, not isolated to one area"

**Rationale:**
The participant rarely synthesizes state for the technical team. They relay information back (repeating what Daniel says) but don't post synthesis statements that orient the team on what's been ruled out or what the current working theory is. The technical team largely drives itself through Daniel and Tanya's findings, with the participant asking for updates rather than framing the investigation scope.

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
- L3: The ownership statement ("I will take the balme") comes after Bez explicitly prompts "make the call and own it." This is a boundary call between 2 and 3; rated 3 because the participant does ultimately make the call and accept responsibility, and they drive the response throughout (pulling Tanya, declaring incident, directing rollbacks).
- K2: The "Firm estimate" of 10 minutes with no basis is problematic — it's substantive in form but misleading in content. Rated 2 rather than 1 because the initial update does contain scope information.
- M5: The pivot to logs is partially NPC-prompted (Daniel suggests "if we could follow the logs"), but the participant had already expressed the same idea moments before ("I think by now we should be looking into the logs"). Credited to the participant.

---