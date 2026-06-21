# Snipe Hunt — Initial Seven Runs vs All Runs Comparison

This report compares the performance of the initial seven Snipe Hunt drills, excluding Swetha's first two runs (`9058` and `9311`), against the performance of the full attached cohort of all runs.

The initial comparison set contains **7 sessions**. The full cohort contains **124 sessions**.

## Headline Comparison

| Metric | Initial 7 excluding 9058/9311 | All runs | Difference |
|---|---:|---:|---:|
| Sessions | 7 | 124 | — |
| Average Overall Score | 0.512 | 0.570 | -0.058 |
| Average Mean Facet Score | 2.03 | 2.26 | -0.23 |
| Average Mean Marker Score | 2.10 | 2.33 | -0.23 |

The initial seven are around **0.23 points lower** on both mean facet and mean marker scores. On a 1–4 scoring scale, that is a meaningful but not catastrophic gap. The initial group sits in a “developing / practicing” band, while the full cohort has moved closer to a stronger “practicing+” level.

## Facet Comparison

| Facet | Initial 7 | All runs | Difference |
|---|---:|---:|---:|
| F1 — Misleading correlations | 1.86 | 1.86 | 0.00 |
| F2 — Hidden coupling | 2.00 | 2.40 | -0.40 |
| F3 — Decreased access to team | 2.14 | 2.43 | -0.29 |
| F4 — Interdependencies / coordination bottlenecks | 2.29 | 2.60 | -0.31 |
| F5 — Data overload / buried information | 1.86 | 2.03 | -0.17 |

The interesting result is **F1 is identical**. The initial seven were no worse than the full cohort at dealing with misleading correlations, at least on average. That suggests the early group’s problem was not simply that they chased the wrong thing more than everyone else.

The bigger gaps are elsewhere. **F2 — Hidden coupling** is the largest facet gap at **-0.40**, which suggests the initial cohort struggled more with recognising delayed, non-obvious system interactions. **F4 — Interdependencies / coordination bottlenecks** is also notably lower at **-0.31**, which points to more difficulty turning blocked approval paths, constrained people, and dependencies into an explicit coordination strategy. **F3 — Decreased access to team** is lower by **-0.29**, reinforcing that the initial group was less mature in adapting to unavailable or constrained teammates.

## Marker Group Comparison

| Marker Group | Initial 7 | All runs | Difference |
|---|---:|---:|---:|
| Leadership | 2.57 | 2.78 | -0.21 |
| Coordination | 2.29 | 2.49 | -0.20 |
| Communication | 1.79 | 1.88 | -0.09 |
| Mindset | 1.89 | 2.23 | -0.34 |

The clearest group-level gap is **Mindset**, down **0.34** versus the full cohort. That is consistent with the facet picture: the initial group was not just less coordinated; it was less likely to reason explicitly through uncertainty, consequences, and adaptation.

**Communication** is the smallest gap, only **-0.09**. This means the initial cohort was roughly comparable to the full cohort in communication markers, though both groups are still relatively low there. In other words, communication appears to be a broader cohort issue rather than something unusually weak in the first seven.

## Marker-Level Comparison

| Marker | Initial 7 | All runs | Difference |
|---|---:|---:|---:|
| L3 — Takes explicit ownership | 2.57 | 2.78 | -0.21 |
| C1 — Asks clarifying questions before acting | 2.86 | 2.89 | -0.03 |
| C3 — Checks for recent changes | 2.14 | 2.25 | -0.11 |
| C4 — Delegates tasks to specific people | 2.29 | 2.74 | -0.45 |
| C6 — Runs parallel investigation threads | 1.71 | 1.98 | -0.27 |
| C7 — Escalates when stuck | 2.43 | 2.60 | -0.17 |
| K2 — Provides substantive updates to business stakeholders | 1.86 | 1.91 | -0.05 |
| K4 — Communicates issue scope clearly to the technical team | 1.71 | 1.85 | -0.14 |
| M2 — Forms and tests working hypotheses | 2.00 | 2.12 | -0.12 |
| M3 — Uses evidence to narrow the scope | 2.00 | 2.25 | -0.25 |
| M4 — Considers potential consequences before acting | 1.29 | 1.91 | -0.62 |
| M5 — Adapts approach when initial path isn't working | 2.29 | 2.64 | -0.35 |

The most important single-marker gap is **M4 — Considers potential consequences before acting**, where the initial group scores **1.29** versus **1.91** across all runs. That is a large difference. It suggests the early group was particularly prone to authorising or suggesting actions without visibly asking:

- What could this break?
- What happens if this is wrong?
- What are the risks of this mitigation?

The next largest gap is **C4 — Delegates tasks to specific people**, down **0.45**. So the initial group appears less able to turn the incident into named work packages. They may have asked questions or engaged generally, but were less effective at saying “Daniel do X, Tanya do Y, Shay check Z.”

**M5 — Adapts approach when initial path isn’t working** is also materially lower at **-0.35**. Combined with the F2 gap, this suggests the first seven were more likely to stay in the original frame after a failed action, rather than treating failure as diagnostic information.

## Interpretation

The initial seven runs look like a cohort that could **engage**, **ask clarifying questions**, and **communicate at a basic level**, but was less strong at turning that engagement into structured incident command.

Their strongest relative marker is **C1 — Asks clarifying questions before acting**, where they are almost identical to the full cohort. So the issue was not lack of curiosity. The issue was what happened after the questions: weaker delegation, weaker parallelisation, weaker consequence checking, and weaker adaptive reframing.

The full cohort’s improvement appears to come less from better handling of misleading correlations and more from better **incident-shaping behaviours**:

- assigning work;
- adapting after failed paths;
- reasoning about consequences;
- recognising hidden coupling;
- making coordination constraints explicit.

## Practical Takeaway

For the early group, the biggest development focus would be **“from asking to structuring.”**

They need to move from asking useful questions to creating a visible operating model:

- explicit hypotheses;
- named owners;
- parallel workstreams;
- decision-risk checks;
- visible pivots when evidence changes.

The comparison suggests that later or broader cohort performance improved not because people became dramatically better at avoiding misleading correlations, but because they became better at shaping the incident response around uncertainty, constraints, and emerging evidence.
