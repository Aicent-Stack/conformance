# lra-runner — RTTP & IQA independent runner for lease-revocation-axes

Independent Python implementation and conformance run report for the `lease-revocation-axes` family (revision 2, candidate) of the [Agent Authority Conformance lab](https://github.com/Agent-Authority-Conformance/aps-conformance-suite) (PR #180), maintained by the RTTP (Resonant Time Transfer Protocol) & IQA (Identity Quality Assurance) side of the W3C AI Agent Protocol CG discussion.

## Provenance

Independently authored Python implementation (~650 lines, stdlib-only, Python 3.10+): the lab's TypeScript model (`verify.ts` / `harness.ts`) was reviewed as the interface contract only, with no code reused; every pass/fail comparison is made against the frozen vectors and their pinned expected values, never against lab model output; the declaration mapping (`not_claimed` / `not_supported` / `supported`) is frozen before any verifier is constructed.

Declared claim set: `evidence_freshness`, `authority_validity`, `action_authorization` under the `P1-current-observation` policy (zero age tolerance); action-time authorization is not claimed (by design).

## Integrity gate

The runner enforces the lab's `SHA256SUMS.txt` digest as a hard gate — it refuses to score any vectors whose sha256 is not pinned (`vectors.json` sha256 `a0a07ea58bcacfd056cbd648e03de4ff14778aa151e8b5d2574e43e31a111ed8`); a tampered copy is rejected before any scoring occurs, making the "comparisons only against frozen vectors" discipline machine-enforced rather than self-attested.

## Results (2026-10-23 run) — `independent_run_matched`

48 baseline runs (4 profiles × 12 cases), 176 calls, 528 axis comparisons, 176 composite comparisons — zero failures, status `matched` on all runs; 12/12 defective mutants fail on exactly their pinned case sets (including `second-worker-stale` verified w2-only and `fabricated-live-read` caught via read provenance); 20/20 post-expiry diagnostic runs clean; 12/12 hand-reasoned oracle checkpoints; 5/5 reporting-semantics checks; three consecutive full runs produce byte-identical JSON reports; full run cost ~0.2 s wall-clock including interpreter startup (pure in-memory replay — no network, no RPC).

See [RUN-REPORT-2026-10-23.md](RUN-REPORT-2026-10-23.md) for the full report and [run-output.json](run-output.json) for the machine-readable result. On 2026-10-24 the run was re-verified (three fresh full runs, byte-identical JSON) and the record was filed under `interop/` on the [aps-conformance-suite](https://github.com/Agent-Authority-Conformance/aps-conformance-suite) repository.

## Replay

```
python lra_runner.py            # human summary
python lra_runner.py --json     # full machine-readable report
```

The frozen inputs are vendored under `vendor/` (copied verbatim from the lab's PR #180, `revision-2/`); the digest gate verifies them against the pinned manifest before any scoring, so a one-command replay works offline.

## Repository layout

`lra_runner.py` — the runner · `vendor/vectors.json` + `vendor/SHA256SUMS.txt` + `vendor/oracle-checkpoints.json` — frozen lab inputs, verbatim · `RUN-REPORT-2026-10-23.md` — full run report · `run-output.json` — machine-readable result of the 2026-10-23 run.

## Archive of record and addresses

The organ-sealed snapshot of this experiment, [`lra-runner-20261023c.tar.gz`](https://iqa.org/conformance/files/lra-runner-20261023c.tar.gz) (sha256 `94bbaf3c292abf69595bf5782d1db8cbb4178536d53182578b46cff94a5c4b15`; rev c supersedes rev b, which supersedes rev a — both remain sealed as history. Rev c carries two reporting fixes made after the independent reproduction review on PR #180: the process exit status now reflects the run status, and the `oracle_inputs_not_read` reporting check is executed via a runtime guard rather than asserted; no scoring logic, vectors, or result numbers changed), is pinned on the archive of record at [iqa.org/conformance/lra-runner/](https://iqa.org/conformance/lra-runner/). The artifact carries two addresses — one per sister scheme, both derived from the artifact's own digest, nothing invented, nothing registered:

- [`rttp://94bbaf3c.conformance.iqa`](https://rttp.com/open/?uri=rttp://94bbaf3c.conformance.iqa) — the question (WHERE + WHEN), intent side. intent = first 8 hex of the artifact digest (the intent field is 8 lowercase hex by grammar); pillar and root are operator-chosen labels.
- [`iqa://94bbaf3c292abf69595bf5782d1db8cb.forge.iqa`](https://iqa.org/open/?uri=iqa://94bbaf3c292abf69595bf5782d1db8cb.forge.iqa) — the answer (WHETHER), attestation side. subject = first 32 hex of the same digest; organ `forge` (closed set). This is the exact subject the organ seal attests; the organ answers live at [organ-api/v1/production?subject=94bbaf3c292abf69595bf5782d1db8cb](https://iqa.org/organ-api/v1/production?subject=94bbaf3c292abf69595bf5782d1db8cb).

Note: this section postdates the seal of the artifact it describes (a digest cannot be carried in the bytes it hashes, so the sealed copy carries the pointer without the digest), and re-archiving from HEAD yields a different digest — the sealed bytes remain the archive of record.

## License & credits

This repository: Apache-2.0. The vectors, oracle checkpoints and SHA256SUMS manifest under `vendor/` are by the Agent Authority Conformance lab (PR #180), Apache-2.0, vendored verbatim with digest verification; the runner implementation is by the RTTP & IQA side (Aicent Stack).
