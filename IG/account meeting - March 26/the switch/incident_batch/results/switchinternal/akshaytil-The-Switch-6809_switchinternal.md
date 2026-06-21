# akshaytil-The-Switch-6809.csv

| Criterion | Grade | Evidence | Rationale |
|---|---|---|---|
| Customer Impact Awareness | ❌ | "Bob Please make sure This info of getting DDoS attack shouldn't be conveyed to users" | No directive for a customer-facing banner/status page; instead the player restricted what to share. This misses proactive outward communication. |
| Customer Impact Assessment | ✅ | "Bob What is scope of impact and regions affected?"<br>"Bob how many reports so for?" | Asked for concrete scope and volume of reports to quantify customer impact. These are specific, metric-focused requests. |
| Issue Reproduction | ❌ | "Shay and Daniel in the mean time try coordinate and try to pin point issue by back tracking"<br>"Daniel you do you and try to figure out" | No explicit attempt or direction to reproduce the issue or gather reproduction evidence. Requests were generic and not tied to repro steps. |
| Check Platform Changes | ✅ | "Shay, Daniel, Tanya check your recent changes, please."<br>"Shay check from changes pov" | Clearly initiated a review of recent changes. This directly targets potential platform-change causes. |
| Concurrent Investigations | ✅ | "Maya can check from security pov"<br>"Tanya Can we bring in network team"<br>"Shay and Daniel in the mean time try coordinate and try to pin point issue by back tracking"<br>"Shay check from changes pov and Tanya please check from infra pov" | Launched multiple parallel streams (security, network/infra, change review) with named owners and goals. This demonstrates coordinated concurrent investigation. |
| Escalation | ⚠️ | "Hamed S Can you please provide a hand here!" | The player escalated to Hamed but only after another teammate suggested it. Partial credit for executing the escalation, not for initiating it. |
| Timeboxing | ❌ |  | No explicit time limits or follow-up cadences were set for tasks. Urgency was implied but not timeboxed. |
| Leadership & Command | ✅ | "Summary: There is a spike in outbound connections in the edge router and the origin IP block 10.50.0.0/24."<br>"Maya can check from security pov"<br>"Shay check from changes pov and Tanya please check from infra pov"<br>"increasing the sev level to 2" | Gave clear assignments, posted periodic summaries, and adjusted severity, showing active command and structure. |
| Resolution Verification | ✅ | "Bob Can youu check any reports now?"<br>"Issue seems to be resolved" | Verified restoration by checking with Support on incoming reports before declaring resolution. Confirmation was based on stakeholder data. |

## Summary
- Strong leadership: assigned clear owners across security, infra, and change review, and posted timely summaries and severity updates.
- Good customer impact assessment: proactively queried scope, regions, and report counts.
- Missed proactive customer comms: did not request a status page/banner; focused instead on limiting disclosure.
- Gaps in execution hygiene: no explicit timeboxing and no directed reproduction steps or evidence requests.
- High-leverage improvements: add a default customer communication step (status page/holding banner), include explicit timeboxes with check-ins, and direct a concrete repro with artifacts (timestamps, screenshots, error IDs).
