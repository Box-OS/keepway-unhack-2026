import csv,os,sys;sys.path.insert(0,'scripts')
from sources_data import SRC
from cost_config import RATES,GLOBAL,SINGLE,RF,OPTIONS
H=["id","community","parameter","value","unit","source_url","source_date","location","evidence_class","database_check","assumptions_notes"]
rows=[list(r) for r in SRC]
for rid,(item,unit,lo,ce,hi,src,url,note) in RATES.items():
    ev="Estimated ([JUDGMENT])" if "[JUDGMENT]" in src else ("Verified (published rate; proxy location)" if "Alberta" in src else "Reported (benchmark, escalated)")
    rows.append(["RATE_"+rid,"All",item,"%s / %s / %s (low/central/high)"%(lo,ce,hi),"CAD 2026 per "+unit,url,"2026 (accessed 2026-11-07)","Alberta / Canada proxy; x regional factor",ev,"n/a",src+(" | "+note if note else "")])
for gid,desc,vals,basis in GLOBAL:
    rows.append(["GLOBAL_"+gid,"All",desc,"%s / %s / %s"%vals,"fraction","","2026-11-07","All communities","Estimated","n/a",basis])
for sid,desc,val,basis in SINGLE:
    rows.append(["GLOBAL_"+sid,"All",desc,val,"","","2026-11-07","All communities","Estimated","n/a",basis])
for com,(vals,basis) in RF.items():
    rows.append(["RF_"+com.replace(" ","_"),com,"Regional/remote construction factor","%s / %s / %s"%vals,"x","","2026-11-07",com,"Estimated","n/a",basis])
for op in OPTIONS:
    for name,val,unit,basis,ev in op["params"]:
        rows.append([name,op["community"],"%s: %s"%(op["short"],basis),val,unit,"(see community research notes)" ,"2026-11-07",op["community"],ev,"n/a","Formula in Construction_Cost_Workbook.xlsx" if str(val).startswith("=") else "Input in Construction_Cost_Workbook.xlsx"])
    for lab,v in (("Surveys/geotech allowance",op["surveys"]),("Permits/consultation allowance",op["permits"])):
        rows.append([op["id"]+"_"+lab.split("/")[0].upper(),op["community"],"%s: %s"%(op["short"],lab),"%s / %s / %s"%tuple(v),"CAD 2026","","2026-11-07",op["community"],"Estimated","n/a","[JUDGMENT]"])
    rows.append([op["id"]+"_CLOSURE",op["community"],"%s: expected closure days/yr now / with option"%op["short"],"%s / %s"%op["closure"],"days/yr","","2026-11-07",op["community"],"Estimated [ILLUSTRATIVE]","n/a","Planning assumption from reported closure history"])
with open("Source_Register.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f);w.writerow(H);w.writerows(rows)
print(len(rows))
