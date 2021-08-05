init:
	    pip install -r requirements.txt

test:
	    python3 -m pytest

clean:
			rm -rf .pytest_cache
			rm -rf generic_validation/__pycache__
			rm -rf dist/*

build:
			pip install --upgrade build
			python3 -m build

publish:
			pip install --upgrade twine
			python3 -m twine upload --repository testpypi dist/*

.PHONY: test
