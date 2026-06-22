# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to navigate systemic complexity under pressure — sorting misleading signals from real causes, working through access constraints, and coordinating a team when the path forward isn't obvious. This report covers what showed up in your run and where the growth edges are for your next rep.

---

## F1 — Misleading correlations

**Operating at: Not yet evident**

Early in the drill, you locked onto the email maintenance timing as your leading hypothesis and pursued a rollback even after a team member explicitly disconfirmed the mechanism — noting that email confirmations were still going out and the maintenance hadn't touched the relevant system. Ordering the rollback past that direct disconfirmation shows the correlation was driving your actions rather than mechanism reasoning. You did eventually move on once the rollback produced no change, but that pivot was reactive to experimental failure rather than to the evidence already available.

*Growth edge:* When a teammate names a specific reason why a correlation can't be causal, treat that as a filter — not as something to override with "roll back anyway." Practice pausing to ask yourself: "What mechanism would connect these two things?" before committing to action on a timing coincidence.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the certificate thread once a teammate surfaced the week-old rotation, and you asked reasonable follow-up questions about why the new cert wasn't being picked up. However, you didn't independently frame the question of what might have changed beyond the 24-hour window, and when the first restart didn't resolve the issue, you didn't articulate how the post-restart error differed structurally from the pre-restart error. The team drove the investigation to the bundle-ordering issue while you followed their framing.

*Growth edge:* Practice expanding your change-window scan beyond the obvious recent timeline. When a fix doesn't work, name what's different about the new failure state — that reframing is what surfaces hidden coupling layers.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You encountered multiple unavailable team members and did eventually walk the escalation chain to find someone who could authorize action. However, you re-pinged a teammate after already receiving their auto-reply, and when you needed a key person pulled off another engagement, you routed that through a third party rather than articulating the cost trade-off yourself. You never explicitly named the access constraint pattern — that key approvers were unavailable and this was shaping your options.

*Growth edge:* When you hit an auto-reply or unavailability signal, name the constraint out loud for the team: "Hamed is out, Tinus is out — here's what that means for our options." This makes the constraint visible and helps you reason about workarounds rather than retrying the same path.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You did ultimately take the override decision on the restart authorization, claiming delegated authority and directing the action. That moment showed ownership. However, you arrived there only after a senior stakeholder explicitly pushed the decision back to you as incident lead. You didn't proactively name the coordination bottleneck or sequence the escalation chain before NPCs raised it. Your delegation also tended toward serial rather than parallel — you largely followed investigation threads one at a time rather than fanning out work to multiple people simultaneously.

*Growth edge:* Practice naming the dependency structure early: "I need X to happen, which requires Y's approval, and Y is unavailable — so here's my plan." Proactive sequencing reduces the back-and-forth that slows resolution. Also look for moments where two people could be working different threads at the same time.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked for logs and system health checks, which is appropriate, but your requests were broad ("can someone check system health and logs?") rather than targeted at the specific service showing failures. You accepted teammate summaries and followed their filtering rather than driving the triage yourself. Key distinctions — like the reload-versus-restart difference in the runbook, or the bundle ordering issue — were surfaced by teammates rather than caught through your own directed investigation.

*Growth edge:* When you ask for logs, name the specific service and the specific signal you're looking for. Targeted requests produce faster, more useful answers and help you maintain ownership of the diagnostic thread rather than waiting for teammates to synthesize for you.

---

## Looking Forward

You showed a willingness to step up and make decisions under pressure — particularly when you claimed authority for the restart. That ownership instinct is a real asset. For your next rep, the biggest leverage comes from slowing down at two moments: before committing to a hypothesis (ask "what's the mechanism?") and before delegating (ask "who specifically, and what exactly am I asking them to find?"). Those two pauses will shift you from reactive to directive, which is where the next level of incident leadership lives.