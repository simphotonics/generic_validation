init:
	    pip install -r requirements.txt

test:
		  cd src && python3 -m pytest ../tests

clean:
			rm -rf .pytest_cache
			rm -rf src/generic_validation/__pycache__
			rm -rf dist/*
			rm -rf src/generic_validation/*.egg-info

build:
			pip install --upgrade build
			python3 -m build

lint:
			pylint -f colorized src/generic_validation

publish:
			pip install --upgrade twine
			python3 -m twine upload --repository testpypi dist/*

.PHONY: test
