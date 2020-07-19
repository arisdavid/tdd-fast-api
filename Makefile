dev-configure:
	pip3 install -r src/requirements-dev.txt
	pre-commit install

test:
	coverage run --source=src -m pytest -v --tb=line src/tests/
	coverage report