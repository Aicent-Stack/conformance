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

Classification follows the lab's definition (`CONTRIBUTING.md`): a record is *independent* when its producer authored neither the vectors, the claim inputs, nor the implementation that supplies the recomputation — here the operator wrote the runner, so both records are author-produced, while the runner itself (`lra_runner.py`) is written independently of the lab's corpus. Larry Lewis independently reproduced both revisions on 2026-10-29 (zero baseline failures, all 12 mutation failure sets matching); a replay of these records by an operator who authored none of the above may be recorded alongside as an independently produced record.

The specification under test is the combined Individual Submission Internet-Draft [`draft-li-rttp-iqa-addressing`](https://datatracker.ietf.org/doc/draft-li-rttp-iqa-addressing/) (revision -01, 34 pp., 2026-10-27); each record's own README names the sections it exercises.

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
- Organization profile — [github.com/Aicent-Stack](https://github.com/Aicent-Stack)

## License

Apache-2.0. Vendored upstream inputs remain the work of their authors, credited per record in each directory's PROVENANCE.
