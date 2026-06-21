# aashishku-The-Switch-8000.csv

| Criterion | Grade | Evidence | Rationale |
|---|---|---|---|
| Customer Impact Awareness | ❌ | "We have an attack on our network, we are trying to use backup system" | No directive to post a status page, banner, or customer-facing notice was made. Communications stayed internal only. |
| Customer Impact Assessment | ⚠️ | "@bob have you observe any effect from business side ?" | Asked about business impact but in a vague way without requesting specific metrics or scope. |
| Issue Reproduction | ❌ |  | No attempt to reproduce the issue or direction to reproduce with evidence was given by the player. |
| Check Platform Changes | ✅ | "could anyone let us know the recent deployment?"<br>"@shay could you please check the recent deployment change and discuss this with @daniel" | Clearly initiated and assigned verification of recent deployments. |
| Concurrent Investigations | ✅ | "Hi @tanya, @hamed , @daniel we have a incident, could you pelase analyse and come back in 2mins"<br>"@shay could you please check the recent deployment change and discuss this with @daniel"<br>"@maya  could you please check any thing from the security side"<br>"@maya @hamed , @daniel , @shay , @tanya could you please analyse from the logs whats going on here" | Launched multiple parallel streams with owners (deployments, security/network, logs) and clear asks. |
| Escalation | ✅ | "Hi @tanya, @hamed , @daniel we have a incident, could you pelase analyse and come back in 2mins" | Proactively engaged Hamed (an authority) without prompting, constituting escalation. |
| Timeboxing | ✅ | "could you pelase analyse and come back in 2mins"<br>"@maya could you please find the solution and come back in 2mins"<br>"@daniel , @shay any updated from the recent deployment?" | Set explicit 2-minute timeboxes and followed up for updates, showing cadence. |
| Leadership & Command | ✅ | "HI team, we are having a huge traffice, created a SEV-2 incident"<br>"this is sevior issue , increasing the seviority of incident to SEV-1"<br>"@maya , @hamed , can we switch back to backup now, then please do it immediately"<br>"Looks to be 50% of users have slow load times... 7% ... global" | Took command by creating/upgrading the incident, assigning tasks, directing failover, and summarizing impact to stakeholders. |
| Resolution Verification | ✅ | "@Bob, could you confirm the current situation"<br>"@maya is the issue resolved?"<br>"@shay , @tanya , @hamed , @daniel could you pelase check the network ping and logs if everythibg is correct?"<br>"We have resolved the issue, network is good now" | Verified restoration through customer confirmation and team data checks before announcing resolution. |

## Summary
- Strong leadership: created and upgraded the incident, assigned owners, and drove a clear restoration path (backup switch).
- Good parallelization and timeboxing: multiple concurrent workstreams with explicit 2-minute cadences and follow-ups.
- Solid resolution verification: cross-checked with customers and multiple technical teams before declaring resolved.
- Gaps in customer comms: did not request a status page/holding banner or explicit customer-facing notice.
- High-leverage improvement: add a customer communication step early (status page/banner) and direct explicit issue reproduction with requested evidence.
