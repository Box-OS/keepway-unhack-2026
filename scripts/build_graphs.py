"""Graph1 (flood vs road elevation) and Graph2 (capital & lifecycle cost) from cost_config + cost_results.json."""
import json, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
D = os.path.join(os.path.dirname(__file__), ".."); plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
    "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none"})
INK, MUTED, BLUE, RED, GREEN, ORANGE, GREY = "#1f2933", "#6b7280", "#2563eb", "#c2410c", "#15803d", "#d97706", "#9ca3af"

# ---------------- Graph 1
fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5.6), gridspec_kw={"width_ratios": [1.6, 1]})
L = 3.5; x = [0, L]
a1.axhspan(7, 9, color=GREY, alpha=0.18); a1.text(0.05, 7.1, "Community ground el. 7-9 m (Reported, Hatch 2018)", color=MUTED, fontsize=9)
a1.plot(x, [8.5, 8.5], color=INK, lw=2.5, label="Existing road crown 8.5 m [ILLUSTRATIVE - not surveyed]")
a1.plot(x, [9.3, 9.3], color=BLUE, lw=2, ls="--", label="1 May 2025 ice-jam stage 9.3 m [ILLUSTRATIVE] - road overtopped (event Reported)")
a1.plot(x, [9.8, 9.8], color=BLUE, lw=2, label="Design flood stage 9.8 m = 2025 + 0.5 m ice/climate allowance (Estimated)")
a1.plot(x, [10.8, 10.8], color=GREEN, lw=3, label="Proposed crown 10.8 m = design + 1.0 m freeboard (Estimated)")
a1.scatter([L], [11.0], marker="^", s=120, color=ORANGE, zorder=5, label="Airport CZKE 11 m AMSL (Reported, CFS-derived)")
a1.annotate("", xy=(1.75, 10.8), xytext=(1.75, 8.5), arrowprops=dict(arrowstyle="<->", color=INK))
a1.text(1.82, 9.55, "raise 2.3 m", fontsize=10, color=INK, weight="bold")
a1.set_xlim(-0.1, L + 0.3); a1.set_ylim(6.5, 12); a1.set_xlabel("Distance along airport access road from townsite (km, ~3.5 km Estimated)")
a1.set_ylabel("Elevation (m, datum presumed geodetic)"); a1.set_title("Kashechewan airport road: flood stage vs road elevation", loc="left", weight="bold")
a1.legend(loc="upper left", fontsize=8, frameon=False); a1.grid(axis="y", color="#e5e7eb")
names = ["Kashechewan\n(airport road)", "English River\n(Hwy 918, 5 sites)", "Minegoziibe\n(Hwy 20, 3 sites*)", "Potlotek\n(Chapel Is. Rd)"]
raise_ = [2.3, 1.0, 1.0, 0.6]; cols = [GREEN, GREEN, ORANGE, GREEN]
b = a2.bar(names, raise_, color=cols, width=0.6)
for rect, v, t in zip(b, raise_, ["vs 2025 stage\n(conceptual)", "flood level\nUnknown", "sites & levels\nUnknown", "+ 3.0 x 3.0 m\narch (Q~18 m3/s)"]):
    a2.text(rect.get_x() + rect.get_width() / 2, v + 0.05, "%.1f m\n%s" % (v, t), ha="center", fontsize=8.5, color=INK)
a2.set_ylim(0, 3.1); a2.set_ylabel("Proposed grade raise above existing crown (m)")
a2.set_title("Proposed grade raise by community (Estimated)", loc="left", weight="bold"); a2.tick_params(axis="x", labelsize=8.5)
fig.text(0.01, 0.01, "Measured: none at road (no WSC gauge at Kashechewan; nearest 04HA002 ~100 km upstream on assumed datum). Reported: community 7-9 m, airport 11 m, "
         "2025 road flooding. Estimated/[ILLUSTRATIVE]: road crown, 2025 stage, allowances. *Minegoziibe failure sites unverified.\n"
         "Sources: Hatch 2018 tech. paper; Canada Flight Supplement via Wikipedia; TimminsToday/Turtle Island News 2025-05-01; Construction_Cost_Workbook.xlsx. Survey required before design.",
         fontsize=7.5, color=MUTED)
fig.tight_layout(rect=(0, 0.06, 1, 1))
for ext in ("png", "svg"): fig.savefig(os.path.join(D, "Graph1_Flood_vs_Road_Elevation." + ext), dpi=200)

# ---------------- Graph 2
rows = [r for r in json.load(open(os.path.join(D, "scripts", "cost_results.json"))) if r[0]]
lab = {"KA1": "A1 raise +\narmour (hybrid)", "KA2": "A2 333 km\nregional rd", "KB": "B diversion\n+ storage",
       "ERH": "Hybrid crossings", "ERA": "A new 87 km\nalignment", "ERB": "B ditches +\nponds",
       "MIH": "Hybrid crossings", "MIA": "A 12 km\nbypass", "MIB": "B reservoir",
       "POH": "Hybrid crossing", "POA": "A 0.8 km\nrealignment", "POB": "B diversion\n+ pond"}
ids = ["KA1", "KA2", "KB", "ERH", "ERA", "ERB", "MIH", "MIA", "MIB", "POH", "POA", "POB"]
fig, ax = plt.subplots(figsize=(14, 6.2)); w = 0.38; xs = []
pos = 0
for k, r in enumerate(rows):
    if k and r[0] != rows[k - 1][0]: pos += 0.7
    xs.append(pos); pos += 1
for i, (r, xx) in enumerate(zip(rows, xs)):
    rec = r[2].startswith("RECOMMENDED"); rej = ids[i] in ("KA2", "KB", "ERA", "ERB", "MIA", "MIB", "POA")
    c = GREEN if rec else (GREY if rej else ORANGE)
    capL, capC, capH = r[3] / 1e6, r[4] / 1e6, r[5] / 1e6
    lcL, lcC, lcH = r[7] / 1e6, r[8] / 1e6, r[9] / 1e6
    ax.bar(xx - w / 2, capC, w, color=c, edgecolor=INK, lw=0.5)
    ax.bar(xx + w / 2, lcC, w, color=c, alpha=0.45, edgecolor=INK, lw=0.5, hatch="//")
    ax.errorbar(xx - w / 2, capC, yerr=[[capC - capL], [capH - capC]], color=INK, capsize=3, lw=1)
    ax.errorbar(xx + w / 2, lcC, yerr=[[lcC - lcL], [lcH - lcC]], color=INK, capsize=3, lw=1)
    ax.text(xx, lcH * 1.25, ("$%.1fM" % capC) if capC < 100 else ("$%.1fB" % (capC / 1000)), ha="center", fontsize=8, weight="bold" if rec else None)
ax.set_yscale("log"); ax.set_ylim(0.3, 3e4)
ax.set_xticks(xs); ax.set_xticklabels([lab[i] for i in ids], fontsize=8)
for com, xm in zip(["Kashechewan", "English River", "Minegoziibe", "Potlotek"], [1, 4.7, 8.4, 12.1]):
    ax.text(xm, 1.2e4, com, ha="center", weight="bold", fontsize=11)
ax.set_ylabel("2026 CAD, millions (log scale)")
ax.set_title("Capital cost and 30-year lifecycle cost (PV, 3% real) by option - central estimate, bars show low-high range", loc="left", weight="bold")
ax.legend(handles=[Patch(color=GREEN, label="Recommended"), Patch(color=ORANGE, label="Feasible, not preferred"),
                   Patch(color=GREY, label="Rejected / not recommended (illustrative lower bound)"),
                   Patch(facecolor="white", edgecolor=INK, label="Solid = capital"), Patch(facecolor="white", edgecolor=INK, hatch="//", label="Hatched = 30-yr lifecycle PV")],
          loc="upper right", bbox_to_anchor=(1, 0.93), fontsize=8, frameon=False, ncol=1)
ax.grid(axis="y", color="#e5e7eb", which="major")
fig.text(0.01, 0.01, "All values Estimated (AACE Class 5, -50%/+100%): quantities from conceptual sections, rates = Alberta Transportation 2026 unit price averages x regional factor "
         "(Kashechewan 1.5-2.5x), + markups, engineering, 30-50% contingency.\nNo site survey. Land, relocation and taxes not priced. Source: Construction_Cost_Workbook.xlsx; Source_Register.csv.",
         fontsize=7.5, color=MUTED)
fig.tight_layout(rect=(0, 0.06, 1, 1))
for ext in ("png", "svg"): fig.savefig(os.path.join(D, "Graph2_Construction_Lifecycle_Costs." + ext), dpi=200)
print("ok")
