# Snipe Hunt — Post-Drill Developmental Report

This drill puts you in the middle of a live checkout outage with multiple possible causes, limited team availability, and pressure to coordinate across technical and business layers simultaneously. It's designed to stress your ability to reason through misleading signals, surface hidden system relationships, and manage coordination under constraint.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, when the email maintenance timing was raised as a possible cause, you directed Tanya to investigate it. Once she reported back that email confirmations were unaffected, you moved on — which is the right outcome. The growth edge here is in *how* you moved on: the pivot came because Tanya told you it wasn't the cause, rather than because you reasoned through whether email could plausibly break payment at all. On your next rep, try articulating the mechanism before assigning someone to investigate — "could this change reach the failing component?" If the answer is no, you save time and team bandwidth without needing someone else to rule it out for you.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the certificate thread once it was surfaced by your team, and you recognised the expired-cert evidence when it appeared. The gap is in who drove the discovery: the connection between a week-old cert rotation and today's failure was identified by NPCs, and after the first restart failed, you asked for ideas rather than reframing why a restart might not resolve a cert-loading issue. The next growth edge is noticing when a fix fails and asking yourself *what structural assumption did I just invalidate?* — that's the moment where hidden coupling becomes visible, and it's worth pausing to reason through rather than immediately asking others what to try next.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You walked the escalation chain — pinging Hamed, Tinus, and eventually pulling Tanya off her vendor call. The pattern that emerged, though, was multiple individual pings to people who had already signalled unavailability, and several separate requests to Tanya rather than a single batched ask. On your next rep, try naming the constraint pattern to yourself early: "Who is actually available right now, and what can each person uniquely do?" That framing helps you economise attention — both yours and theirs — and makes the decision to pull someone off another task more deliberate rather than incremental.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

This was your strongest facet in this run. You walked the approval chain to exhaustion — checking whether Hamed or Tinus could sign off, confirming both were out, asking if anyone else could authorise, and then explicitly stating you would own the risk. You also delegated parallel work appropriately, assigning Shay to the customer-facing banner while the technical investigation continued. The growth edge toward the next level is naming the dependency structure *before* you hit it — verbalising something like "restart needs sign-off, and both approvers are OOO, so I need to decide now whether I'm willing to own this" as a single constraint statement rather than discovering it through sequential attempts.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

When evidence appeared — logs, cert status, error messages — you engaged with it. But the filtering and interpretation work was largely done by your team members, with you asking follow-up questions after they'd already synthesised. You asked "how do we fix the chain?" only after the chain verification failure had been identified for you. The growth edge is in actively reading the available documentation and evidence yourself, looking for distinctions (like reload-vs-restart) before asking others to interpret. Even a quick scan of an activity doc or error output, with a "what's different here from what I expected?" lens, can surface critical information earlier.

---

## Looking Forward

Across this drill, your coordination instincts — pulling people in, escalating when blocked, taking ownership of risk — are developing well and gave you a solid foundation to work from. The consistent growth edge is in *driving your own reasoning* earlier in the sequence: articulating mechanisms before investigating, reframing when a fix fails, and synthesising evidence yourself rather than waiting for team members to interpret it for you. On your next rep, try narrating your current understanding to the team channel — even a brief "here's what we know and don't know" statement can sharpen your own thinking and keep the investigation coherent.