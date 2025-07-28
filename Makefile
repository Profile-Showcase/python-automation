.PHONY: help install lint format test clean

## show this help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "%-15s %s\n", $$1, $$2}'

# install runtime + dev dependencies into local venv
install:
	pip install -e ".[dev]"

## Run ruff linter
lint:
	ruff src tests

## Format code with black + isort.
format:
	isort src tests
	black src tests

# Run the unit test suite with coverage
test:
	pytest -q --cov=src --cov-report=term-missing


## Remove caches & bytecode
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache .coverage