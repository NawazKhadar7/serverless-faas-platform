import math,time

def handle(function,payload):
    if function=='sum':
        if not isinstance(payload,list) or len(payload)>1000 or any(not isinstance(x,(int,float)) or not math.isfinite(x) for x in payload):raise ValueError('finite numeric list required')
        return sum(payload)
    if function=='upper':
        if not isinstance(payload,str) or len(payload)>4096:raise ValueError('small string required')
        return payload.upper()
    if function=='sleep-demo':
        if not isinstance(payload,(int,float)) or not 0<=payload<=.2:raise ValueError('demo sleep outside 0..0.2')
        time.sleep(payload);return 'slept'
    if function=='fail-demo':raise ValueError('intentional synthetic function failure')
    raise ValueError('unregistered function')
def loop(connection):
    connection.send({'ready':True})
    try:
        while True:
            request=connection.recv()
            if request is None:break
            try:connection.send({'status':'ok','result':handle(request['function'],request['payload'])})
            except Exception as exc:connection.send({'status':'failed','error':str(exc)})
    except (EOFError,BrokenPipeError):pass
    finally:connection.close()
