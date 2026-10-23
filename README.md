# Aicent Stack — Conformance

Conformance runners and run reports for the RTTP (Resonant Time Transfer Protocol) & IQA (Identity Quality Assurance) dual-pillar stack, published as independent recomputations against the [Agent Authority Conformance lab](https://github.com/Agent-Authority-Conformance/aps-conformance-suite).

## Experiments

| directory | what | upstream |
|---|---|---|
| [`lra-runner/`](lra-runner/) | Independent Python runner + 2026-10-23 conformance run report for the `lease-revocation-axes` family (revision 2, candidate) | [aps-conformance-suite PR #180](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/180) |

Each experiment directory is self-contained: its own runner, vendored frozen inputs, digest gate, provenance and run report. See `lra-runner/README.md` to replay in under a second.

## License

Apache-2.0. Vendored upstream inputs remain the work of their authors, credited per experiment in each directory's PROVENANCE.
