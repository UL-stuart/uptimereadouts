# Snipe Hunt — Post-Drill Developmental Report

This drill puts you in the middle of a live outage where multiple signals compete for attention, familiar fixes don't resolve the problem, and the people who normally approve high-risk actions aren't available. It's designed to stress your ability to reason through misleading data, navigate coordination constraints, and adapt when your initial read doesn't hold up.

---

## F1 — Misleading correlations

**Operating at: Not yet evident**

Early in the drill, you latched onto the email-maintenance timing correlation and held onto it even after a team member explicitly stated that email confirmations were working and that the email system was separate from the payment path. You ordered a DNS revert on that basis despite the disconfirmation. The growth edge here is building a habit of pausing when someone with system knowledge names a mechanism break — treating that as a signal to release the hypothesis rather than push through it. On your next rep, practice naming the correlation aloud ("I notice X happened right before Y") and then asking "what's the mechanism?" before acting on it.

---

## F2 — Hidden coupling

**Operating at: Practicing**

You did eventually engage with the certificate thread — asking whether the SSL cert had expired and following up when the restart didn't resolve the issue. That pivot showed willingness to move into unfamiliar territory. However, the investigation into the cert was surfaced by teammates rather than by your own questioning, and when the restart produced a different error, you didn't reframe the problem as structurally new (e.g., a chain or bundle issue versus a simple expiry). The next-rep growth edge is noticing when a fix changes the error signature and treating that as a new diagnostic moment rather than continuing with the same mental model.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You handled the access constraints well. When your first escalation attempt returned an auto-reply, you moved to the next person, accepted that result, tried a third path, and ultimately took personal accountability for the restart decision. You also pulled a team member off a vendor call to redirect their effort. The growth edge is making those constraints visible to the rest of the team — stating aloud that approvers are unavailable and naming the trade-off you're making ("I'm pulling Tanya off the vendor call because the global outage outweighs the vendor window"). That explicit framing helps the team understand your reasoning and builds shared situational awareness.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain to exhaustion in a clear sequence and then issued the authorisation yourself as a distinct decision. You also delegated parallel work — routing platform checks to one person and service investigation to another. The growth edge is compressing the time between recognising the bottleneck and acting on it. You spent extended back-and-forth trying to find someone else to approve before taking ownership. On the next rep, practice setting yourself a mental timer: if the chain doesn't yield an approver within a short window, name the constraint and act.

---

## F5 — Data overload / buried information

**Operating at: Not yet evident**

The loudest signal in the logs — EmailService errors — captured your attention and became your declared root cause, even as teammates surfaced payment-specific evidence (TLS handshake failures) that pointed elsewhere. You didn't independently filter or interrogate the competing signals, and when a teammate offered both a reload and a restart option, you chose without engaging the distinction between them. The growth edge is building a triage step before declaring cause: when logs show multiple error types, ask "which of these is on the critical path to the symptom?" and use that to rank signals rather than defaulting to the loudest one.

---

## Looking Ahead

Two patterns stand out as high-leverage for your next rep. First, practice releasing a hypothesis when someone with direct system knowledge names a mechanism break — that single habit would have changed the trajectory of this drill significantly. Second, when a fix changes the error rather than resolving it, treat that as a fresh diagnostic moment: name the new error, ask what's different, and resist continuing with the prior frame. Your escalation and coordination instincts are solid foundations to build on.