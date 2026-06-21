# Post-Drill Developmental Report

This drill placed you in the middle of a live checkout outage requiring you to coordinate a distributed team, navigate misleading signals, and make decisions under time pressure with limited access to senior engineers. The complexity here is systemic — multiple services, layered dependencies, and information that doesn't point cleanly in one direction.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you identified the email maintenance window as a potential cause based on timing overlap with the outage. You pursued this lead persistently — asking Tanya to roll back changes — even after she clarified that her work was paused before anything reached production and that the email system is architecturally separate from checkout. You did eventually pivot once payment logs surfaced TLS handshake failures, which showed responsiveness to concrete disconfirmation.

The growth edge here is building the habit of asking *how* a candidate cause could produce the observed symptom before investing investigation time in it. When a correlation surfaces, naming the mechanism ("if email maintenance caused this, the path would be…") helps you test it faster and release it sooner when the mechanism doesn't hold.

---

## F2 — Hidden coupling

**Operating at: Practicing**

The deeper structural issue — that a cert rotation from days earlier interacted with the payment gateway's bundle requirements — was surfaced by your teammates rather than through your own questioning. After the restart failed to resolve the outage, you did request a bundle verification, which shows engagement with the coupling. However, you didn't independently reframe the problem when the restart didn't work — the shift came after NPC guidance about the two-cert bundle requirement.

On the next rep, practice asking "what changed beyond the obvious window?" earlier, and when a fix doesn't hold, treat that as a signal that the problem has a different shape than you assumed. The restart failure was structurally informative — it told you the issue wasn't just an expired cert.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You walked the escalation chain from Hamed to Tinus, which is appropriate. When both were unavailable, you re-pinged them rather than immediately adapting to the constraint. You did eventually accept the situation and take ownership of the restart approval yourself. When working with Tanya — your primary available engineer — you directed her toward tasks without explicitly acknowledging her bandwidth limitations or batching your requests to economise her time.

The growth edge is recognising access constraints as a *design input* rather than an obstacle to push against. When a key person is unavailable, the next move is "what can I do with who I have?" rather than repeated attempts to reach the unavailable person.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You took the restart approval decision after learning both approvers were out of hours, which was the right call. The decision came after Tanya explicitly flagged the approval requirement and asked who would take responsibility. You didn't proactively identify the approval bottleneck or sequence work to avoid it. Earlier in the drill, time was spent on the email hypothesis while cert investigation could have been running in parallel — this represents a missed opportunity to manage dependencies by keeping multiple paths active.

For the next rep, look for moments where you can name the dependency structure aloud: "We need approval, both approvers are out, so I'm taking this." That framing — even briefly — signals to the team that you see the bottleneck and are actively managing it. Your delegation also tended toward vague asks rather than scoped, actionable tasks matched to each person's access and expertise.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

The path from checkout errors to PaymentService to TLS failures to the cert issue was largely navigated by your teammates surfacing filtered logs and drawing conclusions. You followed the evidence trail once it was presented, asking reactive questions like whether the rotation could be the issue. You didn't independently drive filtering or use absence of signal as a narrowing tool.

The growth edge is taking a more active role in directing *what* gets looked at and *why*. Rather than asking the team to "see the logs" broadly, try specifying what you're looking for: "Show me outbound connections from PaymentService — I want to know if it's failing to reach the gateway."

---

## Looking Forward

Across this drill, the consistent pattern is reactive engagement — you followed leads and accepted direction from teammates, and you did eventually arrive at productive actions. The next developmental step is moving from reactive to directive: naming your working theory aloud, specifying what evidence would change your mind, and treating constraints (unavailable people, failed fixes) as information that reshapes your approach rather than obstacles to retry. Carry that into your next rep — the goal isn't to know the answer faster, but to *drive the investigation* rather than follow it.