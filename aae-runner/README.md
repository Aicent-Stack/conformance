# aae-runner — independent run record (moltycel-aae-vectors, AAE)

This directory is the in-repository copy of the sealed artifact for our
independent run of the `moltycel-aae-vectors` candidate family (AAE),
authored by Lars Kersten Kroehl (MoltyCel) and merged into the
Agent-Authority-Conformance lab as PR #190.

What happened: following the merge of #190, we ran the candidate's own
pipeline unmodified, as independent operators — 47/47 vectors, 11/11
negative controls, 14/14 unit tests, byte-reproducible output, exit 0.
The candidate's CANDIDATE.md line "No independent run exists yet" is
thereby closed.

Scope: this run covers the candidate's native, enforce and composition
vector sets and the 11 negative controls at source `6bb462f` (published
23 October). The 42 resume vectors and the Python and TypeScript
conformance runners added to the source repository after 23 October are
outside this record; no independent run of those exists yet.

Contents:

- `ENVIRONMENT.txt` — the environment the run was performed in
- `run-output.txt` — the recorded output of the run
- `moltycel-aae-vectors/` — the candidate frozen at commit `6bb462f`,
  vendored byte-for-byte with no modification (see its NOTICE)
- `SHA256SUMS.txt` — digest manifest over the above; CI verifies every
  entry (tests/digest_integrity.py). The manifest here is a path-adapted
  copy of the sealed manifest (which pins paths relative to the extraction
  root); the file bytes and every digest are identical.

Pointers:

- Full report: https://iqa.org/conformance/aae-runner/
- Sealed artifact of record: `aae-runner-20261104a.tar.gz`
  (SHA-256 `5dd92d2729c90932…`), at
  https://iqa.org/conformance/files/aae-runner-20261104a.tar.gz
- Lab interop record: PR #215, merged 2026-11-04
  (https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/215)
- Run date: 2026-11-04 (UTC+8) · operator: Lee / Aicent Stack
  (RTTP, CRI scheme number 27 · IQA, CRI scheme number 28)

This run verifies the vectors, not the spec.


## Replay

```
sh moltycel-aae-vectors/run.sh
```

Requires git, python3 (3.9+) and the pip packages recorded in
`ENVIRONMENT.txt` (cryptography, jsonschema, jcs, pytest). The clone step is
the only network step; every verification after it runs offline behind the
candidate's audit hook. CI replays this pipeline on every push and compares
the fresh output with `run-output.txt` (byte-identical modulo the pytest
elapsed-time figure).
