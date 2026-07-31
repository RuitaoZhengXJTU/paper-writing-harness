from __future__ import annotations
import json, re, sys
from difflib import SequenceMatcher
from pathlib import Path
from common import repo_root, read_json_yaml, changed_files, manuscript_files, safe_text

root=repo_root(); audit=root/'internal/audits'; audit.mkdir(parents=True,exist_ok=True)
files=[p for p in changed_files(root) if root/'paper' in p.parents]
if not files: files=manuscript_files(root) if '--all' in sys.argv else []
findings=[]
# Parse memory files.
for rel in ['PAPER_CONTRACT.yaml','SECTION_CONTRACTS.yaml','CLAIM_LEDGER.yaml','TERMINOLOGY.yaml','STALE_SECTIONS.yaml','EVIDENCE_INDEX.yaml']:
    p=root/'internal'/rel
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: findings.append({'severity':'HIGH','category':'invalid state file','file':str(p.relative_to(root)),'detail':str(e)})
terms=read_json_yaml(root/'internal/TERMINOLOGY.yaml',{}).get('terms',{})
for p in files:
    text=safe_text(p)
    for item in terms.values():
        if not isinstance(item,dict): continue
        for bad in item.get('forbidden_variants',[]):
            if bad and re.search(r'(?<!\w)'+re.escape(bad)+r'(?!\w)',text,re.I):
                findings.append({'severity':'MEDIUM','category':'forbidden terminology','file':str(p.relative_to(root)),'detail':bad})
# Conservative duplicate paragraph check.
paras=[]
for p in manuscript_files(root):
    for i,para in enumerate(re.split(r'\n\s*\n',safe_text(p))):
        norm=' '.join(para.split())
        if len(norm)>=180 and not norm.startswith(('%','```')): paras.append((p,i+1,norm))
for i in range(len(paras)):
    for j in range(i+1,len(paras)):
        if paras[i][0]==paras[j][0] and paras[i][1]==paras[j][1]: continue
        ratio=SequenceMatcher(None,paras[i][2],paras[j][2]).ratio()
        if ratio>=0.93:
            findings.append({'severity':'MEDIUM','category':'near-duplicate paragraph','file':str(paras[i][0].relative_to(root)),'detail':f"paragraph {paras[i][1]} resembles {paras[j][0].relative_to(root)} paragraph {paras[j][1]} ({ratio:.2f})"})
            if len(findings)>100: break
    if len(findings)>100: break
payload={'heuristic':True,'files_inspected':[str(p.relative_to(root)) for p in files],'findings':findings}
(audit/'latest-consistency-report.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# Latest consistency report','', '> Heuristic checks do not establish scientific or semantic completeness.','']
if findings:
    for f in findings: lines.append(f"- **{f['severity']} — {f['category']}** `{f['file']}` — {f['detail']}")
else: lines.append('No heuristic findings in the inspected scope.')
(audit/'latest-consistency-report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({'findings':len(findings),'report':'internal/audits/latest-consistency-report.md'}))
