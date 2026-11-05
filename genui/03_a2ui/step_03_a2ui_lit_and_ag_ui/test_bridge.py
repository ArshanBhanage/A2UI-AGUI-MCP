from bridge import agui_custom_event,decode
def test_representation_and_transport_are_distinct():
    message={'version':'v0.9.1','deleteSurface':{'surfaceId':'main'}}; assert decode(agui_custom_event(message))==message
def test_wrong_event_rejected():
    try: decode({'type':'TEXT_MESSAGE_CONTENT','delta':'x'})
    except ValueError: pass
    else: raise AssertionError
