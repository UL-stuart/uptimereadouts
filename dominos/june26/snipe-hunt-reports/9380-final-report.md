# Post-Drill Report — Snipe Hunt

This drill placed you in a live checkout outage with multiple competing signals, limited team availability, and pressure from business stakeholders. It's designed to stress your ability to reason through systemic complexity — tracing causation across services, managing constrained resources, and synthesising noisy information into a coherent investigation path.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you latched onto the email maintenance timing as a leading hypothesis, asking Tanya directly about its potential impact on checkout. When that was disconfirmed, you moved on — but the pivot came because Tanya told you it wasn't relevant, not because you had reasoned through the mechanism yourself. You also pursued the 10:56 UTC deployment timing without articulating why that deployment would cause the specific symptom you were seeing. Your initial clarifying questions about scope and customer impact were strong — you asked about the error, whether it was total or partial, and requested revenue numbers before jumping in. The growth edge here is building the habit of asking "what mechanism connects this correlation to the symptom?" before investing investigation time in a thread. On the next rep, try naming the causal chain you'd expect if a hypothesis were true, then checking whether the evidence matches that chain.

---

## F2 — Hidden coupling

**Operating at: Not yet evident**

You reached the certificate thread — asking whether there had been recent cert stack updates — but didn't engage with the temporal coupling that made it relevant. When Daniel surfaced that a cert rotation happened seven days ago, the key question was *why would a week-old action cause today's failure?* (reload vs. restart, old cert still in memory, expiry timing). Instead, you treated the cert issue as potentially external and asked Tanya to engage the payment gateway provider. The growth edge is recognising when a piece of evidence has a "why now?" question embedded in it. On the next rep, when someone surfaces a past action, practice asking: what changed between then and now that would make this break today?

---

## F3 — Decreased access to team

**Operating at: Practicing**

You walked the escalation chain appropriately — Hamed was out, Tinus was unavailable, and you pulled Tanya into the incident. You recognised the constraint and named it when escalating. However, once Tanya was engaged, you consumed her bandwidth with repeated low-value status requests rather than batching your asks or giving her space to investigate. Each ping ("Any ETA," "We are waiting for your updates") cost attention without advancing the investigation. The growth edge is treating a constrained resource's time as a budget: batch your questions, make each interaction count, and fill the waiting time with work you can do independently or delegate elsewhere.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You recognised that Tanya was the critical path for platform-side investigation and successfully brought her in. But while waiting for her responses, you didn't structure parallel work — Shay and Daniel were available and could have been investigating other threads (reviewing the cert rotation runbook, checking PaymentService configuration, verifying internal vs. external call patterns). Your delegation, when it happened, was often vague ("please support here," "check on the checkoutservice once") rather than scoped to a specific deliverable. The growth edge is sequencing: when one thread is blocked on a person, name two things others can do in parallel, with specific outputs you expect back.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You made good moves asking for filtered logs and narrowing from the broad error spike to PaymentService specifically. You also asked about TLS errors, which showed you were tracking the right signal. However, you accepted NPC summaries at face value without pushing further into the raw evidence — you never asked about the rotation runbook details, never investigated the reload-vs-restart distinction, and never reasoned about what the absence of internal-call failures might tell you. The growth edge is developing the reflex to ask "what's underneath this summary?" When someone gives you a finding, ask what they looked at and what they didn't — that's where buried information hides.

---

## Looking Forward

Across this drill, your instinct to ask questions and walk escalation paths is solid foundation. The consistent growth edge is moving from *reactive* to *generative*: rather than waiting for NPCs to disconfirm a hypothesis or surface the next clue, practice articulating your own causal reasoning out loud, structuring parallel work while you wait, and pushing one layer deeper into the evidence you receive. On your next rep, try naming your working hypothesis explicitly in the channel and assigning at least one parallel investigation thread before you get stuck waiting.