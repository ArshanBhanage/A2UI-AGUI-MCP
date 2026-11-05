ALLOWED={'ack_issue'}
def dispatch(name,args):
    if name not in ALLOWED: raise PermissionError('action requires authorization')
    if 'issue_id' not in args: raise ValueError('issue_id required')
    return {'terminal':f'ACK {args["issue_id"]}','browser':{'status':'acknowledged','issue_id':args['issue_id']}}
