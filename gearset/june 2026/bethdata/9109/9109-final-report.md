# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, trace hidden system dependencies, coordinate a partially-available team, and manage information flow under pressure. The observations below reflect how you engaged with each of these challenges and where your next growth edges sit.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you pursued the email maintenance correlation as a leading explanation for the checkout failures, asking whether email could cause checkout to crash. You did eventually move past this lead, but the pivot came after multiple disconfirmations from team members rather than from your own mechanism-based reasoning. The shift away from the email thread was driven by exhaustion of the lead rather than proactive elimination.

*Growth edge:* When a correlation surfaces, practice asking yourself — before asking the team — "what mechanism would connect these two systems?" If you can't name one, deprioritise the lead earlier and move to the next candidate. This frees up exchanges for more productive threads.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the certificate-rotation thread emerged, you engaged with it constructively. After the initial restart didn't resolve the issue, you didn't repeat the same action — instead, you traced forward, asking whether certificates had been rolled out to other services and then driving toward the bundle investigation. You recognised that the post-restart failure was structurally different and continued pursuing the dependency chain.

*Growth edge:* The "what changed beyond 24 hours" question was surfaced by your team rather than by you. On the next rep, practice widening your change-window scan independently — ask about changes from the past week, not just the past day — so you're the one surfacing hidden coupling rather than following a teammate's lead.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You accepted auto-replies from unavailable team members without re-pinging, preserved Tanya's vendor-call constraint as long as the investigation allowed, and then made a clear cost trade-off when you needed her platform access — articulating that losing the vendor slot was acceptable given the situation. When the approval chain was exhausted, you explicitly owned the override decision. Your delegation also showed awareness of who could do what: you directed architecture questions to Shay, log work to Daniel, and platform checks to Tanya.

*Growth edge:* You could strengthen this further by naming the constraint landscape to the team earlier — a brief "Hamed and Tinus are both off, so I'm going to own approval if we get there" statement up front sets expectations and removes ambiguity before the moment arrives.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain methodically — reaching out to Hamed, then Tinus via Bez, then taking ownership yourself. You delegated parallel responsibilities (Daniel on logs, Tanya on platform, Bob on customer comms) and surfaced blockers to business stakeholders. This kept the response moving even when the approval path was blocked.

*Growth edge:* Consider verbalising the full dependency map in a single statement early in the incident: "We need X from person A, Y from person B, and Z is blocked until we have both." This makes sequencing visible to the whole team and helps you spot when two threads could be prepared simultaneously rather than sequentially — an area where your investigation tended to run one thread at a time rather than fanning out.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You initially chased the loudest signals — the email correlation and broad error logs — and took considerable time to narrow toward the specific service at fault. When you asked about healthz 500 errors, the request lacked clear filtering logic. The PaymentService focus and the reload-vs-restart distinction were both surfaced by team members rather than driven by your own filtering.

*Growth edge:* When facing a wall of log data or multiple error types, practice stating a filter criterion aloud before asking someone to look: "Show me only errors from the last 30 minutes on the payment path" or "What's different between the services that are healthy and the one that isn't?" This turns a broad ask into a scoped investigation and helps you catch buried details before a teammate has to surface them for you.

---

## Looking Ahead

You showed solid instincts around team coordination, ownership, and adapting when an initial fix didn't land. The clearest growth pattern across this run is moving from *reactive* narrowing — where teammates surface the key insight and you follow — to *proactive* narrowing, where you name the filter, the mechanism, or the wider change window yourself. On your next rep, try articulating your working theory explicitly to the team ("I think it's X because of Y — here's how we test that") and posting a brief scope summary mid-incident so everyone shares the same picture of what's been ruled out. These habits will compound quickly.