# Post-Drill Report — Snipe Hunt

This drill placed you in a complex production incident involving multiple interacting systems, absent key personnel, and a stream of information that could easily pull investigation in unproductive directions. The challenge is designed to stress your ability to reason through misleading signals, surface hidden dependencies, and coordinate a team under pressure — all while managing access constraints and information overload.

---

## F1 — Misleading correlations

**Operating at: Practicing**

You noticed the email maintenance and DNS timing correlation early and pursued it by asking Tanya about DNS changes. When that line was disconfirmed, you shifted to rolling back all production changes — still a correlation-driven approach (recent change = likely cause) rather than one grounded in mechanism reasoning. The pivot away from rollbacks came only after they failed to resolve the issue, rather than from reasoning about *why* a particular change could produce the observed symptoms.

*Growth edge:* When a correlation is disconfirmed, practise articulating what mechanism would need to be true for the next candidate to be the cause. This slows down the impulse to act on timing alone and builds the habit of asking "how would this change produce *this specific* failure?" before committing to a remediation path.

---

## F2 — Hidden coupling

**Operating at: Practicing**

The week-old certificate rotation — the actual hidden coupling driving the incident — was surfaced by team members rather than through your own investigation. After the service restart failed, you asked others to check logs but didn't independently reframe the failure as structurally different from the original problem. You engaged with the coupling once it was named, but the discovery work was carried by NPCs.

*Growth edge:* When a remediation doesn't resolve the issue, treat the *new* failure state as a fresh diagnostic moment. Ask: "Is this the same failure or a different one?" Expanding your change-history window beyond the last 24 hours — especially for background operations like cert rotations — can surface couplings that don't appear in the obvious timeline.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You named the access constraints explicitly — Hamed out of office, Tinus at a summit, Tanya on a vendor call — and made a clear cost trade-off when pulling Tanya off her call, articulating that the platform being hard-down outweighed the vendor engagement. You accepted auto-replies as terminating signals and ultimately took ownership of the approval decision. One area to watch: you re-pinged Hamed multiple times after receiving the auto-reply, which consumed time without yielding new information.

*Growth edge:* Once you've confirmed someone is unreachable, treat that as a closed door on the first attempt. The instinct to retry is natural, but in a time-critical incident, each re-ping is a decision point where you could instead be moving to the next option in the escalation chain.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain in a visible, deliberate order — Hamed, then Tinus, then Bez — and when you reached the end of that chain, you issued the authorisation yourself as a distinct, explicit decision. You delegated parallel work to Daniel and Tanya appropriately, routing platform tasks to Tanya and application-side investigation to Daniel. On the second restart (for the bundle fix), you authorised without re-litigating the approval question, which showed you'd internalised the decision structure.

*Growth edge:* Consider naming the dependency structure *before* you hit the bottleneck. Early in an incident, a brief statement like "restart approval requires Hamed or Tinus — both are OOO, so I may need to override" signals to the team what's coming and reduces friction when the moment arrives. You demonstrated strong delegation throughout; pairing that with proactive dependency mapping would round out this skill.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You eventually asked for filtered logs across specific services (PaymentService, CheckoutService, ShippingService), which is a good instinct. However, this came after significant time spent on blanket rollbacks, and the key diagnostic distinctions — the TLS handshake failure, the reload-vs-restart difference, the bundle ordering requirement — were surfaced by team members rather than through your own interrogation of the available data. You did reference the documentation about bundle ordering near the end, showing engagement with buried information when pointed toward it.

*Growth edge:* When you receive log output or documentation, practise scanning for the *unexpected* detail — the thing that doesn't fit your current theory. Building a habit of asking "what in this output contradicts what I believe?" can help you surface buried signals before a teammate needs to flag them for you.

---

## Looking Ahead

You showed clear strength in people-coordination under pressure — pulling in the right person, walking escalation chains, and making decisive calls when access was constrained. The next growth area to focus on is the diagnostic reasoning layer: building the habit of articulating mechanisms before acting, treating disconfirmed hypotheses as scope-narrowing evidence, and independently interrogating data rather than relying on team summaries. Carrying that into your next drill will complement the coordination instincts you already demonstrate.