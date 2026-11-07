# RUN REPORT — icam-runner over icam-temporal-derivation (lab PR #218)

- Date: 2026-11-08
- Runner: `icam_runner.py` — operator-written, independent of the candidate's oracle (rules
  derived from the published draft text, not from the candidate's `check.py`)
- Operator: ShaoBao Li (Lee) / Aicent Stack (RTTP CRI 27 / IQA CRI 28)
- Candidate under test: icam-temporal-derivation, lab PR #218, head `72a0f72` (pre-merge)
- Normative basis: draft-li-rttp-iqa-addressing-02, sections 6.1 / 6.3 / 7.2,
  TXT sha256 02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044
  (byte-verified against the vendor-pinned value in the candidate's own CANDIDATE.md)

## Classification (lab vocabulary)

Stated rather than smoothed over, per the lab's
[CONTRIBUTING.md](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/main/CONTRIBUTING.md):
the vectors and claim inputs are entirely the candidate author's (Nika Novak, danyka-icam); the
implementation that supplies the recomputation is ours. This is a Mode B record with non-author
vectors — it does not claim the lab's `independent` label on the implementation axis, because the
runner itself decides the semantic results it checks. The candidate harness reproduction below is
a thin invocation of an implementation we did not author. Its value is the cross-oracle agreement:
two implementations derived from the same published text answering the same 24 questions
identically.

## What was run

1. Candidate harness reproduction (author-produced, run as-is):
   check.py 24/24 agree, exit 0; mutate.py 8/8 mutants killed, exit 0;
   metamorphic.py 120 invariance checks, exit 0; CHECKSUMS.sha256 6/6 verified.
2. Independent runner (this package): rules derived from the published draft
   text (sections 6.1 reliance derivation; 7.2 step 2 wire time gate), the
   candidate's input/result vocabulary adopted only as the interface contract.

## Results (independent runner)

- Vectors: 24/24 agree with the candidate's expectations (18 DERIVE, 4
  WIRE_TIME_GATE, 2 nondefault-window). The advisory
  supplied_boundary_classification field is never consulted by the runner.
- Independent mutation battery (ours, distinct from the candidate's): 6/6
  killed — trusts-advisory-flag, always-fresh, always-expired,
  wire-gate-rejects-equality, undeclared-boundary-inclusive,
  hardcoded-120s-window.
- Recorded output: run-output.json, sha256
  e6f7c7409126842c94ab00580db93be8ef946c0b7e65c476fa9e727d9d9f7873 (full value also in SHA256SUMS.txt).

## Gates

- Isolated rerun: fresh temp directory, `python3 -I icam_runner.py
  vendor/vectors.json run-output.json`, exit 0.
- Byte replay: rerun output byte-identical to the recorded run-output.json.
- Cross-oracle agreement: independent runner 24/24 and candidate harness
  24/24 against the same frozen vectors.

## Sealed artifact

- Tarball: `icam-runner-20261108a.tar.gz` (11,996 bytes), sha256
  698dfa08223565fd1424984f894ddd7d000a456ed18877c5023f86dc166630e2 —
  [download](https://iqa.org/conformance/files/icam-runner-20261108a.tar.gz)
- Dual addresses: `rttp://698dfa08.conformance.iqa` ·
  `iqa://698dfa08223565fd1424984f894ddd7d.forge.iqa` — resolvable through the
  public resolvers ([rttp.com/open/](https://rttp.com/open/) ·
  [iqa.org/open/](https://iqa.org/open/))
- Bundle: appended to the release-attestations bundles as version
  `2026-11-08-icam-run`, dual-site byte-identical at
  [iqa.org/attestations/](https://iqa.org/attestations/) and
  [rttp.com/attestations/](https://rttp.com/attestations/)
- Report page: [iqa.org/conformance/icam-runner/](https://iqa.org/conformance/icam-runner/)
- Note: the sealed tarball pins the measurement-event snapshot of this report
  (runner, vendored inputs, recorded output). This repository copy is the
  living document — label wording corrected 2026-11-08 against the lab's
  classification vocabulary; the measurement itself is unchanged and the
  recorded output replays byte for byte.

## Scope and limitations

- This is a pre-merge independent run of an unmerged candidate head (72a0f72).
  If the candidate changes before merge, this record pins the head it tested
  and a fresh run would be required for the changed revision.
- The candidate tests its reference oracle and authored expectations; per its
  own CANDIDATE.md no external implementation adapter is included. This run
  closes the independent-verification gap at the oracle level; it is not a
  conformance certification of any runtime.
- A pass of the isolated wire time gate is not an accepted frame: HMAC,
  structure, identity, standing, and authority are outside this scope.
- A recorded run, not a merge vote: maintainer decision at the lab is separate
  from this record (the lab certifies nothing; this is a run record by a
  non-author operator).

## Citation

- Runner: `icam_runner.py` — https://github.com/Aicent-Stack/conformance (`icam-runner/`)
- Operator: Lee / Aicent Stack (ShaoBao Li, @Aicent-com), RTTP CRI 27 · IQA CRI 28
