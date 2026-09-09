import json
from pathlib import Path
base=Path('evidence/sample-flows'); selections={
 'gallery-ai-livechat':{'1695':['method_id','version_id','methodResponseParameters','request_body'],'756':['timeout','data']},
 'gallery-ai-doctor':{'1731':['expression'],'768':['message']},
 'gallery-track-package':{'3':['outputvariablelist']},
 'native-lookup-appointment':{'3':['body']},
 'native-sendsms':{'3':['destination','message']},
 'wxcc-emailinboundflow':{'1898':['body']},
 'wxcc-sms-inbound':{'1186':['message']},
 'wxcc-emailattachmentdropnotification':{'1980':['body']},
 'wxcc-emailinboundsampleflowwithcontactpriority':{'1980':['expression'],'1851':['request_body']},
 'wxcc-task-routed-sample-flow-for-extracting-variables':{'1520':['expression'],'1326':['request_body']},
 'wxcc-livechatinboundsampleflowwithsetvariablepiqandewt':{'2475':['nodeInput'],'2634':['request_body']},
 'wxcc-apple-time-picker-and-list-picker-response-flow':{'336':['expression'],'242':['request_body'],'348':['request_body']},
 'native-checkin':{'3':['body','outputvariablelist']}}
records=[]; nfields=0
for key, nodes in selections.items():
 o=json.loads((base/'observed'/f'{key}.json').read_text());s=json.loads((base/'summaries'/f'{key}.json').read_text()); raw={str(c['id']):c for c in o['cells']}; sm={n['id']:n for n in s['nodes']}; checked=[]
 for node, fields in nodes.items():
  params={p['attributes']['name']:p['text'] for p in raw[node]['value']['children'] if p['tag']=='param'}
  for field in fields:
   assert field in sm[node]['configuration'],(key,node,field,'absent')
   assert params[field]==sm[node]['configuration'][field],(key,node,field)
   checked.append(node+'.'+field);nfields+=1
 records.append({'sample':key,'fields_compared_directly_to_observed_model':checked,'result':'pass'})
o=json.loads((base/'observed/gallery-ai-doctor.json').read_text());raw={str(c['id']):c for c in o['cells']};children=raw['1731']['value']['children'];expr=next(x['text'] for x in children if x['tag']=='param' and x['attributes']['name']=='expression');assignment=next(x for x in children if x['tag']=='session' and x['attributes']['name']=='agentTextResp');msg=next(x['text'] for x in raw['768']['value']['children'] if x['tag']=='param' and x['attributes']['name']=='message')
assert 'agentTextResponse =' in expr and 'agentTextResp =' not in expr
assert assignment['text']==msg=='$(agentTextResp)'
assert any(c.get('edge') and c.get('source')=='1731' and c.get('target')=='768' and c['value']['name']==1 for c in o['cells'])
out={'scope':'Critical AI/email/SMS and bounded other-pattern parameter comparisons; not a runtime test','sample_count':len(records),'parameter_comparisons':nfields,'records':records,'doctor_handoff_witness':{'evaluate_node':'1731','error_js_assignment':'agentTextResponse','onleave_name':'agentTextResp','onleave_value':'$(agentTextResp)','error_edge_internal':1,'send_node':'768','send_message':'$(agentTextResp)','status':'documentation limitation reported to parent'}}
Path('evidence/qa/sample-semantic-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'selected_samples':len(records),'source_parameter_comparisons':nfields,'result':'pass','doctor_mismatch':'confirmed static evidence'}))
