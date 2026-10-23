# Provenance

## Corpus source

| item | value |
|---|---|
| repository | Agent-Authority-Conformance/aps-conformance-suite |
| pull request | #180, "Add candidate lease-revocation-axes family for the W3C revocation timeline" |
| pull request state | open candidate, author aeoess, last updated 2026-10-22T19:51:56Z |
| commit read | `b745d252191e89fe123e33411f124a1b67542c2a` |
| fetch date | 2026-10-22 |

## Manifest pin, and its verification

The lab pins the revision-2 vectors by digest in `fixtures/lease-revocation-axes/revision-2/SHA256SUMS.txt`:

| pinned item | pinned sha256 |
|---|---|
| vectors.json | `a0a07ea58bcacfd056cbd648e03de4ff14778aa151e8b5d2574e43e31a111ed8` |

The copies under `vendor/` are verbatim from the pinned commit. This runner enforces the pinned digest as a hard gate at load time — it refuses to score any vectors whose sha256 is not in the manifest — and the gate was verified negatively: a tampered copy is rejected before any scoring occurs.

## Run mode and authorship

Run mode: **B** (alternate recomputation), per `docs/RUN-REPORT.md`. Authorship: **independent**.

Independence: this run was independently produced. The runner (`lra_runner.py`) was written from the family specification (`README.md`, `CLARIFICATIONS.md`) and the frozen vectors, by a party that is not the pack's author — the pack's model and checkpoint table are authored by aeoess under Tima's direction, per the family README's Verification split. The lab's TypeScript model and harness were read as the interface contract; no lab code was copied or reused, and the runner is stdlib-only Python sharing no code or library with the lab's implementation. The filer authored neither the vectors nor any claim inputs checked: every scored comparison in this run is made against the per-call expected blocks, the pinned mutant failure sets and the hand-reasoned oracle checkpoints contained in the lab's vectors file, never against lab model output. This follows the practice of the lab's exemplar Mode B record (`interop/mih-sato-composition-00/`), whose adapters were likewise written from the published bytes by a party that is not the pack's author.
