# 544 — feat(registry): register refusal-reason-priority, fix Pages

PR opened and merged by the venue ([probityai/agent-evidence-vectors#544](https://github.com/probityai/agent-evidence-vectors/pull/544),
operator Gilda, @astrogilda): opened 2026-11-08T19:39:23Z, **merged 2026-11-10T20:32:28Z**,
merge commit `f76e5fe83d4d7eb642d963f79cd75e030dba8308`; no comments (see
[`ISSUE-RECORDS.md`](ISSUE-RECORDS.md) for the verbatim archive).

What it did, in two commits:

1. **Pages repair.** The site had stopped deploying since 7 Nov 05:35Z and two registry type URIs
   returned 404 (`predicate/v1/refusal-reason-priority` and `predicate/v1/control-decision`); the
   navigation-test fixture now derives its expectations from the registry itself.
2. **The registration.** Our emitter filing from #492 was cast into the registry's formal entry for
   `predicate/v1/refusal-reason-priority` — the bare record envelope, the draft revision pin
   (draft-li-rttp-iqa-addressing-02, sha256 `02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044`),
   the author confirmation, one example record (sha256 `8fdf1041`), and the compatibility rule.
   The RFC table points the `rttp-refusal` slot at this URI, and the corpus checker answers 33 of 33.

Why this node matters to our line: the five-value closed refusal set that entered through our
[#453](../453/) records and was filed by us as the emitter in [#492](../492/) is now a registered
predicate type in the venue's registry, under its own URI, with the author confirmation recorded.
No action was required from us; the venue made all venue-side changes upstream.
