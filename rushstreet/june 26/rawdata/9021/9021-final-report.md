# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, coordinate a partially unavailable team, and trace a failure through layered system dependencies. The observations below reflect how you engaged with each of these challenges and where your next growth edges sit.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you latched onto the email/DNS maintenance as your leading hypothesis based on timing alone — the change went live just before transactions dropped. You pursued this thread to the point of pulling a team member off another task to verify it, and only pivoted once you received concrete disconfirmation that DNS was clean. The growth edge here is pausing before committing resources to a correlation and asking yourself: *does this change have a plausible mechanism to cause the symptom I'm seeing?* Email DNS and payment handshakes operate in different domains — reasoning about that connection before acting would have saved time and preserved team capacity for more productive threads.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the certificate thread surfaced, you engaged with it effectively. You recognized the temporal gap — a cert rotated seven days ago, expiring today — and connected it to the failure. When the first restart didn't resolve the issue, you shifted your framing rather than repeating the same action, asking what new errors were appearing and engaging with the bundle-ordering problem when it was identified. The next growth edge is surfacing these "beyond the obvious window" questions yourself rather than waiting for a teammate to raise them. Asking early on, "what changed in the last week, not just the last hour?" would have brought you to this thread faster.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You explicitly named the access constraints — identifying which team members were unavailable and accepting auto-replies as terminating signals rather than re-pinging. When you needed Tanya, you made a deliberate cost trade-off, acknowledging the priority conflict and pulling her off her vendor call. You also took explicit ownership of the restart decision when both approvers were unreachable. This showed solid constraint management. To build further, consider naming the *cost* of your trade-offs out loud when you make them — articulating what you're giving up (e.g., the vendor call window) helps the team understand your reasoning and builds shared situational awareness.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the approval chain methodically — reaching out to Hamed, then Tinus, recognizing both were unavailable, and then explicitly authorizing the restart yourself with clear ownership language. You also distributed work across available team members. The growth edge is anticipating these bottlenecks before they block you. If you'd identified early that restart approval might be needed and checked approver availability proactively, you could have shortened the delay. On your next rep, try mapping the decision dependencies at the start of an incident: who do you need, for what, and what's your fallback if they're unavailable?

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked for filtered information — change logs, specific service logs — which is a good instinct. However, you frequently accepted NPC summaries without further interrogation and chased a UAT-only change before being corrected. The critical cert-expiry data was surfaced by a teammate rather than through your own filtering. On your next rep, work on driving the filter yourself: when you receive a data dump, actively ask "what's missing?" and "what would I expect to see if my hypothesis were wrong?" This moves you from receiving information to interrogating it.

---

## Looking Forward

You showed clear strengths in owning decisions under pressure and managing team constraints — stepping up when the approval chain was exhausted and making explicit trade-offs about team capacity. The consistent growth edge across this drill is moving from reactive to proactive: questioning causal mechanisms before committing to a hypothesis, surfacing broader change windows earlier, and synthesizing the current state of knowledge for your team rather than waiting for teammates to surface findings. On your next rep, try articulating your working theory and its test criteria out loud to the team early — this will sharpen your own reasoning and help others contribute more effectively to narrowing the problem.