# Production-code mapping (author-produced, informational)

**What this is.** A mapping from the `lease-revocation-axes` family's decision fields to the production surface we publish today. This is not a run report and must not be read as one: no vectors were scored here. It is the honest answer to "what would an author-code run over these vectors look like" — and the reason we are not publishing one.

**What was checked (2026-10-23).** A fresh install of [`rttp` 1.3.1 from PyPI](https://pypi.org/project/rttp/) into a clean virtual environment; its self-test passes 80 checks with 3 skipped on a default install (the Ed25519 vector checks), and the full 83/83 with the optional Ed25519 backend — both matching the numbers published in the package description.

**Why the vectors admit no code-level run at revision 2.** The frozen vectors are deliberately crypto-free: timelines contain only `call` / `revoke` / `availability` events, evidence is an abstract record (`issued_at_ms`, `expires_at_ms`, `status`, `allowed_operations`), and there are no keys, signatures, or URIs anywhere in the bytes. They exercise the **policy layer** (lease arithmetic, revocation propagation, current-observation semantics). Our published packages ship the **addressing and crypto layer**. An adapter that fed these vectors to production code would therefore have to reimplement the entire verifier policy itself and let production functions rubber-stamp it — which is exactly the circularity an author-code run must not commit. So we publish this mapping instead.

## Mapping table

| family decision field | closest production primitive (rttp 1.3.1) | coverage today |
|---|---|---|
| `evidence_binding` | `seal.sign` / `seal.verify` — HMAC over canonical bytes; `aid.derive_from_entropy` — subject derivation; `rttp_uri.parse` / `parse_and_derive` / `derive_route_shard` — address well-formedness | **partial.** Integrity and subject-identity layers exist and are vector-tested (80/80 scoreable self-test checks), but the family vectors carry no signed material, so there is nothing to feed them. |
| `evidence_freshness` | `seal.verify` — the timestamp is inside the signature, with a clock-skew tolerance | **mechanism exists, policy does not.** Signed time is a production fact; the 120 s lease-TTL check from `issued_at_ms` is integrator-side today. A production lease primitive is on our roadmap. |
| `authority_answer` / `current_validity` / `observation` | none in `rttp` (standing/lease semantics are IQA-side; `iqa-mcp` AE-128 envelopes carry a lease but ship no standing registry) | **not in package.** |
| `action_decision` / `downstream_reached` | none in `rttp` (policy layer, integrator-side by design) | **not in package.** |
| `verification_accepted` (composite) | composed of the rows above | follows those rows. |

## What would change this

- A suite family that ships **signed material** (keys, envelopes, URIs) would let us run the crypto layer directly — no reimplementation needed.
- Or, on our side, landing a **production lease primitive** (TTL-anchored freshness over signed evidence) and a standing-feed adapter, which would let the policy rows in the table above move to "in package".

Either development will be followed by a real author-code run in this repository, published as a separate experiment directory with its own report — not folded into the independent run.
