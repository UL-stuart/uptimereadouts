# avinashkr-The-Switch-7888.csv

| Criterion | Grade | Evidence | Rationale |
|---|---|---|---|
| Customer Impact Awareness | ✅ | "@bob May be better to put a banner on the page regarding the slowness in the application"<br>"Regarding the banner in the page for notifying the customers have been taike care"<br>"@bob Its not an attacj, just post about the slowness and mentioned teams are working on it"<br>"@bob  Please confiorm on the status page" | At T+17, PLAYER explicitly requested a customer-facing banner and guided status-page comms. This proactively informed customers about impact. |
| Customer Impact Assessment | ✅ | "@bob  Do we know since when the issues observed?"<br>"@bob  Also wanted to know if its affected all markets or anything specific"<br>"@bob  How about the volumes of customer reporing ?" | Starting at T+8, PLAYER asked for concrete scope: onset time, affected markets, and volume of reports. These are specific impact metrics. |
| Issue Reproduction | ⚠️ | "@daniel  Do you see a ny ossues while trying to place the order ?" | At T+1, they only asked a teammate if they saw issues while ordering, without directing evidence capture or attempting reproduction themselves. |
| Check Platform Changes | ✅ | "CHG89692 - CHG89675"<br>"These are the changes we rolled out on Payment and services"<br>"Have we have verified the changes mentioned above If that cause anything ?" | At T+10, PLAYER surfaced recent change IDs and requested verification of their impact, initiating a concrete changes check. |
| Concurrent Investigations | ✅ | "@daniel  Do you see a ny ossues while trying to place the order ?"<br>"Hey @tanya Are you seeing anything from the logs"<br>"Hey @maya  We have a situation with spike in traffic, could you please check "<br>"@bob  May be better to put a banner on the page regarding the slowness in the application" | Between T+1 and T+17, PLAYER launched multiple parallel tracks with owners and goals (repro/orders, logs, security/traffic legitimacy, and customer comms). |
| Escalation | ✅ | "@hamed  Can you confirm on the recent changes on network side ?"<br>"Copying @tinus  For better visibility and help in case " | PLAYER proactively engaged Hamed and escalated to Tinus at T+18 to ensure leadership visibility and support. |
| Timeboxing | ❌ | "someone please confirm " | No explicit time limits or follow-up cadence were assigned to tasks; requests lacked deadlines. |
| Leadership & Command | ✅ | "\Create an incident - Network Degradation "<br>"upgrade the INC priority to Sev2 as its impacted the order placing "<br>"We have enaged the Cyber team to check further on their side "<br>"Team working on failing over the affected switch to another one" | PLAYER created/structured the incident, set severity, delegated workstreams, and communicated progress, maintaining direction and urgency. |
| Resolution Verification | ✅ | "@maya  are you seeing any changes in the logs now ?"<br>"@tanya  please confirm from your side as well"<br>"The failover comepleted and there are no issues observed so far "<br>"We have less reports from the customer side as well" | After restoration steps, PLAYER sought confirmation from technical owners and noted reduced customer reports, verifying recovery with both ops data and business signals. |

## Summary
- Strong customer awareness: proactively requested a banner and coordinated status communications.
- Good scope assessment: asked for timeframe, market spread, and volumes to quantify impact.
- Demonstrated leadership: created the incident, set Sev2, delegated multiple parallel tracks, and escalated to leadership appropriately.
- Reproduction direction was light; next time, request specific evidence (timestamps, errors, screenshots) or perform a controlled repro.
- Missing timeboxing; add explicit deadlines and follow-up cadence (e.g., “update in 5 minutes with logs and error rates”) to tighten execution.
