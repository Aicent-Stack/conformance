<!--
Archived from https://github.com/probityai/agent-evidence-vectors/issues/585 on 2026-11-14. First archived 2026-11-13
(sha256 of that generation: 72970bc7cf68fedea15989b303c44f5d56a8c6242bb8055119aa8c3f184654d8); the body was
edited the same day at 14:57:44Z to append the Cross-references section (repository archive + sealed family
report). The text below the marker is the issue body verbatim as it now stands, byte-exact as retrieved,
LF-normalized for storage; sha256 of the archived text (the verbatim section as stored, below the marker): 14e0645b4a873a5de351d838faf2bbe9146b32dbb4dd9b50103df1cd16a705b9.-->

Issue #585 verbatim archive (post-edit generation) — sha256 of archived text: 14e0645b4a873a5de351d838faf2bbe9146b32dbb4dd9b50103df1cd16a705b9
================================================================

Following #544 and the `predicate/v1/refusal-reason-priority` entry: that entry works because the normative set and its order stay in the draft, owned and confirmed by its author, while this repository carries the corpus, the rails, and the page. The same draft fixes a second normative object that is evidence-shaped in exactly the same way, and it is the object those refusal answers are answers **over**: the fixed 128-octet attestation envelope of Section 7.2.

Before drafting anything concrete: does a registration of that object fit the registry's scope — a corpus plus rails in this repository, with the byte layout and the closed verdict set normative in the draft and not vendored here? If it fits, the notes below are what I can supply. If it does not, a one-line no is a complete answer and the subject is closed.

## What the draft normatively fixes

Quoted from `draft-li-rttp-iqa-addressing-02`, Section 7.2 (TXT sha256 `02491c5a59d1e7471be04e8e0d4933dfc22ce19f9b054ead0aa449d6b4485044`, 40 pp., 2026-11-01):

> The attestation envelope is the fixed 128-octet answer frame that carries an iqa attestation answer: the standing verdict, its lease, and its authentication.

Frame layout (offset, length, field), verbatim from the section's table: magic `0x49 0x51 0x41 0x45` (ASCII "IQAE") at 0; version 0x01 at 4; algorithm at 5, `0x01 = HMAC-SHA256`, other values undefined in version 1; flags at 6 (2 octets, unassigned, sent as 0x0000); `lease_expiry` at 8 (8 octets, unsigned big-endian, Unix seconds, "the instant until which the answer counts as fresh (Section 6.1)"); `intent_shard` at 16 (16 octets, ROUTE_SHARD of the subject); `attestation` at 32 (32 octets, HMAC-SHA256 over the frame); organ at 64 (exactly 8 octets of US-ASCII); nonce at 72 (8 octets, unique per verdict issued); standing at 80 (1 octet); reserved at 81 (15 octets, MUST be all zeros); extension at 96 (32 octets, MUST be all zeros in version 1).

The verdict byte is a closed set, verbatim:

> The octet at offset 80 takes one of four values, a closed set fixed in this document: 0x00 (ghost), 0x01 (probation), 0x02 (radiant), 0x03 (genesis). No other value is valid. A receiver MUST reject a frame whose standing byte is outside this set.

The freshness rule is receiver-clock semantics, verbatim from the verification procedure:

> (2) rejects the frame if lease_expiry is earlier than the current time, checked against the receiver's own clock (Section 6.1);

The canonical signing rule, verbatim:

> attestation = HMAC-SHA256(key, frame[0:32] || 0x00*32 || frame[64:128])

with the section's own consequence: "a rewrite of the named answerer, the verdict state, or a replayed frame with a swapped standing does not survive verification."

## What a corpus could measure

Offered as material, not prescribed — the corpus design is this repository's call:

- byte-exact reproduction of the Section 7.2.1 test vector `AE128-VECTOR-1` from the parameters alone, and round-trip acceptance — the draft says any implementation MUST reproduce the frame byte for byte;
- fail-closed negatives: length not 128, wrong magic, wrong version, algorithm byte other than 0x01, standing outside the closed set, non-zero reserved or extension fields;
- lease freshness as a two-instant record: the carried `lease_expiry` and the read instant, with the expected verdict following from the pair — the same receiver-clock shape the refusal corpus already exercises through `observation_as_of_ms`;
- canonical-rule checks: the attestation coverage input (frame with bytes 32..63 zeroed), and rejection of a frame whose attestation field was recomputed over a standing-swapped or organ-swapped variant.

## Sources, ownership, boundaries

- Normative source: `draft-li-rttp-iqa-addressing-02`, Sections 7.2, 7.2.1 and 6.1 — <https://datatracker.ietf.org/doc/draft-li-rttp-iqa-addressing/02/>. The object's emitter and owner: Aicent / ShaoBao Li, the same ownership line `predicate/v1/refusal-reason-priority` already records. A later revision that keeps the layout and the closed set is a new confirmation; any change to either is a new URI — the same rule that entry states.
- Published vectors: the AE-128 fail-closed family is recorded, sealed and byte-replayable, at <https://iqa.org/conformance/aicent-ae128-fail-closed/>; the same vectors are filed as a candidate in the LFDT Agent-Authority-Conformance lab at <https://github.com/Agent-Authority-Conformance/aps-conformance-suite/pull/221>.
- Boundary: the envelope's HMAC key material lives with the verifier per [IQA-SPEC]; corpus records would carry frame bytes and verification outcomes, not keys.
- Naming is yours: `attestation-envelope` is a suggestion in this repository's semantic naming style; the draft itself calls the object the attestation envelope (AE-128).

No vendoring is required either way: the layout and the closed set stay normative in the draft, and the entry would name it the way the refusal entry does.

## Cross-references

- Verbatim archive of this issue, kept by the emitter: <https://github.com/Aicent-Stack/conformance/tree/main/probityai/585/>
- The AE-128 family's sealed live report: <https://iqa.org/conformance/aicent-ae128-fail-closed/>
