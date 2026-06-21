---

# Markers Analysis — 9305

## L3 — Takes explicit ownership of the response

**Rating:** 2

**Evidence:**
> "i give my direct authorisation to restart the payments"

**Rationale:**
The participant only took explicit ownership when repeatedly prompted by Daniel that they were the incident lead and needed to personally authorise the restart. Throughout the drill, the participant was reactive rather than directive — asking others "who is running it?" and attempting to delegate the approval to Bez and Daniel before finally accepting the role. Ownership was late and only under strong NPC nudging.

---

## C1 — Asks clarifying questions before acting

**Rating:** 3

**Evidence:**
> "whats the complaints ?" / "how many ?"

**Rationale:**
The participant's first actions after Bob's opening report were scope-validating questions about the nature and volume of complaints. They also later asked "How many customers are blocked from checkout right now? What's the revenue loss per minute? Is this a total outage or are some transactions still going through?" These are targeted clarifying questions before taking action, meeting the novice expectation.

---

## C3 — Checks for recent changes

**Rating:** 2

**Evidence:**
> "@shay please check CHG90437:Frontend:UAT deployment" / "@tanya what about your change CHG90441" / "@daniel CHG90439 can we check this"

**Rationale:**
The participant did check individual changes from the change log, asking team members to verify specific entries. However, they treated the change log as a sequential checklist rather than using it as a candidate-elimination pass. They never synthesized the absence of a mechanism connecting changes to the symptom, and after each was ruled out, simply moved to the next without articulating why changes were unlikely to be the cause.

---

## C4 — Delegates tasks to specific people

**Rating:** 2

**Evidence:**
> "@daniel can you check on this" / "@tanya can we look at this" / "@shay can you and tanya work on this"

**Rationale:**
The participant did use @mentions to direct tasks to specific people, but the asks were frequently vague ("can you check on this," "can we look at this") without specifying what to check or what scope to investigate. The delegation lacked precision about what each person should do, and the participant sometimes tagged people without clear actionable instructions.

---

## C6 — Runs parallel investigation threads

**Rating:** 1

**Evidence:**
> "we have no leads to the problem" (said after sequentially checking individual changes one at a time)

**Rationale:**
The participant worked almost entirely sequentially throughout the drill — asking one question, waiting for a response, then asking the next. There is no evidence of multiple investigation threads running simultaneously. Tasks were assigned one at a time, and the participant waited for each to complete before moving on.

---

## C7 — Escalates when stuck

**Rating:** 2

**Evidence:**
> "@tanya we need your input" / "please pause" / "can bez sign it off?" / "@daniel can you sign this off"

**Rationale:**
The participant did eventually pull Tanya off the vendor call and attempted to find restart approval, but the escalation quality was poor. When told Bez doesn't approve restarts and Daniel can't either, the participant asked "who is running it?" rather than taking ownership. The escalation lacked context and concrete asks — it was reactive rather than decisive, and required multiple NPC prompts before the participant authorised the restart themselves.

---

## M2 — Forms and tests working hypotheses

**Rating:** 2

**Evidence:**
> "mail maintenance started right as checkout began failing" / "do we know for sure its not the the DNS change" / "so this isnt the cause either then?"

**Rationale:**
The participant latched onto the email maintenance correlation as a hypothesis but never explicitly articulated it as a testable hypothesis with a proposed mechanism. They asked others to confirm or deny rather than proposing specific tests. After the email maintenance was ruled out, they didn't form a new explicit hypothesis — instead asking the team broadly for ideas ("we have no leads to the problem"). The hypothesis work was implicit and reactive rather than structured.

---

## M3 — Uses evidence to narrow the scope

**Rating:** 2

**Evidence:**
> "we have no leads to the problem" (said after multiple pieces of evidence had already been provided)

**Rationale:**
The participant received substantial narrowing evidence — DNS scoped to email only, UAT-only deployment, PaymentService as the only failing service, outbound handshake failures — but rarely synthesized this evidence into scope-narrowing statements. They acknowledged individual findings but didn't combine them into a tighter picture. The statement "we have no leads" came after Daniel and Shay had already pointed to PaymentService as the anomaly, suggesting the participant wasn't actively using evidence to narrow scope.

---

## M4 — Considers potential consequences before acting

**Rating:** 1

**Evidence:**
> "please restart" / "can you please restart the payments" / "i give my direct authorisation to restart the payments"

**Rationale:**
The participant never considered potential consequences before taking actions. The restart was authorised without any discussion of what could go wrong, whether the cert on disk was valid, or what the fallback would be if the restart didn't work. Similarly, pausing Tanya's maintenance was done without weighing the 2-week cost — Bez made that call. No "is it safe?" qualifiers appear anywhere in the transcript.

---

## M5 — Adapts approach when initial path isn't working

**Rating:** 1

**Evidence:**
> "I keep coming back to the email maintenance" (repeated multiple times) / "do we know for sure its not the the DNS change" (asked after it was already ruled out)

**Rationale:**
The participant repeatedly returned to the email maintenance hypothesis even after Tanya explicitly stated it was unrelated and DNS was scoped to email only. After the restart failed with payments still down, the drill ended before the participant could adapt. Throughout the drill, the participant showed difficulty pivoting away from disproven leads and did not reframe the problem when initial paths were exhausted.

---

## K2 — Provides substantive updates to business stakeholders

**Rating:** 1

**Evidence:**
> "bez is looking updates atm" / "we are on this now" / "still looking" / "give me 5 minutes"

**Rationale:**
The participant never provided Bez with a substantive update containing impact quantification, working theory, or committed next-update time. All communications to Bez were vague reassurances ("we are on this now," "still looking," "give me 5 minutes"). When Bez repeatedly asked for specifics, the participant deflected or provided no actionable information. No business-framed update was ever delivered.

---

## K4 — Communicates issue scope clearly to the technical team

**Rating:** 1

**Evidence:**
> "we have no leads to the problem" / "checking the payment servers now for an issue" / "can we look at this"

**Rationale:**
The participant never posted synthesis statements to the technical channel summarizing what was known, what was ruled out, or what the current working theory was. Communication to the team consisted of vague requests ("can you check on this") and status acknowledgments without framing. The team received no clear picture of the investigation state from the participant at any point during the drill.

---

## Score Summary

| Marker | Rating |
|--------|--------|
| L3 — Takes explicit ownership | 2 |
| C1 — Asks clarifying questions before acting | 3 |
| C3 — Checks for recent changes | 2 |
| C4 — Delegates tasks to specific people | 2 |
| C6 — Runs parallel investigation threads | 1 |
| C7 — Escalates when stuck | 2 |
| M2 — Forms and tests working hypotheses | 2 |
| M3 — Uses evidence to narrow the scope | 2 |
| M4 — Considers potential consequences before acting | 1 |
| M5 — Adapts approach when initial path isn't working | 1 |
| K2 — Provides substantive updates to business stakeholders | 1 |
| K4 — Communicates issue scope clearly to the technical team | 1 |
| **Mean Marker Score** | **1.67** |

---

## Caveats
- The drill ended shortly after the restart failed, so the participant had no opportunity to demonstrate adaptation to the secondary failure (M5 tier 3+). However, the rating of 1 is based on the repeated failure to pivot away from the email maintenance hypothesis earlier in the drill, which is sufficient evidence.
- For L3, the participant did eventually authorise the restart, but only after being told multiple times by Daniel that they were the incident lead. This is a borderline 1/2 call; rated 2 because the authorisation was eventually given, albeit under heavy prompting.
- K2 is rated 1 rather than 2 because even when Bez explicitly asked for specifics, the participant provided no substantive content — not even a partial or late update with real information.

---