<!--
Archived from https://github.com/probityai/agent-evidence-vectors/pull/483 on 2026-11-09. The text below the marker is the PR body verbatim. The text below the marker is byte-exact as
retrieved, LF-normalized for storage; sha256 of the archived text (the verbatim
section as stored, below the marker): 6e83334365b2c53fe0982759870f23d09d0f8c2bb0ce6e1fbbf3be4673c3f334.-->

PR #483 verbatim archive — sha256 of archived text: 6e83334365b2c53fe0982759870f23d09d0f8c2bb0ce6e1fbbf3be4673c3f334
================================================================

Closes #453. This adds the vectors-refusal-reason-priority corpus: 33 members (15 conformant, 15 nonconformant, 3 ambiguous) built from the records Aicent-com (Aicent Stack) shared on the issue, anchored to sections 6.1, 7.2, 8.1 and 8.2 of draft-li-rttp-iqa-addressing-02. Each member is one attestation response plus the facts it answered over, and the checks cover the contract id, the closed five-value reason set, the first-applicable-condition priority (mismatch, expiry, not determined, revocation, operation not permitted), null as the only permit, the lease-instant boundary, the observation member staying null when the relied-on observation is stale or absent, and a diagnostic read not renewing the grant expiry.

The corpus ships with a generator, a manifest, a Python reader and a Go reader that derive every decision from the record alone, tests for both, a README, the registry and README table entries, the release digest line and the intake records. Run it with `agent-evidence-vectors --corpus vectors-refusal-reason-priority`. While finishing it I fixed the Python reader to retain a null reason as "null" rather than the repr "None", so both readers agree on the retained fields.

Thank you to Aicent-com for the records this is built from.
