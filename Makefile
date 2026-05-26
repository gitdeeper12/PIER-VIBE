
PIER-VIBE Makefile

Predictive Intelligence Engine for Resonance, Vibration, and Integrity in Bridge Environments

.PHONY: help install install-dev test test-cov lint format clean build deploy docker-run docker-build docs

PACKAGE = pier_vibe
PYTEST = pytest
PYTHON = python

help:
@echo "PIER-VIBE Makefile Commands:"
@echo "  make install      - Install production dependencies"
@echo "  make install-dev  - Install development dependencies"
@echo "  make test         - Run unit tests"
@echo "  make test-cov     - Run tests with coverage"
@echo "  make lint         - Run linters"
@echo "  make format       - Format code"
@echo "  make clean        - Remove build artifacts"
@echo "  make build        - Build PyPI package"
@echo "  make deploy       - Upload to PyPI (requires tag)"
@echo "  make docker-build - Build Docker image"
@echo "  make docker-run   - Run Docker container"
@echo "  make docs         - Build documentation"

install:
pip install -r requirements.txt
pip install -e .

install-dev:
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
pre-commit install

test:
python -m unittest discover tests -v

test-cov:
pytest tests/ -v --cov=$(PACKAGE) --cov-report=term --cov-report=html

lint:
flake8 $(PACKAGE)/ tests/
	mypy $(PACKAGE)/ --ignore-missing-imports

format:
black $(PACKAGE)/ tests/ examples/
	isort $(PACKAGE)/ tests/ examples/

clean:
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/
rm -rf .pytest_cache/
rm -rf .coverage
rm -rf htmlcov/
rm -rf pycache/
rm -rf */pycache/

build: clean
python -m build

deploy: build
twine upload dist/*

docker-build:
docker build -t pier-vibe:latest .

docker-run:
docker run -it --rm -p 8501:8501 pier-vibe:latest

docs:
cd docs && make html

run-dashboard:
streamlit run examples/streamlit_live.py

run-example:
python -c "from pier_vibe import BridgeGovernor; print('PIER-VIBE ready')"
