#!/usr/bin/env python3

from database import initialize_database


if __name__ == "__main__":
    print("Initializing SQLite database...")

    if initialize_database():
        print("Database and contacts table are ready.")
    else:
        print("Database initialization failed.")
        raise SystemExit(1)
