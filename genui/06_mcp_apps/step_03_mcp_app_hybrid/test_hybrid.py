from hybrid import route
def test_nested_route(): assert route('inner-sandbox',{'method':'tools/call','params':{'name':'ack_issue'}})
def test_unknown_layer_rejected():
    try: route('dom',{})
    except PermissionError: pass
    else: raise AssertionError
