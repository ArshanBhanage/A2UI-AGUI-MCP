import json
from protocol import validate
stream=[{'version':'v0.9.1','createSurface':{'surfaceId':'main','catalogId':'basic'}},{'version':'v0.9.1','updateComponents':{'surfaceId':'main','components':[{'id':'root','component':'Text','text':'Open issues'}]}},{'version':'v0.9.1','updateDataModel':{'surfaceId':'main','path':'/count','value':12}}]
for item in stream: print(json.dumps(validate(item)))
