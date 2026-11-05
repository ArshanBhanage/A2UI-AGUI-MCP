.PHONY: test lesson-01-1 docs-check verify

test:
	@set -e; for test_file in $$(find genui -name 'test_*.py' -type f | sort); do PYTHONPATH="$$(dirname "$$test_file")" python3 -m pytest "$$test_file" -q; done

lesson-01-1:
	python3 genui/01_foundations/step_01_static_components/demo.py --offline

docs-check:
	python3 scripts/check_docs.py

verify: test docs-check

