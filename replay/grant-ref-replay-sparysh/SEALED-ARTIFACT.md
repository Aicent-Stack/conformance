# Sealed artifact record — replay/grant-ref-replay-sparysh

This file is the repository-side record of the current sealed artifact for the pipeline replay of `sparysh-reading-aicent-grant-ref-20186f3` (lab PR #234, merged 2026-11-17). It is deliberately **not** a member of the sealed tarball: a sealed archive cannot carry its own digest-derived address, because any byte changed inside the archive changes the very digest the address is derived from. The sealed bytes live in the tarball; this file records where they are and how they resolve. It is updated at seal time, before the seal wave is committed — the sealing step precedes every commit and pull request.

## Current cut (first seal, 2026-11-18; page resealed to generations b and c the same day)

- Artifact: `grant-ref-replay-sparysh-20261118a.tar.gz` (55,217 bytes)
- SHA-256: `38ccc8610382c41c72fe5346def75c0a2d1e7c7d7c95b3e3b9408e36c606bd64`
- Dual addresses: `rttp://38ccc861.conformance.iqa` · `iqa://38ccc8610382c41c72fe5346def75c0a.forge.iqa`
- Resolvers: <https://rttp.com/open/> · <https://iqa.org/open/>
- Report page: <https://iqa.org/conformance/grant-ref-replay-sparysh/>
- Page digest (SEAL display block excluded), generation c: `16bc13e0c39c4bb21ea3fe0700a48231c4d6357001b78f6a40fd040998cd0323`
- Site tarball: `grant-ref-replay-sparysh-site-20261118c.tar.gz` (11,238 bytes) — SHA-256 `a301caa44231ed44aa47583794decac0da2dfa741829bd7990e082300cb68a35`
- Page address pair (generation c): `rttp://16bc13e0.site.iqa` · `iqa://16bc13e0c39c4bb21ea3fe0700a48231.forge.iqa`

## Ledger and registration

- Ledger: `attestations/release-attestations.json`, dual-station identical (185 records, station SHA-256 `573eb7727cc47b6547f6c13001028bd30c3d3bbc2860a0f3b99bcd6df8bd0e76`)
- Records appended by this wave: `2026-11-18-grant-ref-replay-sparysh` (sealed-run), `2026-11-18-grant-ref-replay-sparysh-page` (site-freeze), `2026-11-18-replay-reseal-b` (site-freeze — eighteen-block template completion: Oracle checkpoints and On independence added; supersedes the generation-a page record, page digest `86750547a60f8f63…`, site tarball `grant-ref-replay-sparysh-site-20261118a.tar.gz`) and `2026-11-18-replay-reseal-c` (site-freeze — CRLF attribution direction corrected in the Results sentence per the record author's follow-up: the record was produced on Linux with LF-native outputs, the CRLF was written by the replay host on Windows; display-only repair of a doubled scheme prefix in the generation-b seal line; no recorded number changed; supersedes `2026-11-18-replay-reseal-b`, site tarball `grant-ref-replay-sparysh-site-20261118b.tar.gz`)
- Organ registration: subject `iqa://38ccc8610382c41c72fe5346def75c0a.forge.iqa` — standing `radiant`, organ `forge` (production 62 → 63 subjects)
- Wayback pins: generation-a page capture `20261118094036`; generation-b page capture `20261118113642`; generation-c submit deduped by the archive to the morning capture `20261118094036` (short-window dedup; weekly cron backfills)

The full per-cut table (every cut's size, SHA-256 and derived address pair) lives on the report page, which is the canonical display layer for the sealing discipline.
