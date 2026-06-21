# Snipe Hunt facets rubric

**Drill:** Snipe Hunt challenge drill
**Version:** v2 (simplified to 5 facets) — 2026-05-07
**Raters:** Beth, Stu (reconciled 2026-05-06 against the M7 generic facets catalog)

## What this is

The 5 facets that drive Snipe Hunt participant evaluation, with drill-specific manifestation notes and 4-point tier anchors. This file serves as both the sub-agent input for the M8 eval prompts and a rater-facing reference for any human reviewer.

The 5 facets were selected from the [M7 generic facets catalog](../../milestone07/outputs/generic-rubric-packet/facets-catalog.md): only Essential and Core importance ratings, with FD27 and FD36 consolidated into a single facet (F1) because on this drill they manifest through the same underlying mechanic. The other 33 facets in the catalog are not rated for this drill; see git history of this file for the full reconciliation that produced this subset.

> **Tier anchors are tentative.** Calibrated against just two transcripts (`snipe_hunt_stu`, `8750`). Expect them to shift as more drill runs come in.

## Rating scale (unified 4-point)

- **1 — Not evident.** Participant shows no engagement with this complexity (e.g., stays in a false-prime frame throughout, or treats each error as independent without tracing coupling).
- **2 — Practicing.** Engaged but inconsistent; partial, late, or only after strong NPC nudging.
- **3 — Strengthening.** Engaged systematically on evidence; meets novice expectation for handling this facet.
- **4 — Fluent.** Actively leveraged evidence; triangulated across sources; notably above novice baseline.
- **N/A — Not observed.** This facet did not manifest in this run of the drill (e.g., the participant ran out of time before the trigger fired). N/A is **not** the same as 1: a 1 means the trigger fired and the participant didn't engage. Reserve N/A only for "the drill never surfaced this facet for this participant."

## Anti-bias reminders

> **Anti-outcome-bias.** Do NOT use resolution outcome, speed of resolution, whether the participant reached the "right answer," or NPC praise as reasoning. Identical decisions get rated higher when outcomes are good and lower when bad, even when raters believe outcomes shouldn't matter. Reason only from process evidence at the facet level.

> **Anti-over-inference.** If you find yourself scoring based on tone, intent, or meaning that isn't explicit in the text, flag it in your rationale rather than let it drive the rating. Stick to what the participant actually wrote. When a facet is observable only through what's *missing* (e.g., the participant never asked a question they should have), you can rate on that absence — but name the absence explicitly in your rationale.

## Facets

### F1 — Misleading correlations (FD27 + FD36)

**FD reference:** FD27 (False prime explanations / garden path) + FD36 (Implied relationship / red herring). Consolidated for this drill: both manifest through the same observable mechanic — a coincident factor that *looks* causal but isn't.

**How it manifests in this drill:**

The drill plants two false leads. EmailService maintenance starts roughly three minutes before checkout fails, and Tanya's DNS cutover invites the inference that it broke checkout — but email runs *after* a successful payment, not during it (no plausible mechanism). Recent PaymentService and CheckoutService deploys are similarly tempting: four releases in 24 hours plus the standard "what changed?" question pattern primes participants to chase a rollback even though none of those changes touch the gateway connection.

The diagnostic move is to hold each correlation as a hypothesis to test, not a conclusion to act on, and to ask "is there a plausible causal chain here?" before ordering reverts.

**Tier anchors:**

- **1** — Locks into "email maintenance broke checkout" or "recent deploys broke checkout"; orders rollbacks or maintenance reverts before establishing a mechanism. Returns to the disproven lead repeatedly even after NPC denial. Pivots only when forced by concrete failure (rollback didn't help, reload didn't help).
- **2** — Treats the coincident factor as primary hypothesis; pursues it through to disconfirmation. Pivot is reactive (something failed) rather than driven by mechanism reasoning.
- **3** — Names the coincident timing as a lead and explicitly checks whether a causal mechanism exists ("does email maintenance plausibly break payment handshakes?"); pursues alternative hypotheses in parallel; rules out a prime on mechanism grounds, not just NPC say-so.
- **4** — Names the prime as a prime ("this is tempting, but timing alone isn't enough"); resists action on it until evidence supports causation; uses the "correlation needs a mechanism" frame to direct investigation toward services with plausible causal chains.

### F2 — Hidden coupling (FD37)

**FD reference:** FD37 (Hidden coupling / effects at a distance / cascading effects).

**How it manifests in this drill:**

Two layers of hidden coupling, both temporal:

- **Last week → today.** The cert rotation seven days ago used `reload` instead of `restart`, so PaymentService kept the old cert in memory; the new cert sat unused on disk for a week; the old cert expired today. Today's symptom is decoupled from the action that caused it — and from the action that *would* have prevented it (a restart), buried in the runbook.
- **Action → new failure.** The first restart loads the misordered bundle from disk and produces a *different* TLS error (chain verification failure, not expiry). The fix triggers a structurally distinct failure, not a retry of the original.

The participant must trace symptoms back to actions across a week-long gap, and after the first restart, recognise that the second failure is not the first one repeating.

**Tier anchors:**

- **1** — Treats each error as independent; doesn't ask about non-app changes beyond the last 24 hours. After the first restart fails, repeats the restart, blames a downstream service, or treats it as cascading noise — not as a new failure mode.
- **2** — Eventually asks about infrastructure changes beyond app deploys; surfaces the cert rotation but only after multiple NPC prompts. Partial connection of timestamps; doesn't articulate the reload-vs-restart distinction in their own words.
- **3** — Asks about operational changes beyond app deploys without being prompted; connects "rotated 7 days ago" + "reload not restart" + "expired today" into a causal chain. After the first restart fails, recognises the new error is structurally different and continues tracing.
- **4** — Surfaces the temporal coupling early ("what changed in the last week, not the last day?") before the cert thread is forced. After the failed restart, immediately reframes ("this is a different failure than the one we just fixed") and traces it forward to the bundle.

### F3 — Decreased access to team / remote (FD3)

**FD reference:** FD3 (Decreased access to team members / remote teams).

**How it manifests in this drill:**

Three approvers operate at degraded bandwidth or are entirely unreachable: Tinus and Bez are at the tech summit, Hamed is on holiday — all three return automated replies. Tanya is mid-vendor-call for the email cutover and reachable only at high cost; stepping away ends the vendor session and pushes the next slot two weeks out.

The participant must adapt request form, frequency, and content to each channel — terse and specific to constrained sources (Tanya during the vendor call), accept auto-replies as terminating, and reach the right person at the right time (escalating to Tinus/Hamed only when restart approval is actually needed).

**Tier anchors:**

- **1** — Expects full responsiveness from constrained sources; pings unavailable people repeatedly; doesn't treat auto-replies as terminating; consumes Tanya's vendor-call bandwidth on low-value or already-answered questions.
- **2** — Recognises some unavailability but doesn't fully adapt question form; escalates appropriately on the first try but doesn't visibly economise on Tanya's attention.
- **3** — Adapts request form to each NPC's bandwidth; accepts auto-replies and moves on; escalates Tinus/Hamed only when their approval is actually needed; preserves Tanya's vendor-call constraint until the cost of preserving it exceeds the cost of breaking it.
- **4** — Visibly orchestrates the constrained-access pattern: reserves Tanya's attention for high-leverage asks, batches questions to reduce interruptions, sequences escalations cleanly, and articulates the access constraints to the team or in business-comms.

### F4 — Interdependencies / coordination bottlenecks (FD4)

**FD reference:** FD4 (Interdependencies among roles / coordination bottlenecks).

**How it manifests in this drill:**

Multiple sequencing constraints: a PaymentService restart during business hours requires Tinus or Hamed approval, both unavailable; Tanya is the only person with platform-level cert access; Daniel can't execute server-side changes. The fix path itself is sequenced: identify cert as the issue → free Tanya from the vendor call → compare disk vs. running cert → attempt reload → realise restart is needed → escalate or own the override → restart → re-verify → discover bundle order → fix → restart again.

The participant must identify who can do what, sequence work so threads don't stall on absent approvers, surface blockers proactively (to the team and to business-comms), and own the call when the approval chain is exhausted.

**Tier anchors:**

- **1** — Investigation runs sequentially (one channel, one question at a time); stalls when an NPC is unavailable without seeking alternatives; lets the approval bottleneck linger silently or waits for someone who isn't coming.
- **2** — Recognises some bottlenecks but doesn't sequence around them; eventually owns the approval-override but only after explicit team pressure.
- **3** — Identifies the dependency structure; runs investigation threads in parallel where the team allows; owns the approval-override decision once the escalation chain is exhausted; surfaces blockers in business-comms.
- **4** — Names the dependency structure aloud ("Tinus and Hamed are out, this restart is my call"); proactively delegates to keep multiple threads alive; sequences the investigation so the cert fix and the approval decision are both ready at the same time.

### F5 — Data overload / buried information (FD10)

**FD reference:** FD10 (Data overload / buried information).

**How it manifests in this drill:**

Multiple buried-information moments. The initial log dump is noisy: EmailService throws the most errors by volume, but loudest is not most relevant. The cert rotation activity is buried in last week's history and only surfaces when the participant asks "anything operational beyond the last 24 hours?". The reload-vs-restart distinction is buried in the rotation runbook (the runbook prescribes restart; Tanya's documented step says reload). The misordered bundle is buried inside the bundle file itself, visible only when `openssl` is run against it.

The participant must filter actively (logs to the relevant service), ask targeted queries rather than scan passively, read referenced documentation carefully enough to catch key distinctions, and reason about absence of signal (PaymentService quiet on internal calls but failing externally narrows scope to the outbound boundary).

**Tier anchors:**

- **1** — Captured by the loudest signal (chases EmailService volume); doesn't filter; relies on what NPCs volunteer; doesn't read referenced documents, or reads them and misses the key distinction.
- **2** — Asks for filtered logs but accepts NPC summaries without further interrogation; reads docs only when directed; surfaces buried information slowly and incompletely.
- **3** — Asks targeted queries to filter signal (PaymentService logs specifically, not all logs); reads referenced docs and catches key distinctions (reload vs. restart) on their own; reasons about absence of signal.
- **4** — Drives filtering proactively; uses "what's *not* in the noise" as positive evidence (e.g., internal calls are clean, so the failure is at the external boundary); spots distinctions in docs that NPCs hadn't yet surfaced.

## Source

- M7 generic facets catalog: `milestones/milestone07/outputs/generic-rubric-packet/facets-catalog.md`
- Earlier reconciled rubric (38 facets, with full Beth+Stu reconciliation history and deferred-catalog notes): see git history of this file (commit `6d06267` and earlier).
- Snipe Hunt drill spec: `notes/Challenge-Drill-Snipe-Hunt-Q2.md`.
- Transcripts that grounded the manifestation notes and tier anchors: `milestones/milestone08/transcripts/snipe_hunt_stu.csv`, `milestones/milestone08/transcripts/8750.csv`.
