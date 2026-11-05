from agent import correction_loop,offline_messages
def test_offline_generation_validates(): assert len(correction_loop(offline_messages()))==2
def test_correction_rejects_unrecoverable():
    try: correction_loop([{'version':'v1.0','createSurface':{'surfaceId':'x','catalogId':'basic'}}])
    except ValueError: pass
    else: raise AssertionError
