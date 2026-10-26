# Conformance Run Report — lease-revocation-axes (revision 3, merged)

**Runner** RTTP & IQA independent Python runner (`lra-runner/lra_runner.py`, `--revision 3`) · **Date** 2026-10-26 · **Status** `independent_run_matched` (exit 0)

**Frozen input** `fixtures/lease-revocation-axes/revision-3/vectors.json` · sha256 `3b7b3fb97682fb967801641b8ed680a9cae608ff57738a594fc6f0314aac1bb6` · digest gate vs pinned `SHA256SUMS.txt`: OK (hard gate — runner refuses to score any vectors whose digest is not pinned)

## Provenance

Independently authored Python implementation (741 lines, stdlib-only). The lab's TypeScript model (PR #191, `verify.ts`/`harness.ts`/`generate.py`) was reviewed only as the interface contract; no lab code was reused. All pass/fail comparisons are made against the frozen vectors file and its pinned expected values — never against lab model output. The lab's `model.json` (pinned `b71f02f5…`) is deliberately not vendored and not read; the file-read surface is instrumented (`builtins.open` guard), so the not-read claim is executed, not asserted. Declaration mapping (`not_claimed` / `not_supported` / `supported`) is frozen before any verifier is constructed.

Corpus: revision 3 was added by PR #191 (merged 2026-10-25T18:46:20Z, merge `7774dae`, head `9a282619`). The vendored `vendor-r3/` inputs are byte-identical to the merged head, re-verified byte-for-byte on 2026-10-26.

## Declared claim set

- Claimed axes: `evidence_freshness` · `authority_validity` · `action_authorization`
- Action policy: `P1-current-observation` (zero age tolerance)
- Note: **action-time authorization is not claimed (by design)** — the runner scores the three declared axes only.

## What revision 3 adds

Two fields on every decision record:

- `refusal_reason` — closed five-value set, evaluated in priority order: `evidence_binding_mismatch` → `evidence_expired` → `authority_not_determined` → `authority_revoked` → `operation_not_permitted`. A denial names exactly one reason: the first condition that failed in priority order.
- `grant_ref` — back-reference binding each decision to the evidence it was made from: grant, evidence id, issue/expiry instants, and `observation_as_of_ms`.

Key semantic: **a diagnostic read performed after evidence expiry does not renew the evidence.** `grant_ref.observation_as_of_ms` is null when the only available observation is stale, even if a fresh observation exists later in the timeline — diagnostic reads inform the report, never the authorization. (First-run deviation on exactly this point was found and fixed during development; the recorded run is post-fix.)

## Baseline: 4 profiles × 12 cases = 48 runs (dual-mode, separately scored)

| Profile | Runs | Calls | Axis comparisons | Composite comparisons | Failures |
|---|---|---|---|---|---|
| `cached_lease` × exclusive | 12 | 44 | 132 | 44 | 0 — matched |
| `cached_lease` × inclusive | 12 | 44 | 132 | 44 | 0 — matched |
| `live_standing_read` × exclusive | 12 | 44 | 132 | 44 | 0 — matched |
| `live_standing_read` × inclusive | 12 | 44 | 132 | 44 | 0 — matched |
| **Total** | **48** | **176** | **528** | **176** | **0** |

Tri-axis result: all three axes scored on every supported comparison; status `matched` on all 48 runs. All five refusal values are exercised across the 117 denying decision records of 176 calls; all 176 records carry `grant_ref`.

## Source-read contract (instrumented, not asserted)

- `cached_lease`: **0** authority reads per call (lease decides from carried evidence)
- `live_standing_read`: exactly **1** instrumented read per unexpired + bound call
- Outage calls: getter returns null, the **attempt is recorded**, diagnostics must be backed by actual reads
- Hostile-call boundary: the runner raises if any implementation path touches expected/truth inputs mid-call
- Post-expiry diagnostic reads: recorded and reported, **never** fed back into `grant_ref.observation_as_of_ms` (evidence is not renewed by diagnosis)

## Mutation observation — 12 defective variants, pinned failure sets, 12/12 MATCH

`lease-ignores-expiry` · `sliding-lease` · `live-fail-open` · `sticky-unavailable` · `retrieval-renews-evidence` · `deny-but-dispatch` · `deny-everything` · `live-first-read-only` · `second-worker-stale` (w2-only failure verified) · `fabricated-live-read` (read-provenance-only verification) · `selective-not-supported` · `ignore-evidence-binding`

The observed failure sets are identical to revision 2's pinned sets — the rev-3 fields refine the *reasons* attached to decisions, not the decisions themselves.

## Post-expiry diagnostics — 20/20 clean

5 diagnostic cases × 4 profiles; every emitted diagnostic is backed by an actual recorded read; no speculative diagnostics; no diagnostic read renews expired evidence.

## Oracle checkpoints — 12/12

Hand-reasoned checkpoint table (frozen alongside vectors in `revision-3/oracle-checkpoints.json`, sha256 `08293dbd…`) replayed against runner output: all field values — including the rev-3 `refusal_reason` and `grant_ref` fields — and `downstream_reached` match; zero failures.

## Reporting semantics — 5/5

`no_scored_coverage` · `statement_only_matched` · `policy_mismatch_partial` · `unsupported_only_no_coverage` · `oracle_inputs_not_read` — all true, executed not asserted: during all scoring phases the runner wraps `open()` and records any attempt to read a file whose name contains `oracle`; the check is the measured result of that guard.

## Exit status

The process exit code is `0` only when the run status is `independent_run_matched`, and `1` otherwise — including digest-gate refusal and `independent_run_diverged`.

## Negative-path self-check

Tampered copy of the vectors file (one case id altered) → digest gate rejects before any scoring: `DIGEST GATE FAILED ... refusing to score`. Machine-enforced, not merely stated.

## Determinism

Three consecutive full runs produce byte-identical JSON reports. Recorded output of the 2026-10-26 run: raw sha256 `d777980195ef1d08…`, canonical (sort, compact) sha256 `78824b82a07eccdb…`. Re-verified 2026-10-26 against the recorded artifact.

## Replay

Full run cost: **~0.2 s wall-clock** (pure in-memory timeline replay — no network, no RPC, no real-time waiting).

```
cd lra-runner
python lra_runner.py --revision 3            # human summary (exit 0 on matched)
python lra_runner.py --revision 3 --json     # full machine-readable report
```

## Report metadata (per docs/RUN-REPORT.md required fields)

| field | value |
|---|---|
| who ran it | ShaoBao Li (Lee) (@Aicent-com); repository maintained under the @Aicent-Stack org |
| date | 2026-10-26 |
| run mode | B — alternate recomputation |
| implementation name | `lra_runner.py` (RTTP & IQA independent Python runner), revision 3 support |
| implementation repo and commit | https://github.com/Aicent-Stack/conformance — `lra-runner/`; the code-as-run identity of this record is the sealed cut `lra-runner-20261026a.tar.gz` (sha256 printed on the archive of record); the GitHub commit pin is assigned at filing time and postdates the seal, as in the rev-c precedent |
| corpus reference | aps-conformance-suite PR #191 (merged `7774dae`, head `9a282619`); frozen inputs re-verified byte-identical at that head on 2026-10-26 |
| per-vector result | table below (48/48 matched) |
| verbatim command and output | below, uncut |
| environment | Python 3.14.2, Windows 11 (10.0.26300) |
| author-produced or independent | **Mode B — author-produced** under the lab's rules (independent *implementation* — no lab code, no lab model input — but run by its author; third-party reproductions are the independent records) |
| suspected defective vectors | none observed |

## Revision history (append-only narrative)

- **rev a / rev b / rev c** (2026-10-23): revision-2 cuts; rev c is the sealed archive of record for the revision-2 run (see RUN-REPORT-2026-10-23.md).
- **2026-10-26 cut (revision 3)**: runner extended with `--revision {2,3}`, `vendor-r3/` frozen inputs, refusal-reason priority and grant-ref semantics; first runs surfaced two deviations (exit-code plumbing and the expired-diagnostic `observation_as_of_ms` null rule), fixed before recording; the recorded run is post-fix. Revision-2 replay remains byte-identical to the recorded rev-c output — one runner, two revisions, two recorded outputs.

## Per-vector results (Mode B, revision 3)

| Case | Mode | Boundary | Status | refusal_reason values observed |
|---|---|---|---|---|
| LRA-01 | `cached_lease` | `exclusive` | matched | authority_not_determined |
| LRA-02 | `cached_lease` | `exclusive` | matched | authority_not_determined |
| LRA-03 | `cached_lease` | `exclusive` | matched | authority_not_determined |
| LRA-04 | `cached_lease` | `exclusive` | matched | evidence_expired |
| LRA-05 | `cached_lease` | `exclusive` | matched | authority_not_determined,evidence_expired |
| LRA-06 | `cached_lease` | `exclusive` | matched | authority_not_determined |
| LRA-07 | `cached_lease` | `exclusive` | matched | authority_not_determined,evidence_expired |
| LRA-08 | `cached_lease` | `exclusive` | matched | authority_not_determined,evidence_expired |
| LRA-09 | `cached_lease` | `exclusive` | matched | authority_not_determined,operation_not_permitted |
| LRA-10 | `cached_lease` | `exclusive` | matched | authority_not_determined,evidence_expired |
| LRA-11 | `cached_lease` | `exclusive` | matched | authority_not_determined |
| LRA-12 | `cached_lease` | `exclusive` | matched | authority_not_determined,evidence_binding_mismatch |
| LRA-01 | `cached_lease` | `inclusive` | matched | authority_not_determined |
| LRA-02 | `cached_lease` | `inclusive` | matched | authority_not_determined |
| LRA-03 | `cached_lease` | `inclusive` | matched | authority_not_determined |
| LRA-04 | `cached_lease` | `inclusive` | matched | evidence_expired |
| LRA-05 | `cached_lease` | `inclusive` | matched | authority_not_determined,evidence_expired |
| LRA-06 | `cached_lease` | `inclusive` | matched | authority_not_determined |
| LRA-07 | `cached_lease` | `inclusive` | matched | authority_not_determined,evidence_expired |
| LRA-08 | `cached_lease` | `inclusive` | matched | authority_not_determined,evidence_expired |
| LRA-09 | `cached_lease` | `inclusive` | matched | authority_not_determined,operation_not_permitted |
| LRA-10 | `cached_lease` | `inclusive` | matched | authority_not_determined,evidence_expired |
| LRA-11 | `cached_lease` | `inclusive` | matched | authority_not_determined |
| LRA-12 | `cached_lease` | `inclusive` | matched | authority_not_determined,evidence_binding_mismatch |
| LRA-01 | `live_standing_read` | `exclusive` | matched | - |
| LRA-02 | `live_standing_read` | `exclusive` | matched | authority_revoked |
| LRA-03 | `live_standing_read` | `exclusive` | matched | authority_not_determined |
| LRA-04 | `live_standing_read` | `exclusive` | matched | evidence_expired |
| LRA-05 | `live_standing_read` | `exclusive` | matched | evidence_expired |
| LRA-06 | `live_standing_read` | `exclusive` | matched | authority_revoked |
| LRA-07 | `live_standing_read` | `exclusive` | matched | authority_not_determined,evidence_expired |
| LRA-08 | `live_standing_read` | `exclusive` | matched | authority_revoked,evidence_expired |
| LRA-09 | `live_standing_read` | `exclusive` | matched | operation_not_permitted |
| LRA-10 | `live_standing_read` | `exclusive` | matched | evidence_expired |
| LRA-11 | `live_standing_read` | `exclusive` | matched | authority_not_determined,authority_revoked |
| LRA-12 | `live_standing_read` | `exclusive` | matched | evidence_binding_mismatch |
| LRA-01 | `live_standing_read` | `inclusive` | matched | - |
| LRA-02 | `live_standing_read` | `inclusive` | matched | authority_revoked |
| LRA-03 | `live_standing_read` | `inclusive` | matched | authority_not_determined |
| LRA-04 | `live_standing_read` | `inclusive` | matched | evidence_expired |
| LRA-05 | `live_standing_read` | `inclusive` | matched | evidence_expired |
| LRA-06 | `live_standing_read` | `inclusive` | matched | authority_revoked |
| LRA-07 | `live_standing_read` | `inclusive` | matched | authority_not_determined,evidence_expired |
| LRA-08 | `live_standing_read` | `inclusive` | matched | authority_revoked,evidence_expired |
| LRA-09 | `live_standing_read` | `inclusive` | matched | operation_not_permitted |
| LRA-10 | `live_standing_read` | `inclusive` | matched | evidence_expired |
| LRA-11 | `live_standing_read` | `inclusive` | matched | authority_not_determined,authority_revoked |
| LRA-12 | `live_standing_read` | `inclusive` | matched | evidence_binding_mismatch |

`-` = every decision record in the case is a permit (no refusal reason attached). All five refusal values appear across the battery.

## Verbatim command and output

```
$ python lra_runner.py --revision 3

candidate lease-revocation-axes revision 3, vectors sha256 3b7b3fb97682fb96
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

The complete artifact (code, both revisions' frozen inputs, run reports, recorded outputs) is pinned and organ-sealed on the archive of record: `lra-runner-20261026a.tar.gz` (sha256 and dual addresses printed on the report page at iqa.org/conformance — a digest cannot appear inside the bytes it hashes, so the sealed copy of this report carries the archive pointer without the digest, as in the rev-c precedent). The artifact carries two addresses derived from its own digest — one per sister scheme: `rttp://<first 8 hex>.conformance.iqa` (the question, WHERE+WHEN) and `iqa://<first 32 hex>.forge.iqa` (the answer, WHETHER — the exact organ-sealed subject).
