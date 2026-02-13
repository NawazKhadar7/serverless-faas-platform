from .common import validate_case
from .scheduler import Scheduler
FAMILIES=('warm','cold','quota','timeout','failure','tenants')
def run_case(case):
    validate_case(case)
    if case['family'] not in FAMILIES:raise ValueError('unknown FaaS family')
    n=case['size'];family=case['family'];counts={};correct=True;outputs=[]
    with Scheduler(quota=max(1,n//2) if family=='quota' else n+1,timeout=.01 if family=='timeout' else 1) as pool:
        for i in range(n):
            tenant=f'tenant-{i%2}' if family=='tenants' else 'tenant-demo';function='sleep-demo' if family=='timeout' else 'fail-demo' if family=='failure' else 'sum';payload=.1 if family=='timeout' else [i,i+1]
            result=pool.invoke(tenant,function,payload,cold=family=='cold');status=result['status'];counts[status]=counts.get(status,0)+1
            if status=='ok':correct=correct and result['result']==2*i+1
            outputs.append(result)
        starts,reuses=pool.starts,pool.reuses
    return {'metrics':{'requests':n,'ok':counts.get('ok',0),'limited':counts.get('limited',0),'timeouts':counts.get('timeout',0),'failed':counts.get('failed',0),'accounted':sum(counts.values())==n,'results_correct':correct,'worker_starts':starts,'warm_reuses':reuses,'untrusted_code_enabled':False},'output':outputs[:8]}
