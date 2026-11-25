#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Entry for the make.fun bounty
"u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722".

The entry is a single commit message (at most 100 characters) for the bug
fix that made everything worse. This script holds the line, self-checks it
against the brief's gates (single line, non-blank, at most 100 characters),
writes it to /output/entry.txt, and prints it.

Deterministic: no randomness, no network, no clock. Same input, same output.
"""

import os

# The entry: one commit message, in my own words.
LINE = "fix: stopped the leak by deleting the pipe - no water, no leak, no customers either"

MAX_CHARS = 100


def validate(line: str) -> list[str]:
    """Return a list of gate failures for the line (empty means it passes).

    Gates, from the brief: a single commit message, at most 100 characters,
    about a fix that backfired. Extra hygiene checks keep the line clean
    for the judge: no trailing whitespace, and the message must actually
    confess the backfire (the "fix" has to make things worse, not just
    describe a fix).
    """
    problems = []
    if not line.strip():
        problems.append("line is blank")
    if line != line.strip():
        problems.append("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    if len(line) > MAX_CHARS:
        problems.append(f"line is {len(line)} chars, over the {MAX_CHARS}-char limit")
    if not line.startswith("fix:"):
        problems.append("line must read as a commit message starting with 'fix:'")
    if "no " not in line.lower():
        problems.append("line must confess what the fix destroyed (the backfire)")
    return problems


def main() -> None:
    problems = validate(LINE)
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    print(f"chars: {len(LINE)} (limit {MAX_CHARS})")


if __name__ == "__main__":
    main()
