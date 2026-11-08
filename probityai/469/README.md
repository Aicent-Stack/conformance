# 469 — principal standing rows PS1, PS2 and PS1b

PR by the venue ([probityai/agent-evidence-vectors#469](https://github.com/probityai/agent-evidence-vectors/pull/469)),
opened 2026-11-06T20:24:08Z, **merged 2026-11-06T23:16:39Z** (refs #412).

What it does (see [`PR-RECORDS.md`](PR-RECORDS.md) for the venue's verbatim text): adds rows PS1 and PS2 of
Appendix B of draft-gilda-audit-agent-audit-record-03 to the agent audit record corpus, plus the boundary
member `PS1b` beside them. The records were contributed by Wes Jackson (@wjatx) in #412; the boundary case
was raised by Girish Konda on the WIMSE thread.

Relation to our thread: `PS1b` is the case the venue matched to **Record 5 of #453** — see
[`../453/`](../453/). It is indeterminate between draft-jackson-wimse-evaluation-05 (an input at or past
its horizon is forbidden) and draft-gilda-audit-agent-audit-record-03 as filed (FR2: an age equal to
`maxAge` is fresh); the venue's reference reader keeps -03's boundary. This mirrors our lease-boundary
family's declared-convention reading: the record alone cannot decide the instant — see the
`aicent-lease-boundary` family page at https://iqa.org/conformance/aicent-lease-boundary/.
