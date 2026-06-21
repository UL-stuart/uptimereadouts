# Post-Drill Developmental Report

This drill placed you in a live incident with compounding complexity: misleading signals, unavailable team members, layered system dependencies, and a volume of information that required active filtering. The facets below capture how you navigated each of those pressures and where your next growth edges sit.

---

## F1 — Misleading correlations

**Operating at: Practicing**

You pursued the email maintenance and recent deploy hypotheses with energy, rolling back multiple changes before shifting your attention elsewhere. The pivot away from those threads came after concrete experiment failures — the rollbacks didn't resolve the issue — rather than from reasoning about whether a plausible mechanism connected those changes to the symptom. Disconfirming information from teammates (explicit statements that email wouldn't affect checkout) was available well before you moved on.

*Growth edge:* When a correlation looks compelling, practise asking "what mechanism would connect this cause to this symptom?" before committing to a remediation action. If you can't articulate the mechanism, treat the correlation as unconfirmed and keep other threads alive.

---

## F2 — Hidden coupling

**Operating at: Practicing**

When the first service restart didn't resolve the problem, your instinct was to restart additional services rather than reframe the failure as structurally different from what you'd assumed. The cert-bundle dependency — the idea that a single restart wouldn't suffice because two certificates were needed — was surfaced by a teammate rather than through your own investigation of why the post-restart behaviour differed from the pre-restart behaviour.

*Growth edge:* After a remediation attempt fails, pause and ask "is the error I'm seeing now the *same* error or a *different* one?" That reframing question is often the fastest route to uncovering hidden coupling between components.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You named the access constraints early — noting that key approvers were offline — and accepted auto-replies as terminating rather than spinning on unavailable people indefinitely. You escalated to an alternative authority for restart approval and eventually made the cost trade-off to pull a teammate off a vendor call. Your delegation throughout the drill was directed at named individuals with specific tasks, which helped keep work moving despite reduced availability.

*Growth edge:* When pulling someone into the response who has competing obligations, batch your questions before interrupting them. Repeated single-question pings to a constrained teammate can erode cooperation and slow the overall response.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Strengthening**

You walked the escalation chain in a visible, logical order — attempting standard approvers, recognising they were unavailable, then escalating to a senior leader for authorisation. You delegated parallel tasks to available teammates and used the approval you obtained to unblock the restart without re-litigating it later. The sequencing was sound.

*Growth edge:* Try naming the dependency structure aloud as a single statement early in the incident ("we need restart approval; Hamed and Tinus are out; I'm going to Bez now"). Making the constraint explicit — rather than discovering it step by step — lets you pre-position decisions alongside investigation work rather than sequencing them reactively.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You were captured by the loudest signal — the email maintenance window — for an extended stretch, and you repeated requests for email-related information even after teammates explicitly confirmed it was unrelated to checkout. Once the cert thread was surfaced by others, you engaged with it effectively, but the filtering work was largely NPC-driven rather than self-initiated.

*Growth edge:* When a teammate gives you a clear "that's unrelated" statement, treat it as a data point that closes a thread rather than one that needs re-verification. Keeping a short written list of ruled-out causes can help you avoid revisiting closed threads under pressure.

---

## Looking Ahead

Two patterns stand out as high-leverage for your next rep. First, building the habit of articulating a mechanism before acting on a correlation — even a single sentence ("I think X caused Y because Z") — will sharpen your filtering and reduce time spent on dead-end rollbacks. Second, when a remediation fails, treating the post-failure state as new diagnostic information (rather than a prompt to repeat the same class of action) will help you surface hidden coupling faster. Your ownership instincts and escalation sequencing are solid foundations to build on.