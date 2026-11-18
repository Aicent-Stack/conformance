# Sealed artifact record — replay/grant-ref-replay-sparysh

This file is the repository-side record of the current sealed artifact for the pipeline replay of `sparysh-reading-aicent-grant-ref-20186f3` (lab PR #234, merged 2026-11-17). It is deliberately **not** a member of the sealed tarball: a sealed archive cannot carry its own digest-derived address, because any byte changed inside the archive changes the very digest the address is derived from. The sealed bytes live in the tarball; this file records where they are and how they resolve. It is updated at seal time, before the seal wave is committed — the sealing step precedes every commit and pull request.

## Current cut (first seal, 2026-11-18; page resealed to generation b the same day)

- Artifact: `grant-ref-replay-sparysh-20261118a.tar.gz` (55,217 bytes)
- SHA-256: `38ccc8610382c41c72fe5346def75c0a2d1e7c7d7c95b3e3b9408e36c606bd64`
- Dual addresses: `rttp://38ccc861.conformance.iqa` · `iqa://38ccc8610382c41c72fe5346def75c0a.forge.iqa`
- Resolvers: <https://rttp.com/open/> · <https://iqa.org/open/>
- Report page: <https://iqa.org/conformance/grant-ref-replay-sparysh/>
- Page digest (SEAL display block excluded), generation b: `f02f5ef667cb094122406daffe07a2681de651f15986571b90c95dc9102ef35e`
- Site tarball: `grant-ref-replay-sparysh-site-20261118b.tar.gz` (11,224 bytes) — SHA-256 `29364af455a60b9a1ddec5e2c1f6e8d03c97906412caecee05356e7d47eb7967`
- Page address pair (generation b): `rttp://f02f5ef6.site.iqa` · `iqa://f02f5ef667cb094122406daffe07a268.forge.iqa`

## Ledger and registration

- Ledger: `attestations/release-attestations.json`, dual-station identical (184 records, station SHA-256 `bbb051295d03025ebf938358e039a134e81937aa67c8da634d1dfd261e8d9a3d`)
- Records appended by this wave: `2026-11-18-grant-ref-replay-sparysh` (sealed-run), `2026-11-18-grant-ref-replay-sparysh-page` (site-freeze) and `2026-11-18-replay-reseal-b` (site-freeze — eighteen-block template completion: Oracle checkpoints and On independence added, no recorded number changed; supersedes the generation-a page record, page digest `86750547a60f8f63…`, site tarball `grant-ref-replay-sparysh-site-20261118a.tar.gz`)
- Organ registration: subject `iqa://38ccc8610382c41c72fe5346def75c0a.forge.iqa` — standing `radiant`, organ `forge` (production 62 → 63 subjects)
- Wayback pins: generation-a page capture `20261118094036`; generation-b page capture `20261118113642`

The full per-cut table (every cut's size, SHA-256 and derived address pair) lives on the report page, which is the canonical display layer for the sealing discipline.
