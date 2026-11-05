from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parents[1]/'step_01_render_ui_tool'))
from render_ui import render_ui
MAX=32000
def artifact(source):
    if len(source.encode())>MAX: raise ValueError('artifact too large')
    return {'sandbox':'allow-scripts','source':source}
def choose(kind,payload):
    if kind=='catalog': return render_ui(payload)
    if kind=='artifact': return artifact(payload)
    raise ValueError('unknown hybrid region')
