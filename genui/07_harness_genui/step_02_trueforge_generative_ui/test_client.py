from client import health
def test_missing_runtime_is_blocked(monkeypatch):
    monkeypatch.delenv('TRUEFORGE_URL',raising=False)
    assert health()['status']=='BLOCKED'
