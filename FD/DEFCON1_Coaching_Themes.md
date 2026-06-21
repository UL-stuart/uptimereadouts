# DEFCON 1 — Coaching Themes for the Pair (Shea Hoey & Joseph Patterson)

Three patterns emerge across *both* ICs in the DEFCON 1 runs (9314 and 9300) — not just in one. That's what makes them worth coaching as a pair rather than individually.

## 1. Neither names the frame shift out loud — they relay the model instead of reframing it

The DEFCON 1 arc has two hinge points: *load/infra → deliberate attack*, and *contain → restore*. At both, Maya and Tanya did the cognitive work and the ICs passed it along rather than capturing it as a decisive, shared reframe.

- Shea kept probing the dead theory: after Tanya's clear disconfirmation at T+7 ("this does not behave like a platform problem… even I tried scaling up, still seeing the spike"), he was still asking "Can we add more space to that" at T+8. When Maya confirmed ransomware at T+13, his reply was a question — "So it was an attack?" — not a broadcast.
- Joseph framed the early picture well but at the confirmation moment his energy went into a (strong) business update; the internal pivot was left implicit. The team reoriented around Maya, not around an IC-stated frame.

**Focus:** when a responder confirms or kills a theory, make the very next move a one-line reframe to the whole team — "Update: Tanya's ruled out load. We're treating this as a deliberate security event now. Maya owns diagnosis — everyone reorient." It costs one message and gives the team a shared checkpoint instead of drifting on the old hypothesis.

## 2. Neither has a reliable habit of routing irreversible actions through the domain owner before they fire

This is the highest-leverage one because it's where real damage happened — and the pair is instructive precisely because they *diverged* on outcome but share the underlying weakness.

- Joseph ordered "@tanya please kill the script" (T+20) under pressure from Shay and Tanya, *before* the security lead weighed in. Ransom doubled to $10M (T+21); Maya's "killing the script could make things worse" landed at T+22 — too late.
- Shea hit the identical pressure (Shay: "We must get this script killed asap", T+13) but routed it — "Can we check if this is a real attack maya" — and Maya said "Do not kill the script!" Good outcome. But Shea *also* floated unilateral high-risk suggestions of his own ("Can we unencrypt the file", "reboot the server") that would have been just as damaging had the team acted on them.

So it's not "Shea good, Joseph bad" — Shea's better result was partly that Maya re-engaged before the kill in his run. Neither IC has the *habit*; one got away with it.

**Focus:** a standing rule that any irreversible containment step — kill, restart, delete, wipe, failover — gets a named-owner check before execution. The move under floor pressure is to surface the open question to the responsible lead, not to authorise (Joseph) or improvise (Shea): "Maya, before we touch it — snapshot-first or kill-first?"

## 3. Both under-use structured *internal* current-state broadcasts

Joseph is genuinely strong at structured, quantified updates — but he points that discipline *outward* at the business channel and runs the internal channel as task directives. Shea hasn't built the habit in either direction; his internal comms are reactive one-liners ("Is everyone looking into this issue?", "Do we have anything running twice?").

**Focus:** both adopt a periodic internal broadcast in the format your strongest performer (Seth L) used — "SEV-X · current situation · current action · next update in X". For Joseph that's porting an existing skill inward; for Shea it's building it from scratch. It's the practical mechanism that makes Theme 1 happen on a cadence rather than only at crises.

---

**Through-line for the pair:** the IC's job here was to capture and broadcast the team's shared model and broker the high-consequence calls through their owners — and both did the brokering-to-business well (ransom, restore approval) but not the brokering-of-technical-containment or the internal narration.
