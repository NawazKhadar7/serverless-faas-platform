import multiprocessing,threading
from .worker import loop
from .tenant import TenantPolicy
class Scheduler:
    """Trusted predefined handlers in tenant-owned reusable processes."""
    def __init__(self,quota=1000,max_workers=4,timeout=1):
        if max_workers<1 or timeout<=0:raise ValueError('positive worker and timeout limits required')
        methods=multiprocessing.get_all_start_methods();self.context=multiprocessing.get_context('fork' if 'fork' in methods and threading.active_count()==1 else 'spawn');self.policy=TenantPolicy(quota);self.workers={};self.capacity=max_workers;self.timeout=timeout;self.starts=0;self.reuses=0
    def retire(self,tenant):
        worker=self.workers.pop(tenant,None)
        if worker:
            connection,process=worker
            connection.close();process.terminate();process.join(.2)
            if process.is_alive():process.kill();process.join(1)
            process.close()
    def invoke(self,tenant,function,payload,cold=False):
        if not self.policy.admit(tenant):return {'status':'limited'}
        if cold:self.retire(tenant)
        if tenant in self.workers:self.reuses+=1
        else:
            if len(self.workers)>=self.capacity:self.retire(next(iter(self.workers)))
            parent,child=self.context.Pipe();process=self.context.Process(target=loop,args=(child,),daemon=True);process.start();child.close();self.workers[tenant]=(parent,process);self.starts+=1
            if not parent.poll(5):self.retire(tenant);return {'status':'startup-failed'}
            parent.recv()
        parent,process=self.workers[tenant]
        try:
            parent.send({'function':function,'payload':payload})
            if not parent.poll(self.timeout):self.retire(tenant);return {'status':'timeout'}
            result=parent.recv()
        except (EOFError,BrokenPipeError,OSError):self.retire(tenant);return {'status':'worker-lost'}
        if cold:self.retire(tenant)
        return result
    def close(self):
        for tenant in list(self.workers):self.retire(tenant)
    def __enter__(self):return self
    def __exit__(self,*args):self.close()
