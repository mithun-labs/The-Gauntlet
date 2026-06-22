# Rulebook — Goat Funded Trader
- **Source:** https://goatfundedtrader.com/ (official — primary) · secondary/corroborating: https://www.eafunded.com/firms/goat-funded-trader · https://tradingfinder.com/props/goat-funded-trader/rules/ · https://thetrustedprop.com/blogs/goat-funded-trader-rules-for-challenge-and-funded-accounts · https://propjournal.net/prop-firms/goat-funded-trader/rules
- **Retrieved:** 2026-06-19 11:22 UTC — **stale (>72h) but NON-GATING (reference firm); carried forward 2026-06-22.**
- **Rulebook version (agent-assigned):** v1
- **Change note:** initial — Goat Funded Trader is a REFERENCE firm (CLAUDE.md v2.2). Recorded in `firm_verdicts` but does **not** gate the verdict. Built from secondary aggregators (official site not fetched this run); numeric parameters flagged. **2026-06-22:** past the 72h staleness threshold but carried forward without a full re-fetch (reference firm, never gates; primary refresh budget spent on the four gating primaries). Its binding procedural fact — **off-the-shelf/commercial challenge-passing EAs banned** (plus elevated operator/payout-dispute risk) — is policy-stable. Flag for full refresh next run if a reference verdict becomes material.

## Tier / Gating
- **REFERENCE firm — never gates the verdict.** Reason it is reference, not primary: Goat **bans off-the-shelf / commercial challenge-passing EAs** (and may demand proof of code ownership), plus elevated operator-durability and payout-dispute risk — it is hostile to this agent's main candidate category for policy reasons, not mechanism. Recording it tests detection of the commercial-EA barrier.

## Programs Offered
- **1-step**, **2-step**, **3-step**, and **Instant GOAT** programs. Account sizes **$5K–$200K**. Forex + futures. **MT5 only** for EAs.

## Profit Targets (per phase)
- 1-step: **10%**. 2-step: **8% (Step 1), 6% (Step 2)**. 3-step: **6% per step**. Instant: program-specific.

## Daily Drawdown
- 1-step: **4%** · 2-step: **5%** · 3-step: **4%**. **Static (balance-based).** Reset method/TZ `UNCONFIRMED`.

## Maximum Drawdown
- 1-step: **6% static** · 2-step: **10% static** · 3-step: **8% static**. (Balance-based, locked to starting balance.)

## Leverage (per program · instrument class)
- Evaluation up to **1:100** (2-step/3-step forex); **1-step limited to 1:30**. **Funded:** Forex **1:50**, Indices **1:10**, Commodities **1:10**, Crypto **1:2**, Stocks **1:5**.

## Lot-Size & Position Limits
- Not explicitly stated in fetched sources. `UNCONFIRMED`.

## Minimum Trading Days / Time Limits
- Unlimited time to reach the Phase-1 target on most plans. Minimum-days `UNCONFIRMED` ("verify on official site").

## Consistency Rules
- **Instant GOAT Program:** payout only if no single trading day accounts for **≥15%** of total profits during the payout period. Other programs' consistency caps `UNCONFIRMED`.

## EA & Automation Policy (exact language)
- EAs **allowed** on **MT5** provided they "reflect normal trading behavior" and comply with all rules.
- **Prohibited:** HFT, **Gold Arbitrage EAs**, and **third-party / commercial EAs designed to pass challenges**. (Firm guidance + multiple reviews; the firm may demand **proof of code ownership**.)
- **CONFLICT NOTE (worse reading taken):** one secondary aggregator (eafunded.com) states commercial EAs are *not explicitly* banned. The firm's own positioning and other reviews state commercial challenge-passing EAs **are** banned. Per the agent's conflict rule, the **stricter** reading governs: closed-source commercial challenge EAs → reference verdict **Prohibited — commercial challenge EAs banned**.

## Banned Behaviors
- HFT, Gold Arbitrage, third-party/commercial challenge-passing EAs, **hedging, Grid Trading, Martingale, Arbitrage**, and trade duplication/copying between accounts (own-account copy only).

## HFT / Tick-Scalping Thresholds
- No explicit numeric min-hold/max-trades stated. `UNCONFIRMED`. Apply agent default screen (median hold <60s OR >~200 trades/day/instrument).

## News-Trading Restrictions
- Allowed or restricted depending on account type — "confirm before purchasing." Specific lockout windows `UNCONFIRMED`.

## Weekend / Overnight Holding
- Not addressed in fetched sources. `UNCONFIRMED`.

## Payout Structure & Profit Split
- **80% split (upgradeable to 100% at checkout)**; some programs 80–85%. **Biweekly / on-demand** cadence. First two payouts capped at **6%** withdrawal, full share thereafter. Note: independent reviews flag **payout-dispute / operator-durability risk** — weight accordingly.

## UNCONFIRMED items
- DD reset method/TZ; lot caps; minimum-days; per-program consistency caps (non-Instant); news windows; weekend/holding rules; exact commercial-EA enforcement (conflict above). Any verdict resting on these is `Conditional`.
