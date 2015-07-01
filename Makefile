# A super simple and dumb Makefile.
# Only exists to make it easy for me to clean up and run tests.

all: test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -exec rm -f {} \;

test:
	python -m py.test
