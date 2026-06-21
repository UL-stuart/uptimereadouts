---

# Markers Analysis — 9171

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "As Hamid and Tinus are out I will approve the restart"

**Rationale:**
The participant eventually takes explicit ownership of the restart decision when both approvers are unavailable, stating they will approve it themselves. However, this comes after first attempting to get Bez to approve ("can you please approve this") and being told it's the incident lead's call. The ownership is real but reactive rather than proactive — they needed the nudge from Bez before stepping up.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "Hi Bob, what is the scope of the impact?" ... "any region in particular?"

**Rationale:**
The participant's first actions are scope-validating questions to Bob about impact and region before taking any remediation action. They ask about scope and region specifics before declaring the incident or ordering changes. This meets the novice expectation of gathering information before acting, though the questions are somewhat basic rather than deeply probing (e.g., they don't ask about error types or specific payment methods).

---

## C3 — Checks for recent changes

**Rating:** 3

**Evidence:**
> "Okay @tanya can you please check your email maintenance change, @shay can you also please check if any other changes were made recently on the software side"

**Rationale:**
The participant asks for recent changes early in the investigation and receives the full change list. Later, after the restart fails, they ask Daniel to confirm "none of these changes would break checkout" and review Tanya's changes. They use the change log as a candidate-elimination pass ("none of the recent changes appear to be the culprit on initial inspection" in the escalation to Tinus). However, they do repeatedly ask Shay and Daniel to re-review changes even after they've been cleared, showing some difficulty fully letting go of the deploys lead.

---

## C4 — Delegates tasks to specific people

**Rating:** 3

**Evidence:**
> "Tanya and Daniel can you please check the payments app from your side. Daniel check the code and Tanya the infra"

**Rationale:**
The participant consistently delegates to named individuals with specific tasks — Tanya for infra/platform checks, Daniel for app-side code review, Shay for change review. The delegation to "Daniel check the code and Tanya the infra" shows awareness of access boundaries. However, there are some instances of asking Tanya when she's explicitly said she's mid-maintenance, and asking Shay to check logs when Daniel is the log-puller.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "Okay @tanya can you please check your email maintenance change, @shay can you also please check if any other changes were made recently on the software side"

**Rationale:**
The participant shows some parallel delegation early on (Tanya on email maintenance, Shay on other changes). However, the investigation is largely sequential after that — they wait for one thread to complete before starting the next. After the restart fails, they ask for the change list again and work through it serially rather than fanning out multiple threads simultaneously. The parallelism is limited and inconsistent.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "Hi @tinus, escalating due to the severity of this incident. Customers globally are facing an error at checkout, none of the recent changes appear to be the culprit on initial inspection"

**Rationale:**
The participant escalates to Tinus with reasonable context (severity, global impact, changes ruled out). However, when Tinus auto-replies, they ask the channel "does anyone have the escalation procedure at hand?" rather than immediately working the chain or taking ownership. The escalation to pull Tanya off the vendor call is also hesitant — they say "this is more important" but Tanya initially refuses, and the participant doesn't forcefully pull her until later. The quality of escalation context is decent but the follow-through when blocked is weak.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "have we checked for expired certs"

**Rationale:**
The participant does not explicitly articulate hypotheses with proposed tests. They ask questions that implicitly contain hypotheses (e.g., "have we checked for expired certs") but never frame them as "my hypothesis is X, let's test by doing Y." The cert question comes after Tanya identifies the TLS handshake failure, so it's more reactive than hypothesis-driven. They also repeatedly circle back to the email maintenance and recent changes without explicitly framing these as hypotheses to test and disconfirm.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "appears to be a total checkout outage" ... "Daniel do you agree that none of these changes would break checkout"

**Rationale:**
The participant does some narrowing — they confirm it's a total outage, and they get Daniel to confirm changes aren't the cause. However, they don't produce synthesis statements that combine multiple pieces of evidence. After the restart fails, they ask for the change list again and ask Daniel to re-review changes that were already cleared, suggesting they aren't effectively using prior evidence to narrow scope. The narrowing to PaymentService happens largely through NPC guidance rather than participant synthesis.

---

## M4 — Considers potential consequences before acting

**Rating:** 3

**Evidence:**
> "whats the impact of the full restart" ... "how long will the graceful reload take" ... "please try that first" ... "with caution"

**Rationale:**
The participant asks about the impact of a full restart and the duration of a graceful reload before choosing the lower-risk option first. They also say "with caution" when approving the restart. This shows consequence-weighing behavior. However, they don't anticipate secondary failure modes (the bundle issue after restart) and don't name the cost of pulling Tanya off the vendor session.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 2

**Evidence:**
> "can you please walk me through the recent change in detail Daniel, focusing on those which took place when the incident started" ... "please review again"

**Rationale:**
After the first restart fails, the participant goes back to reviewing recent changes — asking Daniel to walk through them again and even saying "please review again" after Daniel has already double-checked. This shows difficulty adapting when the initial path isn't working. They don't recognize the new error (chain verification vs. expiry) as structurally different until Tanya explicitly identifies it. They eventually follow the bundle thread but only after NPCs surface it.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "first reported about 20 mins ago, affecting customers globally" ... "appears to be a total checkout outage" ... "no ETA as of yet"

**Rationale:**
The participant provides some information to Bez (global impact, total outage) but the updates lack business framing (no revenue quantification despite Bob providing it), no working theory, and no committed next-update time. When Bez asks for specifics, the participant says "we can work out the revenue details once it is resolved" — deflecting rather than providing what's available. The later update ("We have found an expire cert, however we will need to complete a full restart") is more substantive but comes very late.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 2

**Evidence:**
> "failure is at TLS handshake before data exchange. - can you please check this further @tanya"

**Rationale:**
The participant rarely synthesizes the investigation state for the technical team. They relay information back (quoting Tanya's findings) but don't produce original synthesis statements like "we've ruled out deploys, focus is now on PaymentService outbound." The one instance of scope communication ("failure is at TLS handshake before data exchange") is essentially quoting what Tanya already said. The team is left to piece together the investigation state from the question/answer exchanges rather than receiving clear scope summaries.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 3 |
| C4 — Delegates tasks to specific people | 3 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 3 |
| M5 — Adapts approach when initial path isn't working | 2 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 2 |
| **Mean Marker Score** | **2.42** |

---

## Caveats
- L3 is a borderline 2/3 call. The participant does eventually take ownership of the restart approval, but only after being told by Bez that it's their call. Rated 3 because they do explicitly state "I will approve the restart" rather than continuing to defer.
- M5 is a borderline call — the participant does eventually follow the bundle thread, but only because NPCs surfaced it. The repeated requests to re-review already-cleared changes weigh toward a 2.
- K2 could be argued as a 1 given the deflection of Bez's requests, but the participant does provide some factual information (global, total outage, cert found) so rated 2.

---