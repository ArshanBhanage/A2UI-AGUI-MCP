"""Small v0.9.1 envelope validator based on the pinned production spec."""
VERSION='v0.9.1'; TYPES={'createSurface','updateComponents','updateDataModel','deleteSurface'}
def validate(message):
    if message.get('version') != VERSION: raise ValueError('A2UI version must be v0.9.1')
    keys=set(message)-{'version'}
    if len(keys)!=1 or next(iter(keys)) not in TYPES: raise ValueError('one A2UI envelope key required')
    kind=next(iter(keys)); body=message[kind]
    if kind=='createSurface':
        if not {'surfaceId','catalogId'}<=body.keys(): raise ValueError('createSurface requires surfaceId and catalogId')
    elif 'surfaceId' not in body: raise ValueError(f'{kind} requires surfaceId')
    if kind=='updateComponents' and not any(x.get('id')=='root' for x in body.get('components',[])): raise ValueError('updateComponents requires root component')
    return message

