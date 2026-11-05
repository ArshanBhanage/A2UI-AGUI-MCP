from events import event,sse,demo_stream
def test_event_lifecycle(): assert [x['type'] for x in demo_stream()]==['RUN_STARTED','TEXT_MESSAGE_CONTENT','RUN_FINISHED']
def test_sse_frame(): assert sse(event('RUN_STARTED',run_id='x')).startswith('data: {')
def test_unknown_event_rejected():
    try: event('HTML_EXECUTION')
    except ValueError: pass
    else: raise AssertionError('unknown event accepted')
