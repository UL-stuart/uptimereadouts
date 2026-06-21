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

You showed clear strength in people-coordination under pressure — pulling in the right person, walking escalation chains, and making decisive calls when access was constrained. The next growth area to focus on is the diagnostic reasoning layer: building the habit of articulating mechanisms before acting, treating disconfirmed hypotheses as scope-narrowing evidence, and independently interrogating data rather than relying on team summaries. Carrying that into your next drill will complement the coordination instincts you already demonstrate.# Facets Analysis — 9390

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." ... "@shay - Please expand on the DNS changes, what CR was that change made in?" ... "To be safe, i want to roll back ALL changes pushed to production today to take us back to a last known healthy baseline"

**Rationale:**
The participant initially pursued the email/DNS correlation after Shay raised it, asking Tanya about DNS changes multiple times. After Tanya explicitly denied DNS changes and the email mechanism was disconfirmed, the participant pivoted to rolling back all production changes — another correlation-based approach (recent changes = cause). However, after rollbacks failed to resolve the issue, the participant did pivot to investigating PaymentService logs and the TLS handshake failure. The pivot was reactive (driven by failed experiments rather than mechanism reasoning), placing this squarely at tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "checked payments deployment history, only cert-related change is CHG90123, Tanya, PROD, SSL cert rotation across four services, 7 days ago." ... "@tanya - We need to urgently fix that, can you follow the steps in the document to clear that?"

**Rationale:**
The participant did not independently surface the "what changed beyond 24 hours?" question — Daniel/Shay surfaced the cert rotation history. After the reload failed and the restart also failed (post-restart layer), the participant asked for logs again but did not independently articulate that the new error was structurally different. They relied on Daniel/Tanya to identify the chain verification failure and bundle issue. The participant engaged with the week-ago coupling only after NPCs named it, and after the restart failed, they asked others to check logs rather than reframing the failure themselves. This is tier 2: engagement with the hidden coupling only when NPCs surface it, and partial connection of the reload-vs-restart distinction taken on NPC framing.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "@tanya - The entire platform is hard down, this is more important. Tinus and Hamed are OOO right now, i insist that you step in here, the business is at stake" ... "Then we have no other option, i have to approve this change on their behalf. Please proceed with it right now"

**Rationale:**
The participant named the access constraints explicitly (Hamed OOO, Tinus at summit, Tanya on vendor call). They pulled Tanya off the vendor call with a clear cost trade-off articulation ("the entire platform is hard down, this is more important"). They accepted auto-replies as terminating after attempting escalation. They eventually took ownership of the restart approval after exhausting the chain. However, they did re-ping Hamed multiple times after receiving the auto-reply (at least 2-3 attempts), which is a tier-1/2 signal. On balance, the explicit naming of constraints and the cost trade-off on Tanya's vendor call push this to tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "@bez - I am requesting your approval to restart the services... Hamed and Tinus are OOO and NOT answering calls" ... "Then we have no other option, i have to approve this change on their behalf. Please proceed with it right now"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Hamed (auto-reply), pinged Tinus (auto-reply), escalated to Bez, was told Bez can't approve, then explicitly took ownership. This matches tier 3 path (b) — walking the escalation chain to exhaustion and then issuing the authorisation as a distinct message. They also delegated parallel work to Daniel and Tanya appropriately. However, they did not name the dependency structure proactively before the approval moment arose, and the escalation to Bez (who cannot approve technical restarts) suggests incomplete understanding of the role structure. On the second restart (bundle fix), they authorised without re-litigating, which is a tier-4 signal. Overall, tier 3 is appropriate.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "@daniel - Please review those urgently and let me know what you find" ... "@tanya - See the doc ¹ PaymentService - The external payment gateway performs strict chain validation..."

**Rationale:**
The participant did eventually ask for filtered logs (PaymentService, CheckoutService, ShippingService) but only after significant time spent on rollbacks. They did not independently identify the cert expiry from the logs — NPCs surfaced the TLS handshake failure and the cert rotation history. After the restart failed, the participant asked others to check logs rather than driving the filter themselves. They did reference the documentation about bundle ordering near the end, which shows some engagement with buried information. However, the key distinctions (reload vs. restart, bundle ordering) were surfaced by NPCs, not independently discovered. The participant accepted NPC summaries without deep interrogation for most of the incident. This is tier 2: asks for filtered logs but relies on NPC summaries and reads docs only when directed.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.40** |

---

## Caveats
- F3 was a boundary call between 2 and 3. The participant re-pinged Hamed after auto-replies (tier-1 signal) but also explicitly named constraints and made the Tanya cost trade-off verbally (tier-3/4 signals). Weighted toward tier 3 based on the explicit constraint naming and cost articulation.
- F5 was a boundary call between 2 and 3. The participant did reference the documentation about bundle ordering near the end, but it's unclear whether they independently read and identified the distinction or whether NPC messages guided them to it. Rated conservatively at 2.
- The participant's repeated pinging of Hamed (3+ times after auto-reply) is a notable negative signal across both F3 and F4 but was weighed against stronger positive signals in both facets.

------

# Markers Analysis — 9390

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "Then we have no other option, i have to approve this change on their behalf. Please proceed with it right now"

**Rationale:**
The participant drives the response throughout, directing team members by name, making decisions, and ultimately taking the override approval when both Hamed and Tinus are unavailable. They explicitly state they are approving on behalf of the absent approvers. However, they don't proactively name the cost or blowback risk — they frame it as "no other option" rather than explicitly accepting consequences, which keeps this at tier 3 rather than 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "What are you seeing/hearing @bob ?"

**Rationale:**
The participant's first action after Bob's complaint is to ask what Bob is seeing. They gather information from Bob (regions, volume, pattern) before declaring the incident or taking remediation steps. The incident declaration comes after receiving Bob's detailed responses. This meets the novice expectation of scope-validating before acting, though the questions aren't as targeted or multi-dimensional as a tier-4 response.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "To be safe, i want to roll back ALL changes pushed to production today to take us back to a last known healthy baseline"

**Rationale:**
The participant does engage with recent changes — they review the deployment log and ask about DNS changes. However, rather than using the change log as a candidate-elimination pass, they order a blanket rollback of all production changes without articulating a mechanism connecting any specific change to the symptom. This is despite Shay noting deployment timings don't line up. They asked the question but used the answer as a rollback queue rather than an elimination tool.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@daniel - Please pull the logs from your side, let us know what you see" ... "@tanya - Can you give some context around the maintenance you started?"

**Rationale:**
The participant consistently delegates to specific named individuals throughout the drill — Daniel for logs, Tanya for platform/cert work, Bob for customer validation. They generally route tasks to the appropriate person (Daniel for app-side, Tanya for platform-side). The routing is mostly correct, though there are a few instances of asking Tanya to do things Daniel could handle and vice versa, keeping this at tier 3.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@shay - While we're doing this, can you see any further logs from the application services?"

**Rationale:**
The participant shows one clear instance of parallel investigation — asking Shay to check logs while rollbacks are in progress. However, for most of the drill, the investigation is largely sequential: they pursue one thread at a time (email maintenance → DNS → blanket rollbacks → payment logs → certs). The parallel work is inconsistent and mostly emerges late in the drill.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya - The entire platform is hard down, this is more important. Tinus and Hamed are OOO right now, i insist that you step in here, the business is at stake"

**Rationale:**
The participant escalates effectively in two key moments: pulling Tanya off the vendor call with clear justification ("the business is at stake"), and working through the approval chain (Hamed → Tinus → Bez) when the restart needs sign-off. They accept auto-replies as terminating and move forward. However, they don't explicitly name the cost of pulling Tanya (the 2-week vendor window loss), which would push to tier 4.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "The error messages Shay provided suggest a DNS issue is impacting these services, @tanya do we use a 3rd party external DNS provider, like Akami for example in this service?"

**Rationale:**
The participant forms a DNS hypothesis and tests it by asking Tanya, which is good. However, after the DNS hypothesis is disconfirmed, they don't articulate a new hypothesis — instead they default to blanket rollbacks without a stated theory. The email maintenance timing correlation is noted but never explicitly framed as a testable hypothesis. The hypothesis-test linkage is inconsistent throughout.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "@tanya - What is the expiry date on the certs we're using?"

**Rationale:**
The participant eventually narrows to PaymentService and then to certs, but the path is inefficient. After DNS is ruled out and deployment timings don't match, they still order blanket rollbacks rather than using the negative evidence to narrow scope. They don't produce synthesis statements combining evidence to rule things out. The narrowing that does occur (to PaymentService outbound) is largely driven by Daniel's and Tanya's findings rather than the participant's own synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "Let's start with ALL changes, starting from the bottom (Most recent) one by one, and we will validate each post change"

**Rationale:**
The participant shows some consequence awareness by rolling back changes one at a time and validating after each, rather than all at once. They also pull Tanya off the vendor call with awareness it's a trade-off. However, they don't ask "is it safe?" before the restart, don't anticipate secondary failure modes, and don't verify the bundle on disk before restarting. The blanket rollback approach itself shows limited consequence consideration — no mechanism articulated for why any change might be harmful.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "@daniel @tanya - Please check the logs again, what do you see now post change?"

**Rationale:**
After the blanket rollbacks fail (4 rollbacks, no improvement), the participant does eventually shift approach — moving to log analysis and then the cert investigation. After the first restart fails, they don't simply retry it; they ask for new logs and engage with the new error (cert chain/bundle issue). They adapt to the structurally different failure and trace it to the bundle ordering problem. The adaptation is present but somewhat slow — the rollback phase consumed significant time before pivoting.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "We suspect this is a SSL certificate issue, we are working on resolution. No ETA at the moment"

**Rationale:**
The participant provides several updates to Bez and the business channel, but they are mostly vague — "we continue to investigate," "no ETA," "the restart was unsuccessful." They do eventually provide the revenue figure (relaying Bob's £1,000–£1,500/min) and later give a 2-minute ETA for the cert fix. However, most updates lack business framing, committed next-update times, or working theories. The substantive updates come very late in the drill.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Let's review the logs of the following - checkout service Payment service Shipping service"

**Rationale:**
The participant directs the team to investigate specific services but rarely synthesizes what's been learned or ruled out. They don't post summary statements like "DNS is ruled out, deploys don't match timing, focus on PaymentService outbound." The team receives task assignments but not state-of-the-world updates. The participant asks questions and delegates but doesn't orient the team with synthesis messages at decision points.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.42** |

---

## Caveats
- L3 is a borderline 3/4 call. The participant does take the override decision but frames it as "no other option" rather than proactively accepting risk/blowback. Rated 3.
- M5 is a borderline 2/3 call. The participant does eventually pivot away from rollbacks and adapts after the first restart fails, but the rollback phase was prolonged. Rated 3 because the post-restart adaptation (engaging with the new cert chain error) is clear.
- C3 is a clear tier 2: the participant asked about changes but used the information as a rollback queue rather than an elimination tool, despite NPC evidence that timings didn't match.

---