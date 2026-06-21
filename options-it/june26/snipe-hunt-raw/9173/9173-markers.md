---

# Markers Analysis — 9173

## L3 — Takes explicit ownership of the response

**Rating:** 3

**Evidence:**
> "As they are both out I will own the risk. Please restart the process"

**Rationale:**
The participant explicitly takes ownership of the restart decision when both approvers are unavailable, stating they will "own the risk." However, this came only after multiple back-and-forth exchanges where they asked others if they could sign off and seemed to need prompting from NPCs about who would need to take responsibility. The ownership statement is clear but arrived late in the sequence rather than proactively.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "What are customers complaing about?" ... "How many customers are blocked from checkout right now? What's the revenue loss per minute? Is this a total outage or are some still getting through?"

**Rationale:**
The participant's first response to Bob's complaint is a clarifying question about what customers are experiencing. They follow up with scope-quantifying questions about how many are affected and whether it's total or partial. These questions precede any remediation actions, showing a clear information-gathering-first approach before declaring the incident.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "can I see the recent changes" ... "can you investigate this further whther this could be causing the issues?"

**Rationale:**
The participant asks for the change log, which is good. However, when Shay notes "none of these changes look like they'd break checkout end-to-end like this," the participant doesn't use this as elimination evidence. Instead, they ask "so we think its one of the checkout changes that could have caused this?" — suggesting they didn't process the absence-of-mechanism signal. They asked the question but didn't effectively use the answer for candidate elimination.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "Hi @daniel , @hamed please can you take a look customers are unable to check out" ... "@tanya please can you leave the maintenace and help investigate urgently" ... "@shay can you help Tanya at all"

**Rationale:**
The participant does use @mentions to direct tasks to specific people. However, the initial delegation to Daniel and Hamed is vague ("take a look"), and Hamed is OOO. The ask to Shay to "help Tanya" is imprecise — Shay can't do platform work. The participant routes tasks to named people but often without specific scope or awareness of access boundaries.

---

## C6 — Runs parallel investigation threads

**Rating:** 2

**Evidence:**
> "@shay @daniel @hamed is there anything else we can check in the meanwhile"

**Rationale:**
The participant mostly works sequentially — asking Tanya to check email maintenance, then waiting, then asking Daniel for logs, then waiting for Tanya to check certs. The one attempt at parallelism ("is there anything else we can check in the meanwhile") is a vague broadcast rather than distinct tasks assigned to distinct people. The investigation proceeds largely as a single thread at a time.

---

## C7 — Escalates when stuck

**Rating:** 3

**Evidence:**
> "@tanya yes please pause" ... "@tinus do you think we should pull Tanya"

**Rationale:**
The participant escalates by pulling Tanya off the vendor call when the investigation is blocked at the platform layer. They first try Tinus for approval (who auto-replies), then make the call themselves. The escalation is concrete — they tell Tanya to pause and help investigate. However, they initially asked Tinus whether to pull Tanya rather than making the call directly, showing some hesitation before committing.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "so we think its one of the checkout changes that could have caused this?" ... "So is this a certificate error?"

**Rationale:**
The participant rarely articulates explicit hypotheses. They ask questions that imply hypotheses (checkout changes? email maintenance? certificates?) but don't frame them as testable theories. The closest to hypothesis formation is asking about the certificate error after seeing the evidence, but this is more reactive observation than proactive hypothesis-test pairing. They follow NPC leads rather than forming and testing their own theories.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "So is this a certificate error? 'Certificate on disk (not loaded by process):'"

**Rationale:**
The participant does eventually recognize the certificate issue from the evidence Tanya presents, but they don't actively synthesize evidence to narrow scope. When Daniel reports "PaymentService fails all outbound gateway handshakes. Checkout is healthy, just getting errors," the participant doesn't use this to explicitly narrow the problem. They rely heavily on NPCs to interpret evidence rather than performing their own synthesis and elimination.

---

## M4 — Considers potential consequences before acting

**Rating:** 2

**Evidence:**
> "What do we think the risks are to restart the payment process?"

**Rationale:**
The participant does ask about risks before the restart, which shows some consequence consideration. However, this is a single instance, and they don't consider consequences before other actions (pulling Tanya off the vendor call without weighing the 2-week cost, or considering what might happen if the restart doesn't fix the issue). The risk question about the restart is good but isolated.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 3

**Evidence:**
> "@tanya any other ideas?" ... "@daniel can you check app side" ... "how do we fix the chain?"

**Rationale:**
After the first restart fails, the participant doesn't simply retry the same action. They ask for new ideas and direct Daniel to check the app side, which surfaces the cert chain issue. When Tanya identifies the bundle problem, they move forward with the fix. The pivot isn't deeply analytical (they ask others for ideas rather than reframing themselves), but they do adapt rather than repeating the failed approach.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 2

**Evidence:**
> "We are checking the payment gateway connection from the server side now" ... "No ETA yet, will update ASAP" ... "Correcting the cert chain bundle order now, 2 mins ETA"

**Rationale:**
The participant provides some updates to Bez but they lack business framing. "We are checking the payment gateway connection from the server side" is technical, not business-oriented. They don't quantify impact in business terms (despite having the data — 90% order drop), don't provide a working theory in accessible language, and their updates are reactive to Bez's questions rather than proactive. The ETA commitment is vague ("ASAP") until the very end.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 1

**Evidence:**
> "here are some logs that daniel pulled, failure is at the connection layer" ... "can we restart the process?"

**Rationale:**
The participant rarely synthesizes the current state of understanding for the technical team. They relay information between NPCs ("here are some logs that daniel pulled") but don't post synthesis statements like "we've ruled out deploys and email maintenance, focus is now on PaymentService outbound TLS." The team receives questions and directives but not a coherent picture of what's known and unknown.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 3 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 2 |
| C7 — Escalates when stuck | 3 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 2 |
| M5 — Adapts approach when initial path isn't working | 3 |
| K2 — Provides substantive updates to business stakeholders | 2 |
| K4 — Communicates issue scope clearly to the technical team | 1 |
| **Mean Marker Score** | **2.25** |

---

## Caveats
- L3 rating is a borderline 2/3 call. The participant does eventually make the ownership statement clearly, but it required multiple NPC prompts about who would need to take responsibility. Rated 3 because the statement itself is unambiguous.
- M5 is a borderline 2/3. The participant adapts by asking others for ideas rather than reframing the problem themselves, but they do move forward rather than repeating the failed restart.
- K4 at tier 1 reflects a complete absence of synthesis statements to the technical channel throughout the drill. The participant asks questions and relays information but never posts a "here's where we are" summary.

---