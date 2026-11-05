from hybrid import choose
def test_catalog_and_artifact_boundaries():
    assert choose('catalog',{'type':'Metric','props':{}})['browser']
    assert choose('artifact','<h1>custom</h1>')['sandbox']=='allow-scripts'
def test_unknown_region_rejected():
    try: choose('script','x')
    except ValueError: pass
    else: raise AssertionError
