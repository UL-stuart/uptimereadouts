# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate misleading signals, absent team members, hidden system dependencies, and dense operational information — all while coordinating a distributed team under time pressure. The observations below reflect how you engaged with each of these challenges.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you latched onto Tanya's email maintenance change as the leading cause of checkout failures. Even after Tanya explicitly stated that email confirmations were unrelated to the checkout path, you continued pursuing that thread for several more exchanges before pivoting. The pivot eventually came once Daniel's logs surfaced concrete disconfirming evidence (TLS handshake failures pointing to PaymentService), rather than from your own mechanism reasoning about why email maintenance couldn't cause the observed symptoms.

*Growth edge:* When a team member offers a clear disconfirmation, practise pausing to ask yourself "what mechanism would connect this change to the symptom I'm seeing?" If you can't articulate one, move on sooner. The goal is to let mechanism reasoning — not just new evidence from elsewhere — drive your pivots.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once Daniel surfaced the 7-day-old cert rotation (CHG90123), you engaged with the cert thread and asked relevant questions about expiry. When the first restart didn't resolve the issue, you redirected within a few exchanges — asking for fresh logs and requesting a review of the cert documentation rather than proposing another restart. You followed the chain from cert rotation through to the bundle ordering issue with NPC assistance, connecting the layers of the problem as they emerged.

*Growth edge:* You didn't independently surface the "what changed beyond 24 hours" question — Daniel found the older change. On your next rep, try broadening your change-window scan earlier. Asking "what changed in the last week, not just today?" can surface hidden coupling before a teammate happens to find it.

---

## F3 — Decreased access to team / remote

**Operating at: Strengthening**

You handled the absence of Hamed and Tinus by accepting their auto-replies and moving forward. You made an explicit ownership statement when authorising the restart, and you made a clear cost trade-off by pulling Tanya off the vendor call — escalating from "pause" to "postpone altogether" when the situation demanded it. You also routed delegation appropriately given who was available, assigning Daniel to logs and Tanya to platform investigation.

There was some inefficiency: you continued attempting to reach Tinus through Bob and Daniel even after already receiving auto-replies and having already authorised the change yourself. This created noise without adding decision-making value.

*Growth edge:* Once you've taken ownership and made the call, trust your own authority. Continuing to chase an absent approver after you've already acted can signal uncertainty to the team and consume coordination bandwidth.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain in a visible, logical order — attempting Hamed, then Tinus, then explicitly taking ownership when both were unavailable. On the second restart (after the bundle fix), you authorised without re-litigating the approval chain, which showed you'd internalised the decision authority. You also delegated parallel work appropriately, with Daniel on logs and Shay/Daniel on the customer-facing banner.

*Growth edge:* Consider articulating the full dependency structure in a single statement early in the incident — something like "we need platform access, approval authority, and vendor coordination; here's who owns each." Naming the structure aloud helps the team see bottlenecks before they bite, and positions you to act faster when one path closes.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You showed awareness of the cert documentation by asking the team to review it, but you didn't independently catch the key distinctions within it (reload vs. restart, bundle ordering). The log filtering that pointed to PaymentService was driven by Daniel, and the bundle issue was surfaced by Tanya. You accepted NPC summaries without further interrogation, and your engagement with buried details came after teammates had already extracted them.

*Growth edge:* When a teammate surfaces a finding, try asking one layer deeper before accepting it — "what else is in that log section?" or "what does the runbook say about failure modes after a restart?" Practising active interrogation of data sources, rather than waiting for filtered summaries, builds the muscle for catching buried signals yourself.

---

## Looking Forward

You showed clear strengths in taking ownership under pressure and adapting your approach when the first fix didn't work — you didn't simply retry the restart, you redirected investigation. Carry that adaptiveness into your next rep, and pair it with earlier mechanism reasoning when evaluating candidate causes. The combination of decisive authority (which you demonstrated) and independent evidence interrogation (your next growth area) will strengthen your overall incident command.