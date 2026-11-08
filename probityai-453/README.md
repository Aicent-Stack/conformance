# probityai-453 — the families evaluated against the Probity AI audit-record contract

On 2026-11-05, following the venue's invitation on the WIMSE list (30 October), we filed
[probityai/agent-evidence-vectors#453](https://github.com/probityai/agent-evidence-vectors/issues/453):
five records drawn from our two vector families — [`candidates/aicent-grant-ref/`](../candidates/aicent-grant-ref/)
and [`candidates/aicent-lease-boundary/`](../candidates/aicent-lease-boundary/) — scored under the
audit-record contract's crosswalk, with a crosswalk table mapping the contract's codes onto section 8.1
of the specification under test. The submission was filed as an issue only; no pull request was opened on
the venue's side, and the venue's changes to its own contract are made upstream by the venue.

## Timeline (UTC)

- 2026-11-05 — issue filed: five records + crosswalk (verbatim text in [`ISSUE-RECORDS.md`](ISSUE-RECORDS.md)).
- 2026-11-07 12:12 — the venue's response (astrogilda), verbatim in [`THREAD.md`](THREAD.md).
- 2026-11-07 12:41 — our reply, verbatim in [`THREAD.md`](THREAD.md).
- 2026-11-07 18:22 — issue closed as completed by the venue.

## The venue's response, in substance

- Record 5 was already in the audit-record corpus as case `PS1b`, added upstream in the venue's
  [PR #469](https://github.com/probityai/agent-evidence-vectors/pull/469) (an input's age exactly equals its
  maximum age); that case is open between draft-jackson-wimse-evaluation-05 and
  draft-gilda-audit-agent-audit-record-03, which treat the same instant differently.
- Records 1–4 score responses under section 8.1 rather than being records in the venue's format, so they
  stay out of that set — but they expose a real contract gap: `verifier-contract.md` passes reason parity
  when any emitted code is in `expected.codes`, so `GR-P04` passes today. The venue committed to adding a
  manifest field for families whose source fixes a priority — there, the first emitted code must equal the
  first expected one — with `GR-P03`/`GR-P04` as its paired fixture, credited under our name.
- One crosswalk erratum: the issue's substantive-codes row listed the four substantive codes off-order;
  corrected by us in the issue the same day against section 8.1's fixed priority.

## Status at archive time (2026-11-09, verified live)

The manifest field described above is not yet implemented upstream: `verifier-contract.md` on `main`
carries no priority / first-emitted wording, and no matching PR is open or merged in the venue's
repository. Until it lands, `GR-P04`'s pass under the current parity rule remains the documented gap the
GR-P03/GR-P04 pairing was built to expose.

## Provenance and links

- Family pages (sealed, per-file SHA-256): [iqa.org/conformance/aicent-grant-ref/](https://iqa.org/conformance/aicent-grant-ref/) · [iqa.org/conformance/aicent-lease-boundary/](https://iqa.org/conformance/aicent-lease-boundary/)
- Lab records (same families): [PR #210](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/210) · [PR #212](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/212), merged 2026-11-03
- Venue: [probityai/agent-evidence-vectors](https://github.com/probityai/agent-evidence-vectors) — issue [#453](https://github.com/probityai/agent-evidence-vectors/issues/453) (closed, completed); `PS1b` via the venue's PR #469
- Specification under test: draft-li-rttp-iqa-addressing-02, pinned sha256 `02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044`
- Operator: Lee / Aicent Stack (RTTP, CRI scheme number 27 · IQA, CRI scheme number 28)

This is a thread record, not a run record: no runner executed here, so there is nothing to replay. The
verbatim texts are the artifact; each is pinned by the sha256 of its retrieved text as listed in the
archive headers of the two files above.
