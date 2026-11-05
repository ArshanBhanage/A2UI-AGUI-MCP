"""Allowlisted static component catalog for lesson 01.1."""
import json

COMPONENTS = {"show_metric": "Metric", "show_table": "Table", "show_chart": "Chart"}

def _tool(name, description, properties):
    return {"type":"function","function":{"name":name,"description":description,"strict":True,"parameters":{"type":"object","properties":properties,"required":list(properties),"additionalProperties":False}}}

TOOL_SCHEMAS = [
    _tool("show_metric", "Show one triage metric.", {"title":{"type":"string"},"value":{"type":"string"},"delta":{"type":"string"}}),
    _tool("show_table", "Show issue rows.", {"columns":{"type":"array","items":{"type":"string"}},"rows":{"type":"array","items":{"type":"array","items":{"type":"string"}}}}),
    _tool("show_chart", "Show a trusted chart.", {"kind":{"type":"string","enum":["line","bar"]},"labels":{"type":"array","items":{"type":"string"}},"values":{"type":"array","items":{"type":"number"}}}),
]

def message_from_call(name, arguments):
    component = COMPONENTS.get(name)
    if component is None:
        return None
    try:
        props = json.loads(arguments)
    except (TypeError, json.JSONDecodeError):
        return None
    if not isinstance(props, dict):
        return None
    return {"component": component, "props": props}

