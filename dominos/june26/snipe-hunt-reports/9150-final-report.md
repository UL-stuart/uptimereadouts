# Post-Drill Developmental Report

Snipe Hunt is designed to stress your ability to navigate systemic complexity under time pressure — sorting misleading signals from root causes, coordinating a constrained team, and making decisions when the usual approval paths aren't available. This report walks through what showed up in your run and where the growth edges are for your next rep.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you flagged the timing overlap between email maintenance and the checkout failures and pulled Tanya in to investigate on that basis. When Tanya explicitly disconfirmed the email theory, you pivoted away from it — which is the right move. The growth edge here is making that pivot *before* an NPC hands it to you: asking yourself "what's the actual mechanism that would connect these two?" before committing investigative resources to a coincidence. On the next rep, try articulating the causal chain out loud before treating a correlation as a lead.

---

## F2 — Hidden coupling

**Operating at: Practicing**

The deeper structural issue — a certificate rotation from days earlier interacting with a service restart — was surfaced by your teammates rather than by your own questioning. After the first restart failed and a new error appeared, you moved to cache-clearing questions rather than reframing the problem as structurally different. The growth edge is recognising when a failure mode *changes shape* after an action: that's a signal to pause and ask "what assumption just broke?" rather than continuing down the same path. Building the habit of asking "what changed beyond the obvious window?" early in an incident will help you catch hidden coupling sooner.

---

## F3 — Decreased access to team

**Operating at: Practicing**

You walked the approval chain — Hamed's auto-reply led you to Tinus, then to Bez — which shows awareness that you needed to find someone with authority. However, pulling Tanya off her vendor call happened without visible acknowledgement of the trade-off, and the questions you sent her weren't batched or scoped to minimise her context-switching. The growth edge is treating constrained availability as a design problem: when someone is expensive to interrupt, front-load your asks into a single, well-structured message so you get maximum value from minimum disruption.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

When both approvers were unavailable, you initially tried to route the sign-off decision to a business stakeholder who couldn't grant it. You did eventually take ownership of the call — and did so again on the second restart — but this happened after explicit prompting rather than from your own recognition that the escalation chain was exhausted. Your delegation throughout tended toward serial, one-at-a-time requests rather than parallel tasking. The growth edge is naming the bottleneck explicitly ("approval chain is exhausted, I'm taking the call") and sequencing work so that multiple threads can progress simultaneously rather than waiting on each answer before asking the next question.

---

## F5 — Data overload / buried information

**Operating at: Not yet evident**

Several moments in the drill showed information being available in-channel but not integrated into your decision-making. A deployment list was interpreted as a failure list, leading to an inaccurate scope statement. The maintenance banner was toggled without a clear read on system state, and a premature claim of resolution was made while checkout was still broken. Investigative filtering — identifying which service was actually failing, reading the rotation runbook for the reload-vs-restart distinction — was largely performed by teammates rather than by you. The growth edge here is foundational: before synthesising for others, pause to confirm what you're actually seeing. Read the data yourself, name what's ruled out, and resist the pull to declare resolution until you've verified it against the original symptom.

---

## Looking Ahead

Two things to carry into your next rep. First, practice *pausing before acting*: when you're about to authorise an action or broadcast a status, take five seconds to ask "what could go wrong?" and "is this accurate based on what I actually know?" Second, work on owning the investigative thread yourself — forming a hypothesis, naming what would confirm or disconfirm it, and using NPC findings as inputs to *your* reasoning rather than as the reasoning itself. These habits will compound quickly across reps.