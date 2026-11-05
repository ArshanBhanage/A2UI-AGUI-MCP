"""Capture a complete demo-only video for lesson 01.1."""
import json, shutil, socket, subprocess, sys, threading, time
from pathlib import Path
from playwright.sync_api import sync_playwright
import uvicorn

ROOT = Path(__file__).parents[1]
LESSON = ROOT / "genui/01_foundations/step_01_static_components"
OUT = ROOT / "recordings"
TMP = Path("/private/tmp/genux-01-1-demo-2")
OUT.mkdir(exist_ok=True); TMP.mkdir(exist_ok=True)
sys.path.insert(0, str(LESSON))
import server, llm  # noqa: E402

FIXTURE = [
    {"type":"tool_call","id":"offline-1","name":"show_metric","arguments":json.dumps({"title":"Open issues","value":"12","delta":"-2"})},
    {"type":"tool_call","id":"offline-2","name":"show_chart","arguments":json.dumps({"kind":"bar","labels":["Mon","Tue"],"values":[8,12]})},
    {"type":"usage","prompt_tokens":0,"completion_tokens":0},
]

def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0)); return s.getsockname()[1]

def main():
    port = free_port(); original = llm.stream_chat
    llm.stream_chat = lambda messages, tools=None: iter(FIXTURE)
    instance = uvicorn.Server(uvicorn.Config(server.app, host="127.0.0.1", port=port, log_level="warning"))
    threading.Thread(target=instance.run, daemon=True).start()
    deadline = time.time() + 10
    while not instance.started:
        if time.time() > deadline: raise RuntimeError("server did not start")
        time.sleep(.05)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width":1280,"height":720}, record_video_dir=str(TMP))
        page = context.new_page()
        page.goto(f"http://127.0.0.1:{port}/")
        page.wait_for_timeout(5000)
        page.fill("#prompt", "show today's issue triage summary")
        page.wait_for_timeout(4500)
        page.click("#run")
        page.wait_for_selector("body[data-state=done]", timeout=10000)
        page.wait_for_timeout(9500)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(7500)
        page.set_content("""<html><body style='font:30px system-ui;background:#101827;color:#eef;display:grid;place-items:center;height:100vh;text-align:center'><div><h1>Demo complete</h1><p>Trusted components rendered from an SSE stream.</p><p>Offline fixture • not a live model call</p></div></body></html>""")
        page.wait_for_timeout(7500)
        context.close(); browser.close()
    llm.stream_chat = original
    webm = next(TMP.glob("*.webm"))
    narration = TMP / "narration.aiff"
    text = "This is the complete GenUX lesson zero one point one demo. The page starts with a prompt for an issue triage summary. Static generation means the agent selects trusted components and the application owns the layout, styling, and renderer. I enter the request and submit it. The real local FastAPI endpoint receives the prompt and returns an SSE stream using an explicitly labeled offline fixture. Watch the metric card appear with twelve open issues and a decrease of two. The chart is another trusted component with Monday and Tuesday values. The wire panel records the component messages and then the terminal done frame. That terminal frame matters because the browser can distinguish a finished run from a broken or interrupted stream. This demonstrates the complete request, validation, render, and transport loop. It is genuine local execution, but it is not a live model call. The model SDK is installed separately and a live provider requires credentials. Demo complete."
    subprocess.run(["say", "-r", "145", "-o", str(narration), text], check=True)
    mp4 = OUT / "demo-lesson-01-1-static-components.mp4"
    subprocess.run(["ffmpeg", "-y", "-i", str(webm), "-i", str(narration), "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(mp4)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    (ROOT / "video/CAPTIONS/01_static_components_demo.srt").write_text("""1\n00:00:00,000 --> 00:00:08,000\nThis is the complete GenUX lesson 01.1 demo.\n\n2\n00:00:08,000 --> 00:00:16,000\nIn static generation, the agent selects trusted components and the application owns the layout.\n\n3\n00:00:16,000 --> 00:00:27,000\nThe real local FastAPI endpoint returns an SSE stream using an explicitly labeled offline fixture.\n\n4\n00:00:27,000 --> 00:00:39,000\nThe metric and chart render, followed by the terminal done frame in the wire panel.\n\n5\n00:00:39,000 --> 00:00:48,000\nThis is genuine local execution, not a live model call. Demo complete.\n""", encoding="utf-8")
    print(mp4)

if __name__ == "__main__": main()
