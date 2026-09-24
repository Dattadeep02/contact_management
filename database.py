import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "contacts.db"


def get_connection():
    """Create a connection to the SQLite database."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_table():
    """Create the contacts table if it does not exist."""
    sql = """
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact_number TEXT NOT NULL,
        email TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        local_language TEXT NOT NULL,
        age INTEGER NOT NULL CHECK(age BETWEEN 1 AND 120),
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """

    connection = get_connection()

    try:
        connection.execute(sql)
        connection.commit()
    finally:
        connection.close()


def initialize_database():
    """Initialize the SQLite database and contacts table."""
    try:
        create_table()
        return True
    except sqlite3.Error as exc:
        print(f"Database initialization error: {exc}")
        return False
