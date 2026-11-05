import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parents[1]/'step_01_a2ui_messages_by_hand'))
from protocol import validate
def correction_loop(messages, attempts=2):
    errors=[]
    for _ in range(attempts):
        try: return [validate(x) for x in messages]
        except ValueError as e:
            errors.append(str(e)); messages=[x for x in messages if x.get('updateComponents',{}).get('components')]
            if not messages: break
    raise ValueError('A2UI correction failed: '+errors[-1])
def offline_messages(): return [{'version':'v0.9.1','createSurface':{'surfaceId':'main','catalogId':'basic'}},{'version':'v0.9.1','updateComponents':{'surfaceId':'main','components':[{'id':'root','component':'Text','text':'Open issues'}]}}]
