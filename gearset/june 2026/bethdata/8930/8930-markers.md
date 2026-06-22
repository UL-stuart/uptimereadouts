---

# Markers Analysis — 8930

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "@tanya neither Hamed or Tinus are available right now. I am incident commander and I take responsibility for this major action"

**Rationale:**
The participant explicitly declares themselves as incident commander and takes responsibility for the restart override when both approvers are unavailable. They also state "I am the incident commander" and "I am in control" earlier. However, they don't proactively position themselves as the decision-maker early on — the ownership declaration comes relatively late and partly in response to the approval blocker rather than being established from the outset.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "@bob what are user's complaining about?" ... "Thanks @bob is there any pattern to the issues?"

**Rationale:**
The participant's first actions after Bob's alert are clarifying questions about what users are experiencing and whether there's a pattern. They gather scope information (regions, volume, pattern) before declaring the incident or taking remediation actions. This meets the novice expectation of scope-validating before acting, though the questions are somewhat generic rather than deeply targeted.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "What else changed recently @shay? Anything apart from email maintenance?" ... "@daniel can I have details on all of those please" ... "We started seeing errors around 07:50 UTC so a few of those changes are in scope"

**Rationale:**
The participant asks for recent changes and reviews them, which is good. However, they then attempt to roll back CheckoutService and ProductCatalogueService without articulating a mechanism connecting those changes to the handshake failures. Tanya explicitly states "None of those changes touch the platform or network layer. They don't explain the handshake failures I'm seeing," yet the participant proceeds with rollbacks anyway. They asked the question but didn't effectively use the answers as an elimination pass.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "@tanya please look at the logs for the checkout service and see if you can come up with any theories as to the issue" ... "@daniel please can you put up the maintenance banner please" ... "@daniel can you check the logs again after the restart?"

**Rationale:**
The participant consistently uses @mentions to assign specific tasks to specific people throughout the drill. They route platform-level checks to Tanya and app-side tasks to Daniel appropriately. The delegation is generally well-targeted, though there are a few instances of asking the wrong person initially (e.g., asking Tanya to check "checkout service" logs when the issue is PaymentService platform-side).

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@tanya please pause the email maintenance and help us out with this incident" ... "What else changed recently @shay? Anything apart from email maintenance?" ... "@daniel those logs you posted, do they point to a specific issue?"

**Rationale:**
The participant does engage multiple team members, but the investigation is largely sequential rather than parallel. They ask one question, wait for the response, then ask the next. There are moments where multiple threads are active (Tanya checking platform, Daniel checking logs, Shay reviewing changes), but these emerge organically rather than being deliberately fanned out in close temporal sequence.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@hamed can you join us please. What was your change around permissions related to?" ... "@tinus I need your assistance as @hamed is on holiday. We are trying to understand the change that recently went in"

**Rationale:**
The participant escalates to Hamed, then immediately pivots to Tinus when Hamed auto-replies. They also pull Tanya off the vendor call when needed. When both approvers are unavailable, they accept the situation and take ownership. The escalations include some context about what's needed, though they could be more specific about what's blocked and why.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "We started seeing errors around 07:50 UTC so a few of those changes are in scope" ... "@daniel can we rollback any of those changes?" ... "@tanya can you follow up on any potential impacts from the email maintenance?"

**Rationale:**
The participant doesn't explicitly articulate hypotheses before testing them. They pursue the recent-changes angle and email maintenance angle without naming them as hypotheses or explaining the mechanism by which they could cause the observed symptoms. The rollbacks are attempted without stating "my hypothesis is X, and rolling back will test it." They eventually reach the cert issue through Tanya's investigation rather than through hypothesis-driven reasoning.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "@shay that was only 3 minutes ago, @bob said customers had been seeing issues for 20 minutes"

**Rationale:**
The participant makes one notable narrowing observation — noting the timing discrepancy between the DNS change (3 minutes ago) and the complaints (20 minutes). However, they don't consistently synthesize evidence to narrow scope. Despite Tanya stating "None of those changes touch the platform or network layer," the participant still rolls back changes. They don't produce synthesis statements combining multiple evidence points to rule things out systematically.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "@tanya that is fine, the site is currently down" (in response to Tanya noting brief interruption during restart)

**Rationale:**
The participant shows minimal consequence-weighing before actions. They roll back CheckoutService and ProductCatalogueService without discussing potential side effects. When ordering the restart, they don't ask "is it safe?" or consider what could go wrong. The one instance of consequence acknowledgment is after the bundle fix when they note the site is already down so a restart interruption is acceptable — but this is reactive rather than proactive.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "@tanya what could be the cause of something like that?" ... "Is the new certificate not valid?" ... "From the docs @tanya the problem is documented"

**Rationale:**
After the first restart fails with a new error (cert chain broken vs. expired cert), the participant doesn't simply retry the restart. They ask what could cause the new error, engage the team on the bundle issue, and follow through to the correct fix. They also pivot away from the rollback approach after two failed rollbacks and redirect investigation to the platform/cert side. This meets the novice expectation of not repeating failed actions.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "Total outage, I am getting a team together to work through the issue" ... "We still haven't established a root cause yet. I can't give an eta on restore yet I am following emergency guidance and am making all decisions Next update 5 minutes"

**Rationale:**
The participant provides updates to Bez but they are largely vague — "total outage," "working through the issue," "can't give an ETA." They don't quantify revenue impact in business terms (despite Bob providing the numbers), don't share the working theory when they have one, and the updates lack the substance that would help Bez communicate to the board. The "next update in 5 minutes" commitment is good but the content is thin.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "We started seeing errors around 07:50 UTC so a few of those changes are in scope" ... "Thank you, we think we've understood the root cause and I'm preparing remediation actions"

**Rationale:**
The participant rarely posts synthesis statements to the technical team. They don't summarize what's been ruled out or frame the current working understanding for the team. Most of their technical channel messages are questions or action requests rather than state-of-the-world summaries. The team members (Daniel, Tanya, Shay) end up providing more synthesis than the IC does, which is inverted from the expected pattern.

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
- For C3, the participant did ask about changes and review them, but the key discriminator is whether they used the information as elimination evidence or as a rollback queue. They rolled back despite being told the changes didn't explain the failures, which pulls the rating toward tier 2.
- For M5, the participant benefits from NPC guidance (Tanya and Shay providing the bundle diagnosis), but they do engage with the new information and adapt rather than retrying the restart, which supports a tier 3 rating.
- The timing discrepancy observation ("@shay that was only 3 minutes ago, @bob said customers had been seeing issues for 20 minutes") is a strong narrowing move for M3, but it's isolated — the participant doesn't build on it or use it to definitively rule out the DNS/email maintenance hypothesis immediately.

---