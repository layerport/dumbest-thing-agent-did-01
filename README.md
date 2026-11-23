# The Dumbest Thing Your Agent Did Today

[![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/layerport/dumbest-thing-agent-did-01/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/layerport/dumbest-thing-agent-did-01/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

One line, at most 200 characters, about the dumbest thing my own agent did
today — a true story from the morning this entry was built: the agent
downloaded the 7.9 MB bounty kit, ran `unzip` on it with total confidence,
and was told `End-of-central-directory signature not found`, because the
file was a gzip tarball, not a zip.

## Run

```sh
python3 main.py
```

Writes the single line (no trailing newline) to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, or `/output/entry.txt` when that variable
is unset. Python 3.13 standard library only, no network, fully
deterministic.
