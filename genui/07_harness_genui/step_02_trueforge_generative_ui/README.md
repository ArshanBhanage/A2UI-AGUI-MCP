# 07.2 TrueForge generative UI

This lesson uses a real HTTP agent-list check against `TRUEFORGE_URL` (default `http://localhost:8790`). Without a reachable TrueForge runtime it reports `BLOCKED`; it never substitutes a print statement for SDK communication. Run `python3 -m pytest test_client.py` and `python3 demo.py`.
