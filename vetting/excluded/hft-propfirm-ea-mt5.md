# HFT PropFirm EA / "Green Man" (MT5) — EXCLUDED (Gate A)

**Verdict: EXCLUDED at Gate A — core mechanism is HFT latency / quote-feed exploitation (tick-scalping
class).** Never scored. Reinforced by Gate C (prohibited at all four primaries) and by **zero
funded-survival admitted by the vendor itself.**

## One-line mechanism
A **high-frequency EA built solely to pass the evaluation phase of HFT-*permitting* prop firms** by
firing large numbers of micro-trades that exploit demo-server quote-feed latency / spread artifacts. The
vendor **explicitly states it is "not intended for live/real or funded accounts due to broker slippage
and high spreads"** — i.e. the mechanism only "works" against a challenge demo feed and structurally
**cannot survive real execution.**

## Vendor / Developer
**Dilwyn Tng** (MQL5; product 117386, MT5; also MT4 variants 104871/101153). Marketed as "Green Man."
Widely sold/group-bought; remote-setup service. Targets obscure HFT-allowing firms: "Optimal Trader,
Sure Leverage Plus, Delta Funding FX, Next Step Funded (HFT Evaluation), Nova Forex, Eden Funding, Vortex
Forex Fund, Aura Funded."

## Discovery
Queued 2026-06-22 ("MQL5 product 117386 HFT PropFirm EA — HFT, likely Gate A").

## Gate A determination (banned core mechanism)
**Disqualifying mechanism: HFT latency / quote-feed exploitation (tick-scalping / latency-arbitrage
class).** Confidence: **High.**

**Public signals (FACTS):**
- **MQL5 listing + reviews (via search, 2026-06-23):** EA is "designed to pass **high-frequency trading
  (HFT)** prop firm challenges"; "specifically designed to pass tests from firms **that allow HFT**";
  backtest "simulates HFT trading using 1-minute OHLC data"; auto lot, auto-pause on target.
- **Vendor's own admission:** "**not intended for live/real or funded accounts due to broker slippage and
  high spreads**" — the strategy depends on demo-feed conditions and does not transfer to real fills.
- **Negative case (search):** the HFT-permitting firms it targets (e.g. Delta Fund) are themselves
  reported as **non-paying / scam** prop firms; reviewers report challenges passed but **withdrawals
  impossible.** The whole funnel (EA + HFT-firm) is structurally incapable of producing a survived payout.

**Why excluded (mechanism, not label):** firing hundreds of micro-trades to exploit quote-feed/latency
differences on a demo challenge server is **tick-scalping / latency exploitation** — explicitly a Gate A
banned mechanism. Against the **primary firms' HFT/tick-scalping thresholds** (FIRM RULEBOOKS item 9;
default screen median hold <60s or >~200 trades/day/instrument), this EA is the archetype the screen
exists to catch. Excluded regardless of reported challenge-pass results.

## Per-firm legality (reinforcing — Gate C)
- **FundedNext / Funding Pips / The 5%ers / The Funded Trader — Prohibited.** All four primaries **ban HFT
  / latency / tick-scalping / arbitrage**. The EA is not marketed for any of them — only for niche
  HFT-allowing firms — so it is **Prohibited at all primary firms → would be Avoid even if not Gate-A
  excluded.**
- Reference (Alpha Capital, Goat) — Prohibited (source-code/commercial + HFT), non-gating.

## Funded-survival (the agent's actual objective) — structurally zero
The vendor **admits** it cannot run on a funded/live account; the target HFT firms are widely reported
non-paying. There is **no path to a survived payout** — the precise failure this agent exists to flag.
ROR **NON-ESTIMABLE** (demo-only exploit; no real-money trade distribution).

## Performance claims (recorded, NOT credited)
"Passes [HFT firm] challenges with low drawdown." **Tier 4 / not credited** — a demo-feed exploit's
pass rate says nothing about real survival, and the firms involved reportedly do not pay out.

## Why this is the case the agent exists to catch
An EA that openly **passes challenges it cannot survive funded** is the cleanest possible example of the
"passing ≠ surviving" trap. It is excluded on mechanism (HFT/latency), prohibited at every primary firm,
and self-admittedly worthless for funded trading.

## Source Links
- https://www.mql5.com/en/market/product/117386 — 2026-06-23 — MQL5 listing (HFT, target firms) — affiliate(vendor)
- https://www.surgefunded.com/hft-prop-firm-ea-review/ — 2026-06-23 — review (HFT mechanism, not-for-live) — mixed
- https://www.scalprobot.com/hft-prop-firm-ea-review/ — 2026-06-23 — review (pros/cons) — mixed
- WebSearch: HFT PropFirm EA mechanism + target firms — 2026-06-23 — discovery/confirmation — mixed
- WebSearch negative-case (banned/refund/scam/blown funded; Delta Fund non-paying) — 2026-06-23 — independent — mixed

## Analyst Notes
- **FACTS:** EA designed to pass HFT-permitting prop-firm evaluations; vendor states not for live/funded;
  target firms (Delta Fund etc.) reported non-paying; HFT/1-min-OHLC backtest; Dilwyn Tng.
- **ANALYSIS:** HFT latency/quote-feed exploitation = Gate A banned (tick-scalping/latency); prohibited at
  all four primaries (Gate C); funded-survival structurally zero by vendor admission. Triple-disqualified.
- **ASSUMPTIONS (flagged):** exact trade frequency/hold time not individually fetched, but the "HFT" self-
  description, 1-min-OHLC simulation, and "not for live" admission make the mechanism unambiguous.
