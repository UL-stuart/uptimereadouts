# Snipe Hunt — Post-Drill Report

This drill placed you in a live incident with layered complexity: misleading surface signals, constrained team availability, hidden system coupling, and an approval chain that required navigation under pressure. The observations below reflect how you engaged with each of these dimensions.

---

## F1 — Misleading correlations

**Operating at: Strengthening**

You engaged critically with the email maintenance correlation rather than treating it as a ready-made explanation. When the timing overlap was raised, you challenged it on mechanism — asking why a failure to send an email would produce a checkout error, and pressing for a causal hypothesis beyond coincidence. You held the correlation as a data point without ordering a rollback or pausing the maintenance based on it alone.

Your growth edge here is moving from *challenging* a misleading correlation to *explicitly naming and parking it* for the team. Stating something like "we're noting the timing overlap but not acting on it until we have a mechanism" would sharpen the signal for others and reduce the chance of the team drifting back to it.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the week-old certificate rotation was surfaced, you connected it to the current failure and moved through the investigation — from reload attempt to recognising the bundle ordering issue needed a fix. When the reload didn't resolve the handshake errors, you pivoted cleanly to rebuilding the certificate in the correct order.

The growth edge is in *surfacing* hidden coupling yourself rather than receiving it from a teammate. The "what changed beyond the last 24 hours?" question came from someone else. On your next rep, consider building that question into your early investigation routine — actively asking about changes outside the obvious window.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You accepted unavailability signals without over-pursuing them — moving past Hamed's auto-reply quickly and preserving Tanya's vendor-call time until it became clear she was the only path to platform-level investigation. When you did pull her in, you sent targeted questions rather than open-ended requests. You also explicitly named the constraint when taking ownership of the restart decision.

For your next rep, consider economising even further on constrained team members. You asked Tanya several questions while she was still on the vendor call before making the pull decision. Batching those into a single, scoped ask — or deciding earlier whether to pull her — would reduce the drag on both her and the investigation timeline.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the approval chain methodically — Hamed, then Tinus, then Bez — and when each path terminated, you moved to the next without stalling. When the chain was exhausted, you explicitly took ownership and authorised the restart yourself, naming the accountability clearly. You also delegated parallel work appropriately, routing platform tasks to Tanya and application-layer tasks to Daniel.

The growth edge is anticipating the dependency structure earlier. Rather than discovering each blocker sequentially, consider mapping the approval and access dependencies at the start of an incident — who can approve what, who has platform access — so you can sequence requests to arrive in parallel rather than in series.

---

## F5 — Data overload / buried information

**Operating at: Strengthening**

You filtered effectively past the loudest signal (EmailService errors) to focus on PaymentService connection failures, asking targeted questions about what the service was connecting to and what the handshake error indicated. You engaged with the certificate chain details and caught the bundle ordering discrepancy by referencing the runbook path.

Your growth edge is in proactively driving the "what's buried?" question rather than following the thread once surfaced. You narrowed well once pointed in the right direction, but the initial pivot toward the cert rotation came from a teammate. On your next rep, consider explicitly asking "what are we not seeing?" or scanning for signals outside the immediate noise earlier in the investigation.

---

## Communication as a growth area

Across the drill, your investigation and decision-making were systematic, but your communication to both business stakeholders and the technical team lagged behind your thinking. Business updates were initially generic rather than quantified, and you didn't consolidate findings into synthesis statements for the technical channel. Your teammates ended up providing their own summaries of the investigation state. On your next rep, consider posting brief "here's where we are" messages — both to business stakeholders (with impact and ETA) and to the technical team (with what's been ruled out and what's being pursued). This keeps everyone aligned without requiring them to reconstruct your reasoning from your questions.

---

## Looking forward

You demonstrated consistent mechanism-based reasoning and a willingness to hold uncertainty rather than act prematurely on convenient explanations. The patterns that will serve you well on the next drill are your targeted questioning and your clean pivots when a path doesn't work. The areas to stretch into are earlier self-initiated surfacing of hidden factors, parallel sequencing of dependencies, and real-time synthesis communication that keeps the team and stakeholders inside your decision loop.