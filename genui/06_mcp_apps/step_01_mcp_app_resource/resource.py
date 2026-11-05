def tool_result(): return {'_meta':{'ui':{'resourceUri':'ui://issue-triage/view'}},'structuredContent':{'issue_count':12}}
def validate_bridge(message):
    if message.get('method')!='tools/call' or message.get('params',{}).get('name')!='ack_issue': raise PermissionError('bridge operation not allowed')
    return message
