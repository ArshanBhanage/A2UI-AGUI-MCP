"""Typed allowlist for a small declarative issue-triage tree."""
from jsonschema import Draft202012Validator

SCHEMA = {"type":"object","required":["type","props"],"additionalProperties":False,"properties":{"type":{"enum":["Stack","Metric","IssueList"]},"props":{"type":"object"},"children":{"type":"array"}}}
VALIDATOR = Draft202012Validator(SCHEMA)
PROPS = {"Stack":{"direction":{"enum":["row","column"]}},"Metric":{"title":{"type":"string"},"value":{"type":"string"}},"IssueList":{"issues":{"type":"array","items":{"type":"string"}}}}

def validate_tree(node):
    if node.get("type") not in PROPS: raise ValueError(f"unknown component: {node.get('type')}")
    errors=list(VALIDATOR.iter_errors(node))
    if errors: raise ValueError(errors[0].message)
    for name, schema in PROPS[node["type"]].items():
        if name in node["props"]:
            Draft202012Validator({"type":"object","properties":{name:schema}}).validate({name:node["props"][name]})
    for child in node.get("children",[]): validate_tree(child)
    return node

