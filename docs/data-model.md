# Data Model & Duplicate Detection

> Part of **The Gauntlet** documentation — operating manual: [`../CLAUDE.md`](../CLAUDE.md). **Single source of truth for: the repository layout, the master_index/queue JSONL schemas, and the duplicate-detection fingerprint.**
> References to ALL-CAPS section names in other docs resolve via the [Documentation Map](../CLAUDE.md#documentation-map).

## DUPLICATE DETECTION

Fingerprint in the index: `core-mechanism | strategy-type | instruments | vendor`. **Mechanism
leads; vendor is the trailing, lowest-weight field** — because vendors rebrand and the same
mechanism recurs under many names, so identity must key on *what the EA does*, not who sells it.
- **Substantial match** (same mechanism + strategy-type + instruments) → a rebrand/variant, **even
  if the vendor differs** → update the existing file as a rebrand; append to discovery history;
  no duplicate. A changed vendor name with everything else matching is the *canonical* rebrand
  signal, not a reason to treat it as novel.
- Partial match → cross-link under "Similar EAs."
- Novel (mechanism itself not seen before) → new file + new index row.

---

## DIRECTORY STRUCTURE

```
vetting/
├── README.md                   # landing page — counts, shortlists, legend, latest pass (OUTPUTS §0)
├── daily/                      # YYYY-MM-DD.md, one per run
├── eas/                        # <slug>.md, one per EA surviving the gates
├── excluded/                   # <slug>.md, EAs failing Gate A (banned mechanism), with reasons
├── rulebooks/                  # <firm>.md, versioned + retrieval date
│   ├── fundednext.md
│   ├── the-funded-trader.md
│   └── funding-pips.md
├── rankings/                   # challenge-2step.md, challenge-1step.md, funded-survival.md, comparison.md
├── deployable/                 # rare EAs that clear ALL Deployable gates (needs operator evidence)
├── outcomes/                   # realized challenge/funded results vs predicted verdicts
├── source_archive/             # YYYY-MM-DD.md: URLs + retrieval timestamp + affiliate flag
├── queue.jsonl                 # candidate queue (structured; see below)
├── NEEDS_ATTENTION.md          # present only when a run halted on a blocker (committed; gates next run)
├── .run.lock                   # local-only, gitignored, present only while a run is active
└── master_index.jsonl          # canonical index (structured; see below)
```

### `master_index.jsonl` — one JSON object per line

```json
{"slug":"example-ea","ea_name":"Example EA","vendor":"Acme","fingerprint":"trend-pullback|trend|XAUUSD,EURUSD|Acme","best_tier":"TIER3","overall":4.0,"verdict":"Avoid","binding_criterion":"headline evidence Tier 3 (no independent verification)","firm_verdicts":{"fundednext":{"verdict":"Conditional","rulebook_version":"v2"},"funding-pips":{"verdict":"Permitted","rulebook_version":"v3"},"the-5ers":{"verdict":"Permitted","rulebook_version":"v1"},"the-funded-trader":{"verdict":"Permitted","rulebook_version":"v1"},"alpha-capital":{"verdict":"Prohibited","rulebook_version":"v1","tier":"reference","reason":"source-code submission required"},"goat-funded-trader":{"verdict":"Prohibited","rulebook_version":"v1","tier":"reference","reason":"commercial challenge EAs banned"}},"ror_status":"NON_ESTIMABLE","ror_evidence_tier":"TIER4","funded_evidence":false,"mechanism_confidence":"Low","source_count":8,"independent_source_count":2,"affiliate_source_count":3,"evidence_summary":"vendor claims only for performance; independent comments report grid-like recovery","updated":"2026-06-17"}
```

Append-friendly, diff-friendly, machine-parseable. `verdict ∈ {Deployable, Watchlist, Avoid,
Excluded}`; `best_tier ∈ {TIER0, TIER1, TIER2A, TIER2B, TIER3, TIER4}` (TIER2A = real-money but
caveated; TIER2B = demo/hidden/curve-fit; both use the Tier-2 multiplier); `ror_status ∈
{ESTIMABLE, NON_ESTIMABLE}`; when `ESTIMABLE`, also record `ror_confidence ∈ {High, Low}` (High =
Tier 0/1; Low = Tier 2A); firm
verdicts ∈ {Permitted, Prohibited, Conditional} (reference-firm entries also carry
`"tier":"reference"` and never gate); `mechanism_confidence ∈ {High, Medium, Low,
Unknown}`. Surface only the adjusted `overall` — never the latent score. **Required:** also
record the seven adjusted dimension scores as
`"dimensions":{"survival":..,"compliance":..,"risk":..,"challenge":..,"consistency":..,"transparency":..,"profitability":..}` — the manual validation checklist recomputes the weighted
Overall from them and aborts the commit if the stated Overall disagrees. Because Overall is
deterministic (a weighted sum of integer dimensions), this recompute is an **exact** check, not an
approximation — omitting `dimensions` leaves the Overall unverifiable and is itself a checklist failure.

The public-evidence summary fields `source_count`, `independent_source_count`,
`affiliate_source_count`, `evidence_summary`, and `mechanism_confidence` are **required** — the
manual validation checklist enforces them. `ror_evidence_tier` and `ror_confidence` are required
**whenever `ror_status` is `ESTIMABLE`**: `ror_evidence_tier ∈ {TIER0, TIER1, TIER2A}` records the
real-money trade-level history the estimate rests on, and `ror_confidence` is `High` for Tier 0/1
or `Low` for Tier 2A — letting the checklist catch unsupported `ESTIMABLE` claims (e.g. an
`ESTIMABLE` resting on Tier 2B/3/4 is a contradiction). Both may be omitted only when ROR is
`NON_ESTIMABLE`. `dimensions` is **required** and is always recomputed by the checklist (exact match).

### `queue.jsonl` — one JSON object per line

```json
{"slug":"example-ea","state":"completed","added":"2026-06-15","updated":"2026-06-17"}
```

`state ∈ {pending, vetting, completed, excluded}`.

### `source_archive/YYYY-MM-DD.md`

```
# Source Archive — YYYY-MM-DD
| URL | Retrieved | Used For | Affiliate? |
|-----|-----------|----------|-----------|
| https://www.mql5.com/en/market/product/xxxx | 2026-06-17 07:14 UTC | example-ea.md | no |
| https://fundednext.com/rules | 2026-06-17 07:20 UTC | rulebooks/fundednext.md | n/a |
```

---

