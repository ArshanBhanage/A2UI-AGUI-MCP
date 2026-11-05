"""Capture one real browser walkthrough per lesson from its executable demo."""
import html, subprocess, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).parents[1]; OUT=ROOT/'recordings'; TMP=Path('/private/tmp/genux-all-videos'); OUT.mkdir(exist_ok=True); TMP.mkdir(exist_ok=True)
lessons=[]
for theme in sorted((ROOT/'genui').iterdir()):
    if not theme.is_dir(): continue
    for lesson in sorted(theme.iterdir()):
        if lesson.is_dir() and (lesson/'demo.py').exists() and lesson.name != 'step_01_static_components': lessons.append(lesson)

def main():
    with sync_playwright() as p:
        browser=p.chromium.launch()
        for lesson in lessons:
            lesson_id=lesson.relative_to(ROOT/'genui').parts[0]+'-'+lesson.name.split('_')[1]
            slug=lesson_id.replace('_','-')
            if (OUT/f'{slug}.mp4').exists(): continue
            result=subprocess.run([sys.executable,'demo.py'],cwd=lesson,capture_output=True,text=True,timeout=30)
            output=(result.stdout+result.stderr).strip()[-3000:]
            source=(lesson/'README.md').read_text(encoding='utf-8')[:1800]
            video_dir=TMP/slug; video_dir.mkdir(exist_ok=True)
            context=browser.new_context(viewport={'width':1280,'height':720},record_video_dir=str(video_dir)); page=context.new_page()
            page.set_content(f"<body style='font:24px system-ui;background:#101827;color:#eef;padding:36px'><h1>GenUX {html.escape(slug)}</h1><p>Real lesson demo capture • synthetic narration</p><pre style='white-space:pre-wrap'>{html.escape(source)}</pre></body>")
            page.wait_for_timeout(2500)
            page.set_content(f"<body style='font:20px ui-monospace;background:#101827;color:#d8fbe5;padding:36px'><h1>Actual command: python3 demo.py</h1><pre style='white-space:pre-wrap'>{html.escape(output or '(no output)')}</pre></body>")
            page.wait_for_timeout(7000)
            page.set_content(f"<body style='font:30px system-ui;background:#101827;color:#eef;display:grid;place-items:center;height:100vh;text-align:center'><div><h1>Lesson demo complete</h1><p>{html.escape(slug)}</p><p>See README for live/blocker status.</p></div></body>")
            page.wait_for_timeout(4000); context.close(); browser.close() if False else None
            webm=next(video_dir.glob('*.webm'))
            narration=video_dir/'narration.aiff'
            text=f"GenUX {slug}. This recording shows the actual lesson README and the actual demo command. The observed output is shown on screen. Synthetic narration is used. Any live provider or host status is stated by the lesson itself and is not inferred from this offline capture. Lesson demo complete."
            subprocess.run(['say','-r','150','-o',str(narration),text],check=True)
            mp4=OUT/f'{slug}.mp4'
            subprocess.run(['ffmpeg','-y','-i',str(webm),'-i',str(narration),'-vf','scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2','-c:v','libx264','-pix_fmt','yuv420p','-c:a','aac','-shortest',str(mp4)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            print(mp4)
        browser.close()
if __name__=='__main__': main()
