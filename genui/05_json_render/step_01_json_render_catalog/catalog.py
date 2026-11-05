CATALOG={'Metric':{'title','value'},'IssueList':{'issues'}}
def validate(spec):
    if spec.get('type') not in CATALOG: raise ValueError('unknown catalog type')
    if set(spec.get('props',{}))-CATALOG[spec['type']]: raise ValueError('unknown prop')
    return spec
