<!--
Archived from https://github.com/probityai/agent-evidence-vectors/issues/453
(issue comments) on 2026-11-09. The text below the marker is byte-exact as
retrieved, LF-normalized for storage (the source carried CRLF); sha256 of the
archived text (the verbatim section as stored, below the marker): 3d9b20a6dfab91c9ee3c41a4611fbb5477e581bde205eed421f71d993698f280.
Closure event: closed as completed by astrogilda, 2026-11-07T18:22:27Z.
-->
THREAD verbatim archive — sha256 of archived text: 3d9b20a6dfab91c9ee3c41a4611fbb5477e581bde205eed421f71d993698f280
================================================================



===== astrogilda @ 2026-11-07T12:12:10Z =====
@Aicent-com, thanks for the records, and for catching a gap in our contract.

Record 5 is already in our audit-record corpus as case `PS1b`, added in [#469](https://github.com/probityai/agent-evidence-vectors/pull/469), where an input's age exactly equals its maximum age. That case is open between two drafts, draft-jackson-wimse-evaluation-05 and draft-gilda-audit-agent-audit-record-03, and the second treats that age as fresh. Our record carries no declared boundary, so a reader of the record alone cannot check a Section 6.1 declaration.

Records 1 to 4 score responses under your Section 8.1 vocabulary, not records in our format, so they stay out of that set. The gap they expose is real: `docs/reference/verifier-contract.md` passes reason parity when any emitted code is in `expected.codes`, so `GR-P04` passes today. I'm adding a manifest field for families whose source fixes a priority: there, the first emitted code must equal the first expected one. `GR-P03` and `GR-P04` become its paired fixture, under your name.

One fix to the crosswalk table: 8.1 ranks `evidence_binding_mismatch`, `evidence_expired`, `authority_not_determined`, `authority_revoked`, then `operation_not_permitted`, and the table's row puts them in another order.


===== Aicent-com @ 2026-11-07T12:41:02Z =====
Confirmed — you read the draft correctly, and the crosswalk row in this issue was wrong. The fixed order in section 8.1 is evidence_binding_mismatch, evidence_expired, authority_not_determined, authority_revoked, operation_not_permitted ("the first value in the list whose condition applies", the priority order being part of the definition). The substantive-codes row in the issue body now lists the four codes in that order, with the full five-value sequence quoted for reference; the table is corrected.

Thank you for taking the records, for confirming the contract gap in verifier-contract.md, and for the fixture plan — a manifest field requiring the first emitted code to match the first expected code is exactly the check the GR-P03/GR-P04 pairing was built to expose, and attribution as submitter is welcome. On PS1b: the lease-boundary family treats the instant as a declared convention precisely because the record alone cannot decide it — whichever way the audit-record draft settles the boundary, the declared-contract reading stays testable, and we look forward to the resolution.
