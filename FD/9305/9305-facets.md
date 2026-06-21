# Facets Analysis — 9305

## F1 — Misleading correlations

**Rating:** 1

**Evidence:**
> "mail maintenance started right as checkout began failing" ... "@shay can email maintence be stopped" ... "please pause" ... "do we know for sure its not the the DNS change" ... "the email maintenance kicked off right when checkout failures started. still feels worth keeping an eye on — that timing hasn't gone away."

**Rationale:**
The participant locked onto the email maintenance/DNS correlation and pursued it persistently despite multiple disconfirming signals. Tanya explicitly stated "Email maintenance is paused and unrelated. It's a separate system, no overlap with checkout," yet the participant continued returning to the email hypothesis. They pulled Tanya off her vendor call based on this false lead. Even after DNS was explicitly ruled out, Shay re-raised the timing and the participant echoed it. The participant never articulated a mechanism for how email could break checkout, and pivoted only when Bez/Daniel forced the PaymentService focus through logs — a reactive pivot driven entirely by NPC evidence presentation, not mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "Jun 03 10:46:12 2026 GMT ← EXPIRED" ... "we have an expiry?" ... "not sure why the process isn't picking up the new certificate" ... "can we update this cert? so that it is picked up"

**Rationale:**
The participant engaged with the cert thread only after NPCs surfaced it (Tanya's CHG90123 and the server check). They did not independently ask "what changed beyond the last 24 hours?" — that question was never raised by the participant. When the restart failed, the drill ended before the participant could reframe. The participant accepted the reload-vs-restart distinction only when Tanya raised it ("Since the reload didn't work, a full restart is our next option") rather than reading the runbook themselves. They connected the expired cert to the problem but did not trace the week-old coupling independently. This is tier-2 behaviour: engaging with the cert thread only when NPCs named it, partial connection of timestamps, and no independent mechanism reasoning about the temporal gap.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@hamed can you help with this" [receives auto-reply] ... "@hamed can we check this" [receives auto-reply again] ... "@tinus can you find out how much money we are losing" [receives auto-reply] ... "please pause" [pulls Tanya off vendor call]

**Rationale:**
The participant re-pinged Hamed after already receiving an auto-reply — a clear tier-1 signal. However, they did eventually accept the constraints and move on. They pulled Tanya off the vendor call without batching questions or economising on her time, and the reason given was to investigate the email maintenance lead (low-value). They never articulated the access constraints in their own words. The escalation to Tinus for revenue figures (not his role) shows poor constraint awareness. However, they did eventually work with available team members (Shay, Daniel, Tanya), which prevents a tier-1 rating. Overall this is tier-2: walking the escalation chain without articulating the constraint pattern, consuming Tanya's bandwidth on low-value queries.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "can bez sign it off?" ... "@daniel can you sign this off" ... "who is running it?" ... "i give my direct authorisation to restart the payments"

**Rationale:**
The participant did eventually take ownership of the restart authorisation, but only after multiple NPCs explicitly told them they were the incident lead and that neither Bez nor Daniel could approve it. They did not walk the escalation chain in a structured way — instead they asked Bez, then Daniel, then asked "who is running it?" before being told it was them. The ownership statement ("i give my direct authorisation") came only after repeated NPC prompting, with no reasoning about the exhausted escalation chain. They did not name the dependency structure or sequence work to avoid bottlenecks. This matches tier-2: takes the override call only after explicit NPC prompting, without naming the escalation as exhausted.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "can you look more in to this" [after Daniel posts logs] ... "so this isnt the cause either then?" [after Tanya shares cert rotation activity doc] ... "not sure why the process isn't picking up the new certificate"

**Rationale:**
The participant was initially captured by the loudest signal (email maintenance volume/timing) — a tier-1 behaviour. However, they did eventually engage with the PaymentService logs when Daniel surfaced them and asked Tanya to check the cert. They did not independently filter logs to PaymentService, did not read the activity doc carefully enough to catch the reload-vs-restart distinction, and when Tanya shared the cert rotation doc, the participant's response was "so this isnt the cause either then?" — failing to integrate the information that had just been surfaced. They relied heavily on NPC summaries without further interrogation. This is tier-2: accepting NPC summaries without driving the filter, engaging with key concepts only once NPCs surface them.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 1 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **1.80** |

---

## Caveats
- F1 borderline 1/2: The participant did eventually move off the email lead, but only because NPCs forced the pivot through concrete log evidence (Daniel's PaymentService logs). The pivot was entirely NPC-driven with no mechanism reasoning from the participant. Even after the pivot, Shay re-raised the email timing and the participant echoed it ("we have no leads to the problem" followed by Shay's email comment). Rated 1 because the participant never articulated mechanism reasoning and stayed on the prime through multiple disconfirming signals.
- F2: The drill ended immediately after the restart failed, so the post-restart reframing layer could not be assessed. Rating is based solely on the week-ago coupling surface.
- F3: The double-ping of Hamed is a strong tier-1 signal, but the participant's eventual adaptation to work with available team members prevents a floor rating. Boundary call between 1 and 2; rated 2 because the re-ping pattern was limited to one NPC rather than systematic.

---