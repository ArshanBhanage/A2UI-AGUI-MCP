import copy
def apply(state,patch):
    if patch.get('op')!='replace': raise ValueError('only replace supported')
    key=patch['path'].strip('/')
    if key not in state: raise ValueError('unknown element')
    result=copy.deepcopy(state); result[key]=patch['value']; return result
