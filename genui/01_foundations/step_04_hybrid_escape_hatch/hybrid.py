from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parents[1]/'step_03_open_ended_html'))
from sandbox import sandbox_document

CATALOG={'Metric','IssueList'}
def choose_surface(kind, props):
    if kind in CATALOG: return {'kind':kind,'props':props,'mode':'catalog'}
    if kind == 'GeneratedView': return {'kind':kind,'artifact':sandbox_document(props['html']),'mode':'sandbox'}
    raise ValueError('unapproved surface')

