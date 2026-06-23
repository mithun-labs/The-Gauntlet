"""
Gauntlet v2.4 — archetype regression suite.

Encodes the SCORING + VERDICT logic and asserts the expected verdict CATEGORY for a
spread of EA archetypes. Covers the v2.3 fix (real-money Tier 2A -> Watchlist; demo
Tier 2B -> Avoid) and the v2.4 Gate-B fix (black-box WITH documented controls ->
Watchlist; black-box WITHOUT -> Avoid). Operational fixes (multi-host guard, fingerprint
order, backlog drain, halt notification, queue reset, dimensions-required) are data-flow,
not scoring, so they are verified by inspection, not here.

Run: python3 gauntlet_regression.py   ->   exits non-zero if any archetype mis-verdicts.
"""

import math, sys

MULT_A = {0: 1.00, 1: 0.70, 2: 0.45, 3: 0.25, 4: 0.12}
MULT_B = {0: 1.00, 1: 0.95, 2: 0.60, 3: 0.30, 4: 0.15}
W = {"survival": .30, "compliance": .20, "risk": .15, "challenge": .15,
     "consistency": .10, "transparency": .05, "profitability": .05}

def tnum(t): return {"TIER0":0,"TIER1":1,"TIER2A":2,"TIER2B":2,"TIER3":3,"TIER4":4}[t]
def rhu(x): return math.floor(x + 0.5)
def rhu1(x): return math.floor(x*10 + 0.5)/10
def clamp(x): return max(1, min(10, x))

def score(ea):
    t = tnum(ea["best_tier"])
    surv_mult = min(MULT_A[t], 0.20) if ea["ror_status"] == "NON_ESTIMABLE" else MULT_A[t]
    a = {}
    a["survival"]      = clamp(rhu(ea["L"]["survival"]      * surv_mult))
    a["challenge"]     = clamp(rhu(ea["L"]["challenge"]     * MULT_A[t]))
    a["consistency"]   = clamp(rhu(ea["L"]["consistency"]   * MULT_B[t]))
    a["transparency"]  = clamp(rhu(ea["L"]["transparency"]  * MULT_B[t]))
    a["profitability"] = clamp(rhu(ea["L"]["profitability"] * MULT_B[t]))
    comp_ceil = 5 if not ea["mechanism_verifiable"] else 10           # Gate B
    risk_ceil = min(4 if not ea["mechanism_verifiable"] else 10, ea["risk_control_ceiling"])
    a["compliance"] = clamp(min(ea["L"]["compliance"], comp_ceil))
    a["risk"]       = clamp(min(ea["L"]["risk"], risk_ceil))
    overall = rhu1(sum(W[d]*a[d] for d in W))
    return a, overall

def verdict(ea):
    if ea.get("gate_a_excluded"):
        return "Excluded", "Gate A banned mechanism"
    a, overall = score(ea)
    t = ea["best_tier"]
    if ea["prohibited_all_primary"]:                    return "Avoid", "prohibited all primary"
    if t in ("TIER3", "TIER4"):                         return "Avoid", "headline Tier 3/4"
    if not ea["mechanism_verifiable"] and not ea["documented_risk_controls"]:
        return "Avoid", "black box, no documented controls (criterion 3)"
    crit4 = ea["ror_status"] == "NON_ESTIMABLE" and t in ("TIER2B", "TIER3", "TIER4")
    if crit4:                                           return "Avoid", "ROR non-estimable + weak tier (criterion 4)"
    # Deployable: gate 1 (non-black-box) + gate 2 (Tier0/1) + gate 7 (ROR-High) + gate 8 (funded)
    if (ea["mechanism_verifiable"] and t in ("TIER0","TIER1")
            and ea["funded_evidence"] and ea["ror_confidence"] == "High"):
        return "Deployable", "all gates"
    return "Watchlist", "tracks; fails >=1 Deployable gate"

def EA(**kw):
    base = dict(best_tier="TIER1", ror_status="ESTIMABLE", ror_confidence="High",
                mechanism_verifiable=True, documented_risk_controls=True,
                risk_control_ceiling=10, prohibited_all_primary=False,
                funded_evidence=False, gate_a_excluded=False,
                L=dict(survival=6, compliance=8, risk=7, challenge=5,
                       consistency=5, transparency=8, profitability=5))
    base.update(kw); return base

# --- archetypes: (name, EA, expected verdict, what it verifies) -------------
SUITE = [
 ("Clean Tier-1, no funded evidence",
  EA(best_tier="TIER1", ror_confidence="High",
     L=dict(survival=8, compliance=9, risk=7, challenge=7, consistency=7, transparency=8, profitability=7)),
  "Watchlist", "autonomous ceiling: strong but missing funded evidence (gate 8)"),

 ("Real-money Tier 2A (short/small)",
  EA(best_tier="TIER2A", ror_confidence="Low"),
  "Watchlist", "v2.3 fix: investigate-further candidate surfaced, not Avoided"),

 ("Demo-only Tier 2B (control)",
  EA(best_tier="TIER2B", ror_status="NON_ESTIMABLE", ror_confidence=None),
  "Avoid", "demo distrust preserved — not loosened by the v2.3 fix"),

 ("Black box WITH documented controls (Tier 2A)",
  EA(best_tier="TIER2A", ror_confidence="Low",
     mechanism_verifiable=False, documented_risk_controls=True),
  "Watchlist", "v2.4 Gate-B fix: reaches the Watchlist ceiling (Comp<=5, Risk<=4)"),

 ("Black box, NO documented controls (Tier 2A)",
  EA(best_tier="TIER2A", ror_confidence="Low",
     mechanism_verifiable=False, documented_risk_controls=False),
  "Avoid", "v2.4 Gate-B fix: criterion 3 now does real work — Avoided"),

 ("Disguised martingale",
  EA(gate_a_excluded=True),
  "Excluded", "Gate A pre-screen"),

 ("Vendor-only Tier 4 marketing",
  EA(best_tier="TIER4", ror_status="NON_ESTIMABLE", ror_confidence=None,
     L=dict(survival=5, compliance=6, risk=3, challenge=4, consistency=4, transparency=3, profitability=4)),
  "Avoid", "criterion 2: no independent verification"),
]

print(f"{'Archetype':<46}{'Overall':>8}  {'Verdict':<11} {'exp':<11} PASS?   verifies")
print("-"*132)
fails = 0
for name, ea, expected, note in SUITE:
    v, reason = verdict(ea)
    ov = "  n/a " if ea.get("gate_a_excluded") else f"{score(ea)[1]:>6}"
    ok = (v == expected)
    fails += (not ok)
    print(f"{name:<46}{ov:>8}  {v:<11} {expected:<11} {'PASS' if ok else 'FAIL':<6}  {note}")

print("-"*132)
print("ALL PASS" if fails == 0 else f"{fails} FAILURE(S)")
sys.exit(1 if fails else 0)
