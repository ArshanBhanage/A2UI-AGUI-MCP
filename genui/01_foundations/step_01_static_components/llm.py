"""Optional OpenAI-compatible stream; tests inject a deterministic client."""
import os
from pathlib import Path

API_KEY = os.getenv("API_KEY") or os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL", "https://api.openai.com/v1")
MODEL = os.getenv("MODEL", "gpt-4.1-mini")
client = None
try:
    from openai import OpenAI
    if API_KEY:
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
except ImportError:
    pass

def stream_chat(messages, tools=None):
    if client is None:
        raise RuntimeError("no configured model: set API_KEY and install the OpenAI SDK")
    calls, usage, last_index = {}, {}, None
    response = client.chat.completions.create(model=MODEL, messages=messages, tools=tools or [], stream=True)
    for chunk in response:
        if getattr(chunk, "usage", None):
            usage = {"prompt_tokens": chunk.usage.prompt_tokens, "completion_tokens": chunk.usage.completion_tokens}
        delta = chunk.choices[0].delta if getattr(chunk, "choices", None) else None
        if not delta:
            continue
        if getattr(delta, "content", None):
            yield {"type":"text", "text":delta.content}
        for piece in getattr(delta, "tool_calls", None) or []:
            index = piece.index if piece.index is not None else last_index
            if index is None: index = len(calls)
            call = calls.setdefault(index, {"id":"","name":"","arguments":""})
            last_index = index
            if piece.id: call["id"] = piece.id
            function = getattr(piece, "function", None)
            if function:
                if function.name: call["name"] = function.name
                if function.arguments: call["arguments"] += function.arguments
    for index in sorted(calls):
        yield {"type":"tool_call", **calls[index]}
    yield {"type":"usage", **usage}

