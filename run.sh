#!/usr/bin/env bash
set -e

if [ ! -d "venv" ]; then
    echo "Virtual environment not found."
    echo "Run ./setup.sh first."
    exit 1
fi

source venv/bin/activate
python3 main.py
