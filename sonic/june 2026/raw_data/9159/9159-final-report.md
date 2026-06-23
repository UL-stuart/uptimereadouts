# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to reason through systemic complexity under pressure — sorting misleading signals from real ones, navigating hidden dependencies, coordinating a team with constrained access, and synthesizing noisy information into actionable direction. This report covers what showed up in your run and where the growth edges are for your next rep.

---

## F1 — Misleading correlations

**Operating at: Not yet evident**

Early in the drill, you locked onto the email maintenance correlation and continued pursuing it — including ordering a rollback — even after a team member explicitly disconfirmed the mechanism ("Email service is invoked after payments"). You also ordered a blanket rollback of all recent production changes without articulating a mechanism connecting any specific change to the symptom. The pivot away from these false leads came only after the remediation attempts failed, not from reasoning about *why* the correlation didn't hold.

*Growth edge:* When a team member provides mechanism-disconfirmation (not just "I don't think so" but "here's why it can't be that"), practice treating that as a hard elimination rather than something to override. On your next rep, try naming aloud what would have to be true for a correlation to be causal — and check whether that mechanism exists before acting on it.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You noticed something was structurally wrong when the first restart failed ("it restarted and it's still down? That shouldn't happen if the cert was the only problem"), which is a good instinct. However, the deeper coupling — a cert rotation from days earlier interacting with a service restart — was surfaced by team members rather than by your own reframing. You engaged with the coupling once it was named, but reactively.

*Growth edge:* When a restart or rollback doesn't resolve the issue, practice asking "what else changed that I haven't looked at yet?" before waiting for the team to surface it. Expand your change window beyond the last 24 hours as a deliberate move.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You recognized that key people were unavailable and attempted to route around them — assigning Tanya to fill a gap, escalating to Bez for authorization. However, you assigned tasks to Tanya while she was on a vendor call without explicitly weighing the cost of pulling her off, and you didn't batch your questions to constrained resources. Your delegation was active but didn't economize on the limited bandwidth available.

*Growth edge:* When a key person is occupied, name the trade-off explicitly before pulling them ("Tanya is on a vendor call — pulling her costs us X, but we need Y"). This forces you to be intentional about when and how you use constrained access. Your instinct to route around was solid — the next step is making that routing efficient.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You worked the approval chain for the restart — going to Bez when Hamed and Tinus were unavailable — and eventually took the override call yourself. But the path there was somewhat forced: you claimed authority that wasn't clearly granted, and you needed a team member to prompt you to own the decision. On the second restart, you authorized cleanly without re-litigating, which is a positive signal. The dependency structure (who can approve what, and what happens when they're unavailable) wasn't named proactively.

*Growth edge:* Practice mapping the approval chain early: "If I need to restart a service, who signs off? If they're out, who's next? If no one's available, what's my threshold for self-authorizing?" Naming this structure up front saves time when the pressure hits. Your willingness to eventually take the call is the foundation — the next step is getting there faster and more deliberately.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You delegated log investigation and changelog review to others, which is appropriate. However, when results came back, you accepted summaries without driving further filtering — for example, when told that PaymentService was throwing errors consistently with no recent changes, you didn't independently narrow to that service's dependencies. The critical distinction between a service reload and a full restart (buried in the runbook) wasn't caught. Your team members drove the filtering that ultimately mattered.

*Growth edge:* When a team member surfaces a finding, practice asking one more question before moving on: "What does that rule out? What does it point to?" This turns you from a delegator-and-receiver into someone actively shaping the filter. Also, when runbooks are available, scan for conditional steps (reload vs. restart, partial vs. full) — those distinctions often hide the real fix.

---

## Looking Forward

You showed consistent willingness to take the lead, delegate to named people, and adapt when your initial approach didn't work — these are real strengths to build on. The primary growth area across this run is moving from reactive to proactive reasoning: eliminating hypotheses based on mechanism rather than failed experiments, synthesizing what's been ruled out for your team rather than asking open-ended questions, and naming constraints and trade-offs explicitly before acting on them. On your next rep, try narrating your reasoning out loud — even briefly — before each major action. That single habit tends to surface the gaps before they cost you time.