# shreyarao-The-Switch-7719.csv

| Milestone | Time | Evidence | Rationale |
|---|---|---|---|
| Issue Reproduction | T+1 | "im able to place an order" | PLAYER explicitly attempted the website flow to reproduce the issue. Confirms reproduction by performing an order. |
| Incident Raised | T+4 | "*Incident Number INC100011:* sev3 Issues with late loading of site and placing orders" | uptimelabs created the incident record; this is the first such entry after T₀. |
| Checks Recent Changes | T+2 | "@shay can i get the list of chages that recently went through?" | PLAYER proactively requested recent change details to assess regressions. This aligns with checking the changelog/changes. |
| First Business Comms | T+5 | "Hello @bez , We are looking into this issue, so far the issue is not widespread amongst customers. will update you" | This is PLAYER’s first non-incident-number message in business-comms, providing status to the business. |
| Scope & Impact Sizing | T+1 | "@bob  is there any issue noticed so far from customers perspective?" | PLAYER sought customer impact data to size scope and severity. This directly targets business/customer effect. |
| Network Layer Identification | T+11 | "Noticing a spike in outbound connections."<br>"Security scan shows issues related to our network switch." | After a spike was observed, the investigation focused on the network switch, indicating a shift to network layer components. |
| Security Breach Diagnosis | T+13 | "Security scan shows issues related to our network switch."<br>"The network switch's vulnerabilities were exploited." | Maya confirms exploited vulnerabilities on the switch; combined with team inputs, this establishes the compromised network device diagnosis. |
| Intervention Decision: Restart Switch | – | – | No message from Maya indicating the switch was restarted. In fact, restart was discouraged. |
| Intervention Decision: Failover to Redundant Switch | T+16 | "Your right restarting the switch isnt the best option as it might intruduce some more issues"<br>"We have a redundant switch; we could failover to it!" | Maya rejects restart and proposes failover to the redundant switch, meeting the specified decision criteria. |
| Resolution | T+20 | "the infected switch has been successfully changed over" | Maya confirms the switch changeover, indicating service restoration. |

## Summary
- Not detected: Intervention Decision: Restart Switch
- Ambiguities: The 10.50.0.0/24 block was not explicitly cited; network-layer focus was inferred from “spike in outbound connections” and switch scan results. Botnet/DDOS specifics were stated by Hamed, while Maya confirmed exploited switch vulnerabilities.
- Improvement insights: Encourage stating the full diagnosis (including botnet/DDOS) in a single authoritative message from Maya for clarity. Consider including explicit network/IP scope details when first identifying the network layer to tighten scoping.
