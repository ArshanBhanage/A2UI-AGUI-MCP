import json
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse, Response
from pydantic import BaseModel
import catalog, llm

HERE = Path(__file__).parent
app = FastAPI()
class Run(BaseModel): prompt: str

def sse(message): return f"data: {json.dumps(message)}\n\n"

def components(prompt):
    messages = [{"role":"system","content":"Use only show_metric, show_table, and show_chart tools; never return prose."},{"role":"user","content":prompt}]
    for event in llm.stream_chat(messages, tools=catalog.TOOL_SCHEMAS):
        if event["type"] == "tool_call":
            message = catalog.message_from_call(event["name"], event["arguments"])
            if message is not None: yield message
        elif event["type"] == "text": yield {"note": event["text"]}
        elif event["type"] == "usage": yield {"done": True, **{k:v for k,v in event.items() if k != "type"}}

def guarded(messages):
    try: yield from messages
    except Exception as error: yield {"done": True, "error": f"{type(error).__name__}: {error}"}

@app.post("/api/run")
async def run(body: Run, request: Request):
    async def stream():
        for message in guarded(components(body.prompt)):
            if await request.is_disconnected(): break
            yield sse(message)
    return StreamingResponse(stream(), media_type="text/event-stream", headers={"Cache-Control":"no-cache"})

@app.get("/", response_class=HTMLResponse)
def index(): return (HERE/"page/index.html").read_text()
@app.get("/app.js")
def app_js(): return Response((HERE/"page/app.js").read_text(), media_type="text/javascript")
@app.get("/render.mjs")
def render_js(): return Response((HERE/"page/render.mjs").read_text(), media_type="text/javascript")

