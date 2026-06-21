# Facets Analysis — 9171

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Okay @tanya can you please check your email maintenance change, @shay can you also please check if any other changes were made recently on the software side"

**Rationale:**
The participant initially pursued the email maintenance and recent deploys as leading hypotheses, directing Tanya to check her maintenance change and asking Daniel to review changes. When Daniel and Tanya both confirmed their changes were unrelated, the participant eventually pivoted to investigating PaymentService logs and the TLS handshake failure. However, the pivot was reactive — driven by NPC disconfirmation rather than upstream mechanism reasoning. The participant asked "have we checked for expired certs" only after Tanya explicitly identified the SSL certificate verification failure, and later returned to the email/deploy hypothesis again ("can you please also review Tanyas change again"). The pivot latency was extended (many exchanges after initial disconfirmation), placing this in tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "still a cert error?" ... "can you get on the second cert issue please"

**Rationale:**
After the first restart failed, the participant did not independently reframe the problem as structurally different. They asked "still a cert error?" which shows confusion rather than recognition of a new failure mode. Tanya had to surface the bundle issue ("two certificates needed — it's a bundle, not just a single cert") before the participant engaged with it. The participant never independently surfaced the "what changed beyond the last 24 hours" question — the cert rotation was surfaced by NPCs. The reload-vs-restart distinction was offered by Tanya ("so we have two options") rather than read from the runbook by the participant. The pivot after the first restart failing took several exchanges and was NPC-driven, consistent with tier 2.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "As Hamid and Tinus are out, can you please approve this" [to Bez] ... "As Hamid and Tinus are out I will approve the restart"

**Rationale:**
The participant attempted to escalate to Tinus (received auto-reply), then Hamed (received auto-reply), then asked Bez to approve (who declined), and finally took ownership themselves. This shows walking the escalation chain but without articulating the access constraints proactively. The participant also told Tanya "This is more important than maintenance" and pulled her off the vendor call, but without explicitly naming the cost trade-off. The participant did not batch questions to Tanya or economise on her constrained bandwidth — repeatedly saying "now please" and "@tanya this is your priority." The ownership was eventually taken but reasoning was brief ("As Hamid and Tinus are out I will approve the restart") rather than articulating the constraint pattern fully.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "As Hamid and Tinus are out I will approve the restart"

**Rationale:**
The participant walked the escalation chain in observable order: pinged Tinus (auto-reply), pinged Hamed (auto-reply), asked Bez (declined), then explicitly took ownership and issued the authorisation. This matches tier-3 path (b) — walking the escalation chain to exhaustion and then explicitly taking ownership. The participant also delegated parallel work appropriately (Daniel on code review, Tanya on infra, Shay on logs). On the second restart (after bundle fix), the participant authorised without re-litigating ("restart now"), showing learning. However, the participant did not name the dependency structure aloud as a single enumerated constraint statement before the chain was exhausted, which would have been tier-4 behaviour.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "have we checked for expired certs" ... "please review again"

**Rationale:**
The participant asked "have we checked for expired certs" only after Tanya had already identified the TLS handshake failure, showing some targeted thinking but only after NPC filtering. The participant did not independently filter logs to PaymentService — Shay identified it as the anomalous service. The participant asked Daniel to re-review the CheckoutService timeout change twice ("please review again") even after Daniel confirmed it was clean, showing difficulty integrating already-surfaced information. The participant did not catch the reload-vs-restart distinction from the runbook — Tanya offered both options. After the restart failed, the participant did not independently reason about the bundle issue; Tanya surfaced it. The participant accepted NPC summaries without further interrogation and relied heavily on NPCs to filter and surface buried information.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | 2 |
| F3 — Decreased access to team | 2 |
| F4 — Interdependencies / coordination bottlenecks | 3 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.20** |

---

## Caveats
- F1: The participant did eventually move past the email/deploy hypothesis, but returned to it late in the drill ("can you please also review Tanyas change again" after the restart failed), which reinforces the tier-2 rating rather than tier-3.
- F4: The tier-3 rating is based on path (b) — chain-walk to exhaustion followed by explicit ownership. The second restart authorisation without re-litigation is a positive signal but doesn't elevate to tier 4 given the absence of proactive dependency-structure naming.
- F5: The "have we checked for expired certs" question is a borderline signal — it could indicate proactive thinking, but it came after Tanya had already identified the SSL handshake failure, making it more reactive than proactive.

---