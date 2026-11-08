import formulas,warnings,json,openpyxl;warnings.filterwarnings('ignore')
fn='Construction_Cost_Workbook.xlsx'
sol=formulas.ExcelModel().loads(fn).finish().calculate()
def g(s,c):
    v=sol.get("'[%s]%s'!%s"%(fn,s.upper(),c))
    try: v=v.value[0,0]
    except: pass
    return v
wb=openpyxl.load_workbook(fn); ws=wb['Summary']; out=[]
for r in range(5,ws.max_row+1):
    row=[g('SUMMARY','%s%d'%(c,r)) for c in 'ABCEFGHIJKLMNO']
    out.append([x if isinstance(x,(str,int,float)) or x is None else float(x) for x in row]); print([ (round(x/1e6,2) if isinstance(x,float) and x>1000 else x) for x in row])
json.dump(out,open('scripts/cost_results.json','w'),default=str,indent=0)
for nm in ['KB_V','KB_W','KB_VS','KB_HA','KA1_RAISE','KA1_ZC','ERB_VS','ERB_HA','MIB_VS','MIB_HA','POH_Q','POH_RISE','POB_VS','POB_HA']:
    for sh in wb.sheetnames[1:5]:
        w=wb[sh]
        for row in w.iter_rows(min_col=1,max_col=1):
            if row[0].value==nm: print(nm,g(sh,'D%d'%row[0].row))
