# 01.1 demo record

Command: `python3 demo.py --offline`

Observed 2026-11-04:

```text
mode: OFFLINE FIXTURE (not a live agent run)
3 SSE messages:
  {"component": "Metric", "props": {"title": "Open issues", "value": "12", "delta": "-2"}}
  {"component": "Chart", "props": {"kind": "bar", "labels": ["Mon", "Tue"], "values": [8, 12]}}
  {"done": true, "prompt_tokens": 0, "completion_tokens": 0}
```

This is deterministic offline evidence, not proof of provider availability.

Complete demo video: `recordings/demo-lesson-01-1-static-components.mp4` (34.04 seconds). The shorter walkthrough capture is separate: `recordings/lesson-01-1-static-components.mp4`.

