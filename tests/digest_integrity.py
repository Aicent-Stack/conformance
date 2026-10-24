#!/usr/bin/env python3
"""Verifies every published digest set in the repository.

Mirrors the lab's tests/digest-integrity.test.mjs: a CHECKSUMS.sha256 or
SHA256SUMS.txt pins the exact bytes of the files it lists. This gate reads
every such file, resolves each listed path relative to the digest file's own
directory, recomputes SHA-256 over the exact bytes, and fails on a missing
file, a malformed line, or a mismatch. Standard library only; no network.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKIP_DIRS = {"node_modules", ".git"}
DIGEST_NAMES = ("SHA256SUMS.txt", "CHECKSUMS.sha256")
HEX = set("0123456789abcdefABCDEF")


def find_digest_files(root):
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn in DIGEST_NAMES:
                found.append(os.path.join(dirpath, fn))
    return sorted(found)


def main():
    digest_files = find_digest_files(ROOT)
    if not digest_files:
        print("digest set FAIL: no digest manifest found in the repository")
        return 1
    problems = 0
    for df in digest_files:
        rel_df = os.path.relpath(df, ROOT)
        base = os.path.dirname(df)
        entries = 0
        for raw in open(df, "rb").read().decode("utf-8").splitlines():
            line = raw.strip()
            if not line:
                continue
            parts = line.split(None, 1)
            if len(parts) != 2:
                problems += 1
                print("malformed line in %s: %r" % (rel_df, raw))
                continue
            digest, path = parts[0], parts[1].lstrip("*")
            if len(digest) != 64 or any(c not in HEX for c in digest):
                problems += 1
                print("malformed digest in %s: %r" % (rel_df, digest))
                continue
            fp = os.path.join(base, path)
            if not os.path.isfile(fp):
                problems += 1
                print("missing file pinned by %s: %s" % (rel_df, path))
                continue
            actual = hashlib.sha256(open(fp, "rb").read()).hexdigest()
            if actual != digest.lower():
                problems += 1
                print("digest mismatch for %s (pinned in %s): %s... vs %s..."
                      % (path, rel_df, digest[:16], actual[:16]))
                continue
            entries += 1
        print("digest set ok: %s (%d files verified)" % (rel_df, entries))
    if problems:
        print("digest set FAIL: %d problem(s)" % problems)
        return 1
    print("digest set: all manifests verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
