from state import apply_patch,authorize_tool
def test_patch_updates_snapshot(): assert apply_patch({'status':'open'},{'op':'replace','path':'/status','value':'acknowledged'})['status']=='acknowledged'
def test_bad_patch_rejected():
    try: apply_patch({'status':'open'},{'op':'remove','path':'/status'})
    except ValueError: pass
    else: raise AssertionError
def test_tool_allowlist(): assert authorize_tool('ack_issue',{'issue_id':'ISS-1'})['name']=='ack_issue'
