"""Incrementally parse a complete JSON value from arbitrary text chunks."""
import json

class IncrementalJSON:
    def __init__(self): self.buffer=""
    def feed(self, chunk):
        self.buffer += chunk
        try: return json.loads(self.buffer)
        except json.JSONDecodeError: return None

