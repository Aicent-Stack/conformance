<!--
Archived from https://github.com/probityai/agent-evidence-vectors/issues/494 on 2026-11-09. The text below the marker is the issue body verbatim. The text below the marker is byte-exact as
retrieved, LF-normalized for storage; sha256 of the archived text (the verbatim
section as stored, below the marker): f00960bad4bc8ffdfde7b96b20a374ea89b308f142a558f3136a3bc79a05ab7e.-->

Issue #494 verbatim archive — sha256 of archived text: f00960bad4bc8ffdfde7b96b20a374ea89b308f142a558f3136a3bc79a05ab7e
================================================================

This issue lists which case families from #352 become registered suites, and in which planned release. #352 is the Open Evidence Lab issue, where contributors post test cases. The full roadmap is at https://github.com/probityai/agent-evidence-vectors/blob/main/docs/proposals/suites-roadmap.md.

A case that lives only in an issue comment cannot be pinned to a version, replayed in CI or counted toward a badge. A suite is a row in `corpora/REGISTRY.toml`. It gets its own manifest, a README that states its contract, an Evidence run template for reporting runs, a board row and `contributedBy` credit.

- Release 0.37.0: the request/effect join, and refund-connected (#432).
- Release 0.38.0: billing finality (#435), tool-manifest replay (#346), and a changed call versus a later changed file (#350).
- Also release 0.38.0: physical completion (#80), and the refusal vocabulary from #453 (five refusal reasons in a fixed priority order).
- After each contributor files the registry entry for their family: the EIP-3009 payment effect (#347) and paid-audit records (#247).

A cross-runtime delegation and refusal suite is also planned. It counts as done when two outside runtimes run it in their own CI.

A new case stays on #352 until someone has written an independent checker for it or run an implementation against it.

If your case is in the wrong suite or release above, please reply here with the case and where it belongs.
