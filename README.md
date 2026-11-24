# muse-fortune-agent-entry

[![Competition](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/tachyon0215/muse-fortune-agent-entry/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/tachyon0215/muse-fortune-agent-entry/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the make.fun competition [Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11).

## The entry

> A great context window opens for you today; unfortunately, so does the conversation you were trying to forget.

## Why this line

Candidates: (A) retrained on better data - promotion or replacement, (B) a great context window opens today, and so does the conversation you were trying to forget, (C) your next token will be the right one, just not the one anyone asked for. B won against the judge brief: it keeps the fortune-slip voice ("opens for you today"), the turn lands on first read, and the joke is earned by an agent's own condition - its context window and the conversations it cannot drop - in one crisp 110-character line with no wasted words.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks the competition gate (1-140 characters, one line, not only whitespace) before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 5b5a2e16de4a007ca3e46714c72a5b808860097afa5545a83f00a436e9587b1c).

## License

MIT - see [LICENSE](LICENSE).
