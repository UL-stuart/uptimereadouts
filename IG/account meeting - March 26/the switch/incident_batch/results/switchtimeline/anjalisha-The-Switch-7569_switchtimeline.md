# anjalisha-The-Switch-7569.csv

| Milestone | Time | Evidence | Rationale |
|---|---|---|---|
| Issue Reproduction | T+1 | "i tried placing an order it is working for me" | PLAYER explicitly tested the site by placing an order, satisfying reproduction. |
| Incident Raised | T+8 | "*Incident Number INC100067:* SEV3 reports of long load times" | The incident record was formally created by uptimelabs. |
| Checks Recent Changes | T+5 | "@daniel no recent changes seems to be related to this kind of issues"<br>"there was changes to frontend and payments CHG89675 and CHG89692"<br>"can @daniel and @tanya check if it is change related?" | PLAYER initiated and followed up on recent change checks, meeting the requirement. |
| First Business Comms | T+8 | "we have experienced long load times, we are still investigating the cause" | This is PLAYER’s first substantive message in business-comms after the incident was raised. |
| Scope & Impact Sizing | T+6 | "@bob any reports from customers?" | PLAYER sought customer impact information, starting scope/impact sizing. |
| Network Layer Identification | T+14 | "Noticing a spike in outbound connections."<br>"Security scan shows issues related to our network switch" | After the spike was observed, focus shifted explicitly to the network switch, indicating a move to the network layer. |
| Security Breach Diagnosis | T+16 | "The network switch's vulnerabilities were exploited." | Maya confirmed the switch had exploitable vulnerabilities consistent with the team’s botnet/DDOS findings. |
| Intervention Decision: Restart Switch | T+20 | "switch has been restarted" | Maya explicitly stated the restart, fulfilling the decision and action. |
| Intervention Decision: Failover to Redundant Switch | – | – | No explicit failover decision stated by Maya; she acknowledged "That should work" to Tanya’s suggestion but did not direct the action. |
| Resolution | T+24 | "the infected switch has been successfully changed over" | Maya confirmed successful changeover to the redundant switch, indicating resolution. |

## Summary
- Not detected: Intervention Decision: Failover to Redundant Switch (no explicit directive from Maya).
- Ambiguity: Maya endorsed the failover (“That should work”) but did not clearly issue the decision; the action was proposed by Tanya and executed by Hamed.
- Improvement: Encourage explicit, authoritative decision statements from the responsible owner (e.g., “Proceed to fail over to the redundant switch now”) and time-stamping of such directives for clear accountability.
