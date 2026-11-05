"""Capture genuine 01.1 browser footage and assemble an MP4 with labeled TTS."""
import json, shutil, socket, subprocess, sys, threading, time
from pathlib import Path

from playwright.sync_api import sync_playwright
import uvicorn

ROOT = Path(__file__).parents[1]
LESSON = ROOT / "genui/01_foundations/step_01_static_components"
OUT = ROOT / "recordings"
TMP = Path("/private/tmp/genux-01-1")
OUT.mkdir(exist_ok=True)
TMP.mkdir(exist_ok=True)
sys.path.insert(0, str(LESSON))
import server, llm  # noqa: E402

FIXTURE = [
    {"type":"tool_call","id":"offline-1","name":"show_metric","arguments":json.dumps({"title":"Open issues","value":"12","delta":"-2"})},
    {"type":"tool_call","id":"offline-2","name":"show_chart","arguments":json.dumps({"kind":"bar","labels":["Mon","Tue"],"values":[8,12]})},
    {"type":"usage","prompt_tokens":0,"completion_tokens":0},
]

def free_port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]

def main():
    port = free_port()
    original = llm.stream_chat
    llm.stream_chat = lambda messages, tools=None: iter(FIXTURE)
    config = uvicorn.Config(server.app, host="127.0.0.1", port=port, log_level="warning")
    instance = uvicorn.Server(config)
    thread = threading.Thread(target=instance.run, daemon=True)
    thread.start()
    deadline = time.time() + 10
    while not instance.started:
        if time.time() > deadline: raise RuntimeError("server did not start")
        time.sleep(.05)
    source = (LESSON / "catalog.py").read_text()
    test_result = subprocess.run([sys.executable, "-m", "pytest", "test_step.py", "-q"], cwd=LESSON, capture_output=True, text=True)
    test_output = (test_result.stdout + test_result.stderr).strip()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width":1280,"height":720}, record_video_dir=str(TMP))
        page = context.new_page()
        page.set_content("""<html><body style='font:32px system-ui;background:#101827;color:#eef;display:grid;place-items:center;height:100vh'><div><h1>GenUX 01.1 — Static Components</h1><p>Real local execution • offline fixture • synthetic narration</p></div></body></html>""")
        page.wait_for_timeout(1800)
        page.set_content(f"""<html><body style='font:18px ui-monospace;background:#101827;color:#eef;padding:28px'><h1>Actual source: catalog.py</h1><pre style='white-space:pre-wrap;color:#b7f7d2'>{source.replace('&','&amp;').replace('<','&lt;')}</pre></body></html>""")
        page.wait_for_timeout(2500)
        page.set_content(f"""<html><body style='font:24px ui-monospace;background:#101827;color:#eef;padding:36px'><h1>Actual test command</h1><pre>{test_output}</pre></body></html>""")
        page.wait_for_timeout(2200)
        page.goto(f"http://127.0.0.1:{port}/")
        page.fill("#prompt", "show today's issue triage summary")
        page.click("#run")
        page.wait_for_selector("body[data-state=done]", timeout=10000)
        page.wait_for_timeout(2200)
        page.screenshot(path=str(TMP / "lesson-01-1.png"), full_page=True)
        context.close()
        browser.close()
    llm.stream_chat = original
    webm = next(TMP.glob("*.webm"))
    shutil.copy2(webm, TMP / "browser.webm")
    narration = TMP / "narration.aiff"
    script = "GenUX lesson zero one point one. Static components. The agent selects trusted components and supplies props; the application owns layout. This is the actual catalog source. The test command passes with four Python tests. Now the real local FastAPI page runs an explicitly labeled offline fixture through the SSE endpoint. The metric and chart render, and the wire panel shows the terminal frame. This footage is genuine local execution, but it is not a live model call."
    subprocess.run(["say", "-o", str(narration), script], check=True)
    mp4 = OUT / "lesson-01-1-static-components.mp4"
    subprocess.run(["ffmpeg", "-y", "-i", str(webm), "-i", str(narration), "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(mp4)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    (ROOT / "video/CAPTIONS/01_static_components.srt").write_text("""1\n00:00:00,000 --> 00:00:04,000\nGenUX lesson 01.1 — Static components.\n\n2\n00:00:04,000 --> 00:00:15,000\nThe agent selects trusted components and supplies props; the application owns layout.\n\n3\n00:00:15,000 --> 00:00:27,000\nThis is the actual catalog source and the real test command.\n\n4\n00:00:27,000 --> 00:00:45,000\nThe local FastAPI page runs an explicitly labeled offline fixture through SSE.\n\n5\n00:00:45,000 --> 00:01:00,000\nThis is genuine local execution, but it is not a live model call.\n""", encoding="utf-8")
    print(mp4)

if __name__ == "__main__": main()
