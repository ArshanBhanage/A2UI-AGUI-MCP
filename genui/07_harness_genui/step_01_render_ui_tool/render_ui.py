ALLOWED={'Metric','IssueList'}
def render_ui(spec):
    if spec.get('type') not in ALLOWED: raise ValueError('unknown render_ui type')
    props=spec.get('props',{})
    if not isinstance(props,dict): raise ValueError('props must be an object')
    return {'browser':{'tag':'article','text':str(props)},'terminal':f"[{spec['type']}] {props}"}
