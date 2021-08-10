
.PHONY: clean
clean:
			rm -rf .pytest_cache
			rm -rf src/generic_validation/__pycache__
			rm -rf dist/*
			rm -rf src/*.egg-info

build:
			pip install --upgrade build
			python3 -m build

site:
			portray as_html

init:
	    pip install -r requirements.txt

lint:
			pylint -f colorized src/generic_validation

publish-test:
			pip install --upgrade twine
			python3 -m twine upload --repository testpypi dist/*

publish:
			pip install --upgrade twine
			python3 -m twine upload --repository pypi dist/*

test:
		  cd src && python3 -m pytest -rP ../tests
