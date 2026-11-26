<!--
Archived from https://github.com/probityai/agent-evidence-vectors/issues/453
on 2026-11-09. The text below the marker is byte-exact as retrieved, LF-normalized
where the source carried CRLF (the body carried none); sha256 of the archived text
(the verbatim section as stored, below the marker): cba0b281e3c96c8f3843159e276f958c6159389e0f156ea924ab106beb455e80.
-->
ISSUE-RECORDS verbatim archive — sha256 of archived text: cba0b281e3c96c8f3843159e276f958c6159389e0f156ea924ab106beb455e80
================================================================

Following the invitation on the WIMSE list (30 October): "A test record from you would help. An issue on https://github.com/probityai/agent-evidence-vectors with the record you expect and its verdict is enough, and it goes into the test records under your name." (https://mailarchive.ietf.org/arch/msg/wimse/2Booef4RPGIEMpGjU7D48YViB7s/) The records below come from our two vector families, both merged into the LFDT Agent-Authority-Conformance lab mainline on 3 November (PR [#210](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/210), merge commit 0da1e29; PR [#212](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/212), merge commit 29423aa) and sealed as four-file sets with per-file SHA-256 at https://iqa.org/conformance/aicent-grant-ref/ and https://iqa.org/conformance/aicent-lease-boundary/.

Texts: draft-li-rttp-iqa-addressing-02 (https://www.ietf.org/archive/id/draft-li-rttp-iqa-addressing-02.txt, retrieved copy pinned at sha256 02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044), sections 6.1, 7.2, 8.1 and 8.2. Canonical sources: https://github.com/Aicent-Stack/conformance — candidates/aicent-grant-ref and candidates/aicent-lease-boundary (https://github.com/Aicent-Stack/conformance/tree/main/candidates; each: CANDIDATE.md, vectors.json, check.py, mutate.py). The families are self-contained: every case states the facts at answer time, one response an implementation could produce, the expected verdict, and which rule decides.

Why these map onto this repository's concern: the suite's comparison rules separate normative conformance from reject reason parity — and reason parity is only checkable when the reading order over reason codes is fixed. That is exactly what our section 8.1 fixes: five values, closed set, the reason is the first value in the list whose condition applies. The vocabulary's anchor sentence: "the reason is what makes a refusal auditable," and "a refusal computed over labels, opinions, or unrecorded context alone is not auditable" (section 8.1).

Mapping to the contract used here (offered as a crosswalk, not a claim of equivalence):

| this suite | our draft (-02) |
| --- | --- |
| transient refusal, not-evaluated naming unavailableInput (the audit-record family; never a substantive code) | authority_not_determined — an unreachable source or a stale observation is never read as assent (sect. 8.1, 8.2) |
| substantive reject codes | evidence_binding_mismatch / evidence_expired / authority_revoked / operation_not_permitted, in the fixed priority of sect. 8.1 (evidence_binding_mismatch, evidence_expired, authority_not_determined, authority_revoked, operation_not_permitted) |
| reason parity as a set intersection | reason parity requires the priority order: the emitted code must be the FIRST applicable value, not any applicable value (R-ORDER cases below) |
| the horizon rule at-or-past, settled for this family on the WIMSE list | sect. 6.1 makes the boundary a declared convention: inclusive and exclusive are both conformant when declared; a declaration that contradicts use is not |

Records 1-4 — from aicent-grant-ref (25 cases: 11 conformant, 12 nonconformant, 2 ambiguous; author's runs 25/25 agree, 21/21 mutants killed, exit 0):

**Record 1 (GR-P03 / GR-P04, paired): expiry over revocation.** Facts: the evidence the answer relied on expired before the request; a revocation is also on record. Expected verdict: GR-P03 scores a response answering evidence_expired conformant — the first applicable value in the fixed order, even though a revocation is also on record; GR-P04 holds the same facts with a response answering authority_revoked and scores it nonconformant (sect. 8.1: the reason is the first value in the list whose condition applies). Regression: a checker that scores any applicable code instead of the first fails exactly one of the two.

**Record 2 (GR-P09): no condition, no reason.** Facts: every condition the vocabulary defines is absent — the operation is permitted on the face of the record. Response: the refusal value operation_not_permitted, emitted with no condition behind it. Expected verdict: nonconformant — when no condition applies the reason must be null; emitting a refusal value without a condition is not conformant (sect. 8.1). This is the boundary of the whole scheme: refusal values exist only when their condition applies.

**Record 3 (GR-C04): null is the only permit.** Facts: a response that permits the operation. Expected verdict: conformant if and only if the reason is null over the closed set — there is no affirmative "granted" value (GR-C01), there is no sixth value (GR-C03), and null reason over the set is the only representation of permitted (sect. 8.1). Regression: a response adding a local "granted" code passes GR-C04's twin and fails GR-C03.

**Record 4 (GR-N04): a diagnostic read does not authorize.** Facts: the relied-on evidence was stale at answer time; a later diagnostic read succeeded (at 1150 ms). Response: a permit computed over that later observation, carrying observation_as_of_ms 1150 backfilled from the diagnostic read. Expected verdict: nonconformant — a diagnostic read does not participate in authorisation (sect. 8.1, 8.2), so on stale facts the only conformant answer is authority_not_determined, and even that answer must keep observation_as_of_ms null: the null rule (GR-N01-N03) holds that a later successful observation neither backfills the member nor renews the evidence (GR-N03 scores exactly that backfill nonconformant). The permit's backfilled 1150 is precisely the tell: it was computed over an observation the answer could not rely on.

Record 5 — from aicent-lease-boundary (15 cases: 9 conformant, 5 nonconformant, 1 ambiguous; author's runs 15/15 agree, 17/17 mutants killed, exit 0):

**Record 5 (LB-D01/D02, paired): the boundary is a declaration.** Facts: the observation's age at the lease instant is exactly the lease length — the same edge your Vector B in #412 tests, settled at-or-past on the WIMSE list for the evaluation family. Our draft's section 6.1 takes a different, complementary position: whether the instant counts as fresh or as expired is a deployment convention. Expected verdict: a permit at the instant under a declared inclusive boundary is conformant (LB-D01); an expired refusal at the instant under a declared exclusive boundary is also conformant (LB-D02); a declaration that contradicts use is nonconformant (LB-D03, strict reading disclosed in the CANDIDATE); with no declaration the case cannot be settled and is scored in parts (LB-D04, ambiguous by design). Section 7.2's frame acceptance at the instant does not decide the reliance convention — frame validity and reliance are different layers (LB-D05).

What these records do not claim: the author's runs say nothing about any implementation, and they do not show that the expected results are the right reading of the source — the reading is written out in the CANDIDATE files for anyone to dispute, sentence by sentence, and a correction in a later draft revision overrides the checker. No implementation has been run against these cases beyond the author's own checker-and-mutant batteries.

A second batch is ready to file once it can anchor to filed text: the missing-proof classification vectors wait on the evaluation-side wording decision ("-06"), per the same discipline used above — expected values anchor to published sentences only.

Citation: families aicent-grant-ref and aicent-lease-boundary · repository github.com/Aicent-Stack/conformance (lab: Agent-Authority-Conformance/aps-conformance-suite PRs [#210](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/210) / [#212](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/212), merged) · operator Lee / Aicent Stack, RTTP CRI 27 · IQA CRI 28 · sealed family pages with per-file SHA-256: https://iqa.org/conformance/aicent-grant-ref/ · https://iqa.org/conformance/aicent-lease-boundary/ · Sister pillars: RTTP (rttp://, CRI 27) · IQA (iqa://, CRI 28) — https://rttp.com · https://iqa.org

