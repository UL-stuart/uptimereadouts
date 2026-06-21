# Options IT Player Learnings Summary

This summary is based on the `surprises` and `learnedToday` columns in `options-it-drill-usage.csv`, covering drill experiences from January to June 2026. The source contains 96 drill-session rows, with 83 non-empty responses in each of the two reflection columns.

The comments show that players are learning less from any single technical scenario and more from repeated incident-command patterns: how to stay evidence-led under pressure, how to coordinate people when the obvious route is blocked, and how to communicate clearly while the situation is still ambiguous.

## Main Things Players Learned

### 1. Use facts, scope, and evidence before committing to a theory

Across the reflections, players repeatedly learned not to jump too quickly to the first plausible cause. Several comments mention misleading changes, multiple simultaneous issues, local-vs-global impact, or noisy signals that made the first explanation feel convincing but incomplete.

Common lessons included:

- Check whether the issue is isolated, regional, global, or customer-impacting before escalating severity.
- Do not assume all visible issues are related.
- Use logs, metrics, customer reports, and reproduction attempts to narrow the problem.
- Do not over-trust recent changes or someone's statement that a change "shouldn't" affect production.
- Keep digging when the first fix only partially works or does not explain the full pattern.

Representative reflections:

- Mark McGarry: "Don't assume all issues are related."
- Zach Davis: "Not to assume the first 'obvious' smoking gun is the complete root cause."
- Mark McGarry: "Where are we seeing the errors? Is it isolated to one system, country, subset"
- Leah Murphy: "Not to listen to others and use the facts / data to start investigation"
- Donnchadh Tierney: "Dig deeper when changes are made."
- Lucy McCormack: "Logs never lie!!!"

### 2. Communicate impact and current understanding more clearly

Players frequently mentioned the need to communicate differently to technical and business audiences. The reflections show growing awareness that incident communication is not just "we are investigating"; it needs scope, impact, current theory, what is being done, and what the business should expect next.

Common lessons included:

- Adjust communication depending on whether the audience is technical or business-facing.
- Quantify impact before updating stakeholders.
- Keep Bez/business stakeholders informed earlier and with more useful context.
- Use grounding or summaries so the incident team shares the same working picture.
- Clearly report when there are multiple issues at once.

Representative reflections:

- Ruairi Corrigan: "Adjust communications depending on who you are talking to. Tech/Business"
- Mark McGarry: "Quantify the impact before updating the business. Get % differences etc."
- Donnchadh Tierney: "Be more aware of the business implications and relay these to Bez earlier."
- Jack Walsh: "Use grounding to communicate current working theory."
- Amelia Horwood: "need to clearly report to business comms if there are multiple issues at once"
- Ciaran Hurley: "importance of business comms to seniors"

### 3. Escalate, delegate, and use the available team deliberately

A strong theme across the six months is that incidents become harder when key people are unavailable, distracted, or unresponsive. Players learned to escalate earlier, pull in the right roles, use the team on hand, and avoid relying on one person to resolve the incident.

Common lessons included:

- Escalate when a team member is not responding or an approval path is blocked.
- Use the whole team rather than waiting on one person.
- Pull the right specialist in early, especially infra, security, vendors, or third parties.
- Prioritise the major incident over competing commitments where appropriate.
- Assign specific tasks to named people instead of broadcasting vague asks.

Representative reflections:

- Jack Walsh: "important to escalate early in the event of an issue if a team member is not responding."
- Ciara Scullion: "Dont rely on one person to fix a change"
- Leah Murphy: "To utilise the full team, and to use teamwork to help fill those knowledge gaps"
- Emma Allsopp: "It was good that people were out of office, the drill showed me how to utilise the team on hand."
- Ciaran Hurley: "escalation and resource management"
- Aoife Breen: "Get everyone on board when a p1 incident is on"

### 4. Be decisive under pressure, while still checking consequences

Several drills forced players into uncomfortable decision points: whether to fail over, restart production, approve a change, pull someone off other work, or prioritise restoration over root cause. Players learned that they may not have perfect information, but they still need to make a clear decision and own it.

Common lessons included:

- Stay calm when stakeholders or engineers push for drastic action.
- Prioritise restoration when the service is heavily impacted.
- Make executive decisions with the information available.
- Be clear in your intention and back the choice.
- Consider the consequences of disruptive actions before proceeding.

Representative reflections:

- Aoife Breen: "Prioritise restoration and stay calm"
- Ellie Walsh: "To be decisive and to call out individual team members to look at different things"
- Emma Allsopp: "This incident required me to make an executive decision under pressure, with the information that I had."
- Elsa Savage: "how to perform under pressure and to go off your own judgement"
- Jack Walsh: "Important to not react too quickly into rash decisions"
- Amelia Horwood: "To make decisions fast"

### 5. Verify resolution before closing the loop

Players also learned that apparent recovery is not always full recovery. Several reflections mention temporary fixes, recurrence, incomplete resolution, or the need to confirm service health before telling users or stakeholders the incident is over.

Common lessons included:

- Wait before confirming with users.
- Check that the fix has actually restored service.
- Verify metrics, transactions, or customer symptoms rather than assuming recovery.
- Keep checking for follow-on issues after the main symptom improves.
- Do not close an incident just because the first fix has been applied.

Representative reflections:

- Leah Murphy: "Wait before confirming with users"
- Ritchie McGrath: "Always verify the incident is fully resolved"
- Aoife Breen: "Don't confirm completion or proper resolution until 100% sure"
- Patrick Collins: "we restored service but i didnt check to see or notice when that actually happened"
- Amelia Horwood: "check that nothing has been compromised after issue resolved"

## Notable Surprise Patterns

The `surprises` column adds useful context about what made the drills feel realistic or challenging. Recurring surprise patterns included:

- Multiple issues happening at once, especially when they appeared related but were not.
- Key engineers, approvers, or specialists being unavailable.
- Senior or business stakeholders applying pressure while the technical picture was still unclear.
- Incidents involving third parties, vendors, infrastructure, security, or network layers rather than only application code.
- Fixes that were partial, temporary, or required multiple steps.
- Drills feeling more realistic, human, or high-pressure than expected.

These surprise patterns help explain why the learning themes above recur: the drills repeatedly put players in situations where simple root-cause thinking was not enough, and where incident leadership required coordination, communication, and judgement under uncertainty.

## Overall Takeaway

Over the last six months, the most important player learning has been the shift from "find the technical fix" toward "lead the incident response." Players are learning to gather evidence before committing to a cause, communicate a shared picture, use the team deliberately, make decisions under pressure, and verify recovery before closing the loop.
