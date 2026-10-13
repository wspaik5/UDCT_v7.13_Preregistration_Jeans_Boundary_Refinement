#!/usr/bin/env python3
"""v7.13 preregistration preparation ONLY; no galaxy calculations.
Reads frozen v7.12 published CSVs, verifies hashes and emits the predeclared
24-target inventory. No post-registration scientific result is generated.
"""
import csv,hashlib,json,argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parent
INPUTS={'UDCT_v7_06_Hessian_Term_Sign_Audit_reproduce.py': 'a64440e1350ae8bf10eb3188ec34829b6d586abf275de5cdc841a50ad3478284', 'UDCT_v7_10_Postregistration_run.py': 'a4d1a07ebcaa06348be3022d0f1f6ca463347e00194f7fde59f2bd9dbcd521b7', 'UDCT_v7_11_Preregistration_Anisotropic_Jeans.py': '3f00abae251d7be64a4ca5abb48b4f550644b21c946206571fd448464b13ade2', 'UDCT_v7_12_Preregistration_Jeans_Transition.py': '3b5f93766940243d257f865691f708fd904b2ba9384003ae407f911179059b49', 'UDCT_v7_12_Postregistration_Run.py': '2b7b108a09b60954e18cb3046e4ae1be951580c065193287a51a3ed0c0e8daf6', 'case_decisions.csv': '52ff6ed252afed2dec175566ca32a902c5c2fd2b95eec7b6870df288f7babf3a', 'adaptive_brackets.csv': 'ce19569bb5b533c42605da14a04f362a8e7af45a09a845ac64cb37d52afaee3b', 'requirements.txt': '1668a3152e33680d94637b13421c15e68bd97cd8701f7f555c691f5bc5c0b9f3'}

def main():
 p=argparse.ArgumentParser();p.add_argument('--selftest',action='store_true');p.add_argument('--inventory',action='store_true');a=p.parse_args()
 for name,digest in INPUTS.items():
  path=ROOT/name
  if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest: raise SystemExit('Frozen input missing or changed: '+name)
 with (ROOT/'adaptive_brackets.csv').open(newline='') as f: rows=list(csv.DictReader(f))
 assert len(rows)==24 and all(r['status'].startswith('unresolved_') for r in rows)
 with (ROOT/'case_decisions.csv').open(newline='') as f: cases=list(csv.DictReader(f))
 fixed=[r for r in cases if r['stage'] in ('stage1','stage2')]
 assert len(fixed)==363
 counts={x:sum(r['status']==x for r in fixed) for x in ('N','P','I')}
 assert counts=={'N':274,'P':48,'I':41}
 result={'status':'PRE-REGISTRATION PREPARATION ONLY','frozen_input_verified':True,'fixed_counts':counts,'unresolved_targets':len(rows),'targets':[{'target_id':f'B{i:02d}','axis':r['axis'],'law':r['law'],'fixed_coordinate':r['fixed_coordinate'],'lo':r['lo'],'hi':r['hi'],'previous_stop':r['status']} for i,r in enumerate(rows,1)]}
 if a.inventory: print(json.dumps(result,indent=2))
 else: print('PASS: 24 inherited unresolved brackets; 363 fixed cases (274 N, 48 P, 41 I); frozen inputs verified. No new simulation performed.')
if __name__=='__main__': main()
