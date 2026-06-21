---

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