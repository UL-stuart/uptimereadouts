# Sonic Post-Drill Feedback Themes

Source: `sonic_all_drills.csv`

Scope: drills with `session_start` on or after 1 January 2026. There are 15 drill rows in scope, with 12 usable `surprises` responses and 12 usable `learnedToday` responses after excluding blanks and `n/a`.

## Surprises

The `surprises` column captures what players found unexpected or newly salient during the drills. The strongest pattern is that players were surprised by hidden operational complexity: undocumented infrastructure, multi-layered code or process changes, unusual incident causes, and complications that only emerged through investigation or chat interactions.

### 1. Hidden complexity and undocumented operational context

Players were often surprised when the root cause sat outside the obvious change path, or when critical context was undocumented or only surfaced after asking the right people.

| Example | Verbatim feedback |
| --- | --- |
| Leigh Burton, The Chain Workshop, 13 Feb 2026 | "multi-layered code updates a welcome surprise, the chain of custody/information also an interesting challenge." |
| Seth Lohr, The Switch, 23 Feb 2026 | "OB has an on-prem infrastructure. Yet even more stuff they didn't document." |
| Leigh Burton, Memory Lane Workshop, 22 Apr 2026 | "non-code changes causing issues, something that without the interactions in chat would not have been brought up looking at the usual dashboards." |
| Joe Muller, Snipe Hunt, 26 May 2026 | "I didn't expect to see a much more process-based failure in the fact that there were undocumented aspects of the certificate update process that caused issues." |

### 2. Scenarios challenged assumptions about incident shape and urgency

Several responses point to drills breaking the expected rhythm of an incident: not everything started with urgency, not every issue belonged to software, and not every solution required fixing forward.

| Example | Verbatim feedback |
| --- | --- |
| Joe Muller, The Chain Workshop, 10 Feb 2026 | "It was interesting that there was no pressure to maintain the new feature." |
| Joe Muller, Version confusion, 14 Apr 2026 | "It was surprising to have a drill that didn't begin with urgency, but rather I had to 'tease' the problem out." |
| Joe Muller, The Switch, 19 Mar 2026 | "It was surprising to have a network device be the cause of problems for a change" |
| Leigh Burton, The Switch, 18 Mar 2026 | "it was a good balance of having enough open 'space' to flex the skills we have been learning" |

### 3. People dynamics and pushback became part of the challenge

Players noticed that the interpersonal and organizational side of the scenario mattered: colleague pushback, stakeholder pressure, unclear escalation paths, and needing to know who to contact.

| Example | Verbatim feedback |
| --- | --- |
| Alyssa Afaese, Bezs Beatles Day!, 9 Apr 2026 | "The pushback from colleagues forced me to ask more clarifying questions." |
| Alyssa Afaese, Bezs Beatles Day!, 9 Apr 2026 | "I need to adjust to using the organization chart since I'm not always aware of who I can contact in a specific department." |
| Seth Lohr, Snipe Hunt, 27 May 2026 | "Bez was being a lot more pushy." |
| Leigh Burton, Snipe Hunt, 3 Jun 2026 | "bob not being able to put up a banner" |

### 4. Snipe Hunt stood out for compounded incident complexity

Snipe Hunt feedback repeatedly mentions many competing problems at once: staff absence, multiple failed theories, certificate-chain ordering, and uncertainty over the real fix.

| Example | Verbatim feedback |
| --- | --- |
| Seth Lohr, Snipe Hunt, 27 May 2026 | "The number of complications." |
| Seth Lohr, Snipe Hunt, 27 May 2026 | "the issue wasn't the first 4 fixes... It was the 3rd, 4th, and 5th fix: the cert chain ordering." |
| Seth Lohr, Snipe Hunt, 27 May 2026 | "There were 2-4 really strong theories as to what the issue was" |
| Leigh Burton, Snipe Hunt, 3 Jun 2026 | "Cert bundle out of order." |

## Learned Today

The `learnedToday` column is more action-oriented than `surprises`. Players volunteered lessons about incident command habits: communicate clearly, establish common ground, escalate early, timebox investigation, use specialist teams, understand impact, and manage multiple theories under uncertainty.

### 1. Communication, grounding, and concise handover are core learning points

Several players explicitly identified communication quality as something to improve, especially when establishing common ground or handing information between teams.

| Example | Verbatim feedback |
| --- | --- |
| Seth Lohr, The Chain Workshop, 26 Jan 2026 | "We suck at incident comms. We're looking into getting better at it." |
| Seth Lohr, The Chain Workshop, 26 Jan 2026 | "Establishing common ground would be a really good thing to do." |
| Leigh Burton, The Chain Workshop, 13 Feb 2026 | "to improve information succinctness when handing over information." |
| Leigh Burton, The Chain Workshop, 13 Feb 2026 | "to also think about *what* information is important and what is not." |

### 2. Restore service pragmatically, including rollback when appropriate

The Chain Workshop produced a clear lesson about prioritizing restoration over defending a new feature or trying to fix a complex issue in production.

| Example | Verbatim feedback |
| --- | --- |
| Joe Muller, The Chain Workshop, 10 Feb 2026 | "Don't be afraid to rollback if a new feature doesn't work." |
| Joe Muller, The Chain Workshop, 10 Feb 2026 | "It's better to have a working product than a partially broken one." |

### 3. Escalate early and use the right teams

Players repeatedly learned to bring in the right people earlier: platform, security, domain teams, or multiple reviewers when a problem may have an overlooked factor.

| Example | Verbatim feedback |
| --- | --- |
| Joe Muller, The Switch, 19 Mar 2026 | "Lean on the Security and Platform teams when the issue is outside of Software" |
| Seth Lohr, The Switch, 23 Feb 2026 | "Trust from teams to understand their infrastructure and letting them know how to troubleshoot/mitigate an incident that is within their domain." |
| Joe Muller, Memory Lane Workshop, 28 Apr 2026 | "Be ready to escalate early and try to get more than one person to look at a problem so you don't miss a key factor." |
| Leigh Burton, Snipe Hunt, 3 Jun 2026 | "accepting that you might need to bring in folks from other activities... for the greater good of the company." |

### 4. Timebox, establish impact, and use architecture clues

The Switch and Bezs Beatles Day feedback emphasizes structured investigation: understand impact, notice which users are affected, map changes to architecture, and distinguish business from technical communication channels.

| Example | Verbatim feedback |
| --- | --- |
| Leigh Burton, The Switch, 18 Mar 2026 | "better at timeboxing and making sure we gain an understanding of impact" |
| Leigh Burton, The Switch, 18 Mar 2026 | "folks outside the business network (WFH) were less impacted than folks in the office" |
| Alyssa Afaese, Bezs Beatles Day!, 9 Apr 2026 | "it's important to know where in the architecture those changes have an effect." |
| Alyssa Afaese, Bezs Beatles Day!, 9 Apr 2026 | "Confirming what each chat is for - business vs. online boutique." |

### 5. Improve change visibility and run-plan discipline

Memory Lane feedback highlights that not every relevant operational change appears in a code changelog. Players learned to account for migrations, server setup, and living operational documentation.

| Example | Verbatim feedback |
| --- | --- |
| Leigh Burton, Memory Lane Workshop, 22 Apr 2026 | "not all related changes that can affect an environment are in the change logs" |
| Leigh Burton, Memory Lane Workshop, 22 Apr 2026 | "getting a better scope of ongoing projects like a server migration could help reduce time to resolution." |
| Leigh Burton, Memory Lane Workshop, 22 Apr 2026 | "server migration run-plans include all needed service setup steps" |
| Leigh Burton, Memory Lane Workshop, 22 Apr 2026 | "those docs should be a living document, not make once and forget." |

### 6. Manage uncertainty, stakeholder expectations, and competing theories

Snipe Hunt learning focuses on incident command under pressure: multiple strong theories, unavailable escalation paths, uncertain fixes, and the need to communicate more conservatively with stakeholders.

| Example | Verbatim feedback |
| --- | --- |
| Seth Lohr, Snipe Hunt, 27 May 2026 | "Be careful to always inflate the ETA for Bez" |
| Seth Lohr, Snipe Hunt, 27 May 2026 | "Tips from UL on how to manage multiple competing theories during an incident." |
| Leigh Burton, Snipe Hunt, 3 Jun 2026 | "handling the incident with no specific escalation path available due to the vacations/conferences." |

## Overall Readout

Across the 2026 drill feedback, Sonic players are volunteering lessons that are less about isolated technical fixes and more about incident operating discipline. The strongest themes are communication, grounding, escalation, impact assessment, architectural reasoning, and managing uncertainty when multiple plausible causes exist.

The `surprises` responses show that players are most struck by hidden context and unexpected incident shape. The `learnedToday` responses show that they are translating those surprises into practical habits: communicate more clearly, use the right teams, rollback when restoration matters most, keep operational documentation alive, and manage competing theories without overcommitting.
