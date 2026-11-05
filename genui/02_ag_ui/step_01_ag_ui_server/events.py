import json
EVENTS={'RUN_STARTED','TEXT_MESSAGE_CONTENT','RUN_FINISHED','RUN_ERROR'}
def event(kind, **payload):
    if kind not in EVENTS: raise ValueError('unknown AG-UI event')
    return {'type':kind, **payload}
def sse(item): return 'data: '+json.dumps(item,separators=(',',':'))+'\n\n'
def demo_stream():
    yield event('RUN_STARTED',run_id='offline-run')
    yield event('TEXT_MESSAGE_CONTENT',delta='triage ready')
    yield event('RUN_FINISHED',run_id='offline-run')
