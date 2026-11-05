from render_ui import render_ui
def test_two_targets():
    out=render_ui({'type':'Metric','props':{'title':'Open','value':'12'}}); assert out['browser']['tag']=='article' and '[Metric]' in out['terminal']
def test_invalid_spec_rejected():
    try: render_ui({'type':'Script','props':{}})
    except ValueError: pass
    else: raise AssertionError
