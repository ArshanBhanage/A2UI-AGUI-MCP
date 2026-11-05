# 01.3 Open-ended HTML

This lesson demonstrates the open-ended generation mode: an HTML artifact is bounded and mounted only in an iframe with `sandbox="allow-scripts"`, a restrictive CSP, no host-DOM access, and a size limit. The sample is deterministic offline input; a real model provider is not configured here.

Run `python3 -m pytest test_step.py` and `python3 demo.py`. The artifact wrapper blocks refresh metadata and exposes the iframe boundary explicitly. Open-ended generation is not native to AG-UI or A2UI; those protocols can carry a pointer or adapter result, but the sandbox remains an application security decision.

