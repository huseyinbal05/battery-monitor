#!/bin/bash
cd "$(dirname "$0")"
echo "Starting Battery Monitor..."
uv run src/app.py
