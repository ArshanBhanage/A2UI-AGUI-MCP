from client import health
def test_unreachable_runtime_is_blocked(monkeypatch):
    monkeypatch.setenv('TRUEFORGE_URL','http://127.0.0.1:1')
    assert health()['status']=='BLOCKED'
