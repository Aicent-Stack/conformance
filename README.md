# conformance

This is the central registry of sealed, byte-replayable conformance run records for the **RTTP & IQA** dual-pillar line. Every run against an external conformance suite — independently produced or author-produced — is recorded here as a self-contained, offline-replayable directory and indexed below. Human-readable report pages live at [iqa.org/conformance/](https://iqa.org/conformance/).

## What a run record is

Each record directory is self-contained and carries everything needed to re-run the measurement offline:

- **the runner** — the exact code that was run;
- **vendored frozen inputs** — the test vectors and oracle material, frozen before the run and pinned by digest;
- **a digest gate** — the runner refuses to execute if the frozen inputs do not match their recorded digests;
- **PROVENANCE** — what the inputs are, whose work they vendor, and how this run relates to its authors (author-produced or independently produced is always stated; the lab's charter asks for nothing less);
- **the run report** — the recorded output, sealed per the IQA release discipline.

## Records

| directory | family | revision | mode | recorded | lab record |
|---|---|---|---|---|---|
| [`lra-runner/`](lra-runner/) | lease-revocation-axes | 2 | author-produced (Mode B) | 2026-10-23 | [PR #187](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/187) (merged) |
| [`lra-runner/`](lra-runner/) | lease-revocation-axes | 3 | author-produced (Mode B) | 2026-10-26 | [PR #194](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/194) (merged) |
| [`aae-runner/`](aae-runner/) | moltycel-aae-vectors (AAE) | fixture v0 | independently produced | 2026-11-04 | [PR #215](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/215) (merged) |
| [`icam-runner/`](icam-runner/) | icam-temporal-derivation (ICAM) | candidate v0.3 | independent (non-author-produced) | 2026-11-08 | [PR #218](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/218) (open) |

Classification follows the lab's definition (`CONTRIBUTING.md`): a record is *independent* when its producer authored neither the vectors, the claim inputs, nor the implementation that supplies the recomputation — here the operator wrote the runner, so both records are author-produced, while the runner itself (`lra_runner.py`) is written independently of the lab's corpus. Larry Lewis independently reproduced both revisions on 2026-10-29 (zero baseline failures, all 12 mutation failure sets matching); a replay of these records by an operator who authored none of the above may be recorded alongside as an independently produced record. The `aae-runner` record is independently produced: the family, its vectors, and its pipeline are the work of Lars Kersten Kroehl (MoltyCel), merged upstream as PR #190; our operator ran the candidate's own pipeline unmodified and recorded the output. The `icam-runner` record is a non-author run of a third-party candidate: the vectors, the claim inputs, and the candidate harness are the work of Nika Novak (ICAM), filed upstream as [PR #218](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/218) (head `72a0f72`, pre-merge); our operator wrote the runner from the published draft text (§§6.1 / 6.3 / 7.2) without reference to the candidate's oracle — the candidate's input and result vocabulary is adopted only as the interface contract — and recorded the candidate's own harness reproduction (24/24, 8/8 mutants, 120/120 metamorphic, run as-is) alongside the independent runner's agreement (24/24, with 6/6 mutants killed by an independent battery).

The specification under test is the combined Individual Submission Internet-Draft [`draft-li-rttp-iqa-addressing`](https://datatracker.ietf.org/doc/draft-li-rttp-iqa-addressing/) (revision -02, 40 pp., 2026-11-01); each record's own README names the sections it exercises.

## Vector families

Two vector families of our own authorship are merged into the lab's mainline as candidates; each anchors every expectation to published sections of the specification under test and ships with its own mutation battery:

- [`candidates/aicent-grant-ref/`](candidates/aicent-grant-ref/) — the response semantics of an attestation answer: which refusal value the closed vocabulary owes, when the observation member must be null, and which structure members every response carries. Merged upstream as [PR #210](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/210) (2026-11-03). Family page: [iqa.org/conformance/aicent-grant-ref/](https://iqa.org/conformance/aicent-grant-ref/).
- [`candidates/aicent-lease-boundary/`](candidates/aicent-lease-boundary/) — the lease of an attestation answer: which boundary convention an implementation may declare and apply at the lease instant, what an expired lease still owes, how the declared answer mode shapes the refusal when the organ cannot be reached, and which expiry a verifier checks. Merged upstream as [PR #212](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/212) (2026-11-03). Family page: [iqa.org/conformance/aicent-lease-boundary/](https://iqa.org/conformance/aicent-lease-boundary/).

## External evaluations

Other venues have evaluated the families against their own contracts. Those evaluations are recorded as
thread archives — verbatim issue text and responses, pinned by digest — not as run records: no runner
executed, so there is nothing to replay.

- [`probityai/`](probityai/) — the thread with [probityai/agent-evidence-vectors](https://github.com/probityai/agent-evidence-vectors): our five-record crosswalk filed as issue [#453](https://github.com/probityai/agent-evidence-vectors/issues/453) (closed completed), the venue's refusal-reason-priority corpus built from those records ([PR #483](https://github.com/probityai/agent-evidence-vectors/pull/483), merged, digest-confirmed by us), the predicate-registry RFC ([#492](https://github.com/probityai/agent-evidence-vectors/issues/492), our `predicate/v1/refusal-reason-priority` entry filed) and the suites roadmap ([#494](https://github.com/probityai/agent-evidence-vectors/issues/494), open). Per-node verbatim archives: [`probityai/453/`](probityai/453/) · [`probityai/469/`](probityai/469/) · [`probityai/483/`](probityai/483/) · [`probityai/492/`](probityai/492/) · [`probityai/494/`](probityai/494/).

## Replay

Each directory's README carries the exact command. Replaying a record is a single local command — no account, no network, no trust required; the digest gate fails closed if anything has drifted.

## Sealing and addresses

Stabilized records are sealed per the IQA release discipline and appended to the release-attestations bundles ([rttp.com/attestations/](https://rttp.com/attestations/) · [iqa.org/attestations/](https://iqa.org/attestations/)). Sealed records carry dual addresses and resolve through the public resolvers: `rttp://…` → [rttp.com/open/](https://rttp.com/open/) · `iqa://…` → [iqa.org/open/](https://iqa.org/open/).

## Citation norm

Run reports ship with a citation block naming the runner, its repository, and its operator. Any public reference to an independent run is asked to carry the same three facts.

## Related

- [`rttp`](https://github.com/Aicent-Stack/rttp) — the addressing scheme, Rust implementation
- [`iqa-org`](https://github.com/Aicent-Stack/iqa-org) — attestation standing and envelopes, Rust implementation
- [`iqa-mcp`](https://github.com/Aicent-Stack/iqa-mcp) — the primitives as MCP tools
- [`interchange`](https://github.com/Aicent-Stack/interchange) — multi-party interchange work
- [`azuli.com`](https://azuli.com/) — Azuli, the public brand of this verification venue, operated by the RTTP & IQA Organization
- [`agent-evidence-vectors`](https://github.com/probityai/agent-evidence-vectors) — the Probity AI audit-record contract; venue of the #453–#494 thread (see [`probityai/`](probityai/))
- Organization profile — [github.com/Aicent-Stack](https://github.com/Aicent-Stack)

## License

Apache-2.0. Vendored upstream inputs remain the work of their authors, credited per record in each directory's PROVENANCE.
