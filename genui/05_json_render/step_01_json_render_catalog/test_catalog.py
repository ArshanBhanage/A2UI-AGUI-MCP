from catalog import validate
def test_registered_type(): assert validate({'type':'Metric','props':{'title':'Open'}})['type']=='Metric'
def test_unknown_type_rejected():
    try: validate({'type':'Script','props':{}})
    except ValueError: pass
    else: raise AssertionError
