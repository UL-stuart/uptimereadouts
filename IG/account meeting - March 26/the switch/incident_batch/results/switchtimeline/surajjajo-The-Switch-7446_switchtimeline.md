# surajjajo-The-Switch-7446.csv

| Milestone | Time | Evidence | Rationale |
|---|---|---|---|
| Issue Reproduction | T+1 | "I just tried placing an order and it worked completely fine for me" | PLAYER explicitly attempted to replicate the customer journey on the website. Clear first qualifying reproduction after T₀. |
| Incident Raised | T+4 | "*Incident Number INC10002:* \"Some customers are reporting long load times while placing an order\" SEV-3" | uptimelabs created the formal incident record. This is the earliest post- T₀ incident ticket. |
| Checks Recent Changes | T+5 | "@shay menawhile, can I please get a list of reent changes that went to PROD?" | PLAYER asked for recent production changes to assess regressions. This directly targets recent code/config changes. |
| First Business Comms | T+5 | "nope, only some of them" | This is PLAYER’s first message in business-comms after T₀ and not the incident creation post. It communicates scope to the business channel. |
| Scope & Impact Sizing | T+2 | "@bob are any customers affected by this?"<br>"Do we have any reports?"<br>"@bob could it be regional issue?" | PLAYER probed who is affected, requested report counts, and checked geographic scope, establishing impact and breadth. |
| Network Layer Identification | T+14 | "Noticing a spike in outbound connections."<br>"Security scan shows issues relate to our network switch" | After the outbound spike was noted, the investigation focused on the network switch, indicating a shift to the network/edge layer. |
| Security Breach Diagnosis | T+15 | "Security scan shows issues relate to our network switch"<br>"The network switch's vulnerabilities were exploited." | Maya confirmed a compromised switch via scan results and acknowledged exploited vulnerabilities, matching the breach diagnosis. |
| Intervention Decision: Restart Switch | – |  | No message from Maya indicating a switch restart occurred. |
| Intervention Decision: Failover to Redundant Switch | T+17 | "Your right restarting the switch isnt the best option as it might intruduce some more issues"<br>"I suggest we failover to a redundant switch" | Maya rejected restart and then explicitly recommended failing over to the redundant switch; earliest qualifying decision captured. |
| Resolution | T+24 | "the infected switch has been successfully changed over" | Maya confirmed the failover completion, indicating resolution. |

## Summary
- Not detected: Intervention Decision: Restart Switch
- Notable gaps or ambiguities: No explicit mention of the 10.50.0.0/24 block before shifting to the switch; early acknowledgement of intermittency by PLAYER was brief, but later impact questions were solid. Business-comms updates from PLAYER were terse and could have included clearer status and next steps.
- Improvement insights: PLAYER could proactively summarize scope/impact and owner actions in business-comms earlier. Promptly pushing for concrete network diagnostics (IP ranges, interface stats) might have accelerated the shift to the compromised switch.
