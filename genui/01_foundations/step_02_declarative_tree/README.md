# 01.2 Declarative tree

This lesson adds agent-selected layout inside an allowlisted catalog. `catalog.py` validates a nested JSON tree with JSON Schema; `stream.py` accepts partial chunks and exposes a value only once the JSON is complete. The sample is deterministic offline input, not a live model response.

Run `python3 -m pytest test_step.py` and `python3 demo.py`. Unknown component names and malformed props are rejected before rendering. The model controls structure within the catalog; the application controls the available components and props. This is declarative generation, not AG-UI transport.

Source reference: [upstream lesson](https://github.com/dlmastery/simple-coding-harness/tree/main/genui/01_foundations/step_02_declarative_tree).

