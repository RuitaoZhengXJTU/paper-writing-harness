from __future__ import annotations
import json, re, sys
from pathlib import Path
from common import repo_root, changed_files, manuscript_files, safe_text

root=repo_root(); audit=root/'internal/audits'; audit.mkdir(parents=True,exist_ok=True)
files=[p for p in changed_files(root) if root/'paper' in p.parents]
if not files: files=manuscript_files(root) if '--all' in sys.argv else []
patterns={
 'absolute path': re.compile(r'(?i)(?:[A-Z]:\\\\|/Users/|/home/|/mnt/|/tmp/)'),
 'internal path': re.compile(r'(?i)\b(?:internal|scratch)/'),
 'unfinished marker': re.compile(r'\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b'),
 'agent narration': re.compile(r'(?i)\b(?:the agent|we asked the AI|the prompt|tool call|local script)\b'),
 'shell command': re.compile(r'(?m)^\s*(?:python|bash|sh|pwsh|make|git)\s+[^\n]+$')
}
findings=[]
for p in files:
    text=safe_text(p)
    for label,rx in patterns.items():
        for m in rx.finditer(text):
            line=text.count('\n',0,m.start())+1
            findings.append({'severity':'MEDIUM','category':label,'file':str(p.relative_to(root)),'line':line,'excerpt':m.group(0)[:120]})
report=['# Latest paper guard','', '> Heuristic advisory findings; review false positives manually.','']
if findings:
    for f in findings: report.append(f"- **{f['severity']} — {f['category']}** `{f['file']}:{f['line']}` — `{f['excerpt']}`")
else: report.append('No pattern-based findings in the inspected files.')
(audit/'latest-paper-guard.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print(json.dumps({'findings':len(findings),'report':'internal/audits/latest-paper-guard.md'}))
