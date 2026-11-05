import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from catalog import validate_tree
from stream import IncrementalJSON

def test_nested_tree_validates():
    tree={"type":"Stack","props":{"direction":"column"},"children":[{"type":"Metric","props":{"title":"Open","value":"12"}}]}
    assert validate_tree(tree)["type"] == "Stack"
def test_unknown_component_rejected():
    try: validate_tree({"type":"Script","props":{}})
    except ValueError as e: assert "unknown" in str(e)
    else: raise AssertionError("unknown component accepted")
def test_partial_json_completes_only_at_final_chunk():
    parser=IncrementalJSON(); assert parser.feed('{"type":"Metric",') is None
    assert parser.feed('"props":{"title":"Open","value":"12"}}')["type"] == "Metric"

