import json
def agui_custom_event(message):
    return {'type':'CUSTOM','name':'a2ui','value':json.dumps(message,separators=(',',':'))}
def decode(event):
    if event.get('type')!='CUSTOM' or event.get('name')!='a2ui': raise ValueError('not an A2UI AG-UI custom event')
    return json.loads(event['value'])
