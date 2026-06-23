# Ranking — challenge-1step

_Only EAs with verdict ∈ {Deployable, Watchlist} appear here, referenced via wiki-style slug links._

**Formula:** as 2-step (0.5·Challenge + 0.3·Risk + 0.2·Compliance) **minus a trailing-DD-sensitivity
penalty of 0.5** for EAs whose drawdown profile leaves little headroom (1-step programs typically use
tighter/trailing max-DD, so a near-the-limit DD is penalised harder here than in the 2-step list).

| # | EA | 2-step base | Trailing-DD penalty | Composite | Verdict / note |
|---|----|------------:|--------------------:|----------:|----------------|
| 1 | [[one-man-army-mt5]] | 3.2 | −0.5 | **2.7** | Watchlist — 8.94% max DD ≈ 89% of a 10% limit → highly trailing-DD-sensitive |

**Why this differs from 2-step:** [[one-man-army-mt5]]'s only real-money record shows an **8.94% max
equity DD with essentially no headroom** under a 10% limit, and a multi-pair reversal book can cluster
losses intraday — exactly the profile a **trailing/static 1-step** drawdown rule punishes. Its 1-step
composite (2.7) is therefore below its 2-step composite (3.2). Still the only qualifying EA, and still
**not recommended** (Watchlist).
