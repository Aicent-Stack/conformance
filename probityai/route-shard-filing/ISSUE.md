RTTP/IQA -03: the ROUTE_SHARD derivation — seven records (sixteen cases) from the aicent-route-shard family: deterministic derivation, canonical-form boundary, display-form red line

The families filed in #453 tested attestation answers — the refusal vocabulary and the lease. This filing introduces the addressing side of the same draft: the ROUTE_SHARD derivation of the rttp scheme. These vectors are pure computation — every expected value is recomputable from the standard library's SHA-256 alone, with no keys, no network, and no state — so they can serve as deterministic derivation fixtures wherever a corpus wants inputs whose expected outputs are fixed by published text. The family is merged into the LFDT Agent-Authority-Conformance lab mainline (PR [#224](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/224), 17 November) and sealed with per-file SHA-256 at https://iqa.org/conformance/aicent-route-shard/ — sixteen cases (3 derivation, 13 property) filed below as seven records; author's runs 16/16 agree, 9/9 mutants killed, exit 0.

Texts: draft-li-rttp-iqa-addressing-03 (https://www.ietf.org/archive/id/draft-li-rttp-iqa-addressing-03.txt, retrieved copy pinned at sha256 73470850daae844c51f281d6acf6d74419bb1b8c762270f1c411469c78cbc52c), sections 4.4 (The Address: ROUTE_SHARD Derivation), 4.2 (Reserved Characters and Exclusions), 9.1 (The rttp scheme) and the published vector of section 7.2.1. Canonical sources: https://github.com/Aicent-Stack/conformance — candidates/aicent-route-shard (https://github.com/Aicent-Stack/conformance/tree/main/candidates/aicent-route-shard; CANDIDATE.md, vectors.json, check.py, mutate.py), mirrored in the lab mainline at https://github.com/Agent-Authority-Conformance/aps-conformance-suite/tree/main/candidates/aicent-route-shard.

Revision note: the sealed lab records keep their revision-02 pins (sha256 02491c5a...); the cases retain proposed behavior and were re-assessed against revision 03 (sha256 73470850...), whose sections 4.2, 4.4 and 9.1 carry the rules these cases test. Every expected address quoted in this filing was recomputed with the standard library's SHA-256 at filing time and matches the vectors.json values.

The derivation itself (sect. 4.4): canonical_authority = intent "." pillar "." root (lowercase, US-ASCII); ROUTE_SHARD = SHA-256(ASCII(canonical_authority))[0:16] — "The authority only: the scheme name, "//" and any action are excluded." Its four properties: deterministic, pure computation (no DNS, no registry, no lookup), one-way, and action-independent — "an address is where, not what — and not when".

Mapping to the contract used here (offered as a crosswalk, not a claim of equivalence):

| this suite | our draft (-03) |
| --- | --- |
| deterministic, byte-replayable vectors | sect. 4.4 derivation + the draft's own published vector (sect. 7.2.1 pins 557c8154d3780cb78cc5fa1bd72b331c for the authority f3b2a1c4.pillar.example) |
| canonical-form handling of identifiers | sect. 4.2: "Uppercase is invalid input, not a formatting difference: a parser MUST NOT normalise it, because two distinct strings would then map onto one address." |
| identifier hygiene | sect. 9.1: the 8-hex display forms "are display conveniences over the full hash forms and MUST NOT be used as the sole identifier of a subject (Sections 4.1 and 5.1)." — a 32-bit space, birthday bound roughly 2^16 adoptions |

Records 1-3 — the derivation (R-SHARD, R-ACTION-INDEPENDENT):

**Record 1 (RS-D01): the draft pins its own cross-section vector.** Facts: the authority f3b2a1c4.pillar.example, the sect. 4.1 example. Expected: SHA-256(ASCII(authority))[0:16] = 557c8154d3780cb78cc5fa1bd72b331c — the same value section 7.2.1 publishes inside the AE128-VECTOR-1 frame (bytes 16..31). This is the rare case where a specification pins its derivation to a second section, and a checker can hold both together.

**Record 2 (RS-B01/B02, paired): action-independence.** Facts: two actions on one authority — rttp://f3b2a1c4.pillar.example/vessel and rttp://f3b2a1c4.pillar.example/verify. Expected verdict: both yielding the same address is conformant (B01); different addresses per action is nonconformant (B02) — "Were the action to participate in derivation, two actions on one subject would become two addresses, splitting one subject into several."

**Record 3 (RS-B04): the whole URI string is not the derivation input.** Facts: SHA-256 over the full URI string rttp://f3b2a1c4.pillar.example/vessel yields 437e89b8d2c646e01f96ff9c84461704. Expected verdict: nonconformant — the scheme name, "//" and the action are excluded; only the bare authority f3b2a1c4.pillar.example derives to the published 557c8154d3780cb78cc5fa1bd72b331c (RS-B03).

Records 4-6 — the canonical-form boundary (R-CANONICAL-FORM):

**Record 4 (RS-B05/B06, paired): uppercase is refused, not lowercased.** Facts: the authority F3B2A1C4.PILLAR.EXAMPLE. Expected verdict: refusing the derivation is conformant (B05); silently lowercasing before hashing — which lands on the published 557c8154d3780cb78cc5fa1bd72b331c — is nonconformant (B06): "a parser MUST NOT normalise it, because two distinct strings would then map onto one address."

**Record 5 (RS-B07): non-ASCII input is refused.** Facts: the authority f3b2a1c4.pillár.example (one non-ASCII label character). Expected verdict: conformant when the derivation refuses — canonical_authority is lowercase US-ASCII, and ASCII() of such input is undefined.

**Record 6 (RS-B09): the intent segment alone is not the input.** Facts: SHA-256 over f3b2a1c4 alone yields 24a1c6f17abb7f9041edeb8db20ea7ac. Expected verdict: nonconformant — canonical_authority is intent.pillar.root; the pillar and root participate (RS-B10 holds the same facts in the correct form and is conformant).

Record 7 — the display-form red line (R-DISTINCT-AUTHORITIES):

**Record 7 (RS-B12/B13, paired): the 8-hex display form is not an identifier.** Facts: two distinct authorities (f3b2a1c4.pillar.example, f3b2a1c4.other.example). Expected verdict: routing by the 8-hex display form alone and treating them as one subject is nonconformant (B12) — the display forms fix a 32-bit space whose birthday bound makes them unfit as sole identifiers; using the display form as a convenience over the full hash forms while the derivation keeps the authorities distinct is conformant (B13).

What these records do not claim: the author's runs say nothing about any implementation, and they do not show that the expected results are the right reading of the source — the reading is written out in the CANDIDATE for anyone to dispute, sentence by sentence, and a correction in a later draft revision overrides the checker. No implementation has been run against these cases beyond the author's own checker-and-mutant batteries. The collision bounds of section 9.1 (approximately 2^128 substitution, 2^64 birthday) are design accounts quoted in case notes, not conformance targets; RS-B11 is a distinctness spot check, not a collision search.

Citation: family aicent-route-shard · repository github.com/Aicent-Stack/conformance (lab mainline: Agent-Authority-Conformance/aps-conformance-suite, merged via PR [#224](https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/224)) · operator ShaoBao Li (Lee) / Aicent Stack, RTTP CRI 27 · IQA CRI 28 · sealed family page with per-file SHA-256: https://iqa.org/conformance/aicent-route-shard/ · Sister pillars: RTTP (rttp://, CRI 27) · IQA (iqa://, CRI 28) — https://rttp.com · https://iqa.org
