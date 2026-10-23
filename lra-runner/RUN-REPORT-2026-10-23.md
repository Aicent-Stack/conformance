# Conformance Run Report — lease-revocation-axes (revision 2, candidate)

**Runner** RTTP & IQA independent Python runner (`rttp-iqa-runner/lra_runner.py`) · **Date** 2026-10-23 · **Status** `independent_run_matched`

**Frozen input** `fixtures/lease-revocation-axes/revision-2/vectors.json` · sha256 `a0a07ea58bcacfd056cbd648e03de4ff14778aa151e8b5d2574e43e31a111ed8` · digest gate vs pinned `SHA256SUMS.txt`: OK (hard gate — runner refuses to score any vectors whose digest is not pinned)

## Provenance

Independently authored Python implementation. The lab's TypeScript model (PR #180, `verify.ts`/`harness.ts`) was reviewed only as the interface contract; no lab code was reused. All pass/fail comparisons are made against the frozen vectors file and its pinned expected values — never against lab model output. Declaration mapping (`not_claimed` / `not_supported` / `supported`) is frozen before any verifier is constructed.

## Declared claim set

- Claimed axes: `evidence_freshness` · `authority_validity` · `action_authorization`
- Action policy: `P1-current-observation` (zero age tolerance)
- Note: **action-time authorization is not claimed (by design)** — the runner does not assert that an action is authorized at dispatch time; it scores the three declared axes only.

## Baseline: 4 profiles × 12 cases = 48 runs (dual-mode, separately scored)

| Profile | Runs | Calls | Axis comparisons | Composite comparisons | Failures |
|---|---|---|---|---|---|
| `cached_lease` × exclusive | 12 | 44 | 132 | 44 | 0 — matched |
| `cached_lease` × inclusive | 12 | 44 | 132 | 44 | 0 — matched |
| `live_standing_read` × exclusive | 12 | 44 | 132 | 44 | 0 — matched |
| `live_standing_read` × inclusive | 12 | 44 | 132 | 44 | 0 — matched |
| **Total** | **48** | **176** | **528** | **176** | **0** |

Tri-axis result: all three axes scored on every supported comparison; status `matched` on all 48 runs. Per-axis separation preserved end-to-end (a case may pass on `evidence_freshness` while failing composite acceptance — grading kept distinct per the family spec).

## Source-read contract (instrumented, not asserted)

- `cached_lease`: **0** authority reads per call (lease decides from carried evidence)
- `live_standing_read`: exactly **1** instrumented read per unexpired + bound call
- Outage calls: getter returns null, the **attempt is recorded**, diagnostics must be backed by actual reads
- Hostile-call boundary: the runner raises if any implementation path touches expected/truth inputs mid-call

## Mutation observation — 12 defective variants, pinned failure sets, 12/12 MATCH

`lease-ignores-expiry` · `sliding-lease` · `live-fail-open` · `sticky-unavailable` · `retrieval-renews-evidence` · `deny-but-dispatch` · `deny-everything` · `live-first-read-only` · `second-worker-stale` (w2-only failure verified) · `fabricated-live-read` (read-provenance-only verification) · `selective-not-supported` · `ignore-evidence-binding`

## Post-expiry diagnostics — 20/20 clean

5 diagnostic cases × 4 profiles; every emitted diagnostic is backed by an actual recorded read; no speculative diagnostics.

## Oracle checkpoints — 12/12

Hand-reasoned checkpoint table (frozen alongside vectors) replayed against runner output: all field values and `downstream_reached` match; zero failures.

## Reporting semantics — 5/5

`no_scored_coverage` · `statement_only_matched` · `policy_mismatch_partial` · `unsupported_only_no_coverage` · `oracle_inputs_not_read` — all true.

## Negative-path self-check

Tampered copy of the vectors file (one case id altered) → digest gate rejects before any scoring: `DIGEST GATE FAILED ... refusing to score`. This makes the "comparisons only against frozen vectors" discipline machine-enforced, not merely stated.

## Determinism

Three consecutive full runs produce byte-identical JSON reports (identical sha256), including all axis verdicts, mutant failure sets, and composite comparisons.

## Replay

Full run cost: **~0.2 s wall-clock** (measured 2026-10-23, including interpreter startup; pure in-memory timeline replay — no network, no RPC, no real-time waiting). Verification is cheap by design: any party can reproduce this report in under a second.

```
cd rttp-iqa-runner
python lra_runner.py            # human summary
python lra_runner.py --json     # full machine-readable report
```

## Report metadata (per docs/RUN-REPORT.md required fields)

| field | value |
|---|---|
| who ran it | ShaoBao Li (Lee) (@Aicent-com); repository maintained under the @Aicent-Stack org |
| date | 2026-10-23 |
| run mode | B — alternate recomputation |
| implementation name | `lra_runner.py` (RTTP & IQA independent Python runner) |
| implementation repo and commit | https://github.com/Aicent-Stack/conformance — `lra-runner/` @ `a3e820cf038e15e5c85b0a1772f41ee018710355` (code as run; byte-identical through the monorepo restructure) |
| corpus reference | aps-conformance-suite PR #180, commit `b745d252191e89fe123e33411f124a1b67542c2a` |
| per-vector result | table below (48/48 matched) |
| verbatim command and output | below, uncut |
| environment | Python 3.14.2, Windows 11 (10.0.26300) |
| author-produced or independent | **independent** (see PROVENANCE.md Independence) |
| suspected defective vectors | none observed |

## Per-vector results (Mode B)

| Case | Mode | Boundary | Status |
|---|---|---|---|
| LRA-01 | `cached_lease` | `exclusive` | matched |
| LRA-02 | `cached_lease` | `exclusive` | matched |
| LRA-03 | `cached_lease` | `exclusive` | matched |
| LRA-04 | `cached_lease` | `exclusive` | matched |
| LRA-05 | `cached_lease` | `exclusive` | matched |
| LRA-06 | `cached_lease` | `exclusive` | matched |
| LRA-07 | `cached_lease` | `exclusive` | matched |
| LRA-08 | `cached_lease` | `exclusive` | matched |
| LRA-09 | `cached_lease` | `exclusive` | matched |
| LRA-10 | `cached_lease` | `exclusive` | matched |
| LRA-11 | `cached_lease` | `exclusive` | matched |
| LRA-12 | `cached_lease` | `exclusive` | matched |
| LRA-01 | `cached_lease` | `inclusive` | matched |
| LRA-02 | `cached_lease` | `inclusive` | matched |
| LRA-03 | `cached_lease` | `inclusive` | matched |
| LRA-04 | `cached_lease` | `inclusive` | matched |
| LRA-05 | `cached_lease` | `inclusive` | matched |
| LRA-06 | `cached_lease` | `inclusive` | matched |
| LRA-07 | `cached_lease` | `inclusive` | matched |
| LRA-08 | `cached_lease` | `inclusive` | matched |
| LRA-09 | `cached_lease` | `inclusive` | matched |
| LRA-10 | `cached_lease` | `inclusive` | matched |
| LRA-11 | `cached_lease` | `inclusive` | matched |
| LRA-12 | `cached_lease` | `inclusive` | matched |
| LRA-01 | `live_standing_read` | `exclusive` | matched |
| LRA-02 | `live_standing_read` | `exclusive` | matched |
| LRA-03 | `live_standing_read` | `exclusive` | matched |
| LRA-04 | `live_standing_read` | `exclusive` | matched |
| LRA-05 | `live_standing_read` | `exclusive` | matched |
| LRA-06 | `live_standing_read` | `exclusive` | matched |
| LRA-07 | `live_standing_read` | `exclusive` | matched |
| LRA-08 | `live_standing_read` | `exclusive` | matched |
| LRA-09 | `live_standing_read` | `exclusive` | matched |
| LRA-10 | `live_standing_read` | `exclusive` | matched |
| LRA-11 | `live_standing_read` | `exclusive` | matched |
| LRA-12 | `live_standing_read` | `exclusive` | matched |
| LRA-01 | `live_standing_read` | `inclusive` | matched |
| LRA-02 | `live_standing_read` | `inclusive` | matched |
| LRA-03 | `live_standing_read` | `inclusive` | matched |
| LRA-04 | `live_standing_read` | `inclusive` | matched |
| LRA-05 | `live_standing_read` | `inclusive` | matched |
| LRA-06 | `live_standing_read` | `inclusive` | matched |
| LRA-07 | `live_standing_read` | `inclusive` | matched |
| LRA-08 | `live_standing_read` | `inclusive` | matched |
| LRA-09 | `live_standing_read` | `inclusive` | matched |
| LRA-10 | `live_standing_read` | `inclusive` | matched |
| LRA-11 | `live_standing_read` | `inclusive` | matched |
| LRA-12 | `live_standing_read` | `inclusive` | matched |


## Verbatim command and output

```
$ python lra_runner.py

candidate lease-revocation-axes revision 2, vectors sha256 a0a07ea58bcacfd0
digest gate vs pinned manifest: OK
48 independent baseline runs, 176 calls, 528 axis comparisons; 176 composite comparisons
baseline failures: 0 | statuses: ['matched']
  mutant lease-ignores-expiry         MATCH  failed=LRA-04,LRA-05,LRA-07,LRA-08,LRA-10
  mutant sliding-lease                MATCH  failed=LRA-04,LRA-05,LRA-07,LRA-08,LRA-10
  mutant live-fail-open               MATCH  failed=LRA-03,LRA-07,LRA-11
  mutant sticky-unavailable           MATCH  failed=LRA-03,LRA-07,LRA-11
  mutant retrieval-renews-evidence    MATCH  failed=LRA-04,LRA-05,LRA-08,LRA-10
  mutant deny-but-dispatch            MATCH  failed=LRA-02,LRA-03,LRA-04,LRA-05,LRA-06,LRA-07,LRA-08,LRA-09,LRA-10,LRA-11,LRA-12
  mutant deny-everything              MATCH  failed=LRA-01,LRA-02,LRA-03,LRA-05,LRA-06,LRA-07,LRA-08,LRA-10,LRA-11,LRA-12
  mutant live-first-read-only         MATCH  failed=LRA-01,LRA-02,LRA-03,LRA-06,LRA-07,LRA-08,LRA-09,LRA-10,LRA-11
  mutant second-worker-stale          MATCH  failed=LRA-08
  mutant fabricated-live-read         MATCH  failed=LRA-01,LRA-02,LRA-03,LRA-05,LRA-06,LRA-07,LRA-08,LRA-09,LRA-10,LRA-11,LRA-12
  mutant selective-not-supported      MATCH  failed=LRA-02,LRA-03,LRA-04,LRA-05,LRA-06,LRA-07,LRA-08,LRA-09,LRA-10,LRA-11,LRA-12
  mutant ignore-evidence-binding      MATCH  failed=LRA-12
diagnostic runs: 20 (failures: 0)
oracle checkpoints: 12 (failures: none)
reporting checks: {'no_scored_coverage': True, 'statement_only_matched': True, 'policy_mismatch_partial': True, 'unsupported_only_no_coverage': True, 'oracle_inputs_not_read': True}
RESULT: independent_run_matched
```

## Archive of record

The complete artifact (code, frozen inputs, run report, recorded output) is pinned and organ-sealed on the archive of record: `lra-runner-20261023b.tar.gz`, sha256 `71c4e2a875cfdda1c0f31a1cc8b44bb15e4e80ee0b4076e0cfd2884592c3e892`, at [iqa.org/conformance/lra-runner/](https://iqa.org/conformance/lra-runner/). The artifact carries two addresses derived from its own digest — one per sister scheme: `rttp://71c4e2a8.conformance.iqa` (the question, WHERE+WHEN; intent = first 8 hex) and `iqa://71c4e2a875cfdda1c0f31a1cc8b44bb1.forge.iqa` (the answer, WHETHER; subject = first 32 hex — the exact organ-sealed subject, live at [organ-api/v1/production?subject=71c4e2a875cfdda1c0f31a1cc8b44bb1](https://iqa.org/organ-api/v1/production?subject=71c4e2a875cfdda1c0f31a1cc8b44bb1)). This concrete section was backfilled after the seal of the artifact it describes — a digest cannot appear inside the bytes it hashes, so the sealed copy of this report (inside `lra-runner-20261023b.tar.gz`) carries the archive pointer without the digest; the code-as-run pin above is unchanged.

