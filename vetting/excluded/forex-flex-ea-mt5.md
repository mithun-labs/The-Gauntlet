[← Index](../README.md) · [Rankings](../rankings/) · [Rulebooks](../rulebooks/)

# Forex Flex EA — EXCLUDED (Gate A)
*A "virtual trades" MT4/MT5 EA marketed to pass prop challenges — Excluded at Gate A for grid + martingale basket recovery.*

> 🚫 **EXCLUDED at Gate A** — core mechanism is grid + martingale / basket recovery with no per-trade hard stop. Never scored.

**Verdict: EXCLUDED at Gate A — core mechanism is grid + martingale basket recovery.** Never scored.

## One-line mechanism
A "virtual trades" entry engine feeding a **grid/martingale basket** system: named strategies include
**"HalfGrid"** and **"x3Retrace"**, positions are managed as **per-pair baskets** closed by an
**Equity Trailing TP**, the only stop is an **account-level "DD Stop loss"** (no hard per-trade stop), lot
sizes auto-scale, and independent reviews describe it **scaling in with "Martingale multipliers" / doubling
down into losers** — the textbook banned mechanism.

## Vendor / Developer
Forex Flex EA / **forexflexea.com** (long-running since ~2012; "Steve" / ForexFlexEA team). MT4 + MT5.
~$330+ one-time. Large affiliate/community marketing footprint (ranked #1 on several affiliate "best prop
firm EA 2026" listicles; matches the YouTube "This EA Can Pass EVERY Prop Firm Challenge [86% Winrate]"
content).

## Discovery
Surfaced by **broad keyword discovery** (not a predefined list): recurred across multiple independent web
rankings (newyorkcityservers, trading-guide, eatested) **and** YouTube ("86% winrate pass every prop
challenge"), i.e. the most-attended *new* EA this pass. Also appears on **FundedNext's explicitly
name-banned EA list**.

## Gate A determination (banned core mechanism)
**Disqualifying mechanism: grid + martingale / basket recovery with no per-trade hard stop.** Confidence: **High.**

**Public signals (FACTS):**
- **Vendor page (forexflexea.com, fetched 2026-06-23):** strategy list includes **"HalfGrid"** and
  **"x3Retrace Strategy"**; "Equity Trailing TP" tracks "all trades from each pair in a **basket**";
  risk control is a **"DD Stop loss — set a percentage of your account balance to close all trades at a
  certain drawdown percentage"** (account-level only — **no documented per-trade hard SL**); "Hedging"
  available; "Money Management — adjusts lot sizes based on account balance automatically."
- **Independent reviews (eatested, Medium, FPA, NYCServers-how-to-spot — via search):** "places a series of
  trades (a 'grid') at calculated intervals. When price moves against the initial position, Flex EA **scales
  in using controlled Martingale multipliers**"; critics: "**doubles down when trades go against it, opens
  multiple positions when one is losing, risks 35%+ of account balance on single trades with no stop loss**";
  "developer creates many demo accounts and shows profitable ones, blown accounts deleted."
- **Myfxbook community:** "Forex Flex EA Real1 ForexFBI" account showing large EURUSD lots was made private /
  appears blown; multiple accounts "kept blowing up and being replaced."

**Why excluded (mechanism, not label):** losing positions are **reinforced/averaged into** (x3Retrace +
Martingale multipliers) and managed as a **basket closed at an aggregate profit %**, with **no per-trade
stop loss** — risk is bounded only by a catastrophic account-level DD cutoff. This is grid/martingale by
behavior regardless of the "virtual trades / AI" marketing. Per the **optional-banned-mode rule**, even
though some of the 12 strategies are non-grid, the EA ships and is widely run with grid/martingale strategies
and the assessed live configuration is uninspectable → benefit of the doubt is withheld → **Excluded**.

## Per-firm legality (reinforcing — not needed for the Gate A exclusion)
- **FundedNext — Prohibited (explicit name-ban).** FundedNext's banned-EA list names **Forex Flex EA**
  specifically (alongside X Pass Bot, Gold OneShot EA, PropEA, The Prop Pilot, Fxblood Capital).
- **Funding Pips / The 5%ers / The Funded Trader — Prohibited.** Martingale/grid is prohibited at all; basket
  recovery with no per-trade SL violates risk/overleverage language.
- Reference firms (Alpha Capital, Goat) — Prohibited (procedural, non-gating).

## Performance claims (recorded, NOT credited)
Marketing: "passing FTMO challenges with an **86.96% win rate**, 1.67 RR, challenge in 18 days, DD below
10%." **Tier 4 / unverified** — a high win rate is the *expected* signature of a martingale/grid basket
(many small basket wins masking rare catastrophic losses), not evidence of survival. No inspectable Tier 0/1
record; blown accounts reportedly deleted. ROR **NON-ESTIMABLE**.

## Why this is the case the agent exists to catch
The single most-marketed "best prop firm EA / pass every challenge" product, with an 86%+ win-rate pitch and
a "dedicated prop-firm mode," is a grid+martingale basket that a primary firm (FundedNext) **bans by name**.
High win rate + no per-trade stop + deleted blown accounts is the canonical disguised-martingale profile.

## Source Links
- https://www.forexflexea.com/ — 2026-06-23 — vendor page (fetched: HalfGrid/x3Retrace, basket, DD-stop) — affiliate(vendor)
- https://newyorkcityservers.com/blog/best-ea-for-prop-firm — 2026-06-23 — affiliate ranking (fetched; 86.96% marketing) — affiliate
- https://forextester.com/blog/best-forex-ea-and-forex-robots/ — 2026-06-23 — review (fetched; 'virtual trades'/basket) — mixed
- WebSearch leads (grid+Martingale multipliers; FundedNext name-ban; blown/deleted accounts) — 2026-06-23

## Analyst Notes
- **FACTS:** vendor lists HalfGrid/x3Retrace strategies + basket ETTP + account-level-only DD stop + hedging
  + auto lot MM (fetched); independent sources describe Martingale scaling/doubling-down, no per-trade SL,
  35%+ per basket, blown/deleted accounts; FundedNext name-bans it; 86.96% win-rate marketing.
- **ANALYSIS:** behavior = grid/martingale basket recovery → Gate A exclusion (High confidence); high win
  rate is consistent with the mechanism, not with survival.
- **ASSUMPTIONS (flagged):** some of the 12 strategies may be non-grid, but the live/assessed config is
  uninspectable and the product centers on basket recovery → optional-banned-mode rule excludes.
