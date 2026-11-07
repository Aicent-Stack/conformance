# icam-runner

Independent (non-author-produced) runner for the **icam-temporal-derivation**
candidate (lab PR #218, head `72a0f72`), built and run by Aicent Stack.

- Operator: ShaoBao Li (Lee) / Aicent Stack (RTTP CRI 27 / IQA CRI 28)
- Normative basis: draft-li-rttp-iqa-addressing-02, sections 6.1 / 6.3 / 7.2
  (TXT sha256 02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044),
  byte-verified against the vendor-pinned value in the candidate's own
  CANDIDATE.md
- Result: 24/24 vectors agree with the candidate's expectations; independent
  mutation battery 6/6 killed; two layers kept separate (18 DERIVE, 4
  WIRE_TIME_GATE, 2 nondefault-window)

## Run

```
python3 -I icam_runner.py vendor/vectors.json run-output.json
```

Exit 0 means every vector agrees and every mutant in the independent battery
is killed. A rerun must reproduce the recorded `run-output.json` byte for
byte; the payload also embeds the sha256 of every frozen file under
`vendor/`, so any drift in the vendored candidate inputs breaks the replay.

`SHA256SUMS.txt` pins the package files. `run-output.txt` is the whole-session
console recording; `ENVIRONMENT.txt` records the run environment. See
`RUN-REPORT-2026-11-08.md` for scope and limitations. This is an independent
run record, not a merge vote; the lab certifies nothing and maintainer
decisions at the lab are separate from this record.
