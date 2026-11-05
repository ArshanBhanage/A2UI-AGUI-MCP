from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parents[1]/'step_01_mcp_app_resource'))
from resource import validate_bridge
def route(layer,message):
    if layer not in {'host','inner-sandbox'}: raise PermissionError('unknown layer')
    return validate_bridge(message)
