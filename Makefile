init:
	    pip install -r requirements.txt

test:
	    python3 -m pytest

clean:
			rm -rf .pytest_cache
			rm -rf generic_validation/__pycache__

.PHONY: test
