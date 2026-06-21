
### 5. Three Areas of Focus for the Cohort

---

#### Area 1: The invisible mental model — diagnose out loud or the team can't help

Every player in this cohort builds a working hypothesis privately and acts on it without broadcasting it. The technical team observes their IC issuing task requests without knowing what frame those requests are serving, which means findings cannot be efficiently connected to a shared picture and faulty assumptions go unchallenged. This is not a sensemaking absence — these players are thinking — it is a narration absence, and it is the single most consistently cited gap across all seventeen sessions in the dataset.

**Where the gap shows up:**

> "PLAYER did not construct an explicit working theory or share a mental model with the team — they relayed symptoms and relayed others' findings rather than synthesising them into a narrated picture." — *Andrew, Too Good To Be True*

> "As the incident evolved through three distinct cause hypotheses (payment change → shipping pod crashes → chaos tests in prod), PLAYER absorbed each update from the team but rarely narrated the changing mental model aloud, missing opportunities to shape the team's shared understanding and invite challenge." — *JamieM, Big Investor V2*

> "PLAYER never explicitly articulated a revised mental model to the team ('wait, this is now looking like a DoS, not just overload'). Symptom-to-cause progression was present but largely driven by others; PLAYER's own sensemaking remained at a surface level." — *LewRad, Discount Disaster*

> "PLAYER did not explicitly reframe the incident when the ransomware nature was confirmed… Maya made that announcement and PLAYER absorbed it passively." — *Patric, DEFCON-1*

**What stronger behaviour looks like:**

> "Can we have an inventory of the orders today, and see when this started to change?" / "89415 - what is the impact of rolling that back?" / "And Daniel, Change 89412 - could that have gone from UAT into prod?" — *JamieM, Unknown Unknown* (evaluator note: "PLAYER formed a clear initial frame and iteratively narrowed it through change review, timeline anchoring, and targeted questions about UAT-to-prod propagation… hypothesis-driven questioning that correctly identified the root cause before Daniel confirmed it")

**Recommendation:** At the start of the next drill, each player should commit to broadcasting a working hypothesis to the team at least once in the first ten minutes and at every frame revision thereafter. The format is one sentence: "My current read is [X] because [Y] — we are testing [Z] next." It does not need to be right; it needs to be visible so the team can contribute to or correct it.

---

#### Area 2: Decisions that appear from nowhere — name the trade-off before pulling the trigger

Across the cohort, decisions are correct more often than not, but they arrive without the reasoning attached. The team cannot anticipate what comes next, cannot challenge a call that is about to go wrong, and cannot contribute contingency thinking, because they do not know what trade-offs are being weighed. The most costly single illustration of this pattern is Patric's kill-script decision in DEFCON-1, where a technically irreversible action was executed before Maya — who had relevant information — had the chance to flag the risk. The ransom doubled as a direct result.

**Where the gap shows up:**

> "Can we kill the script please" (T+12) — decisive, though critically this was made without first consulting Maya or weighing the risk of escalation (ransom doubling followed). — *Patric, DEFCON-1*

> "calibrated confidence was absent: PLAYER never verbalised the trade-off between rapid rollback and potential data/state loss, nor did they explicitly name the goal conflict between speed and forensic preservation. No explicit fallback articulated." — *LewRad, Too Good To Be True*

> "The one gap is limited explicit contingency planning; PLAYER did not articulate a fallback if rollback failed. Goal tensions (forensic preservation vs. speed, rollback risk) were not named aloud." — *JamieM, Big Investor V2*

> "No explicit contingency planning was observed (no 'if this doesn't fix it, we will…')." — *Nestor, DEFCON-1*

**What stronger behaviour looks like:**

> "Bez, we may need to halt new orders temporarily to fix this issue - are you ok with that, otherwise we risk spending more to rectify the issue" — *JamieM, Unknown Unknown* (evaluator note: "explicit trade-off articulation before seeking approval — textbook goal-conflict recognition moment")

> "Are we happy to proceed with a restore from backup" — *Patric, DEFCON-1* (evaluator note: "correctly surfaced the data-loss trade-off to the business for explicit approval before proceeding" — notably, this came after the earlier kill-script error; calibration improved within the same session)

**Recommendation:** Before any technically irreversible action — rollback, script kill, order pause, IP block — every player should send one sentence to the team naming the key risk: "If we do X, the downside is Y; Maya / Hamed, are you comfortable?" This creates a natural checkpoint that costs under thirty seconds and prevents the class of error that doubled Patric's ransom demand.

---

#### Area 3: Business communication that informs rather than acknowledges

All five players communicate with business stakeholders, which is a genuine collective strength and a meaningful differentiator from ICs who go silent under pressure. The gap is the content and structure of those communications. The dominant pattern is reactive, thin acknowledgement: "team are investigating," "no root cause yet," updates triggered by the stakeholder asking rather than the IC initiating on cadence, and no next-update commitment. LewRad is the consistent exception — his updates routinely include impact figures, a status line, and a timed next-update commitment. The rest of the cohort communicates honestly but sparsely.

**Where the gap shows up:**

> "Updates were honest but thin — 'team are investigating' without content, impact framing, or next-update timing. No explicit 'next update in X minutes' cadence was established." — *Andrew, Too Good To Be True*

> "Business-comms updates were sparse and reactive — PLAYER largely responded to bez's prompts rather than initiating updates on cadence. Updates lacked structured content (impact, current status, next steps). No ETA was given to bez despite being asked at T+25." — *Andrew, Unknown Unknown*

> "Several business-comms messages were very terse ('hi,' 'so this global,' '180K') and some were reactive responses to bez's questions rather than proactive status pushes. No cadence commitments ('I'll update you in X minutes') were observed." — *Patric, DEFCON-1*

> "Internal communication was minimal — mostly questions rather than shared mental model updates. External updates were reactive, brief, and largely factual without cadence-setting or next-update commitments." — *Nestor, DEFCON-1*

**What stronger behaviour looks like:**

> "300 users are affected and reports are coming in from all regions. Currently liaising with the developers to try to restore the service as quickly as possible. I will update every 20 minutes." — *LewRad, Too Good To Be True* (evaluator: "proactive at T+15 with impact figures and a cadence commitment")

> "Major incident declared: Users are unable to checkout / Impact: Multiple users are unable to checkout / Status: investigating / Next update: 5 minutes or as soon as problem has been identified." — *LewRad, Big Investor V2*

**Recommendation:** Adopt a three-line update template for every business-comms message: (1) Impact — who is affected and at what scale; (2) Status — what is currently happening and what the team's current hypothesis is; (3) Next update — a specific time commitment. LewRad already uses this pattern consistently; the rest of the cohort should study it and replicate it as a default, not a best-effort.
