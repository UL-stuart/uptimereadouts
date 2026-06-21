# harshagar-The-Switch-7272.csv

| Criterion | Grade | Evidence | Rationale |
|---|---|---|---|
| Customer Impact Awareness | ❌ | "yes @bez we are on it" | No request for a status page, banner, holding page, or customer notice was made. Communication stayed internal. |
| Customer Impact Assessment | ⚠️ | "Hey @bob : ar eyou getting any issues from clients as well regarding this?"<br>"@bob : is it specific to a region or global?"<br>"@Bob: from when you are getting complaints"<br>"when its spiking?" | Asked for impact and scope, but the first ask was vague before becoming specific later. |
| Issue Reproduction | ⚠️ | "Platform seems to be working correctly"<br>"are you guys experiencing same things.. for me also it sworking fine" | Attempted to validate and queried others, but provided no steps or evidence and did not direct a structured reproduction. |
| Check Platform Changes | ⚠️ | "@Tanya: can you look from platform side"<br>"LOOKS LIKE THE DEPLOYMENT IS 24 hrs ago" | Mentioned deployments and asked for a platform check, but did not explicitly initiate a targeted review of recent changes/flags/rollouts. |
| Concurrent Investigations | ✅ | "@Shay: can you please check anything is wrong from dev side"<br>"@Tanya: can you look from platform side"<br>"@MAya: any security concers can you please check"<br>"can you check if logs are fine from app side" | Launched multiple parallel streams with clear owners across dev, platform/infra, security, and app logs. |
| Escalation | ✅ | "@hamed : any suggestion from your side" | Proactively engaged Hamed (an authority) for guidance without being prompted. |
| Timeboxing | ⚠️ | "@Maya: can you please try to figure out the things asap please" | Expressed urgency but set no concrete deadlines or follow-up cadence. |
| Leadership & Command | ⚠️ | "we'll take the incident first and try to look into it"<br>"@maya @hamed @tanya please coordinate to get it resolved"<br>"please proceed"<br>"@Bob: now can you help us with the reports" | Provided direction and assignments, but lacked structured updates, explicit owners per stream, and operational cadence. |
| Resolution Verification | ✅ | "@Bob: now can you help us with the reports"<br>"its resolved now"<br>"we are in a good condition" | Confirmed resolution after seeking customer-report data from support, then closed with a clear statement. |

## Summary
- Strong at launching concurrent investigations with clear functional owners (dev, platform/infra, security, app logs).
- Assessed impact and scope, but the earliest asks were vague; tighten the first impact request to be specific (regions, error rates, % failures).
- Missed customer-facing comms; proactively trigger a status page/banner or holding page early to set expectations.
- Weak timeboxing and cadence; set explicit deadlines (e.g., “report back in 5 minutes”) and post periodic summaries to maintain structure.
- Improve technical rigor by directing explicit checks of recent deployments/flags and requesting reproducible evidence (screenshots, timestamps, query IDs).
