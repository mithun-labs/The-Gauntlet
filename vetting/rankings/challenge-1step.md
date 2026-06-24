[← Index](../README.md) · [Funded-survival](funded-survival.md) · [2-step](challenge-2step.md) · [1-step](challenge-1step.md) · [Comparison](comparison.md)

# Ranking — Challenge (1-step)
*Best fit for tighter 1-step / trailing-drawdown challenges. Only EAs with verdict ∈ {Deployable, Watchlist} appear, referenced as `[[slug]]`.*

> **Ranked by:** 2-step composite (`0.5·Challenge + 0.3·Risk + 0.2·Compliance`) **minus a 0.5 trailing-DD-sensitivity penalty** for EAs whose drawdown leaves little headroom (1-step programs use tighter/trailing max-DD, so a near-the-limit DD is punished harder here than in the 2-step list).

| # | EA | Verdict | Score | Overall | 2-step base | 1-step penalty | Legality | Note |
|--:|----|:-------:|:-----:|:-------:|:-----------:|:--------------:|----------|------|
| 1 | [[one-man-army-mt5]] | 🟡 | **2.7** | 3.1 | 3.2 | −0.5 | FN⚠️ FP✅ 5%✅ TFT✅ | 8.94% max DD ≈ 89% of a 10% limit → highly trailing-DD-sensitive |

**Why this differs from 2-step:** [[one-man-army-mt5]]'s only real-money record shows an **8.94% max equity
DD with essentially no headroom** under a 10% limit, and a multi-pair reversal book can cluster losses
intraday — exactly the profile a **trailing/static 1-step** drawdown rule punishes. Its 1-step composite
(2.7) is therefore below its 2-step composite (3.2). Still the only qualifying EA, and still **not
recommended** (Watchlist).
