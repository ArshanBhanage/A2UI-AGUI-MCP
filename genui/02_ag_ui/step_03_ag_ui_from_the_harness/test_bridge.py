from bridge import harness_to_events
def test_callbacks_become_terminal_event_stream():
    items=list(harness_to_events([{'kind':'text','text':'render metric'}])); assert items[1]['delta']=='render metric'; assert items[-1]['type']=='RUN_FINISHED'
def test_error_is_observable(): assert list(harness_to_events([{'kind':'error','message':'offline'}]))[1]['type']=='RUN_ERROR'
