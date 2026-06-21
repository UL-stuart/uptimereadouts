# Player Synthesis — Andrew

## Overall character

Andrew is a composed, procedurally reliable incident commander who consistently does the fundamentals right: he raises the incident record promptly, communicates scope to the business early, delegates to named responders rather than diving into technical diagnosis himself, and closes the incident only after personally verifying resolution. His tone across all four sessions was calm and polite, and he never caused harm through premature closure or reckless escalation. The limitation that defines his profile, however, is equally consistent: Andrew operates as a relay point and approver rather than as a cognitive leader. He does not broadcast a working hypothesis, does not revise his mental model out loud when evidence changes, and does not drive sensemaking — he follows it. Every session saw the critical diagnosis emerge from the technical team (Daniel, Hamed, Tanya) while Andrew endorsed and actioned their conclusions. This gap between solid procedural execution and passive intellectual leadership is the defining developmental theme across his four sessions.

---

## Scores table

| Dimension | Session 1 (Too Good To Be True) | Session 2 (Big Investor V2) | Session 3 (Discount Disaster) | Session 4 (Unknown Unknown) |
|---|:---:|:---:|:---:|:---:|
| Sensemaking | 3 | 3 | 3 | 3 |
| Coordination | 3 | 3 | 3 | 3 |
| Decision-Making | 3 | 2 | 3 | 3 |
| Communication | 3 | 3 | 3 | 3 |
| Adaptive Capacity | 3 | 3 | 3 | 3 |
| Incident Lifecycle Management | 4 | 4 | 4 | 4 |
| **Avg** | **3.17** | **3.00** | **3.17** | **3.17** |

---

## Trajectory analysis

Andrew's trajectory is a plateau. With one exception — Decision-Making dropping to 2 in Session 2 before returning to 3 — every score across all four sessions is either 3 or 4, and the pattern is perfectly consistent throughout. Incident Lifecycle Management holds at 4 in every session; all other five dimensions hold at 3.

The Session 2 dip in Decision-Making reflects the specific scenario's difficulty: Andrew authorised a payment rollback without strong evidence ("lets see if that makes any difference"), was visibly behind the team's diagnostic momentum on the chaos-test reframe, and offered no contingency planning at any point. It did not signal a structural regression — scores returned to baseline immediately — but it was the only movement in the entire dataset.

The behavioural evidence reinforces the flatness of the scores. Session 1 evaluators noted Andrew "relayed symptoms and relayed others' findings rather than synthesising them into a narrated picture." Session 2: "PLAYER did not explicitly revise or articulate a new hypothesis after the payment rollback failed." Session 3: "Andrew never externalized a working hypothesis to the team, never articulated the evolving picture of the incident." Session 4: "PLAYER rarely narrated their evolving mental model to the team or business." This is the same observation, in almost identical language, across all four sessions — the feedback is not translating into changed behaviour between drills.

The one positive signal worth noting: Session 4 contained two small but genuine proactive moments — pausing orders before root cause was confirmed, and independently verifying the maintenance banner removal rather than accepting the team's word. These did not move scores but are building blocks for the shift from adequate to strong command.

---

## 2 most consistent strengths

**1. Incident Lifecycle Management — prompt record creation, scope verification, and grounded closure**

Across every session Andrew raised the incident record early via the `/incident` command, confirmed scope with the business promptly, and validated resolution personally before communicating the all-clear. This is the single dimension to score 4 in all four sessions without exception.

- Session 1 (Too Good To Be True): *"Incident record created at T+12 with P1 severity — prompt and correctly calibrated... PLAYER personally reproduced the issue."* And: *"'I have logged in to the site and was able to place an order it looks like it is now back up and running' (T+29)"* — personal replication of recovery before reporting.
- Session 3 (Discount Disaster): *"Incident record raised promptly at T+4 via /incident command... Closure was communicated at T+24 after clear restoration evidence (PLAYER's personal order placement at T+22; bob's login confirmation at 10:27:14) — closure is valid and appropriately timed."*
- Session 4 (Unknown Unknown): *"PLAYER confirmed resolution with the technical team... and communicated to business-comms... after Daniel's 'We are LIVE for orders back again!' confirmed restoration — temporal gating satisfied."*

The habit of personal verification before closure is a strong and reliable safeguard against premature resolution.

**2. Calm, above-the-line coordination — delegation by name, avoidance of hands-on technical work**

Andrew does not drop into the technical weeds. In every session he delegated investigation to named responders, served as a routing node for information between them, and maintained a calm, polite tone throughout.

- Session 2 (Big Investor V2): *"PLAYER delegated consistently and addressed responders by name, which is positive."*
- Session 3 (Discount Disaster): *"PLAYER stayed mostly above the line, delegating to daniel, shay, hamed, and maya in sequence rather than attempting hands-on technical diagnosis... Information routing at T+19 (asking someone to give Maya the IP) was a positive moment of above-the-line facilitation. Psychological tone was calm and polite throughout."*
- Session 4 (Unknown Unknown): *"PLAYER stayed mostly above the line and did not dive into technical troubleshooting themselves, which is appropriate. Tone throughout was calm and respectful."*

This restraint — knowing what not to do — is underrated in IC development and Andrew demonstrates it consistently.

---

## 2 most persistent development areas

**1. Passive sensemaking — no working hypotheses broadcast, no mental model narrated to the team**

This is the single most consistent gap in the dataset. Andrew never verbally shared his current read of the incident with the team, never said "I think this is X because of Y — does anyone see it differently?", and never explicitly revised his understanding out loud when evidence changed. In every session the critical diagnostic frame was generated by the technical team, not by Andrew.

- Session 1 (Too Good To Be True): *"PLAYER did not construct an explicit working theory or share a mental model with the team — they relayed symptoms and relayed others' findings rather than synthesising them into a narrated picture... cause identification was done by Daniel and Hamed, with PLAYER asking a helpful but late framing question."*
- Session 2 (Big Investor V2): *"PLAYER formed an initial hypothesis (payment service) but did not revise it explicitly when it proved wrong, and the critical diagnosis of chaos tests hitting production was driven by daniel and hamed rather than by PLAYER's directed inquiry."*
- Session 3 (Discount Disaster): *"Andrew never externalized a working hypothesis to the team, never articulated the evolving picture of the incident, and relied almost entirely on other team members to generate, test, and revise frames. Each shift in his focus... was triggered by a prompt from someone else rather than from his own pattern recognition."*
- Session 4 (Unknown Unknown): *"Frame revision was passive — when hamed explained the rollback would not work, PLAYER accepted this without articulating a revised understanding. Root-cause reasoning was largely crowd-sourced from Tanya and Daniel rather than driven by PLAYER."*

**2. Thin, reactive business-comms — updates lack structure, cadence, and content**

In every session Andrew's external communications amounted to "team are investigating" without impact quantification, next-update timing, or structured status framing. Updates were largely triggered by Bez asking rather than by Andrew initiating on a set cadence.

- Session 1 (Too Good To Be True): *"Updates were honest but thin — 'team are investigating' without content, impact framing, or next-update timing... No explicit 'next update in X minutes' cadence was established."*
- Session 2 (Big Investor V2): *"Content quality was acceptable but lean: updates described what the team was doing rather than impact, ETA, or next update timing. No cadence-setting ('I'll update again in 5 minutes')."*
- Session 3 (Discount Disaster): *"Updates were consistently thin: 'i have the team working on this' (T+11) contains no impact, status, next steps, or timeline. No update cadence was set at any point."*
- Session 4 (Unknown Unknown): *"Business-comms updates were sparse and reactive — PLAYER largely responded to bez's prompts rather than initiating updates on cadence. Updates lacked structured content (impact, current status, next steps). No ETA was given to bez despite being asked at T+25."*

---

## Most impactful next step

At the start of the next drill, Andrew should commit to narrating his working hypothesis out loud to the team at least once every five minutes, using a fixed structure: "My current read is [X] because [Y]. The team is testing [Z]. If that fails in [N] minutes, we pivot to [fallback]." Every evaluator across all four sessions independently arrived at the same recommendation. This single habit would address both persistent development areas simultaneously — it externalises the sensemaking that is currently happening silently, gives the business-comms audience a richer and more structured update, and elevates Andrew from a competent relay point into the cognitive leader his procedural discipline already qualifies him to be.
