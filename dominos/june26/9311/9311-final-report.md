# Post-Drill Report — Snipe Hunt

This drill puts you in the middle of a live checkout outage with multiple competing signals, constrained team availability, and a root cause that doesn't surface through obvious channels. It's designed to stress your ability to reason through misleading data, coordinate under pressure, and drive an investigation forward when the system is actively resisting simple answers.

---

## F1 — Misleading correlations

**Operating at: Not yet evident**

Early in the drill, you anchored on the email maintenance timing as the likely cause and returned to that thread repeatedly — even after a team member explicitly confirmed it was unrelated. The pivot away from that lead came when another team member surfaced payment logs, rather than from your own reasoning about why the email hypothesis didn't fit the symptoms. On your next rep, the growth edge here is building a habit of asking "what mechanism would connect this change to this symptom?" before investing investigation time. When a lead is disconfirmed, name *why* you're dropping it — that reasoning is what prevents you from circling back.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the certificate thread once it was surfaced by a team member and followed along through the fix. However, the key investigative move — asking what changed beyond the obvious 24-hour window — came from your team rather than from you. The growth edge is developing the instinct to widen the change window yourself when recent changes don't explain the symptoms. When rollbacks fail, that's a signal to ask "what else changed that we haven't looked at yet?" and to drive that question rather than waiting for someone else to raise it.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You pulled a team member off a vendor call to focus on the production issue, which shows awareness of priority. You also pinged an unavailable manager for help. However, the way you used your available team members' time could be sharper — you asked the same questions about runbook steps multiple times without integrating earlier answers, which consumed bandwidth on a constrained resource. The growth edge is batching your questions and being deliberate about what you need from each person before you ask. When someone is your only available expert, every repeated question is a cost.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

When the approval blocker surfaced — a restart needed sign-off from people who were unavailable — you took the override call. That's a meaningful ownership moment. The growth edge is in how you get there: you didn't attempt the full escalation chain (a second approver was available but never contacted), and the approval itself came without articulating why you had authority or what the cost of waiting would be. On the next rep, try naming the constraint out loud: "Hamed is out, Tinus hasn't responded, we're losing £1,000/min — I'm taking the call." That reasoning protects you and orients the team.

Your delegation pattern also showed up here — you tended to pursue one thread at a time rather than running parallel investigations, which meant team members were idle while you worked sequentially through possibilities.

---

## F5 — Data overload / buried information

**Operating at: Not yet evident**

The drill surfaced multiple error signals — frontend errors, recommendation service issues, email maintenance timing — and you engaged with the loudest ones rather than filtering toward the service most likely to explain the checkout symptom. You didn't drive log filtering yourself; the payment logs that broke the case open were surfaced by a team member's initiative. You also asked for the same information repeatedly without integrating what had already been shared. The growth edge is building a filtering discipline: when you have multiple signals, ask "which of these could actually cause the symptom I'm seeing?" before chasing each one. Absence of signal in a service is also data — if checkout is failing but the frontend is serving pages, the frontend errors are probably noise.

---

## Looking Forward

Two things to carry into your next rep. First, build the habit of stating your working theory out loud — even a wrong hypothesis, named explicitly, gives your team something to confirm or challenge, and it forces you to connect your actions to reasoning. Second, practice fanning out: when you have multiple team members available, give each a distinct task and let them work in parallel rather than sequencing everything through one person. These two shifts — explicit reasoning and parallel coordination — will change the shape of your next drill significantly.