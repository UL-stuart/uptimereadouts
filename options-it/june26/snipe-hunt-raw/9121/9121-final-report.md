# Post-Drill Developmental Report

This drill placed you in a live checkout outage requiring you to navigate misleading signals, trace hidden system dependencies, coordinate a distributed team with limited availability, and manage approval bottlenecks — all while sifting through noisy data under time pressure.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you pursued the recent deploys as a leading hypothesis and ordered a rollback of CheckoutService. When that rollback produced no change, you pivoted to investigating downstream services. The pivot itself was appropriate, but it was driven by the concrete failure of the experiment rather than by reasoning about *why* the deploy couldn't plausibly explain the symptom pattern. The email-maintenance coincidence was never explicitly dismissed on mechanism grounds — it faded from focus rather than being ruled out.

*Growth edge:* Before acting on a correlation, practise articulating the causal mechanism in one sentence ("this change could cause that symptom because…"). If you can't complete the sentence, treat the correlation as unconfirmed and keep other threads open.

---

## F2 — Hidden coupling

**Operating at: Strengthening**

Once Daniel surfaced the PaymentService logs, you connected the 7-day-old certificate rotation to the current SSL verification failure and articulated that connection in your own words. After the first restart failed to resolve the issue, there was a period of uncertainty — but you didn't fall into a pattern of repeating the same action. When the cert-bundle insight emerged, you acted on it. The key observation here is that you engaged the coupling thread and drove it forward once evidence appeared, even though you didn't independently surface the "what changed beyond 24 hours" question.

*Growth edge:* Practise widening the change-window earlier. When recent changes don't explain symptoms, explicitly ask "what changed in the last week or two?" as a deliberate investigative step rather than waiting for a teammate to surface it.

---

## F3 — Decreased access to team / remote

**Operating at: Strengthening**

You handled team-availability constraints well. You accepted Hamed's auto-reply as terminating and moved on after a single ping. You respected Tanya's vendor-call constraint for several exchanges, only pulling her off when the evidence pointed to a platform-level issue that required her expertise — and you framed that as a priority call. Your delegation adapted to who was actually available, routing tasks to Daniel and Shay while Tanya was occupied.

*Growth edge:* When you do pull someone off a competing obligation, briefly name the trade-off out loud ("I know this interrupts the vendor call — the checkout outage is higher priority because…"). This makes the decision legible to the team and reinforces that it was deliberate rather than reactive.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You recognised that restart approval was needed and that the standard approvers were unavailable. You escalated to Bez, who offered backing. However, when NPCs made clear that "whoever proceeds without that sign-off takes on personal accountability," you framed the authorisation as coming from Bez rather than explicitly owning the override yourself. On the second restart you again sought Bez's approval rather than authorising independently. The pattern was one of managing the process while deflecting the accountability question.

*Growth edge:* In situations where the standard approval path is blocked, practise making the override statement explicit and personal: "I'm authorising this; the accountability is mine." This is a distinct communication act — it signals to the team that someone has accepted the risk, which unblocks action faster and builds trust in your leadership of the response.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You delegated investigation effectively — asking Daniel and Shay to dig into services — but largely accepted their summaries without further interrogation. The critical PaymentService errors, the reload-vs-restart distinction, and the cert-bundle detail were all surfaced by teammates rather than by you filtering logs or reading documentation independently. You acted on key information once it appeared, but the discovery work was driven by others.

*Growth edge:* When a teammate surfaces a finding, try asking one follow-up question that tests the finding or extends it ("what else is in that log window?" or "does the runbook say anything about prerequisites for this action?"). This builds your own mental model rather than relying on pre-digested summaries.

---

## Looking Ahead

You showed solid instincts around team coordination — routing tasks to the right people, respecting availability constraints, and making priority calls when needed. The areas that will pay off most on your next rep are: reasoning about *mechanism* before acting on correlations, widening your change-investigation window earlier, and stepping into explicit personal ownership when standard approval paths are blocked. These are all learnable habits that compound with practice.