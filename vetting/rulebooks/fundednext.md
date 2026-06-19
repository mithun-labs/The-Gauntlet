# Rulebook — FundedNext
- **Source (PRIMARY — UNREACHABLE this run):** https://help.fundednext.com/ and https://fundednext.com/ both returned HTTP 503 to the fetch tool on every attempt (article, collection, blog, and landing paths; the underlying Intercom workspace slug could not be resolved). **No FundedNext primary page could be fetched this run.**
- **Source (secondary, fetched):** https://tradetanto.com/learn/fundednext-rules-a-complete-guide-for-cfd-traders (independent aggregator — CFD model parameters, EA policy, consistency)
- **Retrieved:** 2026-06-19 03:53 UTC
- **Rulebook version (agent-assigned):** v1
- **Change note:** initial — **built from SECONDARY sources only; PRIMARY refresh FAILED (503).**
- **STATUS: PROVISIONAL / UNCONFIRMED.** Every rule below is from a secondary aggregator, not FundedNext's primary site. Per HARD RULE 11 and FIRM RULEBOOKS, no Deployable verdict may rest on these rules, and per-firm legality judged against this rulebook is at best `Conditional`. **Flagged for operator: FundedNext primary site was unreachable (503) this run — see daily report.**

## Programs Offered   *(secondary — UNCONFIRMED)*
Stellar 2-Step, Stellar 1-Step, Stellar Lite, Stellar Instant (CFD).

## Profit Targets (per phase)   *(secondary — UNCONFIRMED)*
- 2-Step: P1 8% · P2 5%
- 1-Step: 10%
- Lite: P1 8% · P2 4%
- Instant: none

## Daily Drawdown   *(secondary — UNCONFIRMED)*
Balance-based, static-but-expandable (limit expands by intraday profit), reset at midnight server time:
- 2-Step: 5% · 1-Step: 3% · Lite: 4% · Instant: none

## Maximum Drawdown   *(secondary — UNCONFIRMED)*
- 2-Step: 10% (static, balance) · 1-Step: 6% (static) · Lite: 8% (static) · Instant: 6% (trailing)

## Minimum Trading Days / Time Limits   *(secondary — UNCONFIRMED)*
- 2-Step: 5/phase · 1-Step: 2 · Lite: 5/phase · Instant: none

## Consistency Rules   *(secondary — UNCONFIRMED)*
No CFD consistency rule reported for Stellar CFD models; a 40% consistency rule applies to Futures (except Rapid). (Secondary.)

## EA & Automation Policy   *(secondary — UNCONFIRMED)*
EAs reported allowed on MT4/MT5 (not cTrader/Match-Trader), with customization and a fee. Strategy-consistency clause: "Maintain the same trading strategy throughout your challenge and funded phases. Switching from manual trading to an EA after passing the challenge is prohibited." → A fully-automated commercial EA is **plausibly permitted** at FundedNext (unlike Funding Pips), but this rests on SECONDARY evidence → Conditional only.

## Banned Behaviors   *(secondary — UNCONFIRMED; primary list not fetched)*
Reported prohibited: spoofing, layering, **grid trading**, wash trading, latency arbitrage, reverse hedging, hedging with correlated instruments, account rolling, multi-order spam, slow-data-feed abuse, trading within 2% of CME price limits. **Martingale/grid → treat as Prohibited** (worse reading).

## HFT / Tick-Scalping Thresholds   *(UNCONFIRMED — not retrieved)*
Apply agent default screen (median hold < 60s OR > ~200 trades/day/instrument).

## News-Trading Restrictions   *(UNCONFIRMED — not retrieved)*

## Payout Structure & Profit Split   *(secondary — UNCONFIRMED)*
80% → 90% after FundedNext Pro (Stellar CFD); Instant 70% → 80%.

## UNCONFIRMED items
**Entire rulebook is UNCONFIRMED** (primary unreachable). Refresh from primary FundedNext source required next run; if persistently unreachable, escalate target-firm-set review to operator.
