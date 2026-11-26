<!--
Archived from https://github.com/probityai/agent-evidence-vectors/pull/469 on 2026-11-09. The text below the marker is the PR body verbatim. The text below the marker is byte-exact as
retrieved, LF-normalized for storage; sha256 of the archived text (the verbatim
section as stored, below the marker): f5625cc27a814d9c78b9b66c745086e52a9e63f997b4e625568b960ad4b7f079.-->

PR #469 verbatim archive — sha256 of archived text: f5625cc27a814d9c78b9b66c745086e52a9e63f997b4e625568b960ad4b7f079
================================================================

Refs #412

This adds rows PS1 and PS2 of Appendix B of draft-gilda-audit-agent-audit-record-03 to the agent audit record corpus, plus the boundary case beside them as an open member. Wes Jackson (@wjatx) contributed both records in #412, and the generator builds them exactly as written there. PS1 lands on his file identifier `vd96413ec87814d0b` and the boundary member on `v12896bcb35edd1b1`. Girish Konda raised the boundary case on the wimse thread.

PS1 is `A10` under the v2 predicate type URI. Issuer standing is fresh, principal standing could not be established within its `maxAge`, and the record is `not-evaluated` with `unavailableInput` of `principal-standing-source` and the matching stale entry. A verifier configured for the v2 URI judges it valid with agreement agree. PS2 is the same record under the v1 URI. There the value is outside the closed set, so it is malformed with `value-outside-vocabulary`. A reader that extends the v1 set along with the v2 set passes PS1 and fails PS2.

To make that work, both reference readers (Python `auditrecord.py` and Go `corpusreaders/auditrecord.go`) now take the input set from the URI the verifier is configured for. Under the v2 URI the evaluation and unavailable sets also hold `principal-standing-source`. Under the v1 URI nothing changes. A manifest entry may now carry its own `predicateType`, and the judge builds that member's policy from it. PS1 and the boundary member carry the v2 URI. Every other member is judged under the manifest's v1 URI as before, and no existing member's bytes moved.

The boundary member, `PS1b`, puts principal standing exactly at its `maxAge` with the source not answering, still recorded `not-evaluated`. Section 3 of draft-jackson-wimse-evaluation-05 forbids using an input at or past its horizon, so it requires this record. Section 5.4 of -03 as filed says an age equal to `maxAge` is fresh (FR2), so the derived unavailable set is empty and the record fails the recompute of Section 4.6. No record satisfies both texts. Following the repository rule for questions a specification leaves open, it is an indeterminate member with two readings, `valid` and `malformed`, and each reading's rationale names its resolution: -03 adopts the strict boundary (FR2 then flips and FR8 moves to "equal to"), or -05 reads "past its horizon". The reference reader keeps -03's boundary and returns `malformed` (`evaluation-inconsistent`). FR2 and the freshness comparison are unchanged.

`check_vectors.py` now judges each member under its own policy and gains two section readings: a reader that applies the extended set under the v1 URI fails exactly PS2, and a reader that accepts the v2 URI with the v1 set fails exactly PS1. The corpus README has a section on the three members.
