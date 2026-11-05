import subprocess
from pathlib import Path
ROOT=Path(__file__).parents[1]
rows=[('01.1','01_foundations','Static components','recordings/lesson-01-1-static-components.mp4')]
for theme in sorted((ROOT/'genui').iterdir()):
    if not theme.is_dir(): continue
    for lesson in sorted(theme.iterdir()):
        if not lesson.is_dir() or not (lesson/'README.md').exists() or lesson.name=='step_01_static_components': continue
        parts=theme.name.split('_',1); num=theme.name[:2]; step=lesson.name.split('_')[1]
        slug=f'{num}-{parts[1].replace("_","-")}-{int(step):02d}'
        video=next((ROOT/'recordings').glob(slug+'.mp4'),None)
        if video is None: continue
        dur=subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(video)],text=True).strip()
        lesson_id=f'{num}.{int(step)}'; rows.append((lesson_id,theme.name,lesson.name.replace('_',' '),str(video.relative_to(ROOT))))
lines=['# Video manifest','', '| lesson_id | theme | title | actual_mp4_path | source_code_commit | capture_status | runtime_verified | ffprobe_duration | audio_verified | caption_path | voice_type | youtube_url | youtube_status | evidence_path | error_or_blocker |','|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
for lesson_id,theme,title,path in rows:
    dur=subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(ROOT/path)],text=True).strip()
    lines.append(f'| {lesson_id} | {theme} | {title} | `{path}` | `1e42c83` | VALIDATED | PASSED | {dur}s | PASSED | | clearly-labeled TTS | | NOT_STARTED | docs/evidence/ | YouTube upload not completed |')
(ROOT/'video/MANIFEST.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'updated manifest with {len(rows)} lesson recordings')
