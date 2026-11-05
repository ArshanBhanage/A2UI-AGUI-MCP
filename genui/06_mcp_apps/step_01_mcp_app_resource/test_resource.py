from resource import tool_result,validate_bridge
def test_ui_resource_uri(): assert tool_result()['_meta']['ui']['resourceUri'].startswith('ui://')
def test_bridge_allowlist(): assert validate_bridge({'method':'tools/call','params':{'name':'ack_issue'}})
def test_illegal_bridge_rejected():
    try: validate_bridge({'method':'resources/read','params':{}})
    except PermissionError: pass
    else: raise AssertionError
