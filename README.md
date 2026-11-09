# conformance

This is the central registry of sealed, byte-replayable conformance run records for the **RTTP & IQA** dual-pillar line. Every run against an external conformance suite — independently produced or author-produced — is recorded here as a self-contained, offline-replayable directory and indexed below. Human-readable report pages live at [iqa.org/conformance/](https://iqa.org/conformance/).

## Directory layout — one top-level folder per lab or project

| folder | lab / project | contents |
|---|---|---|
| [`lra-runner/`](lra-runner/) | **Aicent Stack** (RTTP & IQA, ours) — lease-revocation-axes family | our own runner over our own family (lab PRs #187 / #194) |
| [`candidates/`](candidates/) | **Aicent Stack** (RTTP & IQA, ours) — six vector families | our vector families; two merged into the lab mainline (PRs #210 / #212), four filed as candidates there |
| [`interop/`](interop/) | **Aicent Stack** (RTTP & IQA, ours) | clarification records from the lab interop filings |
| [`aae-runner/`](aae-runner/) | **MoltyCel** (Lars Kersten Kroehl) — moltycel-aae-vectors | our independent run of their pipeline (lab PR #215) |
| [`icam-runner/`](icam-runner/) | **ICAM** (Nika Novak, danyka-icam) — icam-temporal-derivation | our independent runner over their candidate (lab PR #218) |
| [`probityai/`](probityai/) | **Probity AI** (Gilda, @astrogilda) — agent-evidence-vectors | thread archive of the crosswalk, per-node: #453 / #469 / #483 / #492 / #494 |

**Paths are frozen.** External filings reference these directories directly — issue [#453](https://github.com/probityai/agent-evidence-vectors/issues/453) and the registry entry on [#492](https://github.com/probityai/agent-evidence-vectors/issues/492) cite `…/tree/main/candidates` verbatim, and the lab's merged records vendor these paths — so existing top-level directories will not be moved or renamed. A new lab or project joins under a single top-level folder of its own (the `probityai/` pattern); established paths stay as first published.

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

Six vector families of our own authorship live under `candidates/`; each anchors every expectation to published sections of the specification under test and ships with its own mutation battery. Two are merged into the lab's mainline; four are filed as candidates there. Every family has a sealed recorded-run report page under [iqa.org/conformance/](https://iqa.org/conformance/), produced by the shared harness [`family_runner.py`](family-runner/family_runner.py) — author-produced, deterministic recorded output (no timestamps, no paths, byte-replayable); across the six families: 125/125 cases agree, 94/94 mutants killed, exit 0.

- [`candidates/aicent-grant-ref/`](candidates/aicent-grant-ref/) — the response semantics of an attestation answer: which refusal value the closed vocabulary owes, when the observation member must be null, and which structure members every response carries. Merged upstream as [PR #210](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/210) (2026-11-03). Family page: [iqa.org/conformance/aicent-grant-ref/](https://iqa.org/conformance/aicent-grant-ref/).
- [`candidates/aicent-lease-boundary/`](candidates/aicent-lease-boundary/) — the lease of an attestation answer: which boundary convention an implementation may declare and apply at the lease instant, what an expired lease still owes, how the declared answer mode shapes the refusal when the organ cannot be reached, and which expiry a verifier checks. Merged upstream as [PR #212](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/212) (2026-11-03). Family page: [iqa.org/conformance/aicent-lease-boundary/](https://iqa.org/conformance/aicent-lease-boundary/).
- [`candidates/aicent-ae128-fail-closed/`](candidates/aicent-ae128-fail-closed/) — byte-level fail-closed discipline of the attestation envelope: the parse-time rejection rules applied before any cryptographic work, the canonical HMAC coverage rule, and the published test vector reproduced byte for byte. Family page: [iqa.org/conformance/aicent-ae128-fail-closed/](https://iqa.org/conformance/aicent-ae128-fail-closed/).
- [`candidates/aicent-pulse-header/`](candidates/aicent-pulse-header/) — the pulse header, wire and behavior: the fixed 128-octet frame layout, the extension-block rules, and the time-and-order semantics (TTL forwarding, timestamp age against standing). Family page: [iqa.org/conformance/aicent-pulse-header/](https://iqa.org/conformance/aicent-pulse-header/).
- [`candidates/aicent-uri-grammar/`](candidates/aicent-uri-grammar/) — the rttp URI grammar: the ABNF (three dot-separated segments, hash-intent versus name-intent, single-segment action) and the exclusions, with one disclosed tightening and one licensed ambiguous edge. Family page: [iqa.org/conformance/aicent-uri-grammar/](https://iqa.org/conformance/aicent-uri-grammar/).
- [`candidates/aicent-route-shard/`](candidates/aicent-route-shard/) — the ROUTE_SHARD derivation: SHA-256 over the ASCII of the canonical authority truncated to 16 octets, the authority-only and canonical-form boundaries, and the display-form red line. Family page: [iqa.org/conformance/aicent-route-shard/](https://iqa.org/conformance/aicent-route-shard/).

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
