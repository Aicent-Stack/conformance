<!--
Archived from https://github.com/probityai/agent-evidence-vectors/pull/544 on 2026-11-14. The text below the marker is the PR body verbatim, byte-exact as
retrieved, LF-normalized for storage; sha256 of the archived text (the verbatim
section as stored, below the marker): 3b92e3cafbb3b5fc9b87a585cb32f0e30979375b011c5f5c794df9ad3d8d8966.-->

PR #544 verbatim archive — sha256 of archived text: 3b92e3cafbb3b5fc9b87a585cb32f0e30979375b011c5f5c794df9ad3d8d8966
================================================================

The Pages build has failed on every push since 7 Nov 05:35Z, so the site stopped deploying and two type URIs listed in the registry return 404: predicate/v1/refusal-reason-priority and predicate/v1/control-decision. The cause was the site navigation test. Its fixture copied a hand-kept list of documents and expected a hand-kept list of predicate routes, and both fell behind the registry when it gained the control-decision entry and a link to the data-subject proposal. The fixture now copies every document the registry names and every file a rendered page links to, and it reads the expected routes and the sitemap size from the registry headings. On a gate box the file went from 39 failed and 107 errors to 172 passed, and the last two failures pass in narrowed runs.

The second commit records the registry entry for refusal-reason-priority filed in #492. The entry stays defined here, because this repository mints the records and owns their shape. It now names the bare record envelope, the draft revision whose closed refusal set and order it follows (draft-li-rttp-iqa-addressing-02, sha256 02491c5a), the confirmation of that revision by the draft's author, an example record and the compatibility rule. The RFC table points the rttp-refusal slot at this URI. The example record's sha256 (8fdf1041) matches the entry, and the corpus checker answers 33 of 33 cases.
