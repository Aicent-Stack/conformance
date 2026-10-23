# Conformance Run Report — lease-revocation-axes (revision 2, candidate)

**Runner** RTTP & IQA independent Python runner (`rttp-iqa-runner/lra_runner.py`) · **Date** 2026-10-23 · **Status** `independent_run_matched` · **Cut** rev c (reporting fixes after independent reproduction review, see Revision history)

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

`no_scored_coverage` · `statement_only_matched` · `policy_mismatch_partial` · `unsupported_only_no_coverage` · `oracle_inputs_not_read` — all true, and since rev c **executed, not asserted**: during all scoring phases (baselines, mutations, diagnostics, declaration-check runs) the runner wraps `open()` and records any attempt to read a file whose name contains `oracle`; the check is the measured result of that guard. A deliberately peeking implementation flips it to False (demonstrated once outside the battery; the mutation battery remains 12 named mutants so the declared failure sets stay frozen).

## Exit status (since rev c)

The process exit code is `0` only when the run status is `independent_run_matched`, and `1` otherwise — including digest-gate refusal and `independent_run_diverged`. Callers no longer need to parse stdout to learn whether the run matched.

## Negative-path self-check

Tampered copy of the vectors file (one case id altered) → digest gate rejects before any scoring: `DIGEST GATE FAILED ... refusing to score`. This makes the "comparisons only against frozen vectors" discipline machine-enforced, not merely stated.

## Determinism

Three consecutive full runs produce byte-identical JSON reports (identical sha256), including all axis verdicts, mutant failure sets, and composite comparisons.

## Replay

Full run cost: **~0.2 s wall-clock** (measured 2026-10-23, including interpreter startup; pure in-memory timeline replay — no network, no RPC, no real-time waiting). Verification is cheap by design: any party can reproduce this report in under a second.

```
cd rttp-iqa-runner
python lra_runner.py            # human summary (exit status 0 on matched, 1 otherwise)
python lra_runner.py --json     # full machine-readable report
```

## Report metadata (per docs/RUN-REPORT.md required fields)

| field | value |
|---|---|
| who ran it | ShaoBao Li (Lee) (@Aicent-com); repository maintained under the @Aicent-Stack org |
| date | 2026-10-23 |
| run mode | B — alternate recomputation |
| implementation name | `lra_runner.py` (RTTP & IQA independent Python runner) |
| implementation repo and commit | https://github.com/Aicent-Stack/conformance — `lra-runner/` @ `8cb2e241419cd03d9be40c5977e0e9caa1d723a4` (code as run, rev c; earlier cuts pinned `a3e820cf038e15e5c85b0a1772f41ee018710355`) |
| corpus reference | aps-conformance-suite PR #180, commit `b745d252191e89fe123e33411f124a1b67542c2a` |
| per-vector result | table below (48/48 matched) |
| verbatim command and output | below, uncut |
| environment | Python 3.14.2, Windows 11 (10.0.26300) |
| author-produced or independent | **Mode B — author-produced** under the lab's rules (independent *implementation* — no lab code — but run by its author; third-party reproductions are the independent records) |
| suspected defective vectors | none observed |

## Revision history (append-only narrative)

- **rev a** (2026-10-23): first cut; sealed, superseded same day.
- **rev b** (2026-10-23): removed the thread-mapping section — a technical artifact carries the measurement; thread politics belong in the accompanying comment. Sealed; rev a kept as sealed history.
- **rev c** (2026-10-23): two reporting fixes after the independent reproduction review (@aeoess, PR #180 comment): (1) process exit status now reflects the run status (0 = matched, 1 = diverged or digest-gate refusal); (2) `oracle_inputs_not_read` changed from an asserted constant to an executed runtime guard over all scoring phases. No scoring logic, vectors, or result numbers changed — the report above is byte-for-byte the same measurement. Sealed; rev a and rev b kept as sealed history.

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

The complete artifact (code, frozen inputs, run report, recorded output) is pinned and organ-sealed on the archive of record: [`lra-runner-20261023c.tar.gz`](https://iqa.org/conformance/files/lra-runner-20261023c.tar.gz), sha256 `94bbaf3c292abf69595bf5782d1db8cbb4178536d53182578b46cff94a5c4b15`, at [iqa.org/conformance/lra-runner/](https://iqa.org/conformance/lra-runner/). The artifact carries two addresses derived from its own digest — one per sister scheme:

- [`rttp://94bbaf3c.conformance.iqa`](https://rttp.com/open/?uri=rttp://94bbaf3c.conformance.iqa) — the question (WHERE+WHEN; intent = first 8 hex)
- [`iqa://94bbaf3c292abf69595bf5782d1db8cb.forge.iqa`](https://iqa.org/open/?uri=iqa://94bbaf3c292abf69595bf5782d1db8cb.forge.iqa) — the answer (WHETHER; subject = first 32 hex — the exact organ-sealed subject, live at the [organ endpoint](https://iqa.org/organ-api/v1/production?subject=94bbaf3c292abf69595bf5782d1db8cb)) This concrete section was backfilled after the seal of the artifact it describes — a digest cannot appear inside the bytes it hashes, so the sealed copy of this report (inside `lra-runner-20261023c.tar.gz`) carries the archive pointer without the digest; the code-as-run pin above is unchanged.

