from patches import apply
def test_ordered_patch(): assert apply({'root':'Metric'},{'op':'replace','path':'/root','value':'IssueList'})['root']=='IssueList'
def test_bad_patch_preserves_previous_state():
    state={'root':'Metric'}
    try: apply(state,{'op':'remove','path':'/root'})
    except ValueError: pass
    assert state=={'root':'Metric'}
