# Rulebook — The 5%ers
- **Source:** https://help.the5ers.com/what-are-the-general-rules-for-the-high-stakes-program/ · https://help.the5ers.com/what-is-the-drawdown-rule-for-high-stakes/ · https://help.the5ers.com/what-is-the-leverage-in-the-high-stakes-program/ · https://www.eafunded.com/firms/the5ers (secondary, EA-policy corroboration)
- **Retrieved:** 2026-06-22 18:33 UTC (re-confirmed; previously 2026-06-19 10:50 UTC)
- **Rulebook version (agent-assigned):** v1
- **Change note:** initial — The 5%ers added as a PRIMARY target firm in CLAUDE.md v2.2; rulebook created this run before any vetting/re-check that gates on it. **2026-06-22 freshness refresh:** High Stakes drawdown rules re-fetched from primary help center (help.the5ers.com) — 5% daily DD (highest of prior-day closing equity/balance, 00:00 server reset, trailing) and 10% absolute/static max DD from initial balance UNCHANGED. No version bump.

## Programs Offered
- **High Stakes** (flagship, 2-step evaluation): New and Classic variants. Account sizes 2.5K, 5K, 10K, 25K, 50K, 100K. Unlimited completion time.
- **Hyper Growth** — one-step evaluation, $10K–$40K, biweekly payouts.
- **Bootcamp** — multi-step (3×6% targets) on sub-account balances; uses relative/trailing DD (less EA-friendly).
- (Pro Growth / Hyper variants also marketed.) Primary verdicts here gate against **High Stakes** unless an EA is specifically evaluated for another program.

## Profit Targets (per phase)
- New High Stakes: Phase 1 = **10%**, Phase 2 = **5%**.
- Classic High Stakes: Phase 1 = **8%**, Phase 2 = **5%**.
- Hyper Growth: **10%** (one step). Bootcamp: **6%** per step (×3).

## Daily Drawdown
- **5%**, calculated from **the closing equity OR balance of the previous day (whichever is higher)**. Reset at **00:00 server time**. (Equity-based intraday; trailing off prior-day high-water of close.)

## Maximum Drawdown
- **10% from initial balance — ABSOLUTE / STATIC** (High Stakes). Bootcamp uses relative **trailing** DD (shrinks as you profit) — treat Bootcamp as tighter/trailing.

## Leverage (per program · instrument class) — High Stakes
- Forex: **1:100** · Metals (incl. XAUUSD): **1:33** · Indices: **1:25**. (Lower metal/index leverage materially changes Gold/index EA sizing and ROR.)

## Lot-Size & Position Limits
- No explicit per-order lot cap found in primary source. `UNCONFIRMED` — not relied upon.

## Minimum Trading Days / Time Limits
- Minimum **3** profitable trading days. No max time on High Stakes (unlimited). Accounts inactive >30 consecutive days expire.

## Consistency Rules
- Not explicitly quantified in the fetched High Stakes general-rules page. `UNCONFIRMED` (a consistency/best-day cap may exist on some programs; do not rely on absence).

## EA & Automation Policy (exact language)
- EAs **allowed** with restrictions. Per The 5%ers standards (corroborated via eafunded.com summary of firm policy): "**HFT, tick scalping, rollover exploitation and shared third-party EA strategies are prohibited**," and "deploying pre-built EAs without understanding or controlling their internal logic is considered a violation of The 5%ers' trading standards." Original automated strategies that comply with the rules are permitted.
- **Material flag for this agent:** the "must understand/control internal logic" + "no shared third-party EA strategies" language is hostile to closed-source, off-the-shelf commercial challenge EAs — similar in spirit (though softer) to the reference-firm barriers. A black-box commercial EA is at best `Conditional` here.

## Banned Behaviors
- HFT, tick scalping, rollover/swap-arbitrage exploitation, shared third-party EA strategies, copy trading & coordinated multi-account strategies, excessive server requests.
- Martingale / grid: **not explicitly banned by name** in the EA-policy summary — but a no-stop-loss grid/martingale typically trips drawdown limits and may fall under "trading standards"/risk-management discretion. Gate A still excludes such EAs on mechanism grounds regardless.

## HFT / Tick-Scalping Thresholds
- No explicit numeric minimum hold time or max-trades/day stated. `UNCONFIRMED`. Apply the agent default screen (median hold <60s OR >~200 trades/day/instrument) for this firm.

## News-Trading Restrictions
- Vary by program; Hyper plan stricter. Specific lockout windows `UNCONFIRMED` from primary source.

## Weekend / Overnight Holding
- No forced-flat rule found for High Stakes; swing/overnight holding appears permitted on standard programs. `UNCONFIRMED` for program-specific swap/weekend rules.

## Payout Structure & Profit Split
- High Stakes withdrawals every **14 days** (Crypto / Rise / Bank Transfer). The 5%ers markets high splits (up to 100% on some scaling tiers). Exact split tier `UNCONFIRMED` from the fetched pages.

## UNCONFIRMED items
- Lot-size/position caps; quantified consistency rule; HFT numeric thresholds; news lockout windows; weekend/overnight swap specifics; exact profit-split tiers. Any legality verdict resting on these is `Conditional` and cannot support Deployable.
