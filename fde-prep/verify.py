#!/usr/bin/env python3
"""Top-level progress tracker for fde-prep.

Discovers every primer and challenge dynamically (nothing is hard-coded, so adding a new
numbered directory just works), runs its pytest suite, and prints a table of which tiers
pass.

Usage:
    python verify.py              # grade your own work in challenges/**/solution.py
    python verify.py --reference  # grade the reference/ solutions (sanity check the harness)
    python verify.py 09           # grade only challenges whose name starts with "09"

Each challenge's tests are split into three tiers — TestBasic, TestEdge, TestStretch — and
each gets its own column. A tier is a tick only if every test in it passed (and at least one
ran). The reference solutions should show a full board of ticks; your job is to get there.
"""
import argparse
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRIMERS_DIR = ROOT / "primers"
CHALLENGES_DIR = ROOT / "challenges"
TIERS = ["TestBasic", "TestEdge", "TestStretch"]

TICK = "✓"  # ✓
CROSS = "✗"  # ✗
DASH = "—"  # —


def discover(directory):
    """Return sorted (name, dir, test_file) for every immediate subdir holding a test."""
    found = []
    if not directory.is_dir():
        return found
    for child in sorted(directory.iterdir()):
        if not child.is_dir():
            continue
        for test_name in ("test_solution.py", "test_primer.py"):
            test_file = child / test_name
            if test_file.exists():
                found.append((child.name, child, test_file))
                break
    return found


def run_pytest(test_file, env):
    """Run pytest on one test file; return {class_name: (passed, total)}."""
    with tempfile.NamedTemporaryFile(suffix=".xml", delete=False) as handle:
        xml_path = handle.name
    try:
        subprocess.run(
            [sys.executable, "-m", "pytest", test_file.name, "-q", "--no-header",
             f"--junit-xml={xml_path}"],
            cwd=test_file.parent,
            capture_output=True,
            env=env,
        )
        return parse_junit(xml_path)
    finally:
        os.unlink(xml_path)


def parse_junit(xml_path):
    """Tally pass/total per test class from a junit xml file."""
    results = {}
    try:
        tree = ET.parse(xml_path)
    except (ET.ParseError, FileNotFoundError):
        return results
    for case in tree.iter("testcase"):
        class_path = case.attrib.get("classname", "")
        short = class_path.split(".")[-1]  # e.g. "test_solution.TestBasic" -> "TestBasic"
        failed = any(child.tag in ("failure", "error") for child in case)
        passed, total = results.get(short, (0, 0))
        results[short] = (passed + (0 if failed else 1), total + 1)
    return results


def cell(results, tier):
    """Render one tier column for one challenge."""
    if tier not in results:
        return DASH
    passed, total = results[tier]
    return TICK if (total > 0 and passed == total) else CROSS


def main():
    parser = argparse.ArgumentParser(description="fde-prep progress tracker")
    parser.add_argument("filter", nargs="?", default="",
                        help="only run dirs whose name starts with this (e.g. '09')")
    parser.add_argument("--reference", action="store_true",
                        help="grade reference/ solutions instead of your own")
    args = parser.parse_args()

    env = dict(os.environ)
    if args.reference:
        env["FDE_REFERENCE"] = "1"

    mode = "REFERENCE solutions" if args.reference else "your solutions"
    print(f"\nfde-prep — verifying {mode}\n")

    # --- Primers (single pass/fail each) ---
    primers = [p for p in discover(PRIMERS_DIR) if p[0].startswith(args.filter)]
    if primers:
        print("PRIMERS")
        for name, _dir, test_file in primers:
            results = run_pytest(test_file, env)
            total = sum(t for _, t in results.values())
            passed = sum(p for p, _ in results.values())
            status = TICK if (total > 0 and passed == total) else CROSS
            print(f"  {status}  {name}  ({passed}/{total} exercises)")
        print()

    # --- Challenges (three tiers each) ---
    challenges = [c for c in discover(CHALLENGES_DIR) if c[0].startswith(args.filter)]
    if challenges:
        header = f"  {'challenge':<24}{'basic':>8}{'edge':>8}{'stretch':>10}"
        print("CHALLENGES")
        print(header)
        print("  " + "-" * (len(header) - 2))
        tier_pass = {tier: 0 for tier in TIERS}
        tier_seen = {tier: 0 for tier in TIERS}
        for name, _dir, test_file in challenges:
            results = run_pytest(test_file, env)
            cells = []
            for tier in TIERS:
                mark = cell(results, tier)
                cells.append(mark)
                if tier in results:
                    tier_seen[tier] += 1
                    if mark == TICK:
                        tier_pass[tier] += 1
            print(f"  {name:<24}{cells[0]:>8}{cells[1]:>8}{cells[2]:>10}")
        print("  " + "-" * (len(header) - 2))
        totals = "  ".join(f"{tier.replace('Test', '').lower()} {tier_pass[t]}/{tier_seen[t]}"
                            for tier, t in zip(TIERS, TIERS))
        print(f"  TOTAL   {totals}")
    print()


if __name__ == "__main__":
    main()
