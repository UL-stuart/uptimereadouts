# Facets Analysis — 9390

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

---