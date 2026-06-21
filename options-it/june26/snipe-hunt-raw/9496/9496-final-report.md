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

You showed clear strengths in taking ownership under pressure and in routing work to the right people with clear asks. The consistent growth edge across this run is moving from *reactive* to *proactive* reasoning: using disconfirmations, failed fixes, and access constraints as active information rather than waiting for alternatives to exhaust themselves. On your next drill, try treating each negative result as a narrowing tool — name what it rules out, say it aloud to the team, and let that shape your next move.