# 585 — Registration candidate: predicate for the AE-128 attestation envelope

Issue filed by us ([probityai/agent-evidence-vectors#585](https://github.com/probityai/agent-evidence-vectors/issues/585)),
2026-11-13T14:50:24Z, **open** (see [`ISSUE-RECORDS.md`](ISSUE-RECORDS.md) for the verbatim archive).

What it proposes: a registration candidate for the second normative object the draft fixes — the
fixed 128-octet attestation envelope of draft-li-rttp-iqa-addressing-02 Section 7.2 (sha256
`02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044`), evidence-shaped in the same way
as the `predicate/v1/refusal-reason-priority` entry already registered via #492: layout and closed
verdict set stay normative in the draft, this repository would carry the corpus and the rails, no
vendoring required. The opening question asks whether the object fits the registry's scope; a
one-line no is stated to be a complete answer.

Material offered if the scope fits: byte-exact reproduction of the Section 7.2.1 vector
`AE128-VECTOR-1`; fail-closed negatives (length, magic, version, algorithm, standing outside the
closed set, non-zero reserved/extension); lease freshness as a two-instant record (the same
receiver-clock shape the refusal corpus exercises through `observation_as_of_ms`); canonical-rule
checks (zeroed attestation coverage input; rejection of standing-swapped or organ-swapped variants).

Sources in the issue: the sealed family report at <https://iqa.org/conformance/aicent-ae128-fail-closed/>
and the same vectors as a candidate in the LFDT lab ([PR #221](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/221), open at archive time).
HMAC key material stays with the verifier; corpus records would carry frame bytes and verification
outcomes, not keys. Naming is the venue's call; `attestation-envelope` is offered as a suggestion.
