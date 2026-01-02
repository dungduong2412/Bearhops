# Makefile for Bearhops

.PHONY: help install test lint format run clean

help:
	@echo "Bearhops - AI Chatbot"
	@echo ""
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linters"
	@echo "  make format     - Format code"
	@echo "  make run        - Run the application"
	@echo "  make clean      - Clean up generated files"

install:
	pip install -r requirements.txt

test:
	pytest --cov=src/bearhops --cov-report=term-missing

lint:
	ruff check src/ tests/
	mypy src/

format:
	black src/ tests/
	ruff check --fix src/ tests/

run:
	python -m src.bearhops.main

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov .mypy_cache .ruff_cache
