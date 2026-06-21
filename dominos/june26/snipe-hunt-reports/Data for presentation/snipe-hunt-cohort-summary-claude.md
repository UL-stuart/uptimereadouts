# Snipe Hunt — Cohort Performance Summary

This report summarises how your cohort performed across seven runs of the Snipe Hunt incident-response drill (run IDs 9150, 9196, 9317, 9380, 9397, 9418 and 9421). Snipe Hunt places an incident manager inside a live checkout outage in which the loudest signals are misleading, the true cause is a hidden dependency surfacing days after a change, key people are hard to reach, and both a technical team and a business stakeholder need managing at once.

The summary is deliberately qualitative and thematic rather than score-by-score. It leads with the patterns that held across the cohort, then walks the five facets the drill is built to stress, then the behavioural markers grouped by Leadership (L), Communication (K), Coordination (C) and Mindset (M), and closes with the two or three areas where focused practice would yield the most improvement.

One note on interpretation before the findings. Three of the seven runs (9380, 9397 and 9418) ended before the drill was complete — typically before the restart-and-recovery sequence — so some behaviours simply had no opportunity to appear. Where that affects a finding it is flagged, and a low signal from an incomplete run should not be read as "did it badly." A second note: throughout this drill the critical findings (the certificate rotation, the misordered bundle, the reload-versus-restart distinction) were generally surfaced by the simulated team rather than by the incident manager personally. That is exactly as it should be. Incident management is a team sport, and the manager's job is not to be the cleverest diagnostician in the room — it is to draw information out of capable colleagues and then act on it well. The findings below are framed accordingly: the cohort is good at *eliciting*, and the highest-value growth is in what happens to that information once it arrives.

---

## Cross-cutting patterns

**The cohort starts incidents well.** Almost every run opened by validating scope before acting — asking what customers were seeing, whether the outage was total or partial, how many regions were affected, and what revenue was being lost per minute. This instinct to size the problem before reaching for a fix was the most consistent strength on display, and it is a strong foundation to build on.

**The cohort will take the call when the chain runs out.** When both authorised approvers were unreachable, most runs eventually owned the override decision and authorised the restart rather than stalling. Several did this cleanly and decisively. This willingness to act under incomplete authority is, again, a genuine strength — the drill is partly designed to make people uncomfortable enough to avoid it, and most of the cohort did not flinch.

**The team-sport model is largely working.** Participants reached out, pulled the right people in, and let the team surface the technical truth. The investigation moved forward because information was elicited, not because any one person had all the answers. This is the correct shape for incident management and should be reinforced.

**The recurring opportunity is what happens *after* information arrives.** Three habits separated the stronger moments from the weaker ones across every run: pausing to weigh cost and safety before acting, integrating incoming information into a clear shared picture, and managing constrained people deliberately rather than pushing through them. These three threads run through the facet and marker detail below and form the basis of the recommendations at the end.

---

## The five facets

**F1 — Misleading correlations.** The cohort sat uniformly at the *Practicing* level here. Everyone engaged with the seductive early correlations — the email-maintenance window that coincided with the outage, the recent deployments around the same time — and most eventually moved off them. The common pattern was that the move came *after* a colleague disconfirmed the lead, rather than after a quick check of whether the correlation could plausibly cause the symptom. The practical cost is concrete: in several runs a constrained colleague was pulled off committed work to chase a lead that a single sentence — "how would an email change break payment processing?" — would have deprioritised. A couple of runs (notably 9421 and 9418) pressed the correlation harder and longer than the evidence justified.

**F2 — Hidden coupling.** This was more mixed. The crux was a certificate rotation from a week earlier whose effect only landed once the old certificate expired, compounded by the difference between reloading config and fully restarting the service. The stronger runs engaged actively once the thread appeared — 9317 stands out for explicitly questioning how a seven-day-old change could cause a failure today, which is the right reasoning even though a teammate raised the rotation. The weaker pattern was treating a failed fix as a prompt to try the next standard fix (9421 reaching for a backup server, 9418 proposing to roll back the rotation) rather than as a signal that the problem was structurally different. Note that 9380, 9397 and 9418 ended before the post-restart bundle layer could be reached, so the deepest version of this facet went untested for them.

**F3 — Decreased access to team.** This was the most uniform facet in the cohort — every run landed at *Practicing*. The shared signature was pulling the platform engineer off her vendor call (a reasonable move for a severe incident) without naming the trade-off being made, and then not economising her time once she joined. Recognising the need to escalate and reach a constrained person was reliably present; treating that person's limited attention as a budget — batching asks, preparing specific questions before pulling them in — was reliably absent.

**F4 — Interdependencies and coordination bottlenecks.** This produced the widest spread. It was the strongest area for several runs (9196, 9317 and 9421 each walked the approval chain to its end and then explicitly took ownership of the decision). It was weaker where the participant tried to route an approval to someone who lacked the authority to give it (9150 and 9418 both turned to the business stakeholder for a technical sign-off), and it could not fully appear in the runs that ended early (9380, 9397). Even among the stronger runs, work tended to proceed one step at a time rather than fanning the approval path and the technical investigation out in parallel, which is where the timeline could have been compressed.

**F5 — Data overload and buried information.** Uniformly *Practicing*. The eliciting was solid — people asked for logs, narrowed toward the payment layer, and engaged with findings once presented. The opportunity sat in interrogating and integrating what came back. The clearest example was a run that read a list of recently deployed services as a list of *failing* services and briefed the team on that basis, and another that declared the incident resolved while checkout was still broken. The unlock here is asking what is *not* failing as actively as what is — clean internal calls alongside failing outbound ones is itself a narrowing signal — and treating each summary as something to probe rather than accept.

---

## Behavioural markers by category

**Leadership (L).** Ownership of the response was a relative bright spot. Most runs reached the point of taking the override decision when the approval chain was exhausted, and several did so firmly. The growth edge is twofold: making the ownership explicit and early ("I'm the escalation lead, both approvers are unreachable, I'm authorising this and it's on me") rather than arriving at it after being prompted, and naming the personal accountability for the call rather than letting it happen quietly.

**Communication (K).** This was the cohort's thinnest area and the most consistent across runs. Updates to the business stakeholder tended to be vague reassurances — "we're working on it," "investigating now" — without quantified impact, a working theory, an ETA, or a committed time for the next update. In several runs the stakeholder asked repeatedly for specifics that did not come. On the technical side, the channel rarely received a synthesis statement — a clear "here is what we know, here is what we've ruled out, here is where we're focusing." The team often self-organised around the evidence because no one was drawing it together for them. Given how well the cohort elicits information, this is the place where a small change in habit would show the largest external difference.

**Coordination (C).** A mixed picture with clear high and low points. Scope-validating questions at the start were a strength across nearly every run. Escalation happened when people were stuck, though it was sometimes directed at the wrong authority. Delegation reached named individuals but the asks were often loosely scoped ("check the logs," "have a look") rather than tied to a specific deliverable. The weakest coordination habit was running investigation threads in parallel — most runs worked serially, asking one question and waiting for the answer before forming the next, which left available colleagues idle and lengthened the incident.

**Mindset (M).** Hypothesis formation and scope-narrowing sat consistently in the middle: working theories were usually implicit rather than named, and narrowing was carried largely by team-supplied evidence — acceptable within the team-sport model, but the integrating step (turning that evidence into an explicit, stated picture) was the missing lever. Adaptation when a path stopped working was variable; the better moments engaged with the *new* error rather than repeating the previous fix. The standout weakness across the whole cohort was weighing consequences before acting: resources were pulled and remediations were fired with little visible "what's the cost?" or "is this safe?" beforehand. This appeared in nearly every run and is the single most concentrated opportunity in the data.

---

## Recommended focus areas

The cohort already does the hard, uncomfortable things well — it sizes problems before acting, draws information out of the team, and takes ownership when the situation demands it. The following three areas build on that foundation rather than replacing it.

**1. Pause to weigh cost, safety and mechanism before acting.** This is the highest-leverage change in the data because it surfaced almost everywhere. Before pulling a colleague off committed work, before authorising a restart or a rollback, and before chasing a correlation, a few seconds of "how would this actually cause the symptom?", "what does this cost us?" and "is it safe?" would prevent dead-end resource spend and catch risk early. The aim is not hesitation — the cohort's decisiveness is an asset — but disciplined decisiveness.

**2. Turn elicited information into a shared picture, in both directions.** The cohort is strong at gathering information and comparatively weak at synthesising it. For the technical team, this means periodically posting a current-state summary: what's confirmed, what's ruled out, where the focus is now. For the business stakeholder, it means updates with quantified impact, a working theory, an ETA, and a committed next-update time. This single habit would directly lift the cohort's weakest markers and is well within reach given how well the underlying eliciting already works.

**3. Treat constrained availability as something to design around, not push through.** When a key person is hard to reach or busy with other committed work, the stronger move is to name the trade-off out loud (which creates a decision record and signals deliberateness), prepare specific batched asks so their limited time is well spent, and fan out the work that doesn't depend on them in parallel so threads stop blocking each other. The cohort already takes ownership at the bottleneck; sequencing around the bottleneck is the next step.

---

*Prepared from seven Snipe Hunt drill evaluations. Findings are qualitative and pattern-based; individual run detail is available in the per-run reports.*
