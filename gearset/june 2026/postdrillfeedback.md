# Gearset Post-Drill Feedback Themes

Source: `gearset_all_drills.csv`  
Date filter: drills with `session_start` on or after 1 March 2026

This summary draws on the player-written `surprises` and `learnedToday` fields from 86 drills. There were 63 non-empty `surprises` responses and 65 non-empty `learnedToday` responses. Blank, `NA`, `N/A`, `n/a`, and similarly non-substantive responses were not treated as themes.

## Themes from `surprises`

### 1. The drills felt realistic, stressful, and emotionally engaging

Many players commented on the scenario realism: the pressure felt close to a live incident, even when they knew it was simulated. The realism came from stakeholder interruptions, uncertainty, imperfect information, human-like responses, and the need to act while still learning the system.

- Rosie Miller: "Too real!"
- Patrick Boyd: "Surprisingly life like."
- Jaime Holland: "The chat bots responded in a very human like manner"
- David Emmerson: "I got a bit panicked even though it's a fake situation :D"
- Antoine Poullet: "Stressful"
- Michael Hillman: "I think having people that also weren't sure of the potential causes replicates a real incident quite well."

### 2. Stakeholder pressure and business-facing expectations were prominent

Players were often surprised by how much the incident commander had to manage outside the technical diagnosis: CEO requests, shareholders, revenue questions, pressure for ETAs, and the need to keep senior stakeholders informed.

- Kenny Vaughan: "Two shareholders adding pressure \"I have a stakeholder meeting in 10 min\" and the CEO saying he wants a specific ETA and dates; both pushing for time to resolution."
- Gabriel: "Getting messages for revenue reports from the CEO when trying to diagnose the problem"
- Michael Hillman: "Adding the onus of updating exec level people really puts the commander skills to the test, it's a nice touch."
- Michael Hillman: "Execs asking about revenue lost is an interesting one when I don't appear to have any direct metrics around it"
- David Rant: "Reminded me to be more enquisitive about the shape of customers impacted, when it began, building up a picture of the incident for reporting upwards."

### 3. People availability, reluctance, and escalation paths created pressure

A recurring surprise was that the right people were not always immediately available or cooperative. Players had to pull people from meetings, push reluctant colleagues, or escalate around blocked channels.

- Sam Williams: "Needing to pull someone out of an important meeting."
- Andy Knox: "That Tanya couldn't step away from what she was doing for a few minutes to look at the error logs"
- Gabriel: "Key members of staff being unavailable was an interesting twist to the challenge."
- Catherine: "having to drag people into it, not having lines to escalate"
- David Rant: "Having to fight to get people engaged with the incident - Tanya being on another call"
- Kenny Vaughan: "I liked that there were some people not available and I had to make an executive decision myself."

### 4. Players noticed ambiguity, red herrings, and misleading or incomplete signals

The drills surprised players by resisting simple root-cause narratives. Several reflected on red herrings, unexpected causes, multiple possible theories, or signals that initially pointed in the wrong direction.

- Sam Williams: "Having a red herring. Having a problem with multiple root causes."
- Julian Wreford: "I had expected the recent changes to be the problem"
- Gabriel: "The cause of the issue was unexpected - something that wasn't tracked as a change and went under the radar because of operational mistakes."
- John Dilley: "Lots of possible theories going on, need to search wide, and not focus too much on one possible cause."
- David Emmerson: "the \"it's fixed, but it's not\" bit threw me..."
- Joshua Quinn: "I wasn't expecting to have to debug the team's browsers"

### 5. Tooling, dashboards, and observability gaps shaped the experience

Some surprises were about the available tools: dashboards, logs, metrics, alerting, or the way the simulated platform behaved. These comments often point to a learning gap around interpreting evidence under pressure.

- David Rant: "It was a bit misleading having two very similar but not identical grafana dashboards"
- Barry: "the lack of metrics for SNS specifically on the dashboard - most would have an alert for that I think"
- Kenny Vaughan: "I didn't expect to be in multiple challenges or to have the dashboards accessible to me directly."
- David Emmerson: "it was hard to figure out the system itself while dealing with the incident"
- Catherine: "It was difficult to come into a system I wasn't familiar with and know what the metrics I was looking at"

### 6. Third parties and external support processes were unexpectedly important

Several players were surprised that resolution depended on external services or indirect escalation paths, especially in Missing Delivery and Snipe Hunt scenarios.

- John Dilley: "Dealing with third party vendors"
- David Rant: "Having to bring in an exec to bypass AWS support, and that it all went through a 3rd party."
- Michael Hillman: "Relying on external services, and their support processes, can be limiting"
- Davide Ungari: "That it was AWS issue was not expecting that"
- Gabriel: "When a third party service is not offering an acceptable resolution, escalation is a good response to reach for."

## Themes from `learnedToday`

### 1. Be more assertive as incident commander

The strongest learning theme was decisiveness: players repeatedly said they needed to take command, set priorities, make calls, and push people when the incident required it.

- Sam Broughton: "Take command and confirm with the bots that they should be doing what they say they're about to do"
- Catherine: "be a bit bossy :)"
- Rosie Miller: "I learned that I could be more assertive during the drill - particularly with Tanya."
- Andy Knox: "To be more decisive about abandoning an unrelated activity to bring the right people onboard for this incident."
- Michael Hillman: "Taking the responsibility during the escalation was interesting"
- Joshua Quinn: "Being more forthright with time boxing"

### 2. Communicate visibly, regularly, and across the right channels

Players learned that incident command is not just diagnosis. It also means surfacing information, communicating sideways and upwards, summarising actions, giving regular updates, and keeping multiple audiences aligned.

- David Rant: "Surface information and communicate sideways/upwards to colleagues sooner before starting to dig into possible root causes."
- Jaime Holland: "Keeping comms going with all parties at all times"
- Catherine: "Regular updates, keep bringing people in and cross checking results"
- Eamonn Boyle: "Having the detail in a call and summarising the actions in chat is much more manageable for people who aren't leading the incident."
- David Rant: "Set clear priorities with others - if the nicident is higher priority than a routine call, make it clear."
- Kenny Vaughan: "I should be more specific with people on what I need from them."

### 3. Delegate, involve the right people early, and escalate sooner

Many learnings centred on bringing in the right people earlier and not trying to solve everything alone. Players identified delegation, escalation, and stakeholder routing as practical behaviours to improve.

- Rosie Miller: "Learn how to delegate. Clear instructions."
- Patrick Boyd: "Escalating early I think."
- John Dilley: "Get the right people on sooner"
- Antoine Poullet: "Knowing when to escalate"
- Barry: "who can escalate the AWS support case"
- Eamonn Boyle: "Press for prioritisation of the incident quicker."

### 4. Investigate broadly before narrowing too hard

Players learned to avoid over-anchoring on obvious or recent changes. Several reflected that they needed to ask wider questions, consider platform or people factors, and test assumptions rather than follow the first plausible route.

- Jaime Holland: "Useful to not focus entirely on known changes, but also to gather information on what else is happening on the infrastructure"
- Kenny Vaughan: "Asking about things that aren't just changes we've tracked."
- David Rant: "I need to question folks explicitly about \"have you done anything that aligns with the incident timewise\""
- Davide Ungari: "To always consider the platform not only the product."
- Joshua Quinn: "Don't just think about changes, but also the People."
- Michael Hillman: "Challenging assumptions and asking people to double check their statements can be useful otherwise you'll end up investigating red herrings."

### 5. Use evidence, timing, and verification more deliberately

Another repeated theme was the importance of checking logs, validating assumptions, lining up timelines, and confirming a fix before declaring the incident resolved.

- Oli: "Verify assumptions"
- Patrick Boyd: "Timings are super important when finding the root cause - push on the thing that lines up with the times."
- Oli: "Double check things are working before declaring things are resolved"
- Julian Wreford: "I jumped to rolling back the wrong service a little too quickly."
- Kenny Vaughan: "I should review the facts more frequently."
- David Emmerson: "Didn't look at the logs early enough or ask the team about errors."

### 6. Prepare incident process, roles, and organisational knowledge before the pressure hits

Players also described more structural learning: knowing the org chart, understanding response procedures, having runbooks, knowing who can approve or escalate, and being familiar with the platform before an incident starts.

- Davide Ungari: "For sure is good to have a clear incident response procedure and have a clear picture of the team and main components"
- Eamonn Boyle: "Having runbooks for key incidents like this is essential to avoid panic in the moment."
- Joshua Quinn: "Understanding business hierarchy is important"
- Davide Ungari: "To study the org chart a little bit better to remember names"
- Gwen Sellers: "It's worth checking whether insurance exists during a ransomware attack, as well as backup"
- Patrick Boyd: "Got a grounding in how the systems work and what is expected of us during a drill."

## Overall Pattern

The volunteered feedback suggests the drills are working less as narrow technical troubleshooting exercises and more as full incident-command rehearsals. Players repeatedly noticed the same pressures that make real incidents difficult: uncertainty, stakeholder demands, incomplete evidence, unavailable experts, red herrings, and the need to communicate while still investigating.

The strongest behavioural takeaways were to be more assertive, communicate earlier and more visibly, bring the right people in sooner, avoid anchoring on the first theory, and use evidence and timing more deliberately before deciding what to do next.
