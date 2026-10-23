# -*- coding: utf-8 -*-
"""Update draft: replay link to lra-runner/ subdir + refresh inline report; then commit+push report fix."""
import os, subprocess

DRAFT = r"E:\WEB\_local-only\iana\outreach\draft-2026-10-23-pr180-independent-run-comment.md"
REPO = r"E:\WEB\_local-only\iana\conformance\lra-runner-repo"
REPORT = os.path.join(REPO, "lra-runner", "RUN-REPORT-2026-10-23.md")

draft = open(DRAFT, encoding="utf-8").read()
report = open(REPORT, encoding="utf-8").read()

marker = "# Conformance Run Report"
idx = draft.find(marker)
assert idx > 0, "report heading not found"
body = draft[:idx].rstrip() + "\n"

old_link = "https://github.com/Aicent-Stack/conformance (the frozen vectors are vendored and digest-gated, so a one-command replay works offline)"
new_link = "https://github.com/Aicent-Stack/conformance/tree/main/lra-runner (the frozen vectors are vendored and digest-gated, so a one-command replay works offline)"
assert old_link in body, "replay link not found"
body = body.replace(old_link, new_link)

open(DRAFT, "w", encoding="utf-8").write(body + "\n\n---\n\n" + report)
print("draft rebuilt")

subprocess.run(["git", "add", "-A"], cwd=REPO)
subprocess.run(["git", "commit", "-m", "Report: implementation field names lra-runner/ path"], cwd=REPO)
r = subprocess.run(["git", "push"], cwd=REPO, capture_output=True, text=True)
tail = (r.stdout or r.stderr).strip().splitlines()
print("push:", tail[-1] if tail else "no output")
