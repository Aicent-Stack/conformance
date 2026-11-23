# Sealed artifact record — replay/lease-boundary-replay-sparysh

This file is the repository-side record of the current sealed artifact for the pipeline replay of `sparysh-reading-aicent-lease-boundary-0e0064b` (lab PR #238, merged 2026-11-23). It is deliberately **not** a member of the sealed tarball: a sealed archive cannot carry its own digest-derived address, because any byte changed inside the archive changes the very digest the address is derived from. The sealed bytes live in the tarball; this file records where they are and how they resolve. It is written at seal time, before the seal wave is committed — the sealing step precedes every commit and pull request.

## Current cut (first seal, 2026-11-24)

- Artifact: `lease-boundary-replay-sparysh-20261124a.tar.gz` (60,210 bytes)
- SHA-256: `d286892febd54b501aad9e6e69e7957b96ebb17f55326ee78aacbd18eb0e5fb6`
- Dual addresses: `rttp://d286892f.conformance.iqa` · `iqa://d286892febd54b501aad9e6e69e7957b.forge.iqa`
- Resolvers: <https://rttp.com/open/> · <https://iqa.org/open/>
- Report page: <https://iqa.org/conformance/lease-boundary-replay-sparysh/>
- Page digest (SEAL display block excluded), generation a: `0ff06e926cf4588f65002abf33dd71f619c081282946496faa575c6843c144f4`
- Site tarball: `lease-boundary-replay-sparysh-site-20261124b.tar.gz` (12,993 bytes) — SHA-256 `454a0bc1ac772493fe237e855e4cbc2297bc0d714892baf948a1d11eb14fd22b`
- Page address pair (generation a): `rttp://0ff06e92.site.iqa` · `iqa://0ff06e926cf4588f65002abf33dd71f6.forge.iqa`

## Ledger and registration

- Ledger: `attestations/release-attestations.json`, dual-station identical (192 records, station SHA-256 `8308f570912cf08fc8944ca26a0821a75e44f3acf3c9fbb5e15aab0e9909795a`)
- Records appended by this wave: `2026-11-24-lease-boundary-replay-sparysh` (sealed-run, artifact) and `2026-11-24-lease-boundary-replay-sparysh-page` (site-freeze, first publication of the report page)
- Organ registration: subject `iqa://d286892febd54b501aad9e6e69e7957b.forge.iqa` — standing `radiant`, organ `forge` (production 65 → 66 subjects, backup `production.json.bak-20261124a-pre65`)
- Wayback pins: report page capture `20261123165838`

The wrapper committed alongside this record is the one extended for this replay: this record's comparison output uses the `match`/`diverge`/`tally_final` summary schema, named through the profile's optional `summary_keys`; the wrapper's default schema is unchanged and the grant-ref replay reproduces byte for byte under the extended wrapper (verified before sealing).

The full per-cut table (every cut's size, SHA-256 and derived address pair) lives on the report page, which is the canonical display layer for the sealing discipline.
