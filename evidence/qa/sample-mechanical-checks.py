from pathlib import Path
from collections import Counter,defaultdict
import json,hashlib,importlib.util,tempfile
root=Path('/home/dgk/workspace/webex_connect_kb'); base=root/'evidence/sample-flows'; obs=base/'observed'; sums=base/'summaries'; issues=[];results=[]
index=json.loads((sums/'index.json').read_text()); inventory=json.loads((base/'sample-inventory.json').read_text())
expected_rows=[r for r in inventory['samples'] if r['cohort'] in {'tenant_gallery','ai_fulfilment_repository','wxcc_repository_v3_5'}]
expected_paths={p for r in expected_rows for p in r['observed_paths']};actual_paths={str(p.relative_to(root)) for p in obs.glob('*.json')};keys={Path(p).stem for p in expected_paths}
assert len(expected_rows)==59 and len(expected_paths)==59
assert expected_paths==actual_paths
assert keys=={p.stem for p in sums.glob('*.json') if p.name!='index.json'}=={r['sample_key'] for r in index['samples']}
notes={}
for file in ['observed-narratives.json','native-narratives.json','wxcc-selected-narratives.json','wxcc-narratives.json','wxcc-social-narratives.json']:
 d=json.loads((base/file).read_text());notes.update(d)
report=(root/'evidence/tenant-samples.md').read_text();detail=(root/'evidence/tenant-sample-relationships.md').read_text()
for key in sorted(keys):
 path=obs/(key+'.json');raw=path.read_bytes();o=json.loads(raw);s=json.loads((sums/(key+'.json')).read_text());cells=o['cells'];byid={str(c['id']):c for c in cells};assert len(cells)==len(byid),(key,'duplicate cell IDs')
 edges={str(c['id']):c for c in cells if c.get('edge')};ends={};nodes={}
 for c in cells:
  if not c.get('vertex') or c.get('edge'):continue
  v=c.get('value') or {}
  if v.get('nodeType')=='end' or v.get('data',{}).get('type')=='end':ends[str(c['id'])]=c
  elif v.get('tag'):nodes[str(c['id'])]=c
 assert s['source_sha256']==hashlib.sha256(raw).hexdigest(),(key,'hash')
 assert s['sample_key']==key and s['runtime_tested'] is False and o['runtime_tested'] is False
 assert s['counts']['cells']==len(cells) and s['counts']['operative_nodes']==len(nodes) and s['counts']['explicit_edges']==len(edges) and s['counts']['terminal_bindings']==len(ends)
 assert s['counts']['variable_references']==len(s['variable_handoffs'])
 assert set(nodes)=={n['id'] for n in s['nodes']} and set(edges)=={e['id'] for e in s['edges']} and set(ends)=={e['id'] for e in s['terminal_bindings']}
 for e in s['edges']:
  orig=edges[e['id']];v=orig['value'];assert (e['source'],e['target'])==(str(orig['source']),str(orig['target']));assert e['event_internal']==v.get('name',v.get('value')) and e['event_label']==v.get('label')
 missing_end_sources=set();groups=Counter();outcomes={str(x['id']):x for x in o['outcomes']}
 for t in s['terminal_bindings']:
  orig=ends[t['id']]['value'];params={x.get('name'):x.get('value') for x in orig.get('params',[])};source=str(orig.get('data',{}).get('parentNode'))
  assert t['source']==source and t['event_internal']==params.get('nodeEvent',orig.get('name')) and t['outcome_id']==params.get('exitResult')
  assert t['producer_captured']==(source in nodes)
  if source not in nodes:missing_end_sources.add(source)
  outcome=outcomes.get(str(params.get('exitResult')),{});assert t['outcome_name']==outcome.get('tagName',outcome.get('value'))
  groups[(source,str(t['event_internal']),str(t['outcome_id']))]+=1
 assert set(s['terminal_sources_not_captured'])==missing_end_sources
 for t in s['terminal_bindings']:assert t['same_binding_record_count']==groups[(t['source'],str(t['event_internal']),str(t['outcome_id']))]
 flagged_groups={(d['source'],d['event_internal'],d['outcome_id']):d['record_count'] for d in s['duplicate_terminal_binding_groups']};assert flagged_groups=={k:v for k,v in groups.items() if v>1}
 graph=defaultdict(set)
 for e in s['edges']:
  if e['source'] in nodes and e['target'] in nodes:graph[e['source']].add(e['target'])
 reachable={}
 for n in nodes:
  seen=set();stack=list(graph[n])
  while stack:
   x=stack.pop()
   if x in seen:continue
   seen.add(x);stack.extend(graph[x]-seen)
  reachable[n]=seen
 independent_cycles=set()
 for n in nodes:
  component=frozenset([n]+[x for x in reachable[n] if n in reachable.get(x,set())])
  if len(component)>1 or n in graph[n]:independent_cycles.add(component)
 assert independent_cycles=={frozenset(c) for c in s['cycles']},(key,'cycles')
 writerids={x['writer_node'] for x in s['custom_variable_assignments']};assert writerids<=set(nodes)
 actual_missing_producers={r['producer_node'] for r in s['variable_handoffs'] if r['producer_node'] and r['producer_node'] not in nodes};assert actual_missing_producers==set(s['node_variable_producers_not_captured'])
 for ref in s['variable_handoffs']:
  assert set(ref['observed_custom_writers'])<=set(nodes)
  assert ref['evidence'] in {'literal_variable_reference','captured_variable_use_metadata'}
 assert s['authored_walkthrough']==notes[key] and all(notes[key].get(k) for k in ['walkthrough','handoffs','limitations'])
 assert f'id="{key}"' in report and f'id="{key}"' in detail
 if missing_end_sources:assert 'End records reference absent producer nodes: ' in detail.split(f'<a id="{key}"></a>',1)[1].split('<a id=',1)[0]
 results.append({'key':key,'counts':s['counts'],'start_nodes':sum((c.get('value') or {}).get('tag')=='start' for c in nodes.values()),'cycle_groups':len(independent_cycles),'stale_end_sources':sorted(missing_end_sources),'missing_node_reference_producers':sorted(actual_missing_producers),'narrative_and_report_coverage':'pass','graph_record_invariants':'pass'})
# Every acquired member is present and hash-valid, and all CCE records stay source-only.
manifest_checks={}
for filename in ['public-native-manifest.json','public-wxcc-manifest.json']:
 records=json.loads((base/filename).read_text());checked=0
 for r in records:
  rel=r.get('local_path') or 'evidence/sample-flows/raw/'+r['file'];p=root/rel
  assert p.exists(),(filename,rel)
  assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],(filename,rel,'hash')
  if 'bytes' in r:assert p.stat().st_size==r['bytes']
  checked+=1
 manifest_checks[filename]={'records':len(records),'local_hashes_checked':checked}
cce=[x for x in inventory['samples'] if x['cohort']=='cce_documented_bundle'];assert len(cce)==15
assert all(not x.get('observed_paths') and x['runtime_tested'] is False for x in cce)
# Fresh in-process search scope plus a temporary fixture proving raw/observed are excluded.
spec=importlib.util.spec_from_file_location('search_sample_qa',root/'scripts/search_kb.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
docs=module.documents(root,'samples');assert len(docs)==59 and all(x['kind']=='sample' and x['runtime_tested'] is False for x in docs)
assert all(x['path'].startswith('evidence/sample-flows/summaries/') and not x['path'].endswith('/index.json') for x in docs)
with tempfile.TemporaryDirectory(prefix='webex-sample-scope-qa-') as tmp:
 t=Path(tmp)
 for sub in ['summaries','observed','raw']:(t/'evidence/sample-flows'/sub).mkdir(parents=True)
 (t/'evidence/sample-flows/summaries/a.json').write_text(json.dumps({'sample_key':'a','title':'Sanitized sample','evidence_type':'synthetic_local_qa','runtime_tested':False,'walkthrough_status':'authored','note':'summarysentinel'}))
 for sub in ['raw','observed']:(t/'evidence/sample-flows'/sub/'fixture.json').write_text(json.dumps({'sample_key':'should-not-index','note':'rawsentinel'}))
 assert len(module.documents(t,'samples'))==1 and not module.search(t,'rawsentinel',scope='samples')
 assert module.search(t,'summarysentinel',scope='samples')[0]['kind']=='sample'
queries={q:[{'path':x['path'],'kind':x['kind'],'evidence_type':x['evidence_type'],'runtime_tested':x['runtime_tested']} for x in module.search(root,q,limit=3,scope='samples')] for q in ['AI Agent Livechat','MessageMetadata','Email Inbound','lookup_appointment','sendSMS']}
out={'scope':'59 = 9 gallery + 17 AI native + 33 WxCC v3.5; CCE15 remain documented-only','coverage':'pass','files_checked':len(results),'totals':dict(sum((Counter(r['counts']) for r in results),Counter())),'graphs_with_stale_end_sources':sum(bool(r['stale_end_sources']) for r in results),'all_graph_invariants':'pass','all_authored_narratives_present':'pass','source_manifest_hash_checks':manifest_checks,'cce_source_only_count':len(cce),'samples_search_count':len(docs),'samples_search_excludes_raw_and_observed_fixture':'pass','search_examples':queries,'records':results}
(root/'evidence/qa/sample-mechanical-checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in {'records','search_examples'}},indent=2))
