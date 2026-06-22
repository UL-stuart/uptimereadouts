---

# Facets Analysis — 9084

## F1 — Misleading correlations

**Rating:** 3

**Evidence:**
> "@shay does the code block on sending the checkout emails? if so, does the email service being down mean it would entirely freeze?"

**Rationale:**
The participant initially considered the email maintenance correlation but explicitly tested the causal mechanism by asking whether checkout blocks on email send. After Shay confirmed it doesn't, the participant moved on without ordering a rollback or pause of email maintenance. They did not paste NPC framing back as their own conclusion. The mechanism-checking question before acting aligns with tier 3's "explicitly checks whether a causal mechanism exists before acting." They didn't quite reach tier 4 because they didn't articulate the correlation-vs-causation frame explicitly to the team.

---

## F2 — Hidden coupling

**Rating:** 3

**Evidence:**
> "that footnote in the instructions is worrying" ... "@tanya can you examine it more closely? check the ordering" ... "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
After the first restart failed, the participant stayed calm ("let's be calm about this and resolve the issue") and within a few exchanges directed Tanya to check the certificate more closely, referencing the footnote about bundle ordering. They recognized the new error was structurally different from the original expiry issue and drove investigation toward the bundle rather than attempting more restarts. However, they did not independently surface the "what changed beyond 24 hours" question — the cert rotation thread emerged through NPC-driven investigation (Daniel/Shay surfacing CHG90123). The reframe after restart failure happened within approximately 3-5 exchanges, consistent with tier 3.

---

## F3 — Decreased access to team / remote

**Rating:** 3

**Evidence:**
> "Hamed is on leave and Tinus is at the conference. I'll authorize it in their absence. Bez is aware."

**Rationale:**
The participant named the access constraints explicitly when making the authorization decision. They accepted auto-replies from Hamed and Tinus as terminating (only one ping each). They initially tried to redirect Tanya from email maintenance, and when she couldn't leave, they escalated through Bez to pull her off. The authorization statement names the constraint pattern clearly. However, they didn't fully batch questions to Tanya or articulate the vendor-call cost trade-off in their own words — Bez made that call. This places them solidly at tier 3.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "Hamed is on leave and Tinus is at the conference. I'll authorize it in their absence. Bez is aware." ... "@daniel can you do that?" ... "@tanya check the payments service certificate"

**Rationale:**
The participant walked the escalation chain (pinged Hamed → auto-reply, pinged Tinus → auto-reply/Bez redirect) and then explicitly took ownership of the authorization decision, naming the constraint. They delegated parallel work appropriately (Daniel on banner, Tanya on cert investigation, Bob on customer comms). On the second restart (after bundle fix), they authorized without re-litigating. This matches tier 3 path (b) — walking the escalation chain to exhaustion then explicitly taking ownership. They didn't quite reach tier 4 because the dependency structure wasn't articulated as a single enumerated constraint statement proactively, and the sequencing wasn't notably ahead of the NPCs' prompting.

---

## F5 — Data overload / buried information

**Rating:** 3

**Evidence:**
> "@tanya can you check that the certificate is correct? that footnote in the instructions is worrying" ... "payments service needs a two-cert bundle to authenticate — tanya can you open the bundle file and check what's in there?"

**Rationale:**
The participant filtered effectively — they moved past the noisy EmailService errors to focus on PaymentService, asked for specific payment logs, and caught the significance of the footnote in the rotation documentation about bundle ordering. After the restart failed, they directed investigation toward the bundle structure rather than accepting surface-level "cert is loaded" confirmation. They read the referenced documentation and caught the key distinction. However, they didn't independently reason about absence of signal (e.g., internal calls clean → external boundary) or drive the initial filtering proactively before NPCs surfaced the payment logs. This places them at tier 3.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 3 |
| F2 — Hidden coupling | 3 |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 3 |
| **Mean Facet Score** | **3.00** |

---

## Caveats
- F2 tier 3 vs 4 was a boundary call. The participant reframed after the restart failure within a reasonable window and drove toward the bundle, but they did not independently surface the "what changed beyond 24 hours" question — that came from NPCs (Daniel/Shay). The lack of independent surfacing of the week-old coupling keeps this at tier 3.
- F4 tier 3 vs 4 was close. The participant named constraints when authorizing but didn't proactively enumerate the dependency structure before the approval moment arose. The second restart authorization was clean and fast, which is a tier-4 signal, but overall the pattern fits tier 3 more cleanly.
- F1 could arguably be tier 4 given the early mechanism-testing question, but the participant didn't explicitly name the correlation-as-prime framing to the team, which is the load-bearing tier-4 signal.

---