# Pipeline replay — grant-ref-replay-sparysh (external reading 1 on aicent-grant-ref)

This directory records **our pipeline replay** of a merged lab record: `sparysh-reading-aicent-grant-ref-20186f3` in [Agent-Authority-Conformance/aps-conformance-suite](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/tree/main/interop/sparysh-reading-aicent-grant-ref-20186f3) (merged via [PR #234](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/234), 2026-11-17T20:40:28Z, merge commit `dbf9c245ecca1636344dc7f2e23af7dd8844f58d`). That record is an outside reading of our vector family `aicent-grant-ref` (revision 1) carried out by **Andrii Sparysh** (GitHub `andreysparish`) from sections 8.1–8.2 of `draft-li-rttp-iqa-addressing-02`: a phase-1 checker written from the draft text, run blind over a shuffled copy of the 25 cases, then compared against the family's expected verdicts. The lab's classification, which we adopt verbatim: the run was **blind to the candidate's expected results**, and its semantic verdicts are labeled **author-produced Mode B because Andrii wrote the checker** (`reader/check_reader.py`) — a reading record, not a certification, not an independent run. The merged lab entry is the source of record; this directory is a replay of it, not a second opinion.

The replay is our hub-card commitment fulfilled: once the record merged, we ran it through our own pipeline and published the complete report page at [iqa.org/conformance/grant-ref-replay-sparysh/](https://iqa.org/conformance/grant-ref-replay-sparysh/). The operator of this replay is ShaoBao Li (Lee) / Aicent Stack — the family's author and the author of the pinned draft, who wrote none of the reading record's checker, comparison script, ambiguity log, or findings.

## What the replay does

The generic thin wrapper [`replay/replay-runner/replay_runner.py`](../replay-runner/replay_runner.py) reads `profile.json` in this directory and:

1. verifies the seven vendor pins (the record's checker and comparison script as run, the pinned draft, the frozen blind copy, and the candidate's sealed vectors, description and id-map) — byte-exact against the digests the record itself publishes; any mismatch aborts before anything executes;
2. executes the record's two commands exactly as the record's run report specifies (`check_reader.py` over the draft and blind copy, then `compare.py` over the produced phase-1 output, the sealed vectors and the id-map);
3. compares every produced output against the record's recorded bytes — byte-identical modulo line endings plus canonical JSON equality, all three recorded artifacts (`phase1.json`, `phase1-sensitivity.json`, `final.json`);
4. asserts the recorded summary (verdict agreement 25/25, zero part divergences, tally 2/11/12) and fails closed on any deviation.

The wrapper adds no verdict logic of its own — the checker that supplies the verdicts is the record's own `check_reader.py`, executed as code-as-run. This record knows nothing that the merged lab record does not publish.

## Result

Exit 0, `status: replay_matched`. All 7 vendor pins and all 3 recorded pins verified; both commands exit 0 with stdout exactly as the record's run report transcribed it (`{"ambiguous": 2, "conformant": 11, "nonconformant": 12}`); all three produced outputs are byte-identical to the recorded artifacts after line-ending normalization (Windows CRLF during recording, LF on Linux) and canonically equal as JSON; the recorded comparison itself reproduces verdict agreement 25/25 and zero named-part divergences. The replay reproduces the record; it does not re-judge it — the value of the match is that the record's bytes are what the record says they are, executable by anyone offline.

## Re-run

From the repository root:

```
python3 -I replay/replay-runner/replay_runner.py replay/grant-ref-replay-sparysh rerun-output.json
cmp rerun-output.json replay/grant-ref-replay-sparysh/run-output.json
```

Expected output begins with `VENDOR PIN OK 7/7 (profile.json vendor_pins)` and ends with `REPLAY ok: sparysh-reading-aicent-grant-ref-20186f3 reproduced (pins 7, commands 2, outputs 3)`, exit status 0. The replay is deterministic: the machine-readable output carries no timestamps and no paths, and a rerun must reproduce the committed `run-output.json` byte for byte. The full console output of the recorded replay is preserved verbatim in `run-output.txt`.

## Files

- `profile.json` — the replay profile: pins, commands, expected summary (machine-readable)
- `run-report.md` — the replay report (scope, method, results, limitations)
- `PROVENANCE.md` — operator, mode, authorship relationships, environment
- `RESULTS.md` — per-case results, transcribed from the record's own comparison output
- `run-output.json` — the machine-readable record of the replay
- `run-output.txt` — the complete console output of the recorded replay, uncut
- `ENVIRONMENT.txt` — the replay environment
- `vendor/` — the frozen external material as run: the record's checker and comparison script, the pinned draft, the blind copy, the candidate's sealed vectors, description and id-map
- `recorded/` — the record's own recorded outputs (the comparison targets)
- `SHA256SUMS.txt` — digests of the accompanying files
