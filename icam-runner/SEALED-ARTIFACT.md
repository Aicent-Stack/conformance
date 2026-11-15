# Sealed artifact record — icam-runner

This file is the repository-side record of the current sealed artifact for the icam-temporal-derivation run. It is deliberately **not** a member of the sealed tarball: a sealed archive cannot carry its own digest-derived address, because any byte changed inside the archive changes the very digest the address is derived from. The sealed bytes live in the tarball; this file records where they are and how they resolve. It is updated at seal time, before the seal wave is committed — the sealing step precedes every commit and pull request.

## Current cut (sixth seal, 2026-11-16)

- Artifact: `icam-runner-20261116a.tar.gz` (16,319 bytes)
- SHA-256: `dcc63ae4888ada873e71395e122d5c6c8d10ad434094b660229f585d0a4b80ce`
- Dual addresses: `rttp://dcc63ae4.conformance.iqa` · `iqa://dcc63ae4888ada873e71395e122d5c6c.forge.iqa`
- Resolvers: <https://rttp.com/open/> · <https://iqa.org/open/>
- Report page: <https://iqa.org/conformance/icam-runner/>
- Page digest (SEAL display block excluded): `531c77a20d70a47c4a20f4da4b3f911fca0dae46b05298d75072d9696c27ead4`
- Site tarball: `icam-runner-site-20261116a.tar.gz` — SHA-256 `8d612a98d6d1ad439bc7d8a33b527736995cace535a13bfc0b38f3a67d6f58a9`

## Ledger and registration

- Ledger: `attestations/release-attestations.json`, dual-station identical (174 records, station SHA-256 `9b4cb15b69b7d93d63d607c6a38071182410e8cfa3342f72935de46023c1b469`)
- Records appended by this wave: `2026-11-16-icam-rerun-record` (sealed-run) and `2026-11-16-icam-rerun-record-page` (site-freeze)
- Organ registration: subject `iqa://dcc63ae4888ada873e71395e122d5c6c.forge.iqa` — standing `radiant`, organ `forge`
- Supersedes: `2026-11-15-icam-pin-boundary` (artifact SHA-256 `135e2d2222675e32…`) and `2026-11-15-icam-pin-boundary-page` (page digest `7c29b72292ff9119…`)

The full per-cut table (every cut's size, SHA-256 and derived address pair) lives on the report page, which is the canonical display layer for the sealing discipline.
