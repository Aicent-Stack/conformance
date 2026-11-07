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
`RUN-REPORT-2026-11-08.md` for scope, limitations, and the classification note.
This is a run record by a non-author operator, not a merge vote; the lab
certifies nothing and maintainer decisions at the lab are separate from this
record.

## Report page and sealed artifact

Full report: [iqa.org/conformance/icam-runner/](https://iqa.org/conformance/icam-runner/).

The measurement is sealed per the IQA release discipline:

- Tarball: `icam-runner-20261108a.tar.gz` (11,996 bytes), sha256
  698dfa08223565fd1424984f894ddd7d000a456ed18877c5023f86dc166630e2 —
  [download](https://iqa.org/conformance/files/icam-runner-20261108a.tar.gz)
- Dual addresses: `rttp://698dfa08.conformance.iqa` ·
  `iqa://698dfa08223565fd1424984f894ddd7d.forge.iqa` — resolvable through the
  public resolvers ([rttp.com/open/](https://rttp.com/open/) ·
  [iqa.org/open/](https://iqa.org/open/))
- Bundle: version `2026-11-08-icam-run`, appended to the release-attestations
  bundles, dual-site byte-identical at
  [iqa.org/attestations/](https://iqa.org/attestations/) and
  [rttp.com/attestations/](https://rttp.com/attestations/)

## Citation

- Runner: `icam_runner.py` — https://github.com/Aicent-Stack/conformance (`icam-runner/`)
- Operator: Lee / Aicent Stack (ShaoBao Li, @Aicent-com), RTTP CRI 27 · IQA CRI 28
