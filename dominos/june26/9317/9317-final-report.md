# Post-Drill Report — Snipe Hunt

This drill placed you in a live checkout outage requiring you to navigate misleading signals, hidden system dependencies, constrained team availability, and approval bottlenecks — all while managing information flow across technical and business channels. The observations below reflect how you engaged with each of these dimensions.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you pursued Tanya's email maintenance as a potential cause given its timing overlap with the complaints. You pulled her off the vendor call to investigate. When the team's log analysis pointed to PaymentService as the source — with no recent code changes on that service — you moved away from the email thread. The pivot happened, but it was driven by your team narrowing the scope rather than by your own reasoning about whether email maintenance could plausibly break checkout. On the next rep, the growth edge is pausing before chasing a coincident event to ask yourself: *what's the mechanism that would connect this change to this symptom?* That upstream reasoning can save you from pulling constrained resources toward a dead end.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

You engaged meaningfully with the temporal puzzle once Daniel surfaced the certificate rotation. Your question about how a week-old rotation could cause today's failure showed active reasoning about the coupling rather than passive acceptance. Once the expiry-window explanation landed, you drove the thread forward toward verification and fix. The growth edge here is surfacing that "what changed beyond the obvious 24-hour window?" question yourself — before a team member brings it to you. Building a habit of asking about delayed-effect mechanisms (expiry windows, cache TTLs, scheduled rotations) will help you catch these earlier.

---

## F3 — Decreased access to team

**Operating at: Practicing**

When Tanya was on the vendor call, you escalated firmly and repeatedly to pull her back. When Hamed and Tinus were unavailable, you pinged both, received auto-replies, and moved on to self-authorize — an appropriate response. However, you didn't articulate the trade-off of pulling Tanya off her call (the two-week reschedule cost), and you didn't batch or economise your requests to her once she arrived. The growth edge is naming the constraint aloud — "I know this costs us the rollout slot, and I'm making that call because checkout is down globally" — and then being efficient with the constrained person's time by preparing specific, scoped questions before pulling them in.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the approval chain in clear sequence: Hamed first, then Tinus, then self-authorization when both were unavailable. You stated the override explicitly rather than letting it happen implicitly. You also delegated parallel work appropriately — Daniel on the maintenance banner, Shay on logs, Tanya on platform checks. The growth edge is sequencing your investigation and your approval path in parallel rather than serially. If you'd started the approval chain while the cert fix was still being prepared, you could have compressed the timeline. Naming the dependency structure aloud ("we need approval before restart, and both approvers may be unavailable") helps you spot these opportunities.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You delegated log investigation broadly rather than filtering to the relevant service, and when you couldn't access logs yourself, you relied on NPC summaries without further interrogation. The certificate rotation, the bundle-order issue, and the reload-vs-restart distinction were all surfaced by team members rather than by your own filtering. You did engage with the openssl verify command once it was raised. The growth edge is driving the filter yourself: when a team member reports log findings, ask "what service, what time window, what error pattern?" to narrow before accepting the summary. Building the habit of specifying what you're looking for — rather than asking broadly — will help you spot buried signals faster.

---

## Looking Ahead

Across this drill, your strongest moments came when you engaged actively with information your team surfaced — questioning the timing of the cert rotation, walking the approval chain to completion, and adapting when early leads didn't pan out. The consistent growth edge is moving upstream: forming your own mechanism questions before chasing leads, naming trade-offs before pulling constrained resources, and driving the information filter rather than receiving it. On your next rep, try articulating one "what would have to be true for this to be the cause?" question before assigning someone to investigate — that single habit touches several of the patterns this drill is designed to surface.