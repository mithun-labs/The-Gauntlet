# Scoring & Verdicts

> Part of **The Gauntlet** documentation — operating manual: [`../CLAUDE.md`](../CLAUDE.md). **Single source of truth for: evidence tiers, eligibility gates (A/B/C), per-EA profile, risk-of-ruin, the skeptic steelman, scoring (dimensions/weights/multipliers/ceilings), and the deployment verdict & bands.**
> References to ALL-CAPS section names in other docs resolve via the [Documentation Map](../CLAUDE.md#documentation-map).

## EVIDENCE STANDARD (verification gating — the core of the task)

Label every performance figure with its tier and put every material claim in the per-EA Evidence
Matrix. Evidence tiers describe **what the public source can support**, not what is probably true.

- **Tier 0 — Verified funded-account evidence (highest):** a verifiable public record from an
  actual prop-firm funded account — payout receipts tied to a named firm, funded statements/dashboards,
  or a track record demonstrably hosted on the prop firm's own server/broker. Still label it as
  public evidence; do not pretend you privately authenticated the account.
- **Tier 1 — Independently verified live (real money):** Myfxbook/FXBlue verified, **real-money,
  public trade history, AND ≥6 months.** State real vs demo explicitly.
- **Tier 2 — Verified but caveated.** Split by whether a **real-money, publicly inspectable
  trade-level record** underlies the headline claim, because the two sub-tiers differ in what they
  can support (ROR-estimability and trackability), even though **both use the Tier-2 evidence
  multiplier**:
  - **Tier 2A — real-money but caveated:** a verified Myfxbook/FXBlue **real-money** account with
    **public, trade-by-trade history** that is demoted from Tier 1 **only** by track length
    (**<6 months**), **low deposit**, or **small sample**. The trades are real and inspectable; the
    record is simply short/small. *The Tier 2A caveats demote an otherwise-Tier-1 record:* a
    real-money but <6-month or low-deposit account is Tier 2A, not Tier 1.
  - **Tier 2B — weakly verified:** verified yet **demo-only**, **hidden/private trade history**, or
    showing **curve-fit to a specific period** — i.e. no inspectable real-money trade-level basis.
    Demo fills, hidden histories, and single-period curve-fits cannot be trusted to behave like a
    real account, so Tier 2B is treated as the weak end of the band.
- **Tier 3 — Vendor-reported / unverifiable:** screenshots, vendor-hosted equity curves, videos,
  MQL5 signal stats without independent verification, or backtests only.
- **Tier 4 — Marketing claim with no inspectable public basis** (and any prop-success claim lacking
  Tier 0).

### Source quality rules

- Vendor pages establish what the vendor claims, not whether the claim is true.
- Affiliate reviews are not independent community sentiment; they may identify claims and products,
  but they cannot corroborate performance.
- Search snippets, AI summaries, unfetched URLs, and private/paywalled channels are not sources.
- Screenshots and dashboard videos remain weak evidence unless they link to a public hosted record.
- A fetched page can support only what it actually says; missing metrics remain `NOT REPORTED`.

### EA-level tier (used by the multiplier and the gates)

Each scored dimension uses the tier of the evidence substantiating **that dimension's specific
claim**. The **EA-level tier** (`best_tier`) is the tier of the evidence **jointly substantiating
the headline return-AND-drawdown pair** — *not* the single best figure — applying the EVIDENCE
STANDARD tier rules to that pair. The **≥6-month window is a requirement for Tier 1**; a real-money
pair that is verified and inspectable but shorter (or low-deposit / small-sample) is **Tier 2A**,
and a demo/hidden/curve-fit pair is **Tier 2B**. One cherry-picked verified micro-account does
**not** raise `best_tier` if the headline metrics it is used to support rest on weaker sources —
this closes the cherry-pick loophole. Record the Tier-2 sub-tier (`TIER2A` real-money-inspectable
vs `TIER2B` demo/hidden/curve-fit); the verdict logic and ROR-estimability key off this distinction.

### Backtest scrutiny

You cannot run or reproduce the backtest. Treat public backtests as claims to inspect, not as proof.
Record whether the public report states real tick data; spread, commission, slippage, swap; multiple
regimes (trending, ranging, shocks — 2020, 2022, any 2024–2026 shifts); and out-of-sample /
walk-forward. A bull-only backtest is near-worthless for an all-weather claim — say so.

### Evidence Matrix (mandatory per EA)

Every surviving EA file must include this table before scoring:

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline return/DD | | vendor / independent / primary / forum / affiliate | independent / vendor / affiliate / unknown | TIER0–TIER4 | YYYY-MM-DD | High / Medium / Low | |
| Mechanism / risk controls | | | | | | | |
| Prop-firm success claim | | | | | | | |
| Negative-case evidence | | | | | | | |

### Tagging (anti-fabrication)

Every figure carries its tier tag and a source link. No inspectable public source → `NOT REPORTED`.
Never estimate, infer, or calculate a missing metric and present it as reported. A thorough-looking
write-up does not promote a tier.

---

## ELIGIBILITY GATES (applied BEFORE scoring — gates, not graded contributors)

Legality and mechanism transparency are pass/fail or ceiling conditions, never things a high score
elsewhere can compensate for.

### Gate A — Pre-screen (banned core mechanism)

Eliminate any EA whose **publicly documented, independently demonstrated, or strongly inferable**
core mechanism is martingale, grid/recovery averaging, latency/arbitrage, tick scalping, or
news-spike exploitation. Disqualifying regardless of reported performance.

Because you have **no source or terminal access**, infer the core mechanism from public signals —
marketing language, equity-curve shape, listing metadata, settings screenshots, community teardowns,
MQL5 comments — per **WEB RESEARCH PROTOCOL §E**, and exclude on the *inferred* mechanism when the
signals are strong enough. Record the signals and confidence.
- Detect **disguised** variants — "smart recovery", "adaptive position sizing", "DCA", "hedging
  basket", "zone recovery", "no-stop averaging". Describe the mechanism, not the label: if losing
  positions are reinforced/averaged down, or size scales with adverse excursion, it is martingale/grid
  → **Excluded**.
- **Tick-scalping / HFT** is judged against the firm's rulebook thresholds (FIRM RULEBOOKS item 9).
  Where a firm states none, default screen: **median hold time < 60s OR > ~200 trades/day per
  instrument** flags it for that firm.
- **Optional banned mode:** a banned behavior present but optional → **Excluded** unless public
  documentation shows it can be hard-disabled **and** the public evidence being assessed clearly uses
  the disabled configuration. If the assessed configuration is unknown, do not give benefit of doubt.
- Record every elimination in `vetting/excluded/<slug>.md` (one-line mechanism + source) and as an
  index row with `verdict: "Excluded"`. No silent drops.

### Gate B — Mechanism transparency ceiling

If the EA's mechanism is **not publicly verifiable** (closed source, no public logic description, no
credible third-party teardown, and no clear mechanism inference)
— not excluded, but constrained, because a black box may conceal a banned mode or unknown risk
behavior:
- **Prop-Firm Compliance score ceiling = 5/10.**
- **Risk Management score ceiling = 4/10** (controls cannot be confirmed publicly).
- **Deployment Verdict ceiling = Watchlist.**
- Record `mechanism_confidence` as `Low` or `Unknown` and "mechanism unverifiable" as a standing red
  flag. Actively hunt the mechanism (WEB RESEARCH PROTOCOL §B and §E — MQL5 comments, settings
  manuals, ForexFactory teardowns) before accepting it as merely unknown.

> **Gate B is about the *mechanism*, not the controls.** A black box may still carry
> vendor-documented risk controls (e.g. a stated hard stop). Such an EA still triggers Gate B
> (its mechanism is opaque, so the ceilings above apply), but it is **not** auto-Avoided by Avoid
> criterion 3 — which fires only on a black box that *also* lacks any documented controls. This is
> what makes the Watchlist ceiling reachable: a documented-control black box can sit at Watchlist
> (constrained), while a no-controls black box is Avoided. (Either way it fails Deployable gate 1,
> which bars an un-inferable black box — so Gate B's Watchlist ceiling is the true cap.)

### Gate C — Per-firm legality

- **Prohibited at a firm** → that firm is removed from the EA's eligibility; the EA cannot be
  Deployable for that firm.
- **Prohibited at all primary firms** → **Verdict = Avoid**, regardless of Overall (still scored and
  recorded for the archive).
- If a legality judgment depends on an `UNCONFIRMED` rule, mark the firm verdict `Conditional`; do
  not use it to clear Deployable.

EAs surviving Gates A–C proceed to profiling and scoring. Surviving is **not** a positive signal.

---

## PER-EA PROFILE (for every EA surviving the gates)

1. EA Name.
2. Vendor/Developer — identifiable & accountable, or anonymous (red flag).
3. MT5 compatibility and dependencies — only what is publicly documented (raw-spread/ECN, GMT
   offset, hedging account, symbols, timeframe, VPS/broker requirements).
4. Trading strategy — the **publicly documented, independently demonstrated, or inferable mechanism**,
   not the marketing category; include `Mechanism Inference Confidence`.
5. Recommended instruments.
6. **Evidence Matrix** — every material claim mapped to fetched source, independence, tier,
   retrieval date, confidence, and notes.
7. **Source Reliability Assessment** — source counts, independent vs vendor vs affiliate, and the
   strongest public evidence found.
8. **Unverified Claims** — performance, prop-passing, payout, risk-control, and stop-loss claims that
   remain unsupported or vendor-only.
9. Average monthly return — with **tier**, source, and **track length**; `NOT REPORTED` if absent.
10. Maximum historical drawdown — with **tier**; verified equity-DD vs vendor claim.
11. Myfxbook/FXBlue verified results — real vs demo, link, track length, broker, public trade-history
    availability.
12. Backtest quality and duration — assessed against the EVIDENCE STANDARD; public backtests are
    claims, not reproduced tests.
13. Per-firm legality verdict — **primary:** FundedNext / Funding Pips / The 5%ers / The Funded
    Trader; **reference:** Alpha Capital / Goat Funded Trader — each `Permitted` / `Prohibited` /
    `Conditional`, **with the rulebook version judged against** (reference verdicts do not gate).
14. Rule-violation flags — each with a one-line public-evidence justification.
15. Mechanical rule-respect — publicly documented or independently demonstrated hard equity-stop /
    daily-loss-stop / max-position controls, or `NOT REPORTED` / manual-only.
16. Recommended risk settings for **50k / 100k / 200k**, sized only from verified public data; if the
    data is insufficient, state that sizing is non-actionable and ROR is `NON-ESTIMABLE`.
17. Cost and licensing model — one-time vs subscription, account/license limits, refund policy.
18. User reviews and community feedback — independent only; summarize the **negative case** explicitly
    (search "[EA] scam", "[EA] blown account", "[EA] refund").
19. Red flags.

---

## RISK-OF-RUIN & LIMIT-VIOLATION ANALYSIS (mandatory)

Default to `NON-ESTIMABLE` for web-researched EAs. ROR is estimable **only from real-money,
publicly inspectable, trade-level history** — Tier 0, Tier 1, **or Tier 2A** (a verified real-money
Myfxbook/FXBlue page exposing trade-by-trade data, or public funded-account trade history). What
makes ROR estimable is a **real per-trade return distribution you can resample**, not the deposit
size or track length — so a short or small-deposit **real-money** record (Tier 2A) is estimable,
just at **lower confidence**. Demo-only or hidden histories (Tier 2B), vendor claims, screenshots,
MQL5 summaries, videos, and backtests are **not** estimable — they have no trustworthy real-money
trade distribution.

**Tag every ROR estimate with a confidence grade tied to its evidence tier:**
- **Tier 0/1 → `ROR-High`:** long real-money trade-level history; the estimate carries normal weight.
- **Tier 2A → `ROR-Low`:** real-money but short (<6 months), low-deposit, or small-sample. The
  estimate is **directional only** — explicitly flag the dominant caveats (short sample → wide
  confidence interval; possible **autocorrelation** in a brief window; **deposit-scaling**
  assumptions when restating risk-per-trade for 50k/100k/200k). A `ROR-Low` estimate informs the
  **score** but **does not satisfy Deployable gate 7**, which still requires Tier 0/1 history.

When real-money Tier 0/1/2A trade-level history is available, estimate:

- **P(violating daily DD)** per phase, against the **tightest primary** firm's daily-DD rule, using its
  actual calculation (equity vs balance, trailing vs static).
- **P(violating max overall DD).**
- **Risk of ruin** over **30 / 90 / 365 trading days.**

State assumptions: (1) the per-trade/daily distribution and whether it came from **real-money
Tier 0/1/2A trade-level public history** (and its `ROR-High`/`ROR-Low` grade) or is unavailable →
`NON-ESTIMABLE`; (2) win rate, avg win/loss, trade frequency; (3) **independent vs autocorrelated**
returns (lumpy curves raise true ROR — flag it; short Tier-2A windows are especially exposed to
this); (4) risk-per-trade tied to the 50k/100k/200k settings; (5) whether tail/shock regimes were
included (a short Tier-2A window usually has **not** seen a shock — say so); (6) the **method**
(closed-form ROR vs Monte Carlo over resampled trades) and sample size.

**Metric-definition reconciliation (mandatory whenever a DD figure is used).** A drawdown value shown
by Myfxbook/FXBlue/MQL5 uses that host's own method and is rarely the same quantity as a firm's
daily or overall DD rule (equity vs balance, trailing vs static, reset window). Never compare a host
DD figure directly to a firm limit: restate it under the firm's definition where the data allows, or
record a `DD-definition mismatch` caveat and treat the comparison as indicative only.

`NON-ESTIMABLE` is a **negative finding for Survival** (it caps the Survival multiplier to
`min(A, 0.20)` — see SCORING) and **bars a Deployable verdict.** An **estimable** ROR — including a
`ROR-Low` estimate from Tier 2A real-money history — does **not** trigger that cap; Survival then
uses the ordinary tier multiplier (which already discounts Tier 2A heavily), and the `ROR-Low`
caveats are carried into the verdict's binding criterion. Never manufacture a distribution from a
single headline return, max drawdown, backtest, screenshot, or vendor statement.

---

## MANDATORY: STEELMAN THE SKEPTIC (before scoring)

Write the strongest case that **this EA will fail** into `## Why This Will Probably Fail`:

1. **Most likely benign explanation** — curve-fit to one regime; a short/demo track sold as proof;
   survivorship among the vendor's many accounts; returns that are hidden leverage or martingale
   not yet visible in a calm period.
2. **Prop-server case** — would a different broker/feed/spread/commission and the firm's own DD
   calculation erase the edge or trip a limit the vendor never tested?
3. **Variance case** — could it pass by luck and then blow the funded account? (Passing and
   surviving are different problems.)
4. **Evidence fragility** — how much rests on Tier 3/4? What single piece of evidence (an
   inspectable funded-account history) would most change your mind — and note you do not have it.

If the skeptic's case is decisively stronger, the verdict is "will probably not survive" — a
successful, valuable outcome. Record it and move on.

---

## SCORING (manual, 1–10 per dimension, latent × evidence multiplier, weighted)

The scoring source of truth is this section. No external scoring engine is required. Every EA file must
show enough arithmetic for a human to reproduce the adjusted dimension scores and Overall.

### Manual scoring steps

1. Assign an integer **latent** score from 1–10 for each dimension, using public evidence only.
   Clamp anything outside the range back to 1–10.
2. Assign the evidence tier supporting each multiplied dimension. Use `best_tier` for the
   return/DD-driven dimensions unless a dimension-specific tier is clearly different.
3. Apply the multiplier or Gate-B ceiling:
   - Survival and Challenge-Passing use Multiplier A.
   - Profitability, Consistency, and Transparency use Multiplier B.
   - Compliance and Risk are mechanism-based and are not multiplied.
   - If ROR is `NON-ESTIMABLE`, Survival uses `min(Multiplier A, 0.20)`. An **estimable** ROR —
     including a `ROR-Low` estimate from Tier 2A real-money history — does **not** trigger this cap;
     Survival then uses the ordinary Multiplier A for its tier. (Tier 2A and Tier 2B both take the
     **Tier-2** multiplier row; they differ only in ROR-estimability and the verdict logic.)
   - If the mechanism is unverifiable, Compliance is capped at 5 and Risk is capped at 4.
   - **Risk control-evidence ceiling.** The Risk score reflects how well hard controls (equity stop,
     daily-loss stop, max-position) are *established*, not merely claimed: independently demonstrated
     (third-party teardown, settings screenshot, observed behavior) -> no extra cap; vendor-documented
     only -> Risk ≤ 5; claimed without documentation -> Risk ≤ 3; not reported or manual-only -> Risk ≤ 2.
     Apply the **lowest** applicable ceiling (this and the Gate-B Risk ceiling of 4).
4. Compute each adjusted dimension:
   - Multiplied dimensions: `adjusted = clamp(round_half_up(latent × multiplier), 1, 10)`.
   - Compliance/Risk: `adjusted = clamp(min(latent, applicable ceilings), 1, 10)`, where applicable
     ceilings = the Gate-B ceiling (if the mechanism is unverifiable) and, for Risk, the
     control-evidence ceiling from step 3 — take the lowest that applies.
5. Compute Overall from adjusted scores:
   `0.30·Survival + 0.20·Compliance + 0.15·Risk + 0.15·Challenge + 0.10·Consistency + 0.05·Transparency + 0.05·Profitability`.
6. Round Overall **half-up to one decimal**. For manual arithmetic, if the second decimal is 5 or
   greater, round the first decimal up.

### Dimensions and weights

| Dimension | Weight | Basis | Adjustment |
|---|---:|---|---|
| **Funded-Account Survival** | 30% | probability of repeated payout and sustained funding | × Multiplier **A** + ROR cap |
| **Prop-Firm Compliance** | 20% | legality across the **primary** firms' current rules (reference firms inform but don't drive the score) | Gate B ceiling 5 if unverifiable; Gate C |
| **Risk Management** | 15% | quality and *evidence level* of hard DD controls (independently demonstrated > vendor-documented > claimed) | Gate B ceiling 4 if unverifiable; control-evidence ceiling (step 3) |
| **Challenge-Passing Probability** | 15% | probability of clearing the evaluation | × Multiplier **A** |
| **Consistency** | 10% | low return dispersion; shallow, brief drawdowns | × Multiplier **B** |
| **Transparency of Results** | 5% | inspectability/independence of the evidence | × Multiplier **B** |
| **Profitability** | 5% | magnitude/durability of verified returns | × Multiplier **B** |

### Latent score anchors (assign the 1—10 before any multiplier)

These anchor the **latent** score so runs stay consistent. Pick the band that fits the public
evidence, then fine-tune within it; the multiplier and gates are applied *after* this.

| Dimension | 1—3 | 4—6 | 7—9 | 10 |
|---|---|---|---|---|
| **Funded-Survival** | no funded evidence; martingale/grid signature or smooth-then-cliff curve | some real-money history but short or caveated; survival plausible, unproven | long verified real-money record consistent with repeated payout | Tier-0 funded record with repeated *realized* payouts |
| **Compliance** | prohibited or likely-prohibited at the primary firms | conditional/unclear; only some rules met | clearly permitted at ≥1 primary firm on current rules | permitted at all primary firms on confirmed current rules |
| **Risk** | no controls, contradicted controls, or manual-only | controls vendor-documented but not independently shown | hard controls independently shown to hold | controls shown to hold across regimes incl. shocks |
| **Challenge-Passing** | metrics far from targets, or untestable | plausibly clears in a calm regime only | verified history clears targets within limits | clears with wide margin across regimes |
| **Consistency** | high dispersion; deep or long drawdowns | moderate dispersion; lumpy recovery | low dispersion; shallow, brief drawdowns | low dispersion across multiple regimes |
| **Transparency** | vendor-only / screenshots (Tier 3—4) | partial public verification | independent verified hosted record | full public trade-level history, long track |
| **Profitability** | unverified, or negative real returns | modest verified returns, short window | solid verified returns over ≥6 months | strong, durable verified returns across regimes |

### Evidence multipliers

```
Multiplier A — Challenge-Passing, Funded-Account Survival
  Tier 0: 1.00   Tier 1: 0.70   Tier 2: 0.45   Tier 3: 0.25   Tier 4: 0.12

Multiplier B — Profitability, Consistency, Transparency
  Tier 0: 1.00   Tier 1: 0.95   Tier 2: 0.60   Tier 3: 0.30   Tier 4: 0.15

Tier 2A and Tier 2B BOTH use the Tier-2 multiplier row (0.45 / 0.60).
ROR cap: if ROR is NON-ESTIMABLE, Survival multiplier becomes min(A, 0.20).
  An ESTIMABLE ROR (incl. ROR-Low from Tier 2A real-money history) does NOT cap Survival.
Gate-B ceilings: mechanism-unverifiable Compliance ≤ 5, Risk ≤ 4.
```

`round_half_up` means ordinary arithmetic rounding: `4.5 → 5`, `2.5 → 3`. The clamp to `[1, 10]`
is mandatory. There are no zero scores and no scores above 10.

### Overall bands and contradiction review

Overall bands: `≥7.5` strong · `6.0–7.4` promising · `4.0–5.9` weak/unproven · `<4.0` poor.

An Overall `≥6.0` paired with an **Avoid** verdict is a contradiction warning, not an automatic
override. Re-check the scoring and gates. If the Avoid verdict is caused by a hard gate, record that
hard-gate reason as the binding criterion; otherwise lower any over-generous soft dimensions before
committing.

The **latent** score exists only to preserve ordering among unproven EAs so a future pass or the
operator knows which are worth chasing funded-account evidence on. Never surface latent as the
headline and never rank by it.

---

## DEPLOYMENT VERDICT — "Would I deploy my own money?"

An absolute investment-quality judgment, bucketed and deterministic. An EA can lead a weak field on
Overall and still be **Avoid**. Because Claude is operating from public web research only,
`Deployable` should normally be unreachable without operator-supplied funded-account evidence.

### Deployable quality gates (ALL required)

1. Mechanism established as non-banned from **public** evidence — published/open logic, public
   settings/risk documentation, or a credible **independent** third-party teardown (not merely the
   vendor's own broad description, and not an un-inferable black box).
2. `best_tier` is **Tier 1 or better** for the headline return+DD pair. (Tier 2A and Tier 2B do
   **not** satisfy this gate — Deployable requires a full ≥6-month real-money verified record.)
3. **≥6 months** verified live (real-money) history.
4. **Verified equity max DD ≤ 60% of the tightest primary firm's max-overall-DD limit** (restated
   under that firm's own DD definition), over a ≥6-month track (e.g. ≤6% against a 10% firm
   limit), **AND** no single day exceeding 60% of the tightest primary daily-DD limit. (Historical max DD understates future max DD; deploy with headroom.)
5. Compatible with **current, confirmed** rules at ≥1 **primary** target firm — not dependent on `UNCONFIRMED`
   rules; not Prohibited at that firm.
6. Demonstrated consistency **across multiple market regimes.**
7. **Estimable and acceptably low** risk-of-ruin from public **Tier 0/1** trade-level history. (A
   `ROR-Low` estimate from Tier 2A real-money history informs the score but does **not** clear this
   gate — Deployable requires `ROR-High` from Tier 0/1.)
8. **Funded-account evidence present** (Tier 0, or operator-confirmed funded statements).

### Verdict assignment (exactly one)

```
EXCLUDED      — failed Gate A (banned/optional-banned core mechanism). Never scored.

AVOID         — any of:
                • Prohibited at all primary firms (Gate C), OR
                • headline return+DD evidence is Tier 3 or Tier 4 (no independent verification), OR
                • mechanism unverifiable (Gate B) AND **no** publicly documented risk controls
                  (a documented-control black box is constrained to Watchlist, not Avoided), OR
                • ROR NON-ESTIMABLE AND best_tier is Tier 2B, Tier 3, or Tier 4
                  (demo-only, hidden-history, curve-fit, or unverifiable — no inspectable
                  real-money trade-level basis).

                NOTE: a real-money, publicly inspectable but caveated record (Tier 2A — short
                <6-month track, low deposit, or small sample) is NOT auto-Avoided here. Its ROR is
                estimable at ROR-Low confidence (RISK-OF-RUIN section), so this criterion does not
                fire on tier alone; such an EA, if it also clears Gate C and is not a black box,
                lands on WATCHLIST as a candidate for further evidence-gathering. (Tier 2A still
                cannot reach Deployable: it fails gates 2, 3, and 7.)

DEPLOYABLE    — Deployable quality gates 1–8 ALL met.

WATCHLIST     — the residual: clears enough to track but fails at least one Deployable gate.
                If the ONLY failing gate is #8 (funded-account evidence), set
                binding_criterion = "lacks funded-account evidence only — candidate for operator
                evidence-gathering" (the operator's cue to go obtain funded statements).
                If the EA rests on Tier 2A (real-money but caveated) evidence, set
                binding_criterion = "real-money but caveated (<6-month / low-deposit / small-sample)
                — needs a ≥6-month real-money track (and DD headroom) to advance" and record the
                ROR-Low caveats. This is the home of promising-but-unproven EAs worth chasing.
```

> **Autonomous ceiling = Watchlist.** Gate 8 (funded-account evidence) is essentially unobtainable
> by a remote web-research routine alone, so a Claude-only vetting pass normally tops out at
> **Watchlist** — the honest limit of what can be concluded without operator-supplied funded
> statements or primary funded-account proof. **Deployable** is reserved for the rare case where
> Tier 0 public funded evidence exists or the operator provides funded evidence. This is by design,
> not a shortfall.

Always state the **binding criterion** — the single reason an EA did not clear Deployable. If no EA
qualifies, say so plainly; "everything is Watchlist or Avoid" is a valid, honest outcome.

---

