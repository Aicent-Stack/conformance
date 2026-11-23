# replay — our pipeline replays of external records

This folder is the dedicated home for **pipeline replays**: records where our
own pipeline executes someone else's merged lab record and verifies its bytes
reproduce. Each subdirectory is one replay record, named per the family-first
convention `<family>-replay-<operator>` (a second replay by the same operator
of the same family takes a numeric suffix: `<family>-replay-<operator>-2`).
The generic thin wrapper that drives every replay lives in
[`replay-runner/`](replay-runner/); each record directory carries a
`profile.json` describing its pins, commands and expected summary, so the
wrapper itself knows nothing about any particular family, candidate, or
external operator.

A replay adds no verdict logic of its own: the checker that supplies the
verdicts is the external record's own code, executed as run. The replay shows
that the merged record's bytes are self-consistent and executable by anyone
offline — nothing more, and honestly nothing less.

- [`replay-runner/`](replay-runner/) — the generic replay harness (`replay_runner.py`)
- [`grant-ref-replay-sparysh/`](grant-ref-replay-sparysh/) — pipeline replay of the merged
  `sparysh-reading-aicent-grant-ref-20186f3` lab record (Andrii Sparysh's outside
  reading of our `aicent-grant-ref` family, lab PR #234)
- [`lease-boundary-replay-sparysh/`](lease-boundary-replay-sparysh/) — pipeline replay of the merged
  `sparysh-reading-aicent-lease-boundary-0e0064b` lab record (Andrii Sparysh's outside
  reading of our `aicent-lease-boundary` family, lab PR #238)
