# Post-Drill Developmental Report

This drill placed you in a live checkout outage with constrained team availability, multiple competing signals, and an escalation structure that required you to navigate coordination dependencies under pressure. The facets below capture how you engaged with the systemic complexity the scenario surfaced.

---

## F1 — Misleading correlations

**Operating at: Not yet evident**

Early in the drill, you identified the timing overlap between email maintenance and the checkout failures and pursued that thread persistently. When team members provided disconfirming information — confirming the maintenance system had no overlap with checkout — you continued returning to the correlation without articulating a mechanism that could explain how one would cause the other. The pivot away from this lead came only when others surfaced concrete log evidence pointing elsewhere.

*Growth edge for next rep:* When a correlation catches your attention, practice naming the mechanism aloud — "email maintenance could break checkout *if* X." If you can't complete that sentence, treat the correlation as background noise rather than a lead. Notice when you're returning to a hypothesis that's already been addressed, and ask yourself what new information would change your mind.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You engaged with the certificate thread once team members surfaced it, connecting the expired cert to the checkout failure. However, you didn't independently ask what might have changed beyond the immediate 24-hour window — the week-old coupling between the cert rotation and the current failure was identified by others rather than through your own temporal reasoning.

*Growth edge for next rep:* Expand your change-window instinct beyond "what happened today." When a system fails without an obvious recent trigger, practice asking "what changed in the last week or month that could have a delayed effect?" This kind of temporal reasoning helps surface hidden couplings before NPCs hand them to you.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You encountered reduced team availability — auto-replies, people on calls — and eventually adapted by working with those who were present. However, you re-contacted a team member after already receiving their out-of-office reply, and when you pulled a colleague off a vendor call, the reason was to investigate a low-value lead rather than a high-priority question. You also directed a revenue-impact question to someone outside that role.

*Growth edge for next rep:* When you hit an access constraint, name it to yourself: "Hamed is unavailable — who else can answer this, or can I proceed without it?" Batch your questions before pulling someone off another task, and match the ask to the person's expertise. Economising on scarce attention is a coordination skill worth practising deliberately.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You ultimately took ownership of the restart authorisation, which was the key coordination bottleneck in this drill. However, you arrived there only after attempting to delegate the approval to multiple people who couldn't provide it, and after being told directly that you were the incident lead. The path to ownership was reactive — you asked "who is running it?" rather than recognising the exhausted escalation chain yourself.

*Growth edge for next rep:* When you find yourself asking two or three people for the same approval and each says "not me," treat that pattern as a signal that the decision sits with you. Practice naming the dependency structure: "No one above me is available to approve this — I'm the decision point." Arriving at that conclusion faster frees the team to act.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You engaged with key data points — logs, cert information, change records — once team members surfaced and summarised them. However, you didn't independently filter or prioritise the incoming information. When a colleague shared documentation about the cert rotation, your response suggested you hadn't fully integrated what it contained. The loudest early signal (email maintenance timing) captured your attention at the expense of quieter but more diagnostic evidence.

*Growth edge for next rep:* When multiple data streams arrive, practice asking "which of these points directly at the failing component?" rather than which is most vivid or coincidental. When a teammate shares a document, take a moment to read it for mechanism clues before asking whether it's relevant — the answer is often inside the document itself.

---

## Looking Forward

Across this drill, you showed willingness to engage with the problem and direct work to team members — the instinct to coordinate is present. The consistent growth edge is moving from *reactive* to *proactive*: forming your own mechanism-based reasoning before others hand you the answer, recognising constraint patterns (unavailable people, exhausted escalation chains) as actionable signals rather than dead ends, and synthesising incoming evidence into a narrowing picture you can articulate to the team. On your next rep, pick one of these edges — mechanism reasoning or constraint recognition — and practise it deliberately. The other skills will follow.