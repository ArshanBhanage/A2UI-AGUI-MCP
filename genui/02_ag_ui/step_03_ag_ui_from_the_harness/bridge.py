from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parents[1]/'step_01_ag_ui_server'))
from events import event
def harness_to_events(callbacks):
    yield event('RUN_STARTED',run_id='harness-offline')
    for callback in callbacks:
        if callback.get('kind')=='text': yield event('TEXT_MESSAGE_CONTENT',delta=callback['text'])
        elif callback.get('kind')=='error': yield event('RUN_ERROR',message=callback['message'])
    yield event('RUN_FINISHED',run_id='harness-offline')
