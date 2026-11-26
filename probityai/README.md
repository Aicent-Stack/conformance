# probityai — thread index for the Probity AI audit-record contract

Venue: [probityai/agent-evidence-vectors](https://github.com/probityai/agent-evidence-vectors) (operator:
Gilda, @astrogilda). Each node below carries a verbatim archive of its issue/PR text and comments, pinned
by digest in the archive headers. Filed as issues and comments only — no pull request was opened by us on
the venue's side; all venue-side changes are made upstream by the venue.

## Timeline (UTC; verified live 2026-11-26)

- 2026-11-04 17:13 — [`refusal-vocabulary-filing/`](refusal-vocabulary-filing/) — we filed issue #453: five records from the aicent-grant-ref and aicent-lease-boundary families under the contract's crosswalk
- 2026-11-06 23:16 — [`principal-standing-rows/`](principal-standing-rows/) — PR #469 merged: PS1/PS2/PS1b principal-standing rows added to the audit-record corpus; PS1b is the case the venue matched to our Record 5
- 2026-11-07 00:43 — PR #483 opened, built from the #453 records ("Closes #453")
- 2026-11-07 04:25 / 04:27 — [`predicate-registry-rfc/`](predicate-registry-rfc/) / [`suites-roadmap/`](suites-roadmap/) — the venue opened the predicate-registry RFC and the suites roadmap; the refusal vocabulary holds a reserved slot in both
- 2026-11-07 16:27 — [`refusal-reason-priority-corpus/`](refusal-reason-priority-corpus/) — our confirmation comment: corpusDigest `372fe137c3ce46096ffa0f8d1348d907219189900669a5badee4578e0040ad65`, provenance block and spec pin all match
- 2026-11-07 16:48 — [`predicate-registry-rfc/`](predicate-registry-rfc/) — our registry entry for `predicate/v1/refusal-reason-priority` filed per the RFC's seven items
- 2026-11-07 18:22 — [`refusal-reason-priority-corpus/`](refusal-reason-priority-corpus/) — PR #483 merged; [`refusal-vocabulary-filing/`](refusal-vocabulary-filing/) closed as completed one minute later
- 2026-11-13T14:50:24Z — [`attestation-envelope-candidate/`](attestation-envelope-candidate/) — we filed issue #585: registration candidate for the AE-128 attestation envelope (draft -02 sec. 7.2/7.2.1), the object the refusal answers are answers over
- 2026-11-08 19:39 — the venue opened PR #544: cast our #492 emitter filing into the formal registry entry for `predicate/v1/refusal-reason-priority`, and repaired the Pages build (two type URIs 404)
- 2026-11-10 20:32 — [`refusal-reason-priority-registration/`](refusal-reason-priority-registration/) — PR #544 merged (f76e5fe8): our refusal vocabulary is now a registered predicate type, RFC table `rttp-refusal` slot points at the URI, corpus checker 33/33
- open — #492 comments open until 20 Nov; [`suites-roadmap/`](suites-roadmap/) roadmap pending discussion
- 2026-11-26 15:11 — [`lease-boundary-filing/`](lease-boundary-filing/) — we filed issue [#759](https://github.com/probityai/agent-evidence-vectors/issues/759): the full lease-boundary family filing (nine records over the fifteen cases), anchored to draft -03
- 2026-11-26 15:11 — [`route-shard-filing/`](route-shard-filing/) — we filed issue [#760](https://github.com/probityai/agent-evidence-vectors/issues/760): the ROUTE_SHARD derivation family filing (seven records over the sixteen cases), anchored to draft -03

## Node index

| node | type | state | one line |
|---|---|---|---|
| [`refusal-vocabulary-filing/`](refusal-vocabulary-filing/) | issue | closed completed | our five-record crosswalk submission; the venue adopted GR-P03/GR-P04 as paired fixtures under our name |
| [`principal-standing-rows/`](principal-standing-rows/) | PR | merged | PS1/PS2/PS1b principal-standing rows (Wes Jackson's records via #412); PS1b matched our Record 5 |
| [`refusal-reason-priority-corpus/`](refusal-reason-priority-corpus/) | PR | merged | the refusal-reason-priority corpus (33 members) built from our records; spec-pinned, digest-confirmed by us |
| [`predicate-registry-rfc/`](predicate-registry-rfc/) | issue | open | predicate-registry RFC; our emitter filing registered by #544 (comments open until 20 Nov) |
| [`suites-roadmap/`](suites-roadmap/) | issue | open | suites roadmap; the refusal vocabulary is planned for release 0.38.0 |
| [`refusal-reason-priority-registration/`](refusal-reason-priority-registration/) | PR | merged | the venue registered our refusal-reason-priority entry (RFC table `rttp-refusal` slot → the URI, checker 33/33) and repaired Pages |
| [`attestation-envelope-candidate/`](attestation-envelope-candidate/) | issue | open | our AE-128 envelope registration candidate; scope question asked first, corpus material offered, no vendoring |
| [`lease-boundary-filing/`](lease-boundary-filing/) | issue | open ([#759](https://github.com/probityai/agent-evidence-vectors/issues/759)) | the full lease-boundary family filing: nine records (fifteen cases) anchored to draft -03; extends Record 5 of #453 to the full case set |
| [`route-shard-filing/`](route-shard-filing/) | issue | open ([#760](https://github.com/probityai/agent-evidence-vectors/issues/760)) | the ROUTE_SHARD derivation filing: seven records (sixteen cases) anchored to draft -03; pure-computation vectors recomputable with SHA-256 alone |
