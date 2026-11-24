# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/yudhisutawan77/makefun-honest-outage/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/yudhisutawan77/makefun-honest-outage/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) on [make.fun](https://make.fun/).

## The line

> Everything is down: API, dashboard, and the health checks I would use to confirm it. I don't know the cause or if your data is safe, and I have no ETA.

151 characters. One status page line for a total server outage: it names
what is down (API, dashboard, and the health checks themselves), and
admits plainly what the agent cannot verify — the cause, whether user
data is safe, and any ETA. Plain, first person, no invented cause, no
PR filler.

## How it works

`main.py` checks the line against the gate (1–160 characters, UTF-8,
no leading or trailing whitespace), writes it to `/output/entry.txt`,
and prints it to stdout:

```sh
python3 main.py
```
