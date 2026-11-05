.PHONY: test lesson-01-1 docs-check verify

test:
	python3 -m pytest genui/01_foundations/step_01_static_components/test_step.py

lesson-01-1:
	python3 genui/01_foundations/step_01_static_components/demo.py --offline

docs-check:
	python3 scripts/check_docs.py

verify: test docs-check

