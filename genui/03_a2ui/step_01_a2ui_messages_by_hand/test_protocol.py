from protocol import validate,VERSION
def test_four_v091_envelopes():
    base={'version':VERSION};
    for key,body in [('createSurface',{'surfaceId':'main','catalogId':'basic'}),('updateComponents',{'surfaceId':'main','components':[{'id':'root','component':'Column'}]}),('updateDataModel',{'surfaceId':'main','path':'/','value':{}}),('deleteSurface',{'surfaceId':'main'})]: assert validate({**base,key:body})
def test_invalid_version_and_missing_root_rejected():
    try: validate({'version':'v1.0','createSurface':{'surfaceId':'x','catalogId':'basic'}})
    except ValueError: pass
    else: raise AssertionError
    try: validate({'version':VERSION,'updateComponents':{'surfaceId':'x','components':[]}})
    except ValueError: pass
    else: raise AssertionError
