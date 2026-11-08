# 483 — the refusal-reason-priority corpus

PR by the venue ([probityai/agent-evidence-vectors#483](https://github.com/probityai/agent-evidence-vectors/pull/483)),
opened 2026-11-07T00:43:21Z, **merged 2026-11-07T18:22:25Z**, filed as "Closes #453" — see [`../453/`](../453/).

What it does (venue's verbatim text in [`PR-RECORDS.md`](PR-RECORDS.md)): the `vectors-refusal-reason-priority`
corpus, built from the records we filed on #453 and anchored to sections 6.1, 7.2, 8.1 and 8.2 of
draft-li-rttp-iqa-addressing-02; it ships a generator, a manifest, Python and Go readers, tests, and
registry/README entries. This is the upstream landing of the manifest field the venue promised in its
#453 response: the first-applicable-condition priority over the closed five-value set is now checkable,
which is exactly the gap the GR-P03/GR-P04 pairing was built to expose.

Our confirmation comment of 2026-11-07T16:27:52Z ([`THREAD.md`](THREAD.md)) verified on our side that the
`corpusDigest` `372fe137c3ce46096ffa0f8d1348d907219189900669a5badee4578e0040ad65`, the provenance block
(author, family links, issue link) and the spec pin sha256 `02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044` all match what we hold, and that the
manifest's priority order reads exactly as section 8.1 fixes it. The venue carries the author credit in
the manifest; per our comment, the family pages will reference the suite now that it has merged
(pending action on https://iqa.org/conformance/).
