#!/bin/bash
echo "Corriendo tests..."
uv run pytest tests/ -v --cov=app --cov-report=term-missing
