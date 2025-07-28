.PHONY: help install lint format test clean

## show this help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "%-15s %s\n", $$1, $$2}'

# install runtime + dev dependencies into local venv
install:
	pip install -e ".[dev]"

## Run all checks (lint, format, test).
all: lint format test

## Run ruff linter
lint:
	ruff check src tests

## Format code with ruff (isort and black replacement).
format:
	ruff format src tests
	ruff check --select I --fix src tests

# Run the unit test suite with coverage
test:
	pytest -q --cov=src --cov-report=term-missing


## Remove caches & bytecode
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache .coverage