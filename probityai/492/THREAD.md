<!--
Archived from https://github.com/probityai/agent-evidence-vectors/issues/492 on 2026-11-09. The text below the marker is the issue's comments verbatim. The text below the marker is byte-exact as
retrieved, LF-normalized for storage; sha256 of the archived text (the verbatim
section as stored, below the marker): be41bfdf3e41a603ef411e6f118bfb04b4332961e6b019bec4d050f943fbba10.
Status at archive time: open; comments on the process are open until 20 Nov.
-->

THREAD verbatim archive — sha256 of archived text: be41bfdf3e41a603ef411e6f118bfb04b4332961e6b019bec4d050f943fbba10
================================================================



===== Aicent-com @ 2026-11-07T16:48:35Z =====
Registry entry for the rttp-refusal slot, filed by the emitter, following the seven items in the RFC.

**URI**: `predicate/v1/refusal-reason-priority`  -  the path form of the contractId already carried by the `vectors-refusal-reason-priority` corpus in PR #483: records in that corpus write the contractId in full as `https://probityai.github.io/agent-evidence-vectors/predicate/v1/refusal-reason-priority`, and this entry names the same URI in registry path form. The RFC table lists this family under the slot name `rttp-refusal`; both names refer to the same family, and we follow the corpus URI unless the slot name should prevail.

**Owner**: Aicent-com (GitHub handle), operating as RTTP & IQA Organization.

**Where the normative field definitions live**: draft-li-rttp-iqa-addressing-02, sections 6.1, 7.2, 8.1 and 8.2  -  official text at https://www.ietf.org/archive/id/draft-li-rttp-iqa-addressing-02.txt, retrieved copy pinned at sha256 02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044. The anchor sentence, verbatim from section 8.1: "For a refusal, the reason is exactly one value from the following closed set, and it is the first value in the list whose condition applies (the priority order is part of this definition)". The closed set in fixed order: evidence_binding_mismatch, evidence_expired, authority_not_determined, authority_revoked, operation_not_permitted. Runnable definitions: the sealed family pages https://iqa.org/conformance/aicent-grant-ref/ and https://iqa.org/conformance/aicent-lease-boundary/ (four-file sets with per-file SHA-256), and the candidates directories at https://github.com/Aicent-Stack/conformance/tree/main/candidates.

**Envelope**: the bare record shape minted by the `vectors-refusal-reason-priority` corpus  -  a JSON object with `contractId` (the URI above), `recordId`, `facts` (the facts the answer was given over), and `response` (the `grantRef` with its lease timestamps, plus the `reason`); the decision is derivable from the record alone. This shape is not an in-toto Statement; if the envelope field must name an in-toto form for this slot, we will file the example wrapped accordingly  -  please confirm which shape the review checklist expects here.

**Example record that validates**: `corpora/vectors-refusal-reason-priority/cases/conformant-expiry-over-revocation/record.json` (record sha256 8fdf1041bc8b0e8dd9c2b47f03649fc7a0f3b313fda633061af309492e5df54f; source case GR-P03; corpus digest 372fe137c3ce46096ffa0f8d1348d907219189900669a5badee4578e0040ad65).

**Compatibility rule**: a v2 is a new URI beside v1, never a change to v1. Within v1 the set is closed and implementations MUST NOT emit values outside it; any change to the value set or to the priority order is a breaking change and goes to a new URI. A later draft revision that leaves the set, the order and the field semantics untouched (for example the pending -03 wording refinements) is compatible and is handled as a new confirmation under confirmed_at, never as an edit of this entry.

**confirmed_at**: Aicent-com confirms draft-li-rttp-iqa-addressing-02 (posted 2026-11-01, sha256 02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044) as the confirmed revision of the field definitions for this entry; this comment is the confirmation record.
