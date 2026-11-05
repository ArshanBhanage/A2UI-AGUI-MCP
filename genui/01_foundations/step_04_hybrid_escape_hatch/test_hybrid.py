import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from hybrid import choose_surface

def test_catalog_surface_is_selected(): assert choose_surface('Metric',{'value':'12'})['mode']=='catalog'
def test_escape_hatch_is_sandboxed(): assert "default-src 'none'" in choose_surface('GeneratedView',{'html':'<h1>custom</h1>'})['artifact']
def test_unapproved_surface_rejected():
    try: choose_surface('Script',{})
    except ValueError: pass
    else: raise AssertionError('unapproved surface accepted')
