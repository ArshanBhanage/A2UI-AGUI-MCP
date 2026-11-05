import copy
ALLOWED_TOOLS={'ack_issue'}
def apply_patch(state, patch):
    if patch.get('op')!='replace' or not patch.get('path','').startswith('/'): raise ValueError('unsupported patch')
    key=patch['path'][1:]
    if key not in state: raise ValueError('unknown state key')
    result=copy.deepcopy(state); result[key]=patch['value']; return result
def authorize_tool(name,args):
    if name not in ALLOWED_TOOLS: raise PermissionError('tool not allowed')
    if not isinstance(args,dict) or 'issue_id' not in args: raise ValueError('invalid tool arguments')
    return {'name':name,'args':args}
