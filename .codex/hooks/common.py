from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

TEXT_EXTENSIONS = {'.tex', '.typ', '.md', '.qmd', '.bib', '.rst'}

def repo_root() -> Path:
    try:
        p = subprocess.run(['git','rev-parse','--show-toplevel'], capture_output=True, text=True, check=True)
        return Path(p.stdout.strip())
    except Exception:
        return Path(__file__).resolve().parents[2]

def read_json_yaml(path: Path, default):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return default

def manuscript_files(root: Path):
    paper = root / 'paper'
    if not paper.exists(): return []
    return [p for p in paper.rglob('*') if p.is_file() and p.suffix.lower() in TEXT_EXTENSIONS]

def changed_files(root: Path):
    try:
        out = subprocess.run(['git','status','--porcelain'], cwd=root, capture_output=True, text=True, check=True).stdout
        paths=[]
        for line in out.splitlines():
            raw=line[3:]
            if ' -> ' in raw: raw=raw.split(' -> ',1)[1]
            p=root/raw
            if p.exists(): paths.append(p)
        return paths
    except Exception:
        return manuscript_files(root)

def emit(payload):
    print(json.dumps(payload, ensure_ascii=False))

def safe_text(path: Path):
    for enc in ('utf-8','utf-8-sig','latin-1'):
        try: return path.read_text(encoding=enc)
        except Exception: pass
    return ''
