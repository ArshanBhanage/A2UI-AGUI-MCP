# 01.1 technical walkthrough

Run `python3 -m pytest test_step.py` to exercise the catalog and server with a deterministic fixture. Then run `node --test tests/render.test.mjs` to verify prop escaping and unknown-component handling. Finally, `python3 demo.py --offline` makes a real request through the FastAPI app and prints the SSE frames. The offline label is deliberate: it proves the application path, not model availability.

