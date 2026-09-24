#!/usr/bin/env bash
set -e

echo "=============================================="
echo " Contact Management System - SQLite Setup"
echo "=============================================="
echo

if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 is not installed."
    echo
    echo "Install it with:"
    echo "  sudo apt update"
    echo "  sudo apt install python3 python3-venv"
    exit 1
fi

echo "[1/3] Checking Python SQLite support..."

python3 - <<'PY'
import sqlite3
print("SQLite version:", sqlite3.sqlite_version)
print("Python SQLite module: OK")
PY

echo
echo "[2/3] Creating Python virtual environment..."

if [ ! -d "venv" ]; then
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

echo
echo "[3/3] Initializing database..."

source venv/bin/activate
python3 setup_db.py

echo
echo "=============================================="
echo " Setup completed successfully!"
echo "=============================================="
echo
echo "Start the program with:"
echo "  ./run.sh"
echo
