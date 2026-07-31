from common import repo_root, read_json_yaml, emit

root=repo_root()
contract=read_json_yaml(root/'internal/PAPER_CONTRACT.yaml', {})
claims=read_json_yaml(root/'internal/CLAIM_LEDGER.yaml', {})
terms=read_json_yaml(root/'internal/TERMINOLOGY.yaml', {})
stale=read_json_yaml(root/'internal/STALE_SECTIONS.yaml', {})
paper=contract.get('paper',{})
def val(key):
    v=paper.get(key,{})
    return v.get('value') if isinstance(v,dict) else v
summary={
  'manuscript_root':'paper/',
  'central_problem':val('central_problem'),
  'central_contribution':val('central_contribution'),
  'reviewer_takeaway':val('reviewer_takeaway'),
  'disclosure_policy':paper.get('disclosure_policy',{}),
  'claims':list(claims.get('claims',{}).keys())[:20],
  'canonical_terms':[v.get('canonical') for v in terms.get('terms',{}).values() if isinstance(v,dict) and v.get('canonical')][:30],
  'stale_sections':[k for k,v in stale.get('sections',{}).items() if isinstance(v,dict) and v.get('status')=='stale']
}
emit({'additionalContext':'Canonical paper state:\n'+__import__('json').dumps(summary,ensure_ascii=False,indent=2)})
