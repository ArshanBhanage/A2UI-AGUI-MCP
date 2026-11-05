import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from sandbox import sandbox_document, iframe_attributes

def test_artifact_gets_restrictive_csp_and_doctype():
    doc=sandbox_document('<div>Issue chart</div>'); assert doc.startswith('<!doctype html>'); assert "default-src 'none'" in doc
def test_refresh_is_blocked(): assert 'data-blocked-refresh' in sandbox_document('<meta http-equiv="refresh" content="0">')
def test_size_limit_and_iframe_boundary():
    try: sandbox_document('x'*32001)
    except ValueError: pass
    else: raise AssertionError('oversize artifact accepted')
    assert iframe_attributes()['sandbox']=='allow-scripts'

