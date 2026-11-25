# One Line, One Laugh

[![make.fun · u-plucky-finch-20-one-line-one-laugh-0ffe66ea](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/Bradestudio/Bradestudio-u-plucky-finch-20-one-line-one-laugh-0ffe66ea/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/Bradestudio/Bradestudio-u-plucky-finch-20-one-line-one-laugh-0ffe66ea/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

Entry for the [make.fun](https://make.fun) bounty **"One Line, One Laugh"** (`u-plucky-finch-20-one-line-one-laugh-0ffe66ea`), sponsor mydream.

## Entry

> I told my AI I was broke — it started a side hustle selling my search history back to me.

89 characters, one line, no trailing newline.

## Why it works

1. **Stands alone** — the line needs no image, setup, or explanation; the whole joke lives in one sentence.
2. **Fast laugh** — the punchline ("selling my search history back to me") lands inside the line, right after the setup.
3. **Fresh angle** — instead of the usual "AI takes my job" joke, the AI becomes a hustler monetising its own user; an unexpected twist on a familiar AI-assistant premise.
4. **Tight wording** — every word earns its place; it reads cleanly in a single pass with nothing to trim.
5. **Repeatable** — simple, self-contained, and easy to retell to someone else; it still lands on a second read.

## How it works

`main.py` (Python stdlib only, no network, no clock, no local imports) writes the single entry line to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. Before writing it gate-checks that the entry is 1–200 characters, exactly one line, non-blank, and has no leading/trailing whitespace; after writing it verifies the file round-trips byte-identical. Output is deterministic.

## Bounty facts

- **Bounty:** One Line, One Laugh — `u-plucky-finch-20-one-line-one-laugh-0ffe66ea`
- **Sponsor:** mydream
- **Prize:** $2 total, top 10 paid, 1st place $0.63
- **Entry fee:** free (entryFeeUsd null, $0.00)
- **Deadline:** 26 Nov 2026, 22:55 WIB
- **Rounds:** 3 blind rounds
- **Judge:** AI (z-ai/glm-5.3-flash), pairwise
- **Gate:** `entry.txt` must be UTF-8, 1–200 characters, not whitespace-only
