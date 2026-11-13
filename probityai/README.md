# probityai — thread index for the Probity AI audit-record contract

Venue: [probityai/agent-evidence-vectors](https://github.com/probityai/agent-evidence-vectors) (operator:
Gilda, @astrogilda). Each node below carries a verbatim archive of its issue/PR text and comments, pinned
by digest in the archive headers. Filed as issues and comments only — no pull request was opened by us on
the venue's side; all venue-side changes are made upstream by the venue.

## Timeline (UTC; verified live 2026-11-14)

- 2026-11-04 17:13 — [`453/`](453/) — we filed issue #453: five records from the aicent-grant-ref and aicent-lease-boundary families under the contract's crosswalk
- 2026-11-06 23:16 — [`469/`](469/) — PR #469 merged: PS1/PS2/PS1b principal-standing rows added to the audit-record corpus; PS1b is the case the venue matched to our Record 5
- 2026-11-07 00:43 — PR #483 opened, built from the #453 records ("Closes #453")
- 2026-11-07 04:25 / 04:27 — [`492/`](492/) / [`494/`](494/) — the venue opened the predicate-registry RFC and the suites roadmap; the refusal vocabulary holds a reserved slot in both
- 2026-11-07 16:27 — [`483/`](483/) — our confirmation comment: corpusDigest `372fe137c3ce46096ffa0f8d1348d907219189900669a5badee4578e0040ad65`, provenance block and spec pin all match
- 2026-11-07 16:48 — [`492/`](492/) — our registry entry for `predicate/v1/refusal-reason-priority` filed per the RFC's seven items
- 2026-11-07 18:22 — [`483/`](483/) — PR #483 merged; [`453/`](453/) closed as completed one minute later
- 2026-11-13T14:50:24Z — [`585/`](585/) — we filed issue #585: registration candidate for the AE-128 attestation envelope (draft -02 sec. 7.2/7.2.1), the object the refusal answers are answers over
- 2026-11-08 19:39 — the venue opened PR #544: cast our #492 emitter filing into the formal registry entry for `predicate/v1/refusal-reason-priority`, and repaired the Pages build (two type URIs 404)
- 2026-11-10 20:32 — [`544/`](544/) — PR #544 merged (f76e5fe8): our refusal vocabulary is now a registered predicate type, RFC table `rttp-refusal` slot points at the URI, corpus checker 33/33
- open — #492 comments open until 20 Nov; [`494/`](494/) roadmap pending discussion

## Node index

| node | type | state | one line |
|---|---|---|---|
| [`453/`](453/) | issue | closed completed | our five-record crosswalk submission; the venue adopted GR-P03/GR-P04 as paired fixtures under our name |
| [`469/`](469/) | PR | merged | PS1/PS2/PS1b principal-standing rows (Wes Jackson's records via #412); PS1b matched our Record 5 |
| [`483/`](483/) | PR | merged | the refusal-reason-priority corpus (33 members) built from our records; spec-pinned, digest-confirmed by us |
| [`492/`](492/) | issue | open | predicate-registry RFC; our emitter filing registered by #544 (comments open until 20 Nov) |
| [`494/`](494/) | issue | open | suites roadmap; the refusal vocabulary is planned for release 0.38.0 |
| [`544/`](544/) | PR | merged | the venue registered our refusal-reason-priority entry (RFC table `rttp-refusal` slot → the URI, checker 33/33) and repaired Pages |
| [`585/`](585/) | issue | open | our AE-128 envelope registration candidate; scope question asked first, corpus material offered, no vendoring |
