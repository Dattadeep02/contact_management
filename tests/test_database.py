import sqlite3

import database


def test_database_connection(tmp_path, monkeypatch):
    db_file = tmp_path / "test_contacts.db"

    monkeypatch.setattr(database, "DB_PATH", db_file)

    connection = database.get_connection()

    assert connection is not None

    connection.close()


def test_create_table(tmp_path, monkeypatch):
    db_file = tmp_path / "test_contacts.db"

    monkeypatch.setattr(database, "DB_PATH", db_file)

    assert database.create_table() is None

    connection = sqlite3.connect(db_file)

    result = connection.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='contacts'
        """
    ).fetchone()

    connection.close()

    assert result is not None
    assert result[0] == "contacts"