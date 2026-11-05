import json, sys
from pathlib import Path
from fastapi.testclient import TestClient
sys.path.insert(0, str(Path(__file__).parent))
import catalog, llm, server

def frames(text): return [json.loads(line[6:]) for line in text.splitlines() if line.startswith('data: ')]
def test_catalog_is_strict_and_closed():
    for schema in catalog.TOOL_SCHEMAS:
        fn=schema['function']; assert fn['strict'] is True; assert fn['parameters']['additionalProperties'] is False
def test_unknown_or_invalid_calls_are_rejected():
    assert catalog.message_from_call('show_gauge','{}') is None
    assert catalog.message_from_call('show_metric','not-json') is None
    assert catalog.message_from_call('show_metric','[1]') is None
def test_server_streams_fixture_and_terminal_frame(monkeypatch):
    fixture=iter([{'type':'tool_call','name':'show_metric','id':'1','arguments':'{"title":"Open","value":"12","delta":"-2"}'},{'type':'usage','prompt_tokens':1,'completion_tokens':2}])
    monkeypatch.setattr(llm,'stream_chat',lambda messages,tools=None: fixture)
    messages=frames(TestClient(server.app).post('/api/run',json={'prompt':'triage'}).text)
    assert messages[0]['component']=='Metric'; assert messages[-1]['done'] is True
def test_model_failure_is_visible_terminal_frame(monkeypatch):
    def broken(*args,**kwargs): raise RuntimeError('provider unavailable')
    monkeypatch.setattr(llm,'stream_chat',broken)
    messages=frames(TestClient(server.app).post('/api/run',json={'prompt':'triage'}).text)
    assert messages[-1] == {'done':True,'error':'RuntimeError: provider unavailable'}

