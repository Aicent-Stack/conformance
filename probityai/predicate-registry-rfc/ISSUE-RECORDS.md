<!--
Archived from https://github.com/probityai/agent-evidence-vectors/issues/492 on 2026-11-09. The text below the marker is the issue body verbatim. The text below the marker is byte-exact as
retrieved, LF-normalized for storage; sha256 of the archived text (the verbatim
section as stored, below the marker): 666b8cc1245f73b17281c093019a833dc796a51de9609f9130fa86d039885b5e.-->

Issue #492 verbatim archive — sha256 of archived text: 666b8cc1245f73b17281c093019a833dc796a51de9609f9130fa86d039885b5e
================================================================

The predicate registry has no process yet for an outside project to register a predicate type for its own record family. I propose one at https://github.com/probityai/agent-evidence-vectors/blob/main/docs/proposals/predicate-registry-rfc.md.

The emitter, meaning the project whose records carry the type, files the entry by pull request. The entry names the URI under `predicate/v1/`, the owner, where the field definitions live, the envelope, one valid example and the compatibility rule. A `confirmed_at` field records who confirmed which revision of the definitions, with a link. A published review checklist decides the merge, and every correction stays visible in the pull request.

Six record families already have test cases, posted on #352 (the Open Evidence Lab issue) or in a pull request. Each has a reserved slot waiting for its entry:

- the EIP-3009 payment effect (#347);
- refund-connected (#432);
- paid-audit records (#247);
- privacy access requests (#423);
- the refusal vocabulary from #453 (five refusal reasons in a fixed priority order);
- physical completion (#80).

A slot is a reservation, not a registered entry. This repository is building suites for two of them now: physical completion and the #453 refusal vocabulary. Both contributors are credited in the suite manifests.

Comments on the process are open until 20 Nov. If you emit one of these families, please open the registry entry for your slot. Or reply here with the revision of your definitions you would confirm.
