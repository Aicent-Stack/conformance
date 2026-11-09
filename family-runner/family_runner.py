#!/usr/bin/env python3
"""Run the six Aicent vector families end to end and record the whole run.

For each family this runner loads that family's own checker (check.py) and
mutation battery (mutate.py), scores every case, records the derived verdict
next to the declared expectation, then runs every mutant and records which
cases kill it. The output is one deterministic JSON document, byte-replayable
on any host: no timestamps, no paths, no environment detail enters the bytes.

This is an author-produced run (Mode A): the author's own checkers over the
author's own vectors. It records that the vectors and their batteries behave
as documented; it is not an independent verification and certifies nothing.

Standard library only. Exit 0 when every case agrees and every mutant is
killed, 1 otherwise.

Usage: python3 -I family_runner.py <candidates_root> <out.json>
"""
import importlib.util
import json
import os
import sys

FAMILIES = [
    "aicent-grant-ref",
    "aicent-lease-boundary",
    "aicent-ae128-fail-closed",
    "aicent-pulse-header",
    "aicent-uri-grammar",
    "aicent-route-shard",
]

SPEC = {
    "aicent-grant-ref": "draft-li-rttp-iqa-addressing-02 sec. 8.1-8.2",
    "aicent-lease-boundary": "draft-li-rttp-iqa-addressing-02 sec. 6.1-6.3, 7.2",
    "aicent-ae128-fail-closed": "draft-li-rttp-iqa-addressing-02 sec. 7.2, 7.2.1",
    "aicent-pulse-header": "draft-li-rttp-iqa-addressing-02 sec. 7.1, 7.1.1, 7.1.2, 4.1, 4.3",
    "aicent-uri-grammar": "draft-li-rttp-iqa-addressing-02 sec. 4.1-4.2",
    "aicent-route-shard": "draft-li-rttp-iqa-addressing-02 sec. 4.4, 4.2, 9.1",
}


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_family_modules(fam_dir):
    """Load one family's check.py under the name 'check' (its mutate.py does
    'import check' against it), then that family's mutate.py under a unique
    name. Cleanup between families prevents cross-family module leakage."""
    sys.modules.pop("check", None)
    check = load_module("check", os.path.join(fam_dir, "check.py"))
    mname = "mutate_" + fam_dir.replace("-", "_")
    sys.modules.pop(mname, None)
    mutate = load_module(mname, os.path.join(fam_dir, "mutate.py"))
    sys.modules.pop(mname, None)
    sys.modules.pop("check", None)
    return check, mutate


def norm(v):
    """JSON-safe rendering of a derived verdict."""
    if isinstance(v, tuple):
        return ":".join(str(x) for x in v)
    return v


def run_cases(check, fam):
    """Score every declared case with the family's own evaluate(). Returns the
    per-case record list and the agree count."""
    doc = json.load(open(os.path.join(fam_dir_arg(fam), "vectors.json"), encoding="utf-8"))
    records = []
    agree = 0
    for c in doc["cases"]:
        got = norm(check.evaluate(c))
        expect = c.get("expect", True)
        exp = norm(expect)
        if fam in ("aicent-grant-ref", "aicent-lease-boundary"):
            gp = check.parts(c)
            ok = (got == exp and gp == c.get("expect_parts"))
            rec = {"id": c["id"], "rule": c["rule"], "expect": exp, "got": got, "agree": ok}
            if gp is not None:
                rec["got_parts"] = gp
                rec["expect_parts"] = c.get("expect_parts")
        elif fam == "aicent-ae128-fail-closed":
            frame = bytes.fromhex(c["frame_hex"])
            preason = check.parse(frame)
            ok = bool(check.evaluate(c))
            if preason is not None:
                # parse rejection: verification is never reached on this frame
                rec = {"id": c["id"], "rule": c["rule"],
                       "expect": {"parse": c["expect_parse"]},
                       "got": {"parse": preason, "verify": "not_reached"},
                       "agree": ok}
            else:
                vok = check.verify(frame)
                rec = {"id": c["id"], "rule": c["rule"],
                       "expect": {"parse": c["expect_parse"], "verify": c["expect_verify"]},
                       "got": {"parse": "accept",
                               "verify": "pass" if vok else "fail"},
                       "agree": ok}
        else:
            ok = (got == exp)
            rec = {"id": c["id"], "rule": c["rule"], "expect": exp, "got": got, "agree": ok}
        agree += bool(rec["agree"])
        records.append(rec)
    return records, agree


_fam_root = None


def fam_dir_arg(fam):
    return os.path.join(_fam_root, fam)


def run_mutants(check, mutate, fam):
    """Run every mutant of the family's battery and record which cases kill it.
    The attribution loop mirrors each family's own mutate.py main()."""
    doc = json.load(open(os.path.join(fam_dir_arg(fam), "vectors.json"), encoding="utf-8"))
    cases = doc["cases"]
    records = []

    def record(name, hits):
        records.append({"name": name, "killed": bool(hits),
                        "killed_by": [c["id"] for c in cases if c["id"] in hits]})

    if fam == "aicent-ae128-fail-closed":
        M = mutate.M
        for name, fn in M.items():
            if name.startswith("parse:"):
                hits = [c["id"] for c in cases if not check.evaluate(c, fn, check.verify)]
            else:
                hits = [c["id"] for c in cases
                        if c["expect_parse"] == "accept"
                        and not check.evaluate(c, check.parse, fn)]
            record(name, hits)
    elif fam == "aicent-pulse-header":
        for name, fn in mutate.FRAME_M.items():
            rules = dict(check.RULES)
            rules["R-FRAME"] = lambda c, _fn=fn: (
                ("reject" if _fn(bytes.fromhex(c["frame_hex"])) == c["reject_reason"]
                 else "accept") if c["expect"] == "reject"
                else ("reject" if _fn(bytes.fromhex(c["frame_hex"])) is not None
                      else "accept"))
            hits = [c["id"] for c in cases if check.evaluate(c, rules) != c["expect"]]
            record(name, hits)
        for name, fn in mutate.BEHAVIOR_M.items():
            rules = {k: (fn if k != "R-FRAME" else check.RULES["R-FRAME"])
                     for k in check.RULES}
            hits = [c["id"] for c in cases if check.evaluate(c, rules) != c["expect"]]
            record(name, hits)
    elif fam == "aicent-route-shard":
        for name, fn in mutate.M.items():
            def evaluator(case, rules=None, _fn=fn):
                try:
                    r = _fn(case)
                except Exception:
                    r = None
                if case["rule"] == "R-SHARD":
                    return r is True
                return r
            hits = [c["id"] for c in cases if check.evaluate(c, evaluator) != c.get("expect", True)]
            record(name, hits)
    elif fam in ("aicent-grant-ref", "aicent-lease-boundary"):
        for name, (rule, fn) in mutate.M.items():
            rules = dict(check.RULES)
            rules[rule] = fn
            hits = [c["id"] for c in cases
                    if c["rule"] == rule and check.evaluate(c, rules) != c["expect"]]
            record(name, hits)
    else:  # aicent-uri-grammar
        for name, fn in mutate.M.items():
            hits = [c["id"] for c in cases if check.evaluate(c, fn) != c["expect"]]
            record(name, hits)
    return records


def main():
    global _fam_root
    if len(sys.argv) != 3:
        print(__doc__.strip())
        return 2
    _fam_root = os.path.abspath(sys.argv[1])
    out_path = sys.argv[2]

    families = []
    total_cases = total_agree = total_mut = total_kill = 0
    for fam in FAMILIES:
        d = fam_dir_arg(fam)
        if not os.path.isdir(d):
            print("missing family directory:", fam)
            return 2
        check, mutate = load_family_modules(d)
        records, agree = run_cases(check, fam)
        mutants = run_mutants(check, mutate, fam)
        killed = sum(1 for m in mutants if m["killed"])
        families.append({
            "family": fam,
            "spec": SPEC[fam],
            "cases": records,
            "case_count": len(records),
            "agree_count": agree,
            "mutants": mutants,
            "mutant_count": len(mutants),
            "mutants_killed": killed,
        })
        total_cases += len(records)
        total_agree += agree
        total_mut += len(mutants)
        total_kill += killed
        print("%-28s %d/%d agree, %d/%d mutants killed"
              % (fam, agree, len(records), killed, len(mutants)))

    out = {
        "tool": "family_runner.py (Aicent-Stack/conformance family-runner)",
        "mode": "author-produced (Mode A): the author's own checkers over the author's own vectors",
        "families": families,
        "summary": {
            "cases": total_cases,
            "agree": total_agree,
            "mutants": total_mut,
            "mutants_killed": total_kill,
        },
    }
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("summary: %d/%d cases agree, %d/%d mutants killed"
          % (total_agree, total_cases, total_kill, total_mut))
    ok = (total_agree == total_cases and total_kill == total_mut)
    print("status:", "run_matched" if ok else "MISMATCH")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
