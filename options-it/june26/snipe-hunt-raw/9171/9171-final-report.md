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

You showed a consistent willingness to engage — asking questions, delegating, and ultimately stepping into the decision-maker role when the situation demanded it. The pattern across this run is that your pivots and reframes tended to follow teammate input rather than leading it. For your next drill, focus on one thing: after each new piece of information lands, pause briefly to state what it changes about your working picture before issuing the next task. That single habit will strengthen both your hypothesis management and your ability to filter noise from signal.