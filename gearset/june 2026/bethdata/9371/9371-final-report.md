# Post-Drill Report — Snipe Hunt

This drill puts you in the middle of a live checkout outage with distributed team members, ambiguous signals, and access constraints. It's designed to stress your ability to reason through misleading correlations, trace hidden system dependencies, and coordinate effectively when key people aren't available.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you latched onto the email maintenance as a likely cause of the checkout failures and returned to it multiple times — even after a teammate explicitly ruled it out by confirming email confirmations were unaffected. You did eventually pivot once payment service logs surfaced TLS errors, but that pivot was driven by new concrete evidence rather than by reasoning through *why* email maintenance couldn't mechanistically cause checkout failures. The growth edge here is building the habit of asking "what's the mechanism?" before investing further in a coincidence. When a teammate disconfirms a lead, treat that as a signal to move on immediately rather than circling back.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once the restart failed to resolve the issue, you didn't repeat the same action or blame downstream services. You engaged with the new error information — the broken certificate chain — and connected it to the bundle structure relatively quickly. You traced forward from the cert rotation to the bundle ordering problem within a few exchanges. The next growth edge is surfacing the "what changed beyond the obvious window" question yourself, rather than waiting for teammates to raise it. Asking early about changes outside the 24-hour window would have accelerated your path to the root cause.

---

## F3 — Decreased access to team / remote

**Operating at: Strengthening**

You handled the access constraints well. When both approvers were unavailable, you named the constraint clearly and took ownership of the restart decision rather than stalling. You also made a deliberate cost trade-off when pulling a teammate off a vendor call. One area to sharpen: while your teammate was on that vendor call, you sent her low-value queries about a hypothesis she'd already ruled out. In future reps, consider what each person is doing before routing questions their way — especially when they're occupied with something you've asked them to do.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain in a visible, logical order — pinging one approver, then the next, then explicitly taking ownership when neither was available. You delegated parallel work to available teammates, routing log investigation and service checks to different people. You also surfaced the business-communication need to the right person. For the second restart after the bundle fix, you authorized without re-litigating the approval chain, which shows good situational awareness. The growth edge is naming the dependency structure aloud for the team — saying something like "we need sign-off, Hamed's out, Tinus is next, and if neither responds I'm calling it" — so the team can anticipate the path rather than watching it unfold step by step.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You did eventually direct investigation toward the payment service specifically, but this came after broad initial requests and after teammates had already surfaced the relevant signals. When technical output came back — like certificate verification results — you asked what it meant rather than interpreting it yourself. You also didn't independently catch the reload-vs-restart distinction from the runbook. The growth edge is driving the filter more actively: when you get a wall of information, name what you're looking for before asking someone to dig, and when technical output arrives, spend a moment interpreting it before asking for translation. This builds your ability to spot buried signals without relying on teammates to surface them for you.

---

## Looking Forward

Across this drill, your coordination instincts — taking ownership, delegating to specific people, escalating with context — served you well and gave the response structure. The areas to carry into your next rep are on the diagnostic side: building the reflex to reason through mechanism before pursuing a correlation, driving your own filtering of information rather than following teammate guidance, and naming your working theory explicitly so you can test it rather than following evidence reactively. These are learnable habits that compound quickly with practice.