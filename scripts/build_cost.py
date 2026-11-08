"""Build Construction_Cost_Workbook.xlsx from cost_config.py. All costs live Excel formulas (2026 CAD)."""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cost_config import RATES, GLOBAL, SINGLE, RF, COMMUNITY, OPTIONS
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

OUT = os.path.join(os.path.dirname(__file__), "..", "Construction_Cost_Workbook.xlsx")
SA = "Sources_Assumptions"
COMMS = ["Kashechewan", "English River", "Minegoziibe", "Potlotek"]
B = Font(bold=True); H1 = Font(bold=True, size=14); HDR = PatternFill("solid", fgColor="DDE6F0")
INP = PatternFill("solid", fgColor="FFF4CC"); TOT = PatternFill("solid", fgColor="E2EFDA")
MONEY = '#,##0;[Red]-#,##0'; SC = ("L", "C", "H")

def q(sheet): return "'%s'" % sheet

wb = Workbook(); summ = wb.active; summ.title = "Summary"
sa = wb.create_sheet(SA)
NAMES = {}  # token -> absolute ref

# ---------------- Sources_Assumptions (all shared inputs)
sa["A1"] = "Sources & assumptions - shared inputs (yellow cells are editable; every cost in the workbook recalculates)"; sa["A1"].font = H1
r = 3
for c, h in enumerate(["ID", "Global scenario parameter", "Low", "Central", "High", "Basis / source"], 1):
    sa.cell(r, c, h).font = B; sa.cell(r, c).fill = HDR
for gid, desc, vals, basis in GLOBAL:
    r += 1; sa.cell(r, 1, gid); sa.cell(r, 2, desc); sa.cell(r, 6, basis)
    for i, v in enumerate(vals):
        sa.cell(r, 3 + i, v).fill = INP; NAMES["%s_%s" % (gid, SC[i])] = "%s!$%s$%d" % (SA, "CDE"[i], r)
r += 2
for c, h in enumerate(["ID", "Single-value parameter", "", "Value", "", "Basis / source"], 1):
    sa.cell(r, c, h).font = B; sa.cell(r, c).fill = HDR
for sid, desc, val, basis in SINGLE:
    r += 1; sa.cell(r, 1, sid); sa.cell(r, 2, desc); sa.cell(r, 4, val).fill = INP; sa.cell(r, 6, basis)
    NAMES[sid] = "%s!$D$%d" % (SA, r)
r += 1; sa.cell(r, 1, "AF"); sa.cell(r, 2, "Annuity (PV) factor for annual O&M over study period")
sa.cell(r, 4, "=(1-(1+%s)^-%s)/%s" % (NAMES["DR"], NAMES["NYR"], NAMES["DR"])); sa.cell(r, 6, "Formula")
NAMES["AF"] = "%s!$D$%d" % (SA, r)
r += 2
for c, h in enumerate(["Community", "Regional / remote construction factor", "Low", "Central", "High", "Basis / source"], 1):
    sa.cell(r, c, h).font = B; sa.cell(r, c).fill = HDR
for com in COMMS:
    vals, basis = RF[com]; r += 1; sa.cell(r, 1, com); sa.cell(r, 2, "Multiplier on Alberta 2026 unit rates"); sa.cell(r, 6, basis)
    for i, v in enumerate(vals):
        sa.cell(r, 3 + i, v).fill = INP; NAMES["RF_%s_%s" % (com, SC[i])] = "%s!$%s$%d" % (SA, "CDE"[i], r)
r += 2
for c, h in enumerate(["Rate ID", "Item", "Low", "Central", "High", "Unit", "Source", "Source URL", "Note"], 1):
    sa.cell(r, c, h).font = B; sa.cell(r, c).fill = HDR
for rid, (item, unit, lo, ce, hi, src, url, note) in RATES.items():
    r += 1; sa.cell(r, 1, rid); sa.cell(r, 2, item); sa.cell(r, 6, unit); sa.cell(r, 7, src); sa.cell(r, 8, url); sa.cell(r, 9, note)
    for i, v in enumerate((lo, ce, hi)):
        sa.cell(r, 3 + i, v).fill = INP; sa.cell(r, 3 + i).number_format = '#,##0.00'
        NAMES["RATE_%s_%s" % (rid, SC[i])] = "%s!$%s$%d" % (SA, "CDE"[i], r)
r += 2
NOTES = [
    "METHOD",
    "Item cost = Quantity x QF (scenario) x Unit rate (scenario) x Regional factor (scenario). Rates are Alberta Transportation 2026 unit price averages unless noted, used as a national proxy.",
    "All-in benchmark options (new roads, Kashechewan diversion) already include field overheads and remote/region effects: no regional factor and no MOB/TEMP/ENV markups are applied to them (lower bound).",
    "Construction = direct + MOB + TEMP + ENV. Base = construction + surveys/geotech + permits/consultation + engineering (ENG x construction). Total capital = Base x (1 + CONT).",
    "Annual O&M = sum of O&M lines x regional factor (or % of an item cost). Lifecycle PV = capital + O&M x AF + rehab events discounted at DR; undiscounted lifecycle also shown.",
    "Class: AACE Class 5 / Class D (order of magnitude, -50%/+100%). No site survey, no geotechnical data, no hydraulic model. Not for funding decisions.",
    "EVIDENCE CLASSES: Verified = primary source checked; Reported = secondary/news/consultant; Estimated = engineering calculation or judgment ([JUDGMENT]); Unknown = not found. [ILLUSTRATIVE] = assumed value used to show method only.",
    "NOT PRICED (Unknown): land acquisition, relocation of the Kashechewan community, Indigenous consultation beyond permit allowance, winter-road/barge logistics beyond regional factor, HST/GST, escalation beyond 2026.",
    "Expected closure days per year (current vs with option) are [ILLUSTRATIVE] planning assumptions derived from reported closure history, not hydrologic return-period analysis.",
]
for n in NOTES:
    sa.cell(r, 1, n).font = B if n.isupper() else Font(); r += 1
for col, w in zip("ABCDEFGHI", (10, 55, 12, 12, 12, 14, 60, 50, 30)): sa.column_dimensions[col].width = w

# ---------------- formula translation
def expand_exp(s): return re.sub(r'(\d+(?:\.\d+)?)e(\d+)', lambda m: repr(float(m.group(0))).rstrip('0').rstrip('.') if False else str(int(float(m.group(0)))), s)
def tr(f):
    s = str(f)
    if not s.startswith("="): return f
    s = expand_exp(s)
    return re.sub(r'\b[A-Z][A-Z0-9_]*\b', lambda m: NAMES.get(m.group(0), m.group(0)), s)

# ---------------- community sheets
SUMROWS = []
for com in COMMS:
    ws = wb.create_sheet(com)
    for col, w in zip("ABCDEFGHIJK", (12, 62, 10, 14, 13, 13, 13, 15, 15, 15, 48)): ws.column_dimensions[col].width = w
    ws["A1"] = "%s - construction cost & lifecycle model (2026 CAD, AACE Class 5)" % com; ws["A1"].font = H1
    ws["A2"] = "Population served: %s" % COMMUNITY[com]["pop_src"]
    ws["A3"] = "Regional factor L/C/H (edit on %s):" % SA
    for i in range(3): ws.cell(3, 8 + i, "=" + NAMES["RF_%s_%s" % (com, SC[i])])
    rfr = ["$%s$3" % "HIJ"[i] for i in range(3)]
    r = 5
    for op in [o for o in OPTIONS if o["community"] == com]:
        allin = op["allin"]; oid = op["id"]
        role = {"H": "RECOMMENDED HYBRID", "A": "SOLUTION A", "B": "SOLUTION B"}[op["kind"]]
        if oid == "KA1": role = "SOLUTION A1 = RECOMMENDED HYBRID (raise + armour + equalization culverts + ice monitoring)"
        ws.cell(r, 1, "%s | %s" % (role, op["name"])).font = Font(bold=True, size=12); ws.cell(r, 1).fill = HDR
        for c in range(2, 12): ws.cell(r, c).fill = HDR
        r += 1; ws.cell(r, 1, "Status:").font = B; ws.cell(r, 2, op["status"]).font = Font(bold=True, color="C00000" if "REJECT" in op["status"] or "NOT" in op["status"] else "006100")
        if allin: r += 1; ws.cell(r, 2, "All-in benchmark option: no regional factor or MOB/TEMP/ENV markups applied (lower bound).")
        # params
        r += 2
        for c, h in enumerate(["Parameter", "Basis", "Unit", "Value"], 1): ws.cell(r, c, h).font = B
        ws.cell(r, 11, "Evidence class").font = B
        for name, val, unit, basis, ev in op["params"]:
            r += 1; NAMES[name] = "%s!$D$%d" % (q(com), r)
            ws.cell(r, 1, name); ws.cell(r, 2, basis); ws.cell(r, 3, unit); ws.cell(r, 4, tr(val)); ws.cell(r, 11, ev)
            ws.cell(r, 4).number_format = '#,##0.00'
            if not str(val).startswith("="): ws.cell(r, 4).fill = INP
        # items
        r += 2
        for c, h in enumerate(["Component", "Description", "Unit", "Quantity", "Rate Low", "Rate Central", "Rate High",
                               "Cost Low", "Cost Central", "Cost High", "Rate basis"], 1):
            ws.cell(r, c, h).font = B; ws.cell(r, c).fill = HDR
        first = r + 1; itemrow = {}
        for it in op["items"]:
            key, comp, desc, unit, qf, rate, basis = it
            r += 1; itemrow[key] = r
            ws.cell(r, 1, comp); ws.cell(r, 2, desc); ws.cell(r, 3, unit); ws.cell(r, 4, tr(qf)); ws.cell(r, 4).number_format = '#,##0.0'
            for i in range(3):
                if isinstance(rate, tuple): ws.cell(r, 5 + i, rate[i]).fill = INP
                else: ws.cell(r, 5 + i, "=" + NAMES["RATE_%s_%s" % (rate, SC[i])])
                ws.cell(r, 5 + i).number_format = '#,##0.00'
                f = "=D%d*%s*%s%d" % (r, NAMES["QF_" + SC[i]], "EFG"[i], r)
                if not allin: f += "*" + rfr[i]
                ws.cell(r, 8 + i, f).number_format = MONEY
            ws.cell(r, 11, (rate if isinstance(rate, str) else "") + " | " + basis)
        last = r
        def line(label, fs, bold=False, fill=None):
            global r
            r += 1; ws.cell(r, 2, label)
            for i in range(3):
                ws.cell(r, 8 + i, fs[i]).number_format = MONEY
                if bold: ws.cell(r, 8 + i).font = B
                if fill: ws.cell(r, 8 + i).fill = fill
            if bold: ws.cell(r, 2).font = B
            return r
        col = lambda i: "HIJ"[i]
        rd = line("Direct construction subtotal", ["=SUM(%s%d:%s%d)" % (col(i), first, col(i), last) for i in range(3)], True)
        mk = []
        for g, lab in (("MOB", "Mobilization / demobilization"), ("TEMP", "Temporary access & traffic management"), ("ENV", "Environmental mitigation, sediment & erosion control")):
            mk.append(line(lab + (" (n/a - all-in benchmark)" if allin else " (% of direct)"),
                           ["=0" if allin else "=%s%d*%s" % (col(i), rd, NAMES["%s_%s" % (g, SC[i])]) for i in range(3)]))
        rc = line("CONSTRUCTION COST", ["=%s%d+%s%d+%s%d+%s%d" % (col(i), rd, col(i), mk[0], col(i), mk[1], col(i), mk[2]) for i in range(3)], True, TOT)
        rs = line("Surveys, LiDAR, geotechnical & hydrology - " + op["surveys_basis"], ["=%s" % v for v in op["surveys"]])
        for i in range(3): ws.cell(rs, 8 + i).fill = INP
        rp = line("Permits, consultation & approvals - " + op["permits_basis"], ["=%s" % v for v in op["permits"]])
        for i in range(3): ws.cell(rp, 8 + i).fill = INP
        re_ = line("Engineering, design & contract administration (% of construction)", ["=%s%d*%s" % (col(i), rc, NAMES["ENG_" + SC[i]]) for i in range(3)])
        rb = line("Base estimate", ["=%s%d+%s%d+%s%d+%s%d" % (col(i), rc, col(i), rs, col(i), rp, col(i), re_) for i in range(3)], True)
        rco = line("Contingency (Class 5)", ["=%s%d*%s" % (col(i), rb, NAMES["CONT_" + SC[i]]) for i in range(3)])
        rt = line("TOTAL CAPITAL COST (2026 CAD)", ["=%s%d+%s%d" % (col(i), rb, col(i), rco) for i in range(3)], True, TOT)
        # O&M
        r += 2
        for c, h in enumerate(["O&M", "Description", "", "Quantity/yr", "Rate Low", "Rate Central", "Rate High", "Annual Low", "Annual Central", "Annual High"], 1):
            ws.cell(r, c, h).font = B; ws.cell(r, c).fill = HDR
        of = r + 1
        for om in op["om"]:
            r += 1; ws.cell(r, 1, "O&M")
            if om[0] == "pct":
                _, desc, key, pct = om
                ws.cell(r, 2, desc); ws.cell(r, 3, "% of item"); ws.cell(r, 4, pct)
                for i in range(3): ws.cell(r, 8 + i, "=%s%d*$D$%d" % (col(i), itemrow[key], r)).number_format = MONEY
            else:
                desc, qf, rate = om
                ws.cell(r, 2, desc); ws.cell(r, 4, tr(qf))
                for i in range(3):
                    if isinstance(rate, tuple): ws.cell(r, 5 + i, rate[i]).fill = INP
                    else: ws.cell(r, 5 + i, "=" + NAMES["RATE_%s_%s" % (rate, SC[i])])
                    ws.cell(r, 8 + i, "=D%d*%s%d*%s" % (r, "EFG"[i], r, rfr[i])).number_format = MONEY
        ol = r
        rom = line("ANNUAL O&M (2026 CAD/yr)", ["=SUM(%s%d:%s%d)" % (col(i), of, col(i), ol) for i in range(3)], True, TOT)
        # rehab
        r += 1
        for c, h in enumerate(["Rehab", "Major rehabilitation event", "Year", "% of constr."], 1): ws.cell(r + 1, c, h).font = B
        r += 1; rpv = []; rund = []
        for desc, yr, pct in op["rehab"]:
            r += 1; ws.cell(r, 1, "Rehab"); ws.cell(r, 2, desc + " (cost, PV in col K note)"); ws.cell(r, 3, yr); ws.cell(r, 4, pct)
            for i in range(3): ws.cell(r, 8 + i, "=%s%d*$D$%d" % (col(i), rc, r)).number_format = MONEY
            rund.append(r)
        rpvl = line("Rehabilitation PV (sum of events discounted at DR)",
                    ["=" + ("+".join("%s%d/(1+%s)^$C$%d" % (col(i), x, NAMES["DR"], x) for x in rund) or "0") for i in range(3)])
        rlc = line("30-YEAR LIFECYCLE COST, PV (capital + O&M x AF + rehab PV)",
                   ["=%s%d+%s%d*%s+%s%d" % (col(i), rt, col(i), rom, NAMES["AF"], col(i), rpvl) for i in range(3)], True, TOT)
        rlu = line("30-year lifecycle cost, undiscounted",
                   ["=%s%d+%s%d*%s%s" % (col(i), rt, col(i), rom, NAMES["NYR"], "".join("+%s%d" % (col(i), x) for x in rund)) for i in range(3)])
        r += 1; ws.cell(r, 2, "[ILLUSTRATIVE] Expected road-closure days/yr: current | with option | reliability gain")
        ws.cell(r, 4, op["closure"][0]).fill = INP; ws.cell(r, 5, op["closure"][1]).fill = INP
        ws.cell(r, 6, "=1-E%d/D%d" % (r, r)).number_format = '0%'; rcl = r
        r += 1; ws.cell(r, 2, "Corridor length served (km)"); ws.cell(r, 4, tr("=" + op["corridor_km"]) if not str(op["corridor_km"]).startswith("=") else tr(op["corridor_km"]))
        SUMROWS.append(dict(op=op, sheet=com, total=rt, om=rom, lc=rlc, lcu=rlu, cons=rc, cl=rcl))
        r += 3

# ---------------- Summary
summ["A1"] = "Construction cost & lifecycle summary - 4 communities (2026 CAD, AACE Class 5 order of magnitude; live links to community sheets)"; summ["A1"].font = H1
summ["A2"] = "Recommended option per community is flagged. Rejected options are priced only as illustrative lower bounds. Closure days are [ILLUSTRATIVE]."
hd = ["Community", "Option", "Role", "Status", "Capital Low", "Capital Central", "Capital High", "Annual O&M Central",
      "30-yr PV Low", "30-yr PV Central", "30-yr PV High", "30-yr undiscounted Central", "Closure days/yr now", "With option", "Reliability gain"]
for c, h in enumerate(hd, 1):
    summ.cell(4, c, h).font = B; summ.cell(4, c).fill = HDR; summ.cell(4, c).alignment = Alignment(wrap_text=True)
r = 4
for s in SUMROWS:
    op = s["op"]; r += 1; sh = q(s["sheet"])
    rec = op["id"] in ("KA1", "ERH", "MIH", "POH")
    summ.cell(r, 1, s["sheet"]); summ.cell(r, 2, op["name"])
    summ.cell(r, 3, ("RECOMMENDED - " if rec else "") + {"H": "Hybrid", "A": "Solution A", "B": "Solution B"}[op["kind"]])
    summ.cell(r, 4, op["status"])
    for i, cc in enumerate("HIJ"): summ.cell(r, 5 + i, "=%s!%s%d" % (sh, cc, s["total"]))
    summ.cell(r, 8, "=%s!I%d" % (sh, s["om"]))
    for i, cc in enumerate("HIJ"): summ.cell(r, 9 + i, "=%s!%s%d" % (sh, cc, s["lc"]))
    summ.cell(r, 12, "=%s!I%d" % (sh, s["lcu"]))
    summ.cell(r, 13, "=%s!D%d" % (sh, s["cl"])); summ.cell(r, 14, "=%s!E%d" % (sh, s["cl"])); summ.cell(r, 15, "=%s!F%d" % (sh, s["cl"]))
    for c in range(5, 13): summ.cell(r, c).number_format = MONEY
    summ.cell(r, 15).number_format = '0%'
    if rec:
        for c in range(1, 16): summ.cell(r, c).fill = TOT
r += 1
summ.cell(r, 2, "Recommended programme total (4 communities)").font = B
for c in range(5, 13):
    L = get_column_letter(c)
    summ.cell(r, c, '=SUMIF($C$5:$C$%d,"RECOMMENDED*",%s5:%s%d)' % (r - 1, L, L, r - 1)).number_format = MONEY
    summ.cell(r, c).font = B
for col, w in zip("ABCDEFGHIJKLMNO", (14, 60, 22, 50, 15, 15, 15, 14, 15, 15, 15, 15, 10, 10, 10)): summ.column_dimensions[col].width = w
summ.freeze_panes = "C5"
wb.move_sheet(SA, offset=4)
wb.save(OUT); print("saved", OUT, "summary rows", len(SUMROWS))
