# 492 — RFC: register domain predicate types under predicate/v1

Issue opened by the venue ([probityai/agent-evidence-vectors#492](https://github.com/probityai/agent-evidence-vectors/issues/492)),
2026-11-07T04:25:49Z, **open**; comments on the process are open until 20 Nov (see [`ISSUE-RECORDS.md`](ISSUE-RECORDS.md)).

What it proposes: a process by which an outside project registers a predicate type for its own record
family — the emitter files the entry (URI under `predicate/v1/`, owner, field definitions, envelope, one
valid example, compatibility rule, `confirmed_at`), a published review checklist decides the merge, and
every correction stays visible. Six record families already hold reserved slots; the refusal vocabulary
from #453 (five refusal reasons in a fixed priority order) is one of them.

Our action (2026-11-07T16:48:35Z, [`THREAD.md`](THREAD.md)): the registry entry for the `rttp-refusal`
slot, filed by the emitter per the RFC's seven items — URI `predicate/v1/refusal-reason-priority` (the
path form of the `vectors-refusal-reason-priority` corpus contractId from #483), owner Aicent-com (RTTP
& IQA Organization), normative definitions = draft-li-rttp-iqa-addressing-02 sections 6.1, 7.2, 8.1 and
8.2 (spec pin sha256 `02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044`), the corpus's bare record envelope, one validating example (source case
GR-P03, record sha256 `8fdf1041bc8b0e8dd9c2b47f03649fc7a0f3b313fda633061af309492e5df54f`, corpus digest
`372fe137c3ce46096ffa0f8d1348d907219189900669a5badee4578e0040ad65`), the compatibility rule, and
`confirmed_at` = draft -02 as the confirmed revision.

Open question we asked and its state: whether the envelope field must name an in-toto form for this slot —
we filed the bare record shape and asked the review checklist to confirm; no answer yet at archive time.
