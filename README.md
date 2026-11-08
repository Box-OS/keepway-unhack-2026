# UNHack 2026: Flood-resilient road access for four First Nations (prototype package)

## Team members

- Sina Akhavansafar
- Kiarash Ordubadi
- Sara Jeibar
- Weijie Zhang
- Noah Cho
- Umaima
- Farooq
- Patoli

Prepared 2026-11-07. All costs are in 2026 CAD at AACE Class 5 / Class D accuracy (order of magnitude). Evidence classes: **Verified** (primary source checked), **Reported** (news, consultant or secondary source), **Estimated** (engineering calculation or judgment), **Unknown** (not found). **[ILLUSTRATIVE]** means an assumed value used only to demonstrate the method.

## Files
| File | What it is |
|---|---|
| `Construction_Cost_Workbook.xlsx` | Live cost model. `Summary` gives capital, O&M, 30-year lifecycle (PV at 3% real and undiscounted) and reliability gain for 12 options. There is one sheet per community with Solution A, Solution B and the recommended hybrid, each priced low / central / high with quantities built from parameter formulas. `Sources_Assumptions` holds every shared input in yellow cells (rates, scenario markups, regional factors, discount rate) plus the method notes. Change any yellow cell and all totals update. |
| `Implementation_Timeline_Workbook.xlsx` | Phase-by-phase schedule (minimum / most likely / delayed) with seasonal construction windows (from the earlier run). |
| `Graph1_Flood_vs_Road_Elevation.png/.svg` | Kashechewan airport road profile: illustrative flood stage vs. road crown, plus the proposed grade raise by community. |
| `Graph2_Construction_Lifecycle_Costs.png/.svg` | Capital and 30-year lifecycle cost of all 12 options (log scale, low–high bars). |
| `Source_Register.csv` | 217 rows: every numerical input with its value, unit, URL, date, location, evidence class and assumption. |
| `Pitch_Summary.md` | The 3–5 minute pitch script. |
| `notes/`, `scripts/` | Research notes and the Python that builds every deliverable (`build_cost.py`, `check_cost.py`, `build_graphs.py`, `build_register.py`, `build_timeline.py`). |

## Feasibility comparison
| Community | Solution A (elevated / alternative road) | Solution B (diversion + storage) | Preferred concept | Evidence confidence |
|---|---|---|---|---|
| Kashechewan | **A1 local raise of airport road: conditionally feasible** (2.3 m raise, $42M). A2 333 km regional road: rejected ($2.2B, tied to relocation) | **Not feasible.** The flood is ice-jam backwater from downstream. Diverting 2,000 m³/s needs a 214 m × 6 m channel and 864 Mm³ (≈430 km²) of storage in peatland ($1.4B lower bound) | A1 raise + armour + equalization culverts + ice/stage monitoring | Low–Medium (event Reported; no measured stage or road elevation) |
| English River | New 87 km alignment: rejected ($346M; crosses the same drainage) | Not recommended: 5 diked ponds of about 20 ha each in muskeg, still need culverts ($43M, dam-safety risk) | Hybrid: upgrade 5 crossings + 1 m local raise + debris deflectors + armour ($9.9M) | Medium–High (5 sites Verified in Hansard; catchments Unknown) |
| Minegoziibe | 12 km bypass: not recommended ($57M; crosses the same streams) | Rejected: a 155 ha reservoir protects one stream only ($21M) | Hybrid after forensic site ID: 3 crossings (1 bridge) + raise ($7.4M) | Low (failure sites unverified; rainfall from a distant station) |
| Potlotek | 0.8 km realignment: not recommended ($7.5M; new footprint near Mniku NHS, still needs a crossing) | Technically possible, not preferred: 5.6 ha pond + smaller culvert ($5.6M) | Hybrid: 3 × 3 m open-bottom arch + embankment rebuild/raise + armour + utility protection ($1.75M) | Medium (closure and culvert inadequacy Reported; catchment and IDF assumed) |

## Weighted decision matrix (recommended option per community, scores 1–5)
Weights: **technical effectiveness 30%** (does it keep the road open under the actual flood mechanism), **evidence confidence 20%** (how much of the design basis is measured or verified), **cost-effectiveness 20%** (central capital per resident served), **time to benefit 15%**, **community & environmental fit 15%** (footprint, fish passage, cultural sites, life-safety value). Score = Σ(score × weight) / 5, out of 100.

| Criterion (weight) | Kashechewan A1 hybrid | English River hybrid | Minegoziibe hybrid | Potlotek hybrid |
|---|---|---|---|---|
| Technical effectiveness (30) | 3 (ice-shove uncertainty) | 4 | 3 (sites unknown) | 4 |
| Evidence confidence (20) | 2 | 4 | 2 | 2 |
| Cost per resident (20) | 3 (~$19k) | 3 (~$20k) | 4 (~$7k) | 5 (~$2.7k) |
| Time to benefit (15) | 1 | 3 | 3 | 5 |
| Community / environment (15) | 4 (evacuation lifeline) | 4 | 3 | 3 (NHS, utilities) |
| **Weighted score** | **53** | **73** | **60** | **76** |

Potlotek is the strongest quick-win prototype. English River is the best-evidenced option and the logical scale-up. Concept-level result: **hybrids win everywhere**. Solution B (diversion + storage) is never preferred, and new-corridor versions of Solution A cost 5–50× more.

## Timeline comparison (from `Implementation_Timeline_Workbook.xlsx`, start early 2027)
| Community | Option | Construction (most likely, months / seasons) | Total implementation: earliest (min) | Total implementation: most likely |
|---|---|---|---|---|
| Kashechewan | A1 airport road raise (recommended) | 24.5 / 3 | 43.9 mo (Aug 2030) | 69.5 mo (Oct 2032) |
| Kashechewan | A2, B | not scheduled (not feasible) | – | – |
| English River | Hybrid (recommended) | 12.0 / 2 | 21.2 mo (Oct 2028) | 34.5 mo (Nov 2029) |
| English River | A new alignment* | 45.0 / 5 | 55.4 mo (Aug 2031) | 92.0 mo (Sep 2034) |
| Minegoziibe | Hybrid (recommended) | 4.5 / 1 | 20.1 mo (Sep 2028) | 33.8 mo (Oct 2029) |
| Minegoziibe | A bypass | 16.5 / 2 | 42.8 mo (Jul 2030) | 58.3 mo (Nov 2031) |
| Potlotek | Hybrid (recommended) | 3.0 / 1 | 19.0 mo (Aug 2028) | 21.6 mo (Oct 2028) |
| Potlotek | A realignment | 13.0 / 2 | 21.2 mo (Oct 2028) | 43.4 mo (Aug 2030) |
| Potlotek | B diversion + pond | 13.5 / 2 | 21.7 mo (Oct 2028) | 43.9 mo (Aug 2030) |

\*The timeline workbook schedules a ~40 km English River realignment; the cost model prices the full 87 km. That is a known inconsistency, and either way the option is rejected.

## Executive decision table
| Community | Recommended solution | Cost CAD low / central / high | Construction time | Total implementation (most likely) | Primary benefit |
|---|---|---|---|---|---|
| Kashechewan | Raise ~3.5 km airport access road 2.3 m (crown 10.8 m) + rock armour + equalization culverts + ice/stage monitoring | $16.1M / $42.3M / $115.3M | ~24.5 months (3 seasons) | ~70 months (2032) | Airport (evacuation and supply lifeline) stays reachable during ice-jam breakup |
| English River | Upgrade 5 Hwy 918 washout crossings + 1 m local raise + debris deflectors + armour | $4.8M / $9.9M / $25.1M | ~12 months (2 seasons) | ~35 months (2029) | Sole road for ~500 residents stops washing out every spring |
| Minegoziibe | Forensic site ID, then 3 crossing upgrades (incl. 1 short-span bridge) + raise on Hwy 20 | $3.7M / $7.4M / $17.1M | ~4.5 months (1 season) | ~34 months (2029) | Hwy 20 link to Camperville / Dauphin services survives rain floods |
| Potlotek | Matle'n's Brook 3 × 3 m arch crossing + embankment rebuild/raise + armour + water/wastewater main protection | $0.87M / $1.75M / $4.56M | ~3 months (1 season) | ~22 months (2028) | Chapel Island Road and community water/wastewater lines protected |
| **Programme** | | **$25.5M / $61.3M / $162.0M** (O&M ≈ $0.36M/yr; 30-yr PV ≈ $71M) | | | |

## Top data gaps before detailed design
1. **Kashechewan elevations:** surveyed road crown, ring dike crest and observed 2025/2006 ice-jam stages in geodetic datum. None exist publicly, so Graph 1's 8.5 m and 9.3 m are illustrative. A breakup stage-frequency analysis is also needed (Knack et al. 2024 DynaRICE results are paywalled).
2. **Geotechnical conditions:** peat, marine clay and permafrost under the Kashechewan road; foundations at all crossing sites; local sources of rock for armour.
3. **English River site hydrology:** creek names, catchment areas and existing culvert sizes at the 17 / 29 / 40 km (and 2 other) washouts; whether burn-area debris load will persist.
4. **Minegoziibe failure sites:** which crossings on Hwy 20 / PR 272 failed in June–July 2026, and on-site rainfall (the Dauphin station is distant).
5. **Potlotek design flow:** Matle'n's Brook catchment (2 km² assumed), ECCC IDF curves with a climate factor, existing culvert sizes, utility locations and the archaeological constraints near the Mniku NHS.
6. **Remote cost factors:** actual winter-road / barge mobilization costs for Kashechewan (1.5–2.5× is a judgment range) and Saskatchewan/Manitoba local bid prices.
7. **Closure records:** actual closure days per year for each road, to replace the illustrative reliability figures.
