# Conformance Run Report — icam-temporal-derivation (candidate v0.3, pre-merge)

**Runner** RTTP & IQA operator-written runner (`icam-runner/icam_runner.py`) · **Date** 2026-11-08 · **Status** 24/24 agree · 6/6 mutants killed (exit 0)

**Frozen input** `vendor/vectors.json` · sha256 `2129f7a50a3ba4099a92f1cedd45e630521c3da3e6a390a3059c9c6dd6f8f61b` · all 7 candidate files checksum-verified 6/6 against the candidate's own `CHECKSUMS.sha256` before anything ran

## Provenance

Operator-written Python implementation (stdlib-only). Rules derived from the published draft text — `draft-li-rttp-iqa-addressing-02`, §§6.1 / 6.3 / 7.2, pinned by TXT sha256 `02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044`, byte-verified against the vendor-pinned value in the candidate's own CANDIDATE.md. The candidate's input and result vocabulary is adopted only as the interface contract; no candidate code is imported or executed by the runner. The advisory `supplied_boundary_classification` is never consulted — the candidate's negative controls exist to punish exactly that. Corpus: lab [PR #218](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/218), head `72a0f72` (pre-merge), vendored frozen under `vendor/`, re-verified byte-identical on 2026-11-08.

## Classification (lab vocabulary)

Stated rather than smoothed over, per the lab's [CONTRIBUTING.md](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/blob/main/CONTRIBUTING.md): the vectors and claim inputs are entirely the candidate author's (Nika Novak, danyka-icam); the implementation that supplies the recomputation is ours. This is a Mode B record with non-author vectors — it does not claim the lab's `independent` label on the implementation axis, because the runner itself decides the semantic results it checks. The candidate harness reproduction below is a thin invocation of an implementation we did not author. Its value is the cross-oracle agreement: two implementations derived from the same published text answering the same 24 questions identically.

## Declared claim set

- Claimed: that an operator-written implementation, derived from the pinned draft text and independent of the candidate's oracle, agrees with every expectation the candidate states — at the oracle level, over the candidate's own frozen vectors.
- Not claimed: conformance certification of any runtime; HMAC, structure, identity, standing, or authority verification. A pass of the isolated wire time gate is not an accepted frame.

## What was run (two layers, separately scored)

| Verification claim | Runner | Mode | Label (lab vocabulary) | Result |
|---|---|---|---|---|
| candidate harness reproduction | `check.py` / `mutate.py` / `metamorphic.py` (run as-is, unchanged) | thin invocation | independent (implementation not ours) | 24/24 fixtures · 8/8 mutants · 120 metamorphic · checksums 6/6 · exit 0 |
| draft-rule recomputation | `icam_runner.py` (this package) | B — alternate recomputation | non-author vectors; implementation ours (see Classification) | 24/24 agree · own battery 6/6 killed · exit 0 |

## Mutation battery — independent, 6/6 killed, none survived

Ours, distinct from the candidate's author-produced 8 (reproduced as-is above):

| Mutant (independent battery) | Killed by |
|---|---|
| `always-expired` | TD-B01, TD-B02, TD-B04, TD-N02, TD-N04, TD-N06, TD-X01, TD-X03, TD-X04, TD-X05, TD-X06, TD-B07 |
| `always-fresh` | TD-B03, TD-B05, TD-B06, TD-N01, TD-N03, TD-N05, TD-X02, TD-X03, TD-X04, TD-X05, TD-X06, TD-B08 |
| `hardcoded-120s-window` | TD-B03, TD-B05, TD-B06, TD-N01, TD-N03, TD-N05, TD-X02, TD-X03, TD-X06, TD-B07, TD-B08 |
| `trusts-advisory-flag` | TD-N01, TD-N02, TD-N03, TD-N04, TD-X04, TD-X06, TD-B08 |
| `undeclared-boundary-inclusive` | TD-X03 |
| `wire-gate-rejects-equality` | TD-B01, TD-B02, TD-B03, TD-B04, TD-B05, TD-B06, TD-N01, TD-N02, TD-N03, TD-N04, TD-N05, TD-N06, TD-X01, TD-X02, TD-X03, TD-X06, TD-W02, TD-W04, TD-B07, TD-B08 |

## Exit status

The process exit code is `0` only when every vector agrees and every mutant in the independent battery is killed, and `1` otherwise.

## Negative-path self-check (executed, not asserted)

Findings on the corpus: none — zero failed checks, no suspected defective vector. Operator-side finding (resolved before recording): the first draft of the independent runner ordered the invalid-convention precondition check after the time comparison; case TD-X06 (expected `invalid_convention`) caught the defect on the first execution — the check was moved before any time comparison and the recorded run is the fixed implementation. The negative-path machinery fired for real, which is what it is for.

## Determinism and cost

Fresh reruns produce byte-identical output; the recorded output (`run-output.json`, sha256 `e6f7c7409126842c94ab00580db93be8ef946c0b7e65c476fa9e727d9d9f7873`) was re-verified byte-for-byte in isolated reruns on 2026-11-08. Full run cost: sub-second, offline, standard library only.

## Report metadata (per the lab's required report fields)

| field | value |
|---|---|
| who ran it | ShaoBao Li (Lee) ([@Aicent-com](https://github.com/Aicent-com)); repository maintained under the [@Aicent-Stack](https://github.com/Aicent-Stack) org |
| date | 2026-11-08 |
| run mode | B — alternate recomputation; non-author vectors (see Classification) |
| implementation name | `icam_runner.py` (RTTP & IQA operator-written runner), stdlib-only |
| implementation repo and commit | https://github.com/Aicent-Stack/conformance — `icam-runner/`; the code-as-run identity of this record is the sealed cut `icam-runner-20261108a.tar.gz` (sha256 in Archive of record); the GitHub commit pin postdates the seal, as in the rev-c precedent |
| corpus reference | icam-temporal-derivation candidate, lab [PR #218](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/218) head `72a0f72` (pre-merge); all 7 files checksum-verified 6/6 against the candidate's own manifest |
| per-vector result | table below (24/24 agree, uncut) |
| verbatim command and output | below, uncut |
| environment | Python 3.14.2, Windows 11 (10.0.26300), win32; standard library only — no third-party packages, no network during verification |
| author-produced or independent | Mode B with non-author vectors: no vector or claim input is ours; the recomputation implementation is (see Classification) |
| suspected defective vectors | none observed |

## Per-vector results (24/24 agree, uncut)

| Case | Layer | Status | Expected | Observed |
|---|---|---|---|---|
| TD-B01 | reliance/normative | agree | `fresh` | `fresh` |
| TD-B02 | reliance/normative | agree | `fresh` | `fresh` |
| TD-B03 | reliance/normative | agree | `expired` | `expired` |
| TD-B04 | reliance/normative | agree | `fresh` | `fresh` |
| TD-B05 | reliance/normative | agree | `expired` | `expired` |
| TD-B06 | reliance/normative | agree | `expired` | `expired` |
| TD-N01 | reliance/normative | agree | `expired` | `expired` |
| TD-N02 | reliance/normative | agree | `fresh` | `fresh` |
| TD-N03 | reliance/normative | agree | `expired` | `expired` |
| TD-N04 | reliance/normative | agree | `fresh` | `fresh` |
| TD-N05 | reliance/normative | agree | `expired` | `expired` |
| TD-N06 | reliance/normative | agree | `fresh` | `fresh` |
| TD-X01 | reliance/normative | agree | `fresh` | `fresh` |
| TD-X02 | reliance/normative | agree | `expired` | `expired` |
| TD-X03 | reliance/interpretive | agree | `boundary_undetermined` | `boundary_undetermined` |
| TD-X04 | reliance/local_precondition | agree | `insufficient_input` | `insufficient_input` |
| TD-X05 | reliance/local_precondition | agree | `insufficient_input` | `insufficient_input` |
| TD-X06 | reliance/local_precondition | agree | `invalid_convention` | `invalid_convention` |
| TD-W01 | wire_time_gate_only/normative | agree | `time_gate_pass` | `time_gate_pass` |
| TD-W02 | wire_time_gate_only/normative | agree | `time_gate_pass` | `time_gate_pass` |
| TD-W03 | wire_time_gate_only/normative | agree | `time_gate_reject` | `time_gate_reject` |
| TD-W04 | wire_time_gate_only/normative | agree | `time_gate_pass` | `time_gate_pass` |
| TD-B07 | reliance/normative | agree | `fresh` | `fresh` |
| TD-B08 | reliance/normative | agree | `expired` | `expired` |

## Verbatim command and output (uncut)

Whole-session console recording — the candidate's three scripts as-is, then the independent runner:

```
$ python3 -I check.py vectors.json
PASS TD-B01 [reliance/normative] expected=fresh actual=fresh
PASS TD-B02 [reliance/normative] expected=fresh actual=fresh
PASS TD-B03 [reliance/normative] expected=expired actual=expired
PASS TD-B04 [reliance/normative] expected=fresh actual=fresh
PASS TD-B05 [reliance/normative] expected=expired actual=expired
PASS TD-B06 [reliance/normative] expected=expired actual=expired
PASS TD-N01 [reliance/normative] expected=expired actual=expired
PASS TD-N02 [reliance/normative] expected=fresh actual=fresh
PASS TD-N03 [reliance/normative] expected=expired actual=expired
PASS TD-N04 [reliance/normative] expected=fresh actual=fresh
PASS TD-N05 [reliance/normative] expected=expired actual=expired
PASS TD-N06 [reliance/normative] expected=fresh actual=fresh
PASS TD-X01 [reliance/normative] expected=fresh actual=fresh
PASS TD-X02 [reliance/normative] expected=expired actual=expired
PASS TD-X03 [reliance/interpretive] expected=boundary_undetermined actual=boundary_undetermined
PASS TD-X04 [reliance/local_precondition] expected=insufficient_input actual=insufficient_input
PASS TD-X05 [reliance/local_precondition] expected=insufficient_input actual=insufficient_input
PASS TD-X06 [reliance/local_precondition] expected=invalid_convention actual=invalid_convention
PASS TD-W01 [wire_time_gate_only/normative] expected=time_gate_pass actual=time_gate_pass
PASS TD-W02 [wire_time_gate_only/normative] expected=time_gate_pass actual=time_gate_pass
PASS TD-W03 [wire_time_gate_only/normative] expected=time_gate_reject actual=time_gate_reject
PASS TD-W04 [wire_time_gate_only/normative] expected=time_gate_pass actual=time_gate_pass
PASS TD-B07 [reliance/normative] expected=fresh actual=fresh
PASS TD-B08 [reliance/normative] expected=expired actual=expired
SUMMARY 24/24 agree; author-produced fixture consistency only

$ python3 -I mutate.py
KILLED trust-unverified-boundary-flag by TD-N01,TD-N02,TD-N03,TD-N04,TD-N06,TD-X04,TD-X05,TD-X06,TD-B08
KILLED always-fresh-at-equality by TD-B05,TD-N03,TD-X03
KILLED always-expired-at-equality by TD-B02,TD-N04,TD-X03
KILLED reversed-time-order by TD-B01,TD-B03,TD-B04,TD-B06,TD-N01,TD-N02,TD-N05,TD-N06,TD-X01,TD-X02,TD-X06,TD-B07,TD-B08
KILLED assume-inclusive-undeclared by TD-X03
KILLED missing-clock-fails-open by TD-X04
KILLED missing-expiry-fails-open by TD-X05
KILLED wire-frame-equality-rejected by TD-W02,TD-W04
SUMMARY 8/8 mutants killed (author-produced)

$ python3 -I metamorphic.py
PASS 120 flag-substitution invariance checks; equality wire-time gate separate (author-produced)

$ python3 -I icam_runner.py candidate/vectors.json run-output.json   (independent runner)
PASS TD-B01 [reliance/normative] expected=fresh                  observed=fresh                  
PASS TD-B02 [reliance/normative] expected=fresh                  observed=fresh                  
PASS TD-B03 [reliance/normative] expected=expired                observed=expired                
PASS TD-B04 [reliance/normative] expected=fresh                  observed=fresh                  
PASS TD-B05 [reliance/normative] expected=expired                observed=expired                
PASS TD-B06 [reliance/normative] expected=expired                observed=expired                
PASS TD-N01 [reliance/normative] expected=expired                observed=expired                
PASS TD-N02 [reliance/normative] expected=fresh                  observed=fresh                  
PASS TD-N03 [reliance/normative] expected=expired                observed=expired                
PASS TD-N04 [reliance/normative] expected=fresh                  observed=fresh                  
PASS TD-N05 [reliance/normative] expected=expired                observed=expired                
PASS TD-N06 [reliance/normative] expected=fresh                  observed=fresh                  
PASS TD-X01 [reliance/normative] expected=fresh                  observed=fresh                  
PASS TD-X02 [reliance/normative] expected=expired                observed=expired                
PASS TD-X03 [reliance/interpretive] expected=boundary_undetermined  observed=boundary_undetermined  
PASS TD-X04 [reliance/local_precondition] expected=insufficient_input     observed=insufficient_input     
PASS TD-X05 [reliance/local_precondition] expected=insufficient_input     observed=insufficient_input     
PASS TD-X06 [reliance/local_precondition] expected=invalid_convention     observed=invalid_convention     
PASS TD-W01 [wire_time_gate_only/normative] expected=time_gate_pass         observed=time_gate_pass         
PASS TD-W02 [wire_time_gate_only/normative] expected=time_gate_pass         observed=time_gate_pass         
PASS TD-W03 [wire_time_gate_only/normative] expected=time_gate_reject       observed=time_gate_reject       
PASS TD-W04 [wire_time_gate_only/normative] expected=time_gate_pass         observed=time_gate_pass         
PASS TD-B07 [reliance/normative] expected=fresh                  observed=fresh                  
PASS TD-B08 [reliance/normative] expected=expired                observed=expired                
SUMMARY 24/24 agree (independent runner, non-author-produced)
MUTANT trusts-advisory-flag           killed by TD-N01,TD-N02,TD-N03,TD-N04,TD-X04,TD-X06,TD-B08
MUTANT always-fresh                   killed by TD-B03,TD-B05,TD-B06,TD-N01,TD-N03,TD-N05,TD-X02,TD-X03,TD-X04,TD-X05,TD-X06,TD-B08
MUTANT always-expired                 killed by TD-B01,TD-B02,TD-B04,TD-N02,TD-N04,TD-N06,TD-X01,TD-X03,TD-X04,TD-X05,TD-X06,TD-B07
MUTANT wire-gate-rejects-equality     killed by TD-B01,TD-B02,TD-B03,TD-B04,TD-B05,TD-B06,TD-N01,TD-N02,TD-N03,TD-N04,TD-N05,TD-N06,TD-X01,TD-X02,TD-X03,TD-X06,TD-W02,TD-W04,TD-B07,TD-B08
MUTANT undeclared-boundary-inclusive  killed by TD-X03
MUTANT hardcoded-120s-window          killed by TD-B03,TD-B05,TD-B06,TD-N01,TD-N03,TD-N05,TD-X02,TD-X03,TD-X06,TD-B07,TD-B08
MUTATION SUMMARY 6/6 killed (independent battery)
run output written: E:\WEB\_deploy\_icam_1108\icam-runner\run-output.json
```

## Archive of record

The complete artifact (runner, vendored candidate inputs, recorded outputs) is pinned and organ-sealed: `icam-runner-20261108a.tar.gz` (11,996 bytes), sha256 `698dfa08223565fd1424984f894ddd7d000a456ed18877c5023f86dc166630e2` — [download](https://iqa.org/conformance/files/icam-runner-20261108a.tar.gz). The artifact carries two addresses derived from its own digest — one per sister scheme: [`rttp://698dfa08.conformance.iqa`](https://rttp.com/open/?uri=rttp://698dfa08.conformance.iqa) (the question, WHERE+WHEN) and [`iqa://698dfa08223565fd1424984f894ddd7d.forge.iqa`](https://iqa.org/open/?uri=iqa://698dfa08223565fd1424984f894ddd7d.forge.iqa) (the answer, WHETHER — the exact organ-sealed subject). Appended to the release-attestations bundles as version `2026-11-08-icam-run`, dual-site byte-identical at [iqa.org/attestations/](https://iqa.org/attestations/) and [rttp.com/attestations/](https://rttp.com/attestations/). Full report page: [iqa.org/conformance/icam-runner/](https://iqa.org/conformance/icam-runner/). The copy of this report inside the sealed tarball is the measurement-event snapshot; this repository copy is the living document (classification wording aligned 2026-11-08 with the lab's vocabulary; verbatim output embedded) — a digest cannot appear inside the bytes it hashes.

## Citation

- Runner: `icam_runner.py` — https://github.com/Aicent-Stack/conformance (`icam-runner/`)
- Operator: Lee / Aicent Stack (ShaoBao Li, @Aicent-com), RTTP CRI 27 · IQA CRI 28
