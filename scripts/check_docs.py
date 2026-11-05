"""Small contract check for the currently implemented lesson."""
from pathlib import Path

ROOT = Path(__file__).parents[1]
lesson = ROOT / "genui/01_foundations/step_01_static_components"
required = ["README.md", "WALKTHROUGH.md", "DEMO.md", "catalog.py", "server.py", "test_step.py"]
missing = [name for name in required if not (lesson / name).exists()]
if missing:
    raise SystemExit("missing lesson files: " + ", ".join(missing))
if (ROOT / ".env").as_posix() in {p.as_posix() for p in (ROOT / ".git").glob("**/*") if p.is_file()}:
    raise SystemExit(".env must not be tracked")
print("docs-check: implemented lesson 01.1 contract present; remaining lessons are not yet implemented")
