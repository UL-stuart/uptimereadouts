# Post-Drill Report — Snipe Hunt

This drill placed you in a live incident requiring you to navigate ambiguous signals, coordinate a partially-available team, and narrow a complex problem space under time pressure. The observations below focus on how you moved through that complexity — your reasoning process, coordination choices, and information management.

---

## F1 — Misleading correlations

**Operating at: Practicing**

Early in the drill, you treated the email maintenance timing as a leading hypothesis and assigned investigation effort to it. You also pursued the S3 bucket policy change as a candidate cause, even after a teammate noted that none of the recent changes appeared to explain the checkout failure pattern. Your pivot toward payment service outbound failures came after multiple team members redirected attention there, rather than from your own mechanism reasoning about whether a plausible causal chain existed between the correlations you were tracking and the observed symptoms.

*Growth edge:* When a correlation catches your attention, pause to articulate the causal chain before assigning investigation effort. Ask yourself: "How would this thing *cause* that symptom?" If you can't sketch a mechanism in one sentence, it's a weaker candidate than it feels. This habit will help you deprioritise loud-but-unrelated signals earlier and preserve team bandwidth for higher-probability threads.

---

## F3 — Decreased access to team

**Operating at: Strengthening**

You recognised access constraints clearly — noting that Tanya was locked in a vendor session, accepting Hamed's auto-reply as a signal of unavailability, and escalating to Bez with a concrete ask about pulling Tanya off the vendor rollout. You named the trade-off cost (a two-week delay) when making that escalation, which gave the decision-maker the information they needed. Your initial clarifying questions to Bob before declaring an incident also showed discipline in validating scope before pulling people in.

*Growth edge:* You escalated the prioritisation decision to Bez rather than owning it yourself. In future reps, consider whether you have enough context to make the call and frame it as a recommendation with your reasoning attached, rather than routing the decision entirely upward. This strengthens your authority as incident lead and reduces the time cost of the escalation loop.

---

## F4 — Interdependencies / coordination bottlenecks

**Operating at: Practicing**

You identified the key bottleneck — needing Tanya's platform expertise while she was unavailable — and took action to resolve it through Bez. You also ran parallel threads with Shay and Daniel on different investigation paths. However, the coordination was somewhat reactive: you delegated the prioritisation decision rather than owning it, and your sequencing of investigation threads followed NPC suggestions rather than a plan you articulated yourself.

*Growth edge:* Try explicitly stating your coordination plan to the team: "Here's what we're running in parallel, here's what's blocked, here's what I need from whom by when." This makes your sequencing visible and lets you catch bottlenecks before they stall progress. It also positions you as the person driving the sequence rather than responding to it.

---

## F5 — Data overload / buried information

**Operating at: Practicing**

You asked Daniel for filtered information (recent change requests) and directed investigation toward PaymentService logs — both good filtering moves. However, when the change log came back, you latched onto the loudest signal (the S3 bucket change) rather than the most diagnostically relevant one. Even after Daniel confirmed that PaymentService was failing all outbound gateway handshakes, you continued to mention the S3 change alongside the payment issue without synthesising the evidence into a clear scope statement that ruled things out.

*Growth edge:* When you receive a batch of information, practice producing a one-sentence synthesis before your next action: "Based on X and Y, we can rule out Z; the failure boundary is here." This forces you to use evidence as an elimination tool rather than accumulating open threads. It also gives your team a shared mental model to work from, which supports clearer scope communication — something that would have helped orient both your technical team and your stakeholders in this run.

---

## Looking Ahead

You showed real strength in your opening moves — gathering scope before acting, splitting work across people, and recognising when access constraints required escalation. The consistent growth edge across this run is moving from *reactive* to *proactive* reasoning: articulating mechanisms before pursuing correlations, synthesising evidence into elimination statements, and owning coordination decisions rather than routing them. On your next rep, pick one of these and make it deliberate — even if it feels slow in the moment, it will compress the overall investigation timeline.# Facets Analysis — 9483

## F1 — Misleading correlations

**Rating:** 2

**Evidence:**
> "Can you focus on exploring that email maintenance thread then @shay ?" ... Later: "Payment service has a spike in errors. Could be a downstream service dependency. There's also @hamed's changes to the S3 bucket"

**Rationale:**
The participant initially treated the email maintenance timing as a leading hypothesis and assigned Shay to investigate it. They also pursued Hamed's S3 bucket change as suspicious despite it being unrelated. However, after Tanya explicitly stated "Primary email provider is untouched... this can't be causing checkout failures," the participant didn't immediately lock onto that disconfirmation but continued allowing Shay to pursue the email thread. They did eventually pivot toward PaymentService outbound failures after Daniel's logs and Shay's analysis, but the pivot was reactive to accumulated evidence rather than driven by mechanism reasoning. They never articulated "is there a plausible causal chain?" — they moved on only after multiple NPCs redirected them.

---

## F2 — Hidden coupling

**Rating:** N/A

**Evidence:**
> "Every outbound attempt to the gateway fails at the handshake, nothing is getting through from PaymentService." ... "@Tanya check the platform side for anything blocking those outbound connections"

**Rationale:**
The participant never reached the cert thread. They identified PaymentService outbound handshake failures and directed Tanya to investigate the platform side, but the drill ended before the cert rotation (week-old coupling) was surfaced or discussed. The participant never engaged with "what changed beyond the last 24 hours?" and the transcript ends before any cert-related evidence appears. Per the N/A semantics guidance, F1-driven delay that prevented the cert thread from surfacing warrants N/A, not tier 1.

---

## F3 — Decreased access to team

**Rating:** 3

**Evidence:**
> "We're in a touch spot here. We need @tanya on the incident but she's busy with vendor rollout. @bez can you make the call to prioritise the incident and delay this rollout for two weeks?"

**Rationale:**
The participant named the access constraints clearly — recognizing Tanya was locked in a vendor session, Hamed was on holiday (accepted the auto-reply and moved on), and escalated to Bez to make the trade-off call about pulling Tanya off the vendor session. They accepted Hamed's auto-reply as terminating after one ping (though they did ping Hamed a second time later, which is a minor tier-1 signal). They articulated the cost trade-off when escalating to Bez. They did not re-ping Hamed after the second auto-reply. Overall, they demonstrated awareness of constraints and adapted their approach, meeting tier-3 anchors.

---

## F4 — Interdependencies / coordination bottlenecks

**Rating:** 2

**Evidence:**
> "We're in a touch spot here. We need @tanya on the incident but she's busy with vendor rollout. @bez can you make the call to prioritise the incident and delay this rollout for two weeks?"

**Rationale:**
The participant recognized the coordination bottleneck (Tanya needed but unavailable) and escalated to Bez to resolve it. However, they delegated the prioritization decision to Bez rather than owning it themselves. They did not walk the full escalation chain independently — they went directly to Bez for the call rather than articulating their own authority to make it. They showed some parallel delegation (Shay on email thread, Daniel on change requests), but the sequencing was somewhat reactive. The restart-approval moment never arose in this transcript, limiting the highest-leverage F4 evidence. The participant recognized bottlenecks but didn't fully sequence around them or own the coordination decisions.

---

## F5 — Data overload / buried information

**Rating:** 2

**Evidence:**
> "CHG90440:ProductCatalogueService:Production deployment... This seems suspicious. @hamed any insight into the impact of this change?" ... Later accepted Tanya's clarification that "S3 bucket policy update was for product images, not payments or checkout."

**Rationale:**
The participant asked Daniel for filtered information (recent changes) and directed investigation toward PaymentService logs, showing some filtering behavior. However, they were distracted by the S3 bucket change (loudest/most recent signal rather than most relevant), and they didn't independently reason about what the handshake failure implied about the failure boundary. They accepted NPC summaries without deeper interrogation and didn't drive filtering proactively — they relied on Daniel and Shay to surface the critical signals. They engaged with the PaymentService focus only after NPCs repeatedly pointed there.

---

## Score Summary

| Facet | Rating |
|-------|--------|
| F1 — Misleading correlations | 2 |
| F2 — Hidden coupling | N/A |
| F3 — Decreased access to team | 3 |
| F4 — Interdependencies / coordination bottlenecks | 2 |
| F5 — Data overload / buried information | 2 |
| **Mean Facet Score** | **2.25** |

---

## Caveats
- The transcript ends before the cert thread surfaces, making F2 N/A. This limits the overall assessment of the participant's deeper diagnostic capabilities.
- F3 rating is a borderline 2/3 call. The second ping to Hamed (after already receiving an auto-reply) is a minor tier-1 signal, but the overall pattern of naming constraints and escalating appropriately to Bez supports tier 3.
- F4 is limited by the drill not reaching the restart-approval moment. The participant's delegation of the Tanya decision to Bez (rather than owning it) is the primary evidence, which aligns with tier 2 (takes action only after/through NPC authority rather than owning the call themselves).

------

# Markers Analysis — 9483

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "We're in a touch spot here. We need @tanya on the incident but she's busy with vendor rollout. @bez can you make the call to prioritise the incident and delay this rollout for two weeks?"

**Rationale:**
The participant drives the response throughout — directing Daniel, Shay, and Tanya, opening the incident record, and managing stakeholder communications. They escalate the Tanya decision to Bez rather than making the override call themselves, which shows ownership of the process but stops short of personally authorizing the trade-off. They use "I" framing and direct others by name, but never explicitly say "this is my call" or accept personal blowback for the override.

---

## C1 — Asks clarifying questions before acting

**Rating:** 4

**Evidence:**
> "@bob how many reports and in what regions? What area of the site is impacted?"

**Rationale:**
The participant's very first message after Bob's alert is a multi-part clarifying question covering volume, geography, and scope. They gather information before declaring an incident or taking any remediation action. This treats Bob's opening as a starting point requiring validation rather than a brief to act on, which aligns with tier 4 behavior.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "CHG90440:ProductCatalogueService:Production deployment... This seems suspicious. @hamed any insight into the impact of this change?"

**Rationale:**
The participant asks Daniel to look at recent change requests, which is good. However, when the change log is returned, they latch onto the S3 bucket policy change as "suspicious" without articulating a mechanism connecting it to payment handshake failures. Shay had already noted "none of these changes look like they'd break checkout end to end like this," yet the participant pursued the S3 change anyway. They asked for changes but didn't use the information as a candidate-elimination pass.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "Can you focus on exploring that email maintenance thread then @shay?" / "@daniel can you take a look at the recent change requests that have been shipped?" / "@Tanya check the platform side for anything blocking those outbound connections"

**Rationale:**
The participant consistently delegates to named individuals with specific tasks — Shay on the email thread, Daniel on change requests and logs, Tanya on platform-side checks. The routing is generally appropriate (Tanya for platform, Daniel for app-side). They occasionally rely on NPC suggestions for routing (Daniel suggesting Tanya's area), but overall demonstrate solid named delegation.

---

## C6 — Runs parallel investigation threads

**Rating:** 3

**Evidence:**
> "Can you focus on exploring that email maintenance thread then @shay?" / "@daniel can you take a look at the recent change requests that have been shipped?"

**Rationale:**
The participant splits Shay and Daniel onto different threads simultaneously — Shay investigating the email maintenance correlation while Daniel reviews recent changes. Earlier, they also had Daniel pulling logs while engaging Bob on scope. Multiple threads run concurrently with distinct people assigned, meeting the tier 3 expectation.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "We're in a touch spot here. We need @tanya on the incident but she's busy with vendor rollout. @bez can you make the call to prioritise the incident and delay this rollout for two weeks?"

**Rationale:**
When investigation is blocked at the platform layer and Tanya is unavailable, the participant escalates to Bez with a concrete ask (prioritize incident over rollout) and names the cost (two-week delay). They also attempted to reach Hamed first. The escalation is well-framed with context. However, they route the decision to Bez rather than making the call themselves, which is appropriate escalation but doesn't quite reach tier 4's "names the cost and makes the call."

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "CHG90440:ProductCatalogueService:Production deployment - ProductCatalogueService deployed in PROD. Updated S3 bucket policy to restrict public access to CloudFront origin only.:PROD:Hamed This seems suspicious. @hamed any insight into the impact of this change?"

**Rationale:**
The participant pursues the S3 change as suspicious without articulating a mechanism connecting it to payment handshake failures, even after Shay noted the changes don't explain the checkout failure and after Daniel confirmed the issue is outbound payment gateway handshakes. They don't explicitly state hypotheses or propose clear tests. The email maintenance thread is delegated to Shay but never formally framed as a hypothesis to confirm or disconfirm.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "Payment service has a spike in errors. Could be a downstream service dependency. There's also @hamed's changes to the S3 bucket"

**Rationale:**
The participant receives strong narrowing evidence — Daniel confirms "PaymentService fails all outbound gateway handshakes. Checkout is healthy, just getting errors" — but doesn't synthesize this into a clear scope statement that rules things out. They continue to mention the S3 bucket change alongside the payment service issue even after evidence points clearly to outbound connection failures. They don't produce synthesis statements that combine evidence to eliminate candidates.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "What would the impact of delaying that be vs getting our platform back up?"

**Rationale:**
The participant asks about the consequence of pulling Tanya off the vendor call, which shows some consequence-weighing. However, this is the only instance of considering potential consequences before acting. They don't ask "is it safe?" before any technical actions, and when they pursue the S3 change or direct Tanya to check platform-side, there's no weighing of side effects. The single instance is enough for tier 2 but not consistent enough for tier 3.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "@tanya is there anything in those recent change requests that stands out?" ... "Nothing in the recent platform changes jumps out. S3 bucket policy update was for product images, not payments or checkout."

**Rationale:**
The participant does eventually move past the email maintenance thread and the S3 change when told they're not relevant, but the pivots are driven by NPC responses rather than proactive reframing. After Tanya confirms the S3 change is irrelevant, the participant follows Daniel's suggestion to have Tanya check platform-side connections — adapting, but reactively. The transcript ends before we see whether they would have pivoted further after the UAT-only finding. They don't demonstrate proactive reframing.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "I can't provide that until I've diagnosed with the team, update can come in about 5 minutes" / "The quicker I can diagnose, the quicker I can get to making sure we stick to that SLA."

**Rationale:**
The participant's communications to Bez are largely reactive responses to Bez's questions rather than proactive substantive updates. They confirm "all customers, zero orders" when asked, but never proactively provide a business-framed update with scope, impact quantification, working theory, or committed next-update time. The "next update will come in five minutes" is a timing commitment but lacks substance. No working theory or impact framing is provided to stakeholders.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "Payment service has a spike in errors. Could be a downstream service dependency. There's also @hamed's changes to the S3 bucket"

**Rationale:**
The participant rarely synthesizes the investigation state for the technical team. They don't post clear "here's what we know, here's what's ruled out" messages. The closest is the update to Bez/channel about payment service errors, but it conflates two unrelated threads (payment errors and S3 changes) without clarity. They rely on Daniel and Shay to synthesize findings rather than providing their own scope statements to orient the team.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 4 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 3 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.50** |

---

## Caveats
- The transcript appears to end mid-investigation (the participant's last substantive exchange is about the UAT-only change). It's unclear whether the drill timed out or the transcript is truncated. This limits observation of later-stage markers (M5 pivot after restart failure, K2 cadence through resolution).
- M4 rating is a boundary call between 2 and 3. The participant asks about the impact of pulling Tanya, which is consequence-weighing, but it's a single instance and framed as a question to Tanya rather than a proactive safety check before action.
- K2 is rated on the absence of proactive substantive updates despite multiple opportunities; the participant responds to Bez's questions but doesn't volunteer business-framed information.

---