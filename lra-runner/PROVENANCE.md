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

The data files under `vendor/` are byte-identical to the pinned commit; the live `SHA256SUMS.txt` is trimmed to the two vendored files, and the lab's full pinned manifest is preserved verbatim as `lab-pinned-manifest.txt`. This runner enforces the pinned digest as a hard gate at load time — it refuses to score any vectors whose sha256 is not in the manifest — and the gate was verified negatively: a tampered copy is rejected before any scoring occurs. Commits on the PR branch after the run revision (`bccef3e`, `86e5e7a`) touch the family README only; the frozen inputs were re-verified on 2026-10-24 — the `revision-2/vectors.json` served at the PR head hashes to the pinned digest above.

## Run mode and authorship

Run mode: **B** (alternate recomputation), per `docs/RUN-REPORT.md`. Record label: **author-produced**, with the following authorship relationship: the filer authored the alternate implementation (`lra_runner.py`) whose behavior supplies the recomputation, so under the definition in `CONTRIBUTING.md` the record cannot be labeled independent.

The filer authored neither the vectors nor any claim inputs being checked (pack author: aeoess, per the family README's Verification split): every scored comparison in this run is made against the per-call expected blocks, the pinned mutant failure sets and the hand-reasoned oracle checkpoints contained in the lab's vectors file, never against lab model output. The implementation is independent of the lab's code: it was written from the family specification (`README.md`, `CLARIFICATIONS.md`) and the frozen vectors, is stdlib-only Python, shares no code or library with the lab's TypeScript model and harness (`verify.ts` / `harness.ts`), which were reviewed as the interface contract only. Third-party reproductions of this runner (or independent implementations of the family) are the independent records for this layer.

## Artifact of record

The sealed artifact of this run is [`lra-runner-20261023c.tar.gz`](https://iqa.org/conformance/files/lra-runner-20261023c.tar.gz) (sha256 `94bbaf3c292abf69595bf5782d1db8cbb4178536d53182578b46cff94a5c4b15`), carrying two addresses derived from its own digest — one per sister scheme, nothing invented, nothing registered, both resolve live: [`rttp://94bbaf3c.conformance.iqa`](https://rttp.com/open/?uri=rttp://94bbaf3c.conformance.iqa) (the question side, WHERE + WHEN) and [`iqa://94bbaf3c292abf69595bf5782d1db8cb.forge.iqa`](https://iqa.org/open/?uri=iqa://94bbaf3c292abf69595bf5782d1db8cb.forge.iqa) (the answer side, WHETHER; subject = first 32 hex of the same digest).

## Revision-3 corpus source

| item | value |
|---|---|
| repository | Agent-Authority-Conformance/aps-conformance-suite |
| pull request | #191, "lease-revocation-axes: revision 3 adds refusal_reason and grant_ref to decision records" |
| pull request state | merged 2026-10-25T18:46:20Z by aeoess; merge commit `7774dae`, PR head `9a282619` |
| revision-3 files | `fixtures/lease-revocation-axes/revision-3/` (vectors.json, oracle-checkpoints.json, model.json, SHA256SUMS.txt) |
| fetch date | 2026-10-26 |

The lab pins the revision-3 inputs by digest in `fixtures/lease-revocation-axes/revision-3/SHA256SUMS.txt`:

| pinned item | pinned sha256 |
|---|---|
| vectors.json (184,582 B) | `3b7b3fb97682fb967801641b8ed680a9cae608ff57738a594fc6f0314aac1bb6` |
| oracle-checkpoints.json (8,977 B) | `08293dbd991fe3f76534e176800e15365545a43a6d94e4d89f79d6d58ec7e830` |
| model.json (573,982 B) | `b71f02f570237a354cf23abd515c1bd1138461016f7eaaed7e83e16d61bc8237` |

The revision-3 data files under `vendor-r3/` are byte-identical to the merged head (re-verified against `9a282619` on 2026-10-26, byte-for-byte); the live `SHA256SUMS.txt` is trimmed to the two vendored files. The lab's third pinned file, `model.json`, is **deliberately not vendored and not read**: it is the lab's own machine-readable model, and this runner's independence claim rests on deriving every verdict from the family specification plus the frozen vectors — consuming the author's model artifact would compromise that claim. The runner's file-read surface is instrumented (`builtins.open` guard), so the not-read claim is executed, not asserted. The digest gate for revision 3 enforces the trimmed manifest the same way as revision 2: it refuses to score any vectors whose sha256 is not pinned.
