# Provenance

## Corpus source

| item | value |
|---|---|
| repository | Agent-Authority-Conformance/aps-conformance-suite |
| pull request | #180, "Add candidate lease-revocation-axes family for the W3C revocation timeline" |
| pull request state | open candidate, author aeoess; PR head `86e5e7a` at filing (2026-10-24) |
| commit read | `b745d252191e89fe123e33411f124a1b67542c2a` |
| fetch date | 2026-10-22 |

## Manifest pin, and its verification

The lab pins the revision-2 vectors by digest in `fixtures/lease-revocation-axes/revision-2/SHA256SUMS.txt`:

| pinned item | pinned sha256 |
|---|---|
| vectors.json | `a0a07ea58bcacfd056cbd648e03de4ff14778aa151e8b5d2574e43e31a111ed8` |

The copies under `vendor/` are verbatim from the pinned commit. This runner enforces the pinned digest as a hard gate at load time — it refuses to score any vectors whose sha256 is not in the manifest — and the gate was verified negatively: a tampered copy is rejected before any scoring occurs. Commits on the PR branch after the run revision (`bccef3e`, `86e5e7a`) touch the family README only; the frozen inputs were re-verified on 2026-10-24 — the `revision-2/vectors.json` served at the PR head hashes to the pinned digest above.

## Run mode and authorship

Run mode: **B** (alternate recomputation), per `docs/RUN-REPORT.md`. Record label: **author-produced**, with the following authorship relationship: the filer authored the alternate implementation (`lra_runner.py`) whose behavior supplies the recomputation, so under the definition in `CONTRIBUTING.md` the record cannot be labeled independent.

The filer authored neither the vectors nor any claim inputs being checked (pack author: aeoess, per the family README's Verification split): every scored comparison in this run is made against the per-call expected blocks, the pinned mutant failure sets and the hand-reasoned oracle checkpoints contained in the lab's vectors file, never against lab model output. The implementation is independent of the lab's code: it was written from the family specification (`README.md`, `CLARIFICATIONS.md`) and the frozen vectors, is stdlib-only Python, shares no code or library with the lab's TypeScript model and harness (`verify.ts` / `harness.ts`), which were reviewed as the interface contract only. Third-party reproductions of this runner (or independent implementations of the family) are the independent records for this layer.
