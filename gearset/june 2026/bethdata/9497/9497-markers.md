---

# Markers Analysis — 9497

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "Ok Bez has given me permission to approve if I am confident. Are we confident that restarting the payments service is ok to do at this point. There are currently no checkouts working anyway" ... "Ok I am good to own the call. Lets restart"

**Rationale:**
The participant explicitly states they are "good to own the call" for the restart decision, demonstrating ownership of the high-stakes override moment. They also direct the investigation throughout (delegating to Daniel, Shay, Tanya) and provide stakeholder updates proactively. However, they sought Bez's permission first and polled the team for confidence before committing, rather than independently declaring ownership and accepting blowback. This is solid tier 3 but lacks the proactive "blowback's on me" framing of tier 4.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob can you tell me the scope of the problem?" ... "How many customers are blocked from checking out? What's the revenue loss per minute right now?" ... "@bob do you have any more firm numbers on users involved"

**Rationale:**
The participant's first action after Bob's alert is a scope-validating question. They follow up with questions about customer count and revenue impact before taking remediation actions. They don't jump to rollbacks or declarations without first understanding the scope. This meets the tier 3 expectation of scope-validating questions before acting.

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "Can you both look more into those PaymentService errors? Have there been any changes to PaymentService recently?" ... "Ok @shay lets park the DNS theory for now until there is more evidence"

**Rationale:**
The participant asks about recent changes to PaymentService and receives the answer that only the cert rotation 7 days ago was the last change. They use this information constructively — the absence of recent code changes points them toward the cert rotation as the relevant event. They also park the DNS/email-maintenance theory when evidence doesn't support it. This is a solid tier 3: they asked for changes and used the answer to narrow scope, though they didn't explicitly frame it as an elimination pass the way a tier 4 would.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@daniel @shay can you take a look" ... "@tanya can you please investigate whether your email maintenance could be related to this?" ... "Can you both look more into those PaymentService errors?" ... "Please check the certs that were rotated a week ago"

**Rationale:**
The participant consistently names specific people for specific tasks — Tanya for platform/cert checks, Daniel and Shay for app-side investigation, Bob for customer numbers. They route cert-checking to Tanya correctly (the only one with platform access). The delegation is generally appropriate, though some early asks are paired ("Can you both") rather than giving distinct tasks to distinct people, which slightly reduces specificity. Solid tier 3.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@daniel @shay can you take a look" ... "@tanya can you please investigate whether your email maintenance could be related to this?" ... "@bob do you have any more firm numbers on users involved"

**Rationale:**
The participant does delegate to multiple people early on, but the investigation largely proceeds sequentially — they pursue the email/DNS theory, then park it, then move to PaymentService logs, then to certs. There's some parallelism in asking Bob for numbers while Daniel/Shay investigate, but the main investigation threads are mostly serial rather than deliberately fanned out. This is tier 2: some concurrent activity but not a deliberate parallel-thread strategy.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "The incident takes precedent. Please pause the vendor session" ... "@bez we need to restart the payments service and need approval from either Hamed or Tinus. Can you get one of them to join us to approve?"

**Rationale:**
The participant escalates Tanya off the vendor call when investigation is blocked at the platform layer, making a clear priority call. When the restart approval is blocked (both Hamed and Tinus unavailable), they escalate to Bez with a concrete ask. They don't leave the chain hanging. However, they don't explicitly name the cost of pulling Tanya off the vendor session until asked — Tanya volunteers the cost and the participant then weighs it. This meets tier 3 expectations.

---

## M2 — Forms and tests working hypotheses

**Rating:** 3

**Evidence:**
> "Its interesting that this was rotated 7 days ago though? Is there any kind of change that happens a week after rotation?" ... "@daniel are certs used for handshakes?" ... "Can you both check to see if the cert rotation was successful? If not we would be pointing at the old one and it would expire?"

**Rationale:**
The participant forms an explicit hypothesis about cert expiry — reasoning that if the old cert was due to expire today, that could explain the failure. They propose a test (check if the rotation was successful and which cert is in use). They also pivot away from the DNS/email theory when evidence doesn't support it. This is a clear tier 3: hypothesis articulated and tested, with pivot on disconfirmation. They don't quite reach tier 4 because they don't explicitly ask "does X plausibly cause Y?" as a mechanism question to dispose of the email prime — they rely on others' evidence rather than proactively testing mechanism.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 3

**Evidence:**
> "Ok @shay lets park the DNS theory for now until there is more evidence" ... "Its interesting that this was rotated 7 days ago though? Is there any kind of change that happens a week after rotation?"

**Rationale:**
The participant uses evidence to narrow scope: they park the DNS theory when no DNS errors appear in logs, they note that PaymentService outbound connections are failing (not checkout itself), and they use the absence of recent code changes to focus on the cert rotation. They synthesize Daniel's log findings to move toward the cert hypothesis. This meets tier 3 — using concrete evidence to rule things out — though they don't explicitly name what's been ruled out in a comprehensive synthesis statement.

---

## M4 — Considers potential consequences before acting

**Rating:** 3

**Evidence:**
> "What is the impact of losing that rollout window?" ... "Is there a downside to restarting? If not, lets do that now" ... "Ok I am good to own the call. Lets restart"

**Rationale:**
The participant explicitly asks about the impact of pulling Tanya off the vendor session before making the call. They also ask "Is there a downside to restarting?" before ordering the restart. These are clear consequence-weighing moments. However, they don't anticipate secondary failure modes (e.g., checking the bundle before restarting) — they proceed with the restart without verifying the on-disk cert would work correctly. Solid tier 3 but not tier 4.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "Ok @shay lets park the DNS theory for now until there is more evidence" ... "Can you both look more into those PaymentService errors? Have there been any changes to PaymentService recently?"

**Rationale:**
The participant cleanly pivots away from the email/DNS theory when evidence doesn't support it, redirecting investigation to PaymentService errors and then to certs. They don't double down on the false prime. When the cert bundle order issue is discovered (a secondary complication), they adapt by addressing it before restarting. This meets tier 3. They don't face the "first restart fails with a new error" scenario in this transcript (the bundle was fixed before restart), so the second pivot moment doesn't fully apply.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 3

**Evidence:**
> "No customers are able to checkout in all regions. Full loss of sales. I have everyone available on it and will update again in 5 minutes" ... "This is a total outage on checkout. No transactions. We have a theory and are looking into testing it. Will update again in 5 minutes" ... "We believe we have identified the issue and are implementing a fix. Will update in 5 minutes."

**Rationale:**
The participant provides multiple substantive updates to the business channel: they quantify impact (full outage, all regions, no transactions), commit to next-update times (5 minutes), and progress through theory → fix stages. They don't provide the specific working theory in business terms until the fix update, and the updates are somewhat formulaic. This meets tier 3 — impact named in business terms with committed update cadence — but doesn't quite reach tier 4's "board-ready framing with working theory at each stage."

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Can you both look more into those PaymentService errors? Have there been any changes to PaymentService recently?" ... "Lets fix that up and get us using the right cert"

**Rationale:**
The participant directs the technical team with questions and action requests but rarely posts explicit synthesis statements summarizing what's been ruled in/out. They don't say something like "OK, it's not DNS, not email maintenance, not recent deploys — focus is now on PaymentService outbound certs." The team orientation happens implicitly through the questions asked rather than through explicit state-of-the-world summaries. This is tier 2: engaged but lacking the synthesis messages that keep the team oriented.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 3 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 3 |
| M3 — Uses evidence to narrow the scope | 3 |
| M4 — Considers potential consequences before acting | 3 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 3 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.83** |

---

## Caveats
- **M5 second pivot moment:** The participant fixed the bundle order before restarting, so the "first restart fails with a new error" scenario didn't occur. The participant's adaptation is evaluated only on the first pivot (DNS/email → certs), which is clean but doesn't test the full range of the marker.
- **L3 boundary call:** The participant sought Bez's permission and polled the team before committing to the restart. This is borderline 3/4 — they ultimately owned the call but the process was more consultative than independently decisive. Rated 3.
- **K4 boundary call:** The participant's technical communication is mostly through questions and directives rather than synthesis statements. This could be argued as implicit scope communication, but the rubric specifically looks for synthesis messages. Rated 2.

---