import html
from pathlib import Path
ROOT=Path(__file__).parents[1]
lessons=[]
for theme in sorted((ROOT/'genui').iterdir()):
    if not theme.is_dir(): continue
    for lesson in sorted(theme.iterdir()):
        if lesson.is_dir() and (lesson/'README.md').exists(): lessons.append((theme.name,lesson))
cards=[]
for theme,lesson in lessons:
    rel=lesson.relative_to(ROOT); title=lesson.name.replace('_',' ').title()
    cards.append(f'<article><h3>{html.escape(theme)} / {html.escape(title)}</h3><p><a href="../{rel}/README.md">README</a> · <a href="../{rel}/WALKTHROUGH.md">Walkthrough</a> · <a href="../{rel}/DEMO.md">Demo</a></p></article>')
site=ROOT/'site'; site.mkdir(exist_ok=True)
content='<!doctype html><meta charset="utf-8"><title>GenUX Assignment 4</title><style>body{font:16px system-ui;max-width:1000px;margin:auto;padding:2rem;background:#101827;color:#eef}a{color:#8bd5ff}article{background:#1b2940;border:1px solid #38506f;border-radius:10px;padding:1rem;margin:.7rem 0}</style><h1>GenUX / Generative UI Codelab Suite</h1><p>Assignment 4 portal generated from the repository lesson inventory.</p><h2>Lessons</h2>'+''.join(cards)+'<h2>Verification</h2><p><a href="../docs/MILESTONES.md">Milestones</a> · <a href="../video/MANIFEST.md">Video manifest</a> · <a href="../README_SUBMISSION.md">Submission report</a></p>'
(site/'index.html').write_text(content,encoding='utf-8')
print(f'generated {site/"index.html"} from {len(cards)} lesson folders')
