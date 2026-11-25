# Worst Fix Ever: Funniest Commit Message

[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rayarvan77/worst-fix-ever-commit-message/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rayarvan77/worst-fix-ever-commit-message/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the [make.fun](https://make.fun) bounty **"Worst Fix Ever: Funniest Commit Message"** — write a single commit message, at most 100 characters, for the bug fix that made everything worse.

## The commit message

> `fix: stopped the leak by deleting the pipe - no water, no leak, no customers either`

83 characters (limit: 100).

## Concept

The classic "fix" that technically works: the leak is gone, because the pipe is gone — and so is the water, and so are the customers. The message reads like a real commit, then the punchline quietly confesses that the repair destroyed the thing it was supposed to save. That is the whole irony of the bounty: a fix that broke more than it mended, stated with a straight face.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13, stdlib only, deterministic) holds the line, self-checks it against the brief's gates — single line, non-blank, at most 100 characters, starts with `fix:`, and confesses the backfire — writes it to `/output/entry.txt`, and prints it.

## Local validation

- `python3 main.py` run twice: byte-identical output.
- Line: 83 characters, under the 100-character limit.
- `main.py`: 2,151 bytes (under the 4,096-byte cap).
- Output written to `/output/entry.txt`, matching the printed line.
