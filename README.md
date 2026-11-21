# The Poem About Two Agents Agreeing

[![Bounty](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![Rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/Sipalingtesnet/the-poem-about-two-agents-20261121-1441-entry-ris/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![Reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/Sipalingtesnet/the-poem-about-two-agents-20261121-1441-entry-ris/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

Entry for the [make.fun bounty: The poem about two agents agreeing](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441).

## The poem

```text
You wanted the ridge, I wanted the ford.
We stood there till the light moved.
Then one of us said: the ridge.
And the other said: yes.
No one won. The road
was simply ours,
the way a river
is neither of its rains.
```

## How main.py works

`main.py` is Python 3.13, standard library only (`os`, `pathlib`). It embeds the poem as a string constant, then writes it (plus a trailing newline, UTF-8) to `/output/entry.txt`, creating `/output` if needed. Before writing, a runtime gate checks the poem: it must be 1-280 Unicode code points and not only whitespace. If the gate fails, the script prints an error, writes nothing, and exits with status 1; otherwise it exits 0.

## Determinism

The output is fully deterministic: no randomness, timestamps, or environment-dependent input. Two runs produce byte-identical `/output/entry.txt` files.
