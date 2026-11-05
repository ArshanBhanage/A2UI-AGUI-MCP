from actions import dispatch
def test_two_targets():
    result=dispatch('ack_issue',{'issue_id':'ISS-1'}); assert result['terminal'].startswith('ACK') and result['browser']['status']=='acknowledged'
def test_unauthorized_action():
    try: dispatch('delete_all',{})
    except PermissionError: pass
    else: raise AssertionError
