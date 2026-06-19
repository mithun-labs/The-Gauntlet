# Rulebook — Alpha Capital Group
- **Source:** https://alphacapitalgroup.uk/ (official; rules-explained-2026 post — primary, 403 to fetch tool this run) · secondary/corroborating: https://www.eafunded.com/firms/alpha-capital · https://tradingfinder.com/props/alpha-capital-group/rules/ · https://thetrustedprop.com/prop-firms/alpha-capital-group · https://propfirmmatch.com/prop-firms/alpha-capital-group (403)
- **Retrieved:** 2026-06-19 11:20 UTC
- **Rulebook version (agent-assigned):** v1
- **Change note:** initial — Alpha Capital Group is a REFERENCE firm (CLAUDE.md v2.2). Recorded in `firm_verdicts` but does **not** gate the verdict. Built from secondary sources because the official rules page and Prop Firm Match both 403'd; numeric parameters flagged accordingly.

## Tier / Gating
- **REFERENCE firm — never gates the verdict.** Does not count toward "prohibited at all firms" and does not set the ROR floor. The reason it is reference, not primary: Alpha **requires EA source-code (.MQ5) submission + written pre-approval**, so closed-source commercial third-party EAs (the bulk of this agent's candidates) are effectively unusable here for procedural reasons unrelated to mechanism. Recording it tests detection of the source-code barrier.

## Programs Offered
- **2-step / 3-step evaluation** (Alpha Pro standard), **Swing** account, **Alpha One** (trailing-DD model), and a **free trial**. Account sizes to $200K (scaling beyond). MT5 only for automation.

## Profit Targets (per phase)
- 3-step: **8% (Step 1), 4% (Step 2), 4% (Step 3)**.
- Swing: **10% per phase**.
- Free trial: **10%**.

## Daily Drawdown
- **Plan-dependent: 4–5%.** 3-step = **4%**; Swing/trial = **5%**. Calculation (balance vs equity / reset TZ) not confirmable from primary this run → `UNCONFIRMED` on method.

## Maximum Drawdown
- **Plan-dependent: 6–10%, STATIC** on most plans (locked to starting balance — e.g. $100K @ 6% floor = $94,000, does not move as the account grows). **Alpha One uses TRAILING drawdown.** 3-step = **6%**; Swing/trial = **10%**.

## Leverage (per program · instrument class)
- Up to **1:100** forex (trial); **1:50** (3-step); **1:30** (Swing); lower on indices/commodities. Per-instrument detail `UNCONFIRMED`.

## Lot-Size & Position Limits
- Alpha is known to enforce sizing/lot constraints (the motivating case for the CLAUDE.md lot-cap field). Specific per-order caps `UNCONFIRMED` from primary this run.

## Minimum Trading Days / Time Limits
- **2-minute average minimum trade duration** rule applies (anti-tick-scalping/anti-HFT). First funded payout requires **≥5 trading days** + a risk interview. Per-phase minimum-days `UNCONFIRMED`.

## Consistency Rules
- **40% Best Day Rule** — no single trading day may contribute more than 40% of total generated profits (checked before withdrawal). **2-minute rule** also gates payout.

## EA & Automation Policy (exact language)
- **MT5 only.** EAs require **pre-approval in writing** AND submission of **both the compiled .EX5 and the original .MQ5 source file**. "Commercial EAs require source code submission and most vendors will not provide .MQ5 files." Personal/custom proprietary EAs for execution or risk control are permitted (virtual/hidden SLs via EA allowed). Copy trading allowed **only** when copying your own external account with proof of ownership.
- **Effect for this agent:** any closed-source commercial third-party EA is **Prohibited (procedural)** here — vendors will not hand over .MQ5. Record reference verdict `Prohibited — source-code submission required` for such EAs.

## Banned Behaviors
- **HFT — prohibited.** Tick scalping — prohibited (inferred + 2-minute rule). Arbitrage / latency-based EAs — strictly prohibited. Copy/group trading across third parties — prohibited (own-account copy with proof only). Martingale — prohibited if flagged as a group-trading strategy; grid — not explicitly named (mechanism still Gate-A excluded by this agent regardless).

## HFT / Tick-Scalping Thresholds
- **2-minute average minimum trade duration** is the operative anchor (trades/closes also barred within 2 min of major news). No explicit max-trades/day stated.

## News-Trading Restrictions
- **No new trades or position closes within 2 minutes before/after major news.**

## Weekend / Overnight Holding
- Swing account explicitly designed for holding over weekend/news; standard accounts more restrictive. Specifics `UNCONFIRMED`.

## Payout Structure & Profit Split
- **80% profit split.** First payout: risk interview + ≥5 funded trading days + 40%-best-day and 2-minute rules satisfied.

## UNCONFIRMED items
- DD calculation method (balance vs equity, reset TZ); per-instrument leverage; lot-size caps; per-phase minimum-days; weekend/holding specifics; whether the official primary page (403 this run) differs. Any verdict resting on these is `Conditional`.
