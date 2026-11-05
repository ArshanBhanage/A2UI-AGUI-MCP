"""Run the lesson offline with a deterministic, explicitly labeled fixture."""
import argparse, json, threading
from fastapi.testclient import TestClient
import server, llm

FIXTURE=[{"type":"tool_call","id":"offline-1","name":"show_metric","arguments":json.dumps({"title":"Open issues","value":"12","delta":"-2"})},{"type":"tool_call","id":"offline-2","name":"show_chart","arguments":json.dumps({"kind":"bar","labels":["Mon","Tue"],"values":[8,12]})},{"type":"usage","prompt_tokens":0,"completion_tokens":0}]
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--offline',action='store_true'); args=parser.parse_args()
    if not args.offline: raise SystemExit('LIVE model demo requires API_KEY, the OpenAI SDK, and Playwright; use --offline for the deterministic fixture.')
    original=llm.stream_chat; llm.stream_chat=lambda messages,tools=None: iter(FIXTURE)
    try:
        response=TestClient(server.app).post('/api/run',json={'prompt':'show issue triage'})
        messages=[json.loads(line[6:]) for line in response.text.splitlines() if line.startswith('data: ')]
        print('mode: OFFLINE FIXTURE (not a live agent run)')
        print(f'{len(messages)} SSE messages:')
        for message in messages: print('  '+json.dumps(message))
    finally: llm.stream_chat=original
if __name__=='__main__': main()

