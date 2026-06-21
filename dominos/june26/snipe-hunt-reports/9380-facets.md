# Facets Analysis — 9380

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "I keep coming back to the email maintenance — DNS changes went live just before this all kicked off. zero successful transactions since then. that's not nothing." ... Participant asks "@tanya As shay mentioned will there be any impacts because of the email maintains?" ... Later pivots to PaymentService after Shay says "PaymentService is throwing errors consistently, but there hasn't been any change on it for ages."

**Rationale:**
The participant initially pursued the email maintenance correlation by asking Tanya about it, echoing Shay's framing. However, after Tanya explicitly disconfirmed the email lead ("Primary email provider hasn't been touched... this can't be causing checkout failures"), the participant did not persist on that thread and moved toward investigating deployments and downstream services. The pivot was reactive — driven by Tanya's disconfirmation and Shay's PaymentService observation rather than by the participant's own mechanism reasoning. The participant also briefly pursued the deployment correlation ("AT what timestamp checkout failures started? immediately after 10:56 deployment") but moved on. This is tier-2 behaviour: treating coincident factors as leading hypotheses and pivoting reactively to disconfirmation rather than from upstream mechanism reasoning.

---

## F2 — Hidden coupling

**Rating:** 1

**Evidence:**
> "Was there any recent update on cert stack?" ... Daniel responds: "There was a cert rotation 7 days ago, but Tanya followed the playbook." ... Participant asks "@tanya Any updates on the Cert stack?" and "@tanya Please engage the Payment gateway provider to check the certificates"

**Rationale:**
The participant reached the cert thread but only superficially. When Daniel surfaced the 7-day-old cert rotation, the participant did not engage with the temporal coupling (reload vs. restart, old cert in memory, expiry timing). Instead, they asked Tanya for updates and then suggested engaging the external gateway provider — treating the issue as potentially external rather than tracing the hidden coupling between last week's rotation and today's failure. There is no evidence of the participant connecting "rotated 7 days ago" + "reload not restart" + "expired today" or engaging with the week-old coupling mechanism at all. They treated each piece of evidence as independent rather than building a causal chain. This is tier-1 behaviour: the cert thread surfaced but the participant did not engage with the hidden coupling.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@hamed Can you check is there any abnormal activity from infra side?" [receives auto-reply] ... "@tinus Hamed is off and @tanya is in email maintaince We need support from Platform team" [receives auto-reply] ... "@tanya please support here its P1 issue" ... Multiple pings to Tanya: "We are waiting for your updates" / "Any ETA" / "Got any insites?"

**Rationale:**
The participant did walk the escalation chain (Hamed → Tinus → Tanya) and accepted auto-replies as terminating for Hamed and Tinus. However, they repeatedly pinged Tanya with low-value status requests ("Any ETA," "We are waiting for your updates," "Got any insites?") without batching or economising on her bandwidth. They did not articulate the access constraint pattern in their own words beyond noting "Hamed is off and Tanya is in email maintenance." The participant pulled Tanya off the vendor call appropriately for a P1, but without explicitly naming the cost trade-off. This is tier-2 behaviour: walking the chain without articulating the constraint, and consuming Tanya's bandwidth on repeated low-value queries.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "@tanya please support here its P1 issue" ... "Its might take next couple of minutes @bez. Platform team is looking into it and I'm following up" ... Participant does not delegate parallel work or sequence investigation threads; repeatedly asks Tanya for updates without structuring the work.

**Rationale:**
The participant recognised that Tanya was needed for platform-side investigation and successfully pulled her into the incident. However, they did not sequence work in parallel — while waiting for Tanya, they did not assign Shay or Daniel to investigate other threads (e.g., reviewing the cert rotation runbook, checking PaymentService config). The participant did not name the coordination bottleneck explicitly or own any override decision. They treated the incident as a serial dependency on Tanya's investigation without structuring around it. The restart-approval moment never arose because the participant never identified the specific fix path, but the broader sequencing/parallelism signals show tier-2 behaviour: recognising some bottlenecks but not sequencing around them.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> Participant asks "can we see logs metrics before and after 10:56 UTC?" ... Shay surfaces PaymentService logs showing TLS handshake failures ... Participant asks "Was there any recent update on cert stack?" but does not follow through on the reload-vs-restart distinction or investigate the cert rotation runbook.

**Rationale:**
The participant did ask for filtered logs and narrowed from the broad error spike to PaymentService specifically. They engaged with the cert stack concept once Daniel surfaced the 7-day rotation. However, they did not drive further into the buried information — they never asked about the rotation runbook, never investigated reload vs. restart, and never reasoned about absence of signal (e.g., internal calls clean but external failing). They accepted NPC summaries without further interrogation and did not catch key distinctions in referenced documentation. This is tier-2 behaviour: asking for filtered information but not following through into the raw evidence or catching buried distinctions.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 1 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **1.80** |

---

## Caveats
- The drill timed out before the participant reached the restart-approval moment, limiting F4 evidence to broader sequencing/parallelism signals. The highest-leverage F4 evidence (ownership of override) never fired.
- F2 rating of 1 is a boundary call: the participant did reach the cert thread and asked about it, but never engaged with the temporal coupling mechanism (reload vs. restart, week-old action causing today's failure). Per the rubric, the cert thread surfaced and the participant did not engage with the hidden coupling — this is tier 1, not N/A.
- The participant's repeated low-value pings to Tanya ("Any ETA," "We are waiting for your updates") could be read as either F3 (access constraint) or F4 (coordination bottleneck) evidence; I weighted it in both facets as it manifests differently in each.

---