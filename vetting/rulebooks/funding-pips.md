# Rulebook — Funding Pips
- **Source (primary):** https://intercom.help/fundingpips/en/articles/8536000-what-are-the-forbidden-strategies (Funding Pips' own Intercom-hosted help center — forbidden-strategy language)
- **Source (secondary, numerics):** https://proptradingvibes.com/blog/fundingpips-rules (independent aggregator — numeric model parameters)
- **Retrieved:** 2026-06-19 03:53 UTC
- **Rulebook version (agent-assigned):** v1
- **Change note:** initial.
- **Access note:** The Funding Pips marketing domain `fundingpips.com` and the custom help domain `help.fundingpips.com` returned HTTP 403/429 to the fetch tool (bot protection). The **forbidden-strategies article was fetched successfully via the firm's underlying Intercom workspace** (`intercom.help/fundingpips`), which serves the same primary help content — so the prohibited-strategy / EA-policy section below is **PRIMARY-SOURCED and CONFIRMED**. The **numeric model parameters** (targets/drawdown/days/splits) below could **not** be fetched from a Funding Pips primary page this run and are taken from an independent secondary aggregator — they are marked **UNCONFIRMED** and must not be used to clear a Deployable verdict.

## Programs Offered
2-Step Standard, 2-Step Pro, 1-Step, Zero (Instant Funding). *(secondary — UNCONFIRMED)*

## Profit Targets (per phase)   *(secondary — UNCONFIRMED)*
- 2-Step Standard: P1 8% · P2 5%
- 2-Step Pro: P1 6% · P2 6%
- 1-Step: 10%
- Zero: none (instant)

## Daily Drawdown   *(secondary — UNCONFIRMED; balance vs equity / reset window not on primary page)*
- 2-Step Standard: 5% (static, balance-based)
- 2-Step Pro: 3% (static, balance-based)
- 1-Step: 5% (static, balance-based)
- Zero: 3% (trailing, equity-based)

## Maximum Drawdown   *(secondary — UNCONFIRMED)*
- 2-Step Standard: 10% (static)
- 2-Step Pro: 6% (static)
- 1-Step: 6% (static)
- Zero: 5% (trailing, equity-based)

## Minimum Trading Days / Time Limits   *(secondary — UNCONFIRMED)*
- 2-Step Standard / 1-Step: 3 trading days; no max time limit stated
- 2-Step Pro: 1 day
- Zero: 7 days before payout

## Consistency Rules   *(mixed)*
- During evaluation: none stated (secondary — UNCONFIRMED).
- Funded / payout: a consistency score requirement is referenced for on-demand/funded payouts (e.g. 35% on Standard, 15% permanent on Zero) — secondary, UNCONFIRMED.

## EA & Automation Policy   (PRIMARY — CONFIRMED)
Verbatim from the primary help article: "Using a third-party Expert Advisor (EA) is allowed as long as it is a trade or risk manager. Using any other third-party Expert Advisor is not allowed." A self-developed EA (proof of ownership) may be permitted for full automation; the **1K Instant account** is an exception where third-party EAs/copiers are permitted.
- **Implication for this agent:** a **commercially purchased, fully-automated third-party EA** (the typical MQL5 Market product this agent vets) is **NOT permitted** on standard Funding Pips evaluations unless it is purely a trade/risk manager. This is decisive for Gate C.

## Banned Behaviors   (PRIMARY — CONFIRMED, verbatim list)
"gap trading, high-frequency trading, server spamming, latency arbitrage, toxic trading flow, hedging, long-short arbitrage, reverse arbitrage, tick scalping, server execution, opposite account trading, and churning and burning." Also prohibited: copy trading with others, account management by third-party vendors.
- **Martingale and grid trading** are reported as prohibited (account suspension/termination). The verbatim primary list above does not itemize the words "martingale/grid", but independent reviews and the firm's risk language describe them as prohibited → treat **martingale/grid as Prohibited** (take the worse reading per HARD RULE 6).

## HFT / Tick-Scalping Thresholds   (PRIMARY language; no explicit numeric threshold retrieved)
HFT and tick scalping are named as forbidden. No explicit minimum-hold-time / max-trades-per-day number was on the fetched primary page → apply the agent default screen (median hold < 60s OR > ~200 trades/day/instrument) for this firm.

## News-Trading Restrictions   *(UNCONFIRMED)*
Gap trading is forbidden (primary). Specific high-impact-news lockout windows were not retrieved from primary this run → UNCONFIRMED.

## Payout Structure & Profit Split   *(secondary — UNCONFIRMED)*
Standard/1-Step: 60% weekly → up to 100% monthly; 90% on-demand (35% consistency). Pro: 80%. Zero: 95% bi-weekly.

## UNCONFIRMED items
All numeric parameters (targets, drawdown values, balance-vs-equity for standard models, reset timezone, min days, splits, consistency percentages, news windows) are from a secondary aggregator and are UNCONFIRMED pending a primary-source fetch. The prohibited-strategy list and EA policy are PRIMARY-CONFIRMED.
