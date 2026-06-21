---

# Facets Analysis — 9050

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "@tanya these errors on emailservice seem to be related to your change, we need you to focus on this urgently" ... "@tanya those changes you made line up with when the issues started happening, is it worth reverting on?" ... "if DNS changes went live just before this happened?"

**Rationale:**
The participant locked onto the email maintenance correlation early and pursued it aggressively — pulling Tanya from her vendor call specifically to investigate EmailService, even after Tanya and Shay explicitly stated email maintenance wasn't touching checkout or payments. However, the participant did eventually pivot once Daniel's logs showed PaymentService SSL failures, moving away from the email hypothesis without ordering a revert. The pivot was reactive (driven by concrete log evidence from Daniel rather than mechanism reasoning) and came after multiple exchanges past disconfirming signals, placing this at tier 2.

---

## F2 — Hidden coupling

**Rating:** 2

**Evidence:**
> "that change was 7 days ago can we then assume not related?" ... "cert has expired?" ... "we need to dive into the other problems" ... "@daniel what else did you see failing"

**Rationale:**
The participant initially dismissed the 7-day-old cert rotation as unlikely ("can we then assume not related?"), only engaging with it after Tanya surfaced the expired cert evidence. After the first restart failed, the participant pivoted within a few exchanges ("we need to dive into the other problems") but did not articulate that the new error was structurally different from the first. The reload-vs-restart distinction was never surfaced by the participant — Daniel volunteered the restart suggestion. The week-ago coupling was engaged only when NPCs drove it forward. This fits tier 2: pivots after concrete failure, engages with the cert thread only when NPCs name it.

---

## F3 — Decreased access to team

**Rating:** 2

**Evidence:**
> "@tanya we need you to focus on this urgently" ... "@tinus can you step in here please" ... "@tanya tinus is ooo, we need you to confirm on this" ... "@hamed"

**Rationale:**
The participant re-pinged Tanya multiple times during her vendor call with low-value requests (checking EmailService, which wasn't the issue), consuming constrained bandwidth on the wrong problem. They pinged Hamed after already receiving an auto-reply. They did eventually accept the constraints and work with available team members, but did not articulate the access constraint pattern or economise on Tanya's time. The participant pulled Tanya off the vendor call for the wrong reason initially. This fits tier 2 — walks the escalation chain but without visible economising or constraint articulation.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 3

**Evidence:**
> "I feel we need to bypass this approval - both ooo and this is critical" ... "bez approved @daniel @tanya go for it" ... "please proceed with restart" ... "i will take responsibility"

**Rationale:**
The participant recognised the approval bottleneck ("both ooo and this is critical") and sought an alternative path through Bez. On the second restart, when the approval constraint resurfaced, the participant explicitly took ownership ("i will take responsibility") without re-litigating the chain. They delegated parallel work to available NPCs (Daniel on logs, Tanya on platform, Shay on comms). This meets tier 3 path (b): walks the escalation chain, recognises it's exhausted, and takes ownership. However, the dependency structure wasn't named as a single enumerated constraint, and the first restart approval was routed through Bez rather than the participant explicitly owning the override themselves.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "Seeing errors on EmailService most, then CheckoutService, AdService, ProductCatalogueService. EmailService is way noisier than the rest." ... "@tanya these errors on emailservice seem to be related to your change"

**Rationale:**
The participant was initially captured by the loudest signal (EmailService volume) and directed investigation there despite Tanya's explicit statement that email wasn't touching checkout. They did eventually accept Daniel's filtered PaymentService logs as the relevant signal, but didn't drive the filtering themselves. The reload-vs-restart distinction in the runbook was never caught by the participant — Daniel suggested the restart. The bundle ordering issue was surfaced entirely by NPCs (Daniel: "just realised — the payments service actually needs two certificates"). The participant accepted NPC-surfaced information but didn't independently filter or interrogate buried signals.

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
- F4 rating is a boundary call between 2 and 3. The participant's first restart approval was routed through Bez (who isn't in the formal approval chain of Hamed/Tinus), which could be read as not fully understanding the dependency structure. However, the second restart ownership statement ("i will take responsibility") and the overall delegation pattern pushed this to tier 3.
- F1 is a boundary call between 1 and 2. The participant pursued the email lead aggressively past multiple disconfirming signals (Tanya's explicit denial, Shay's confirmation that email errors were expected) but did eventually pivot without ordering a revert. The pivot was driven by Daniel's concrete PaymentService evidence rather than by the earlier mechanism-disconfirmation, which is characteristic of tier 2.

---