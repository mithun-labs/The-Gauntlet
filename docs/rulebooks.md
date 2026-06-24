# Firm Rulebooks

> Part of **The Gauntlet** documentation — operating manual: [`../CLAUDE.md`](../CLAUDE.md). **Single source of truth for: the per-firm rulebook system — extraction fields, the rulebook file format, freshness, and bounded re-check.**
> References to ALL-CAPS section names in other docs resolve via the [Documentation Map](../CLAUDE.md#documentation-map).

## FIRM RULEBOOKS (the foundation every verdict rests on)

Rules determine pass/fail and EA legality. Do not rely on training data for any rule. Rulebooks
live in `vetting/rulebooks/<firm>.md`, are versioned, and carry a retrieval date.

### Extract per firm (tabulate in the rulebook file)

1. Program structures (1-step, 2-step, instant) and current names.
2. Profit target per phase.
3. Maximum daily drawdown — and **how it is calculated**: balance vs equity, static vs trailing,
   reset time + timezone.
4. Maximum overall drawdown — static vs trailing.
5. Minimum trading days / time limits.
6. Consistency rules (e.g., best-day caps as a % of total profit).
7. **EA / automation policy** — quote the exact prohibited-strategy language.
8. Explicit bans: martingale, grid, HFT, latency/arbitrage, tick scalping, news straddling,
   reverse trading, copy/group trading, "gambling" clauses.
9. **Quantitative thresholds for HFT / tick-scalping** — minimum hold time, minimum time between
   trades, maximum trades/day, wherever the firm states them. These anchor the pre-screen.
10. News-trading restrictions (lockout windows around high-impact events).
11. Payout structure, profit split, minimum holding/payout cadence.
12. **Leverage** per program / instrument class (e.g. 1:30 vs 1:100) — it changes position
    sizing and therefore the ROR estimate; an EA tuned for one leverage behaves differently at
    another.
13. **Maximum lot / position-size limits** — per-order lot caps, per-strategy allocation caps,
    and any lot-size scaling rules (some firms, e.g. Alpha Capital, enforce these, and they
    directly bound an EA's sizing and ROR).
14. **Weekend / overnight holding rules** — whether positions must be closed before
    weekend/rollover or around news, plus swap/holding restrictions (these can disqualify swing
    EAs regardless of mechanism).

Flag any rule not confirmable from the firm's **primary source** as `UNCONFIRMED`. Any legality
verdict depending on an `UNCONFIRMED` rule is `Conditional — depends on UNCONFIRMED rule X` and
cannot support a Deployable verdict.

### Rulebook file format — `vetting/rulebooks/<firm>.md`

```markdown
# Rulebook — <Firm Name>
- **Source:** <primary URL(s)>
- **Retrieved:** YYYY-MM-DD HH:MM UTC
- **Rulebook version (agent-assigned):** vN
- **Change note:** <what changed vs previous, or "initial">

## Programs Offered
## Profit Targets (per phase)
## Daily Drawdown          (value · equity vs balance · static vs trailing · reset + TZ)
## Maximum Drawdown        (value · static vs trailing)
## Leverage                (per program · instrument class)
## Lot-Size & Position Limits  (per-order cap · per-strategy cap · scaling lot rules)
## Minimum Trading Days / Time Limits
## Consistency Rules
## EA & Automation Policy   (exact language)
## Banned Behaviors
## HFT / Tick-Scalping Thresholds   (min hold time, min time between trades, max trades/day)
## News-Trading Restrictions
## Weekend / Overnight Holding  (forced-flat? · rollover/swap rules · news-close rules)
## Payout Structure & Profit Split
## UNCONFIRMED items
```

### RULEBOOK FRESHNESS CHECK (START-OF-RUN, before vetting any EA)

- **Staleness threshold: 72 hours.** If a rulebook's `Retrieved` is older than 72h, or missing,
  re-fetch the primary source and rewrite the rulebook before vetting.
- If re-fetched rules differ: **bump the version**, write the change note, and identify every EA
  whose `firm_verdicts` cite the old version. (The manual validation checklist also flags these.)
- If a firm's site is unreachable: keep the stored rulebook, mark it `STALE — refresh failed
  YYYY-MM-DD`, and treat verdicts derived from it as provisional in today's report.
- If a firm is **persistently unreachable across runs**, or has **materially restructured or retired**
  the programs you vet against, flag it in the daily report for **operator review of the target-firm
  set** — the primary/reference firm list is not self-updating.

### Tiered, bounded re-check (prevents run starvation at scale)

On a version bump, do **not** re-check the whole database in one run:
- **Immediately** re-check only **Deployable + Watchlist** EAs that cite the old version, capped
  at **N = 10** per run (high-stakes, small set).
- **Queue** all affected **Avoid** EAs for lazy re-check (already negative; non-urgent).
- Record the outstanding re-check backlog in the daily report so it is never lost.
- **Drain before discovery (the cap must not become a leak).** The N = 10 cap bounds work *per
  run*, but the backlog must shrink over time. If a **Deployable/Watchlist** re-check backlog
  exists at START-OF-RUN, spend the re-check budget on **draining it first**, before discovering
  any new EAs — a stale-rulebook verdict on a tracked EA is worse than vetting one fewer new
  candidate. If the Deployable/Watchlist backlog has been non-empty for **3 consecutive runs**,
  **raise the cap** for those runs (e.g. N = 25) and pause new-EA discovery until it clears. A
  Deployable/Watchlist EA must never carry a rulebook version more than **one bump** behind.

---

