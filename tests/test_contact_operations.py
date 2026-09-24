import sqlite3

import database
import contact_operations


def setup_test_database(tmp_path, monkeypatch):
    db_file = tmp_path / "test_contacts.db"

    monkeypatch.setattr(database, "DB_PATH", db_file)

    database.create_table()

    return db_file


def insert_sample_contact(db_file):
    connection = sqlite3.connect(db_file)

    connection.execute(
        """
        INSERT INTO contacts
        (
            name,
            contact_number,
            email,
            city,
            state,
            local_language,
            age
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "Rahul Naik",
            "9876543210",
            "rahul@gmail.com",
            "Panaji",
            "Goa",
            "Konkani",
            25,
        ),
    )

    connection.commit()
    connection.close()


def test_add_contact(tmp_path, monkeypatch):
    db_file = setup_test_database(tmp_path, monkeypatch)

    inputs = iter([
        "Rahul Naik",
        "9876543210",
        "rahul@gmail.com",
        "Panaji",
        "Goa",
        "Konkani",
        "25",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    contact_operations.add_contact()

    connection = sqlite3.connect(db_file)

    row = connection.execute(
        "SELECT * FROM contacts WHERE name = ?",
        ("Rahul Naik",)
    ).fetchone()

    connection.close()

    assert row is not None
    assert row[1] == "Rahul Naik"
    assert row[2] == "9876543210"
    assert row[3] == "rahul@gmail.com"


def test_get_contact(tmp_path, monkeypatch):
    db_file = setup_test_database(tmp_path, monkeypatch)

    insert_sample_contact(db_file)

    contact = contact_operations.get_contact(1)

    assert contact is not None
    assert contact["name"] == "Rahul Naik"
    assert contact["city"] == "Panaji"
    assert contact["state"] == "Goa"
    assert contact["age"] == 25


def test_get_nonexistent_contact(tmp_path, monkeypatch):
    setup_test_database(tmp_path, monkeypatch)

    contact = contact_operations.get_contact(999)

    assert contact is None


def test_search_contacts(tmp_path, monkeypatch, capsys):
    db_file = setup_test_database(tmp_path, monkeypatch)

    insert_sample_contact(db_file)

    inputs = iter([
        "Rahul",
        "",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    contact_operations.search_contacts()

    output = capsys.readouterr().out

    assert "Rahul Naik" in output
    assert "9876543210" in output


def test_show_contact(tmp_path, monkeypatch, capsys):
    db_file = setup_test_database(tmp_path, monkeypatch)

    insert_sample_contact(db_file)

    contact_operations.show_contact(1)

    output = capsys.readouterr().out

    assert "Rahul Naik" in output
    assert "9876543210" in output
    assert "rahul@gmail.com" in output
    assert "Panaji" in output
    assert "Goa" in output
    assert "Konkani" in output


def test_show_nonexistent_contact(tmp_path, monkeypatch, capsys):
    setup_test_database(tmp_path, monkeypatch)

    contact_operations.show_contact(999)

    output = capsys.readouterr().out

    assert "Contact not found" in output


def test_update_contact(tmp_path, monkeypatch, capsys):
    db_file = setup_test_database(tmp_path, monkeypatch)

    insert_sample_contact(db_file)

    inputs = iter([
        "1",
        "1",
        "Rahul Shetgaonkar",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    contact_operations.update_contact()

    connection = sqlite3.connect(db_file)

    row = connection.execute(
        "SELECT name FROM contacts WHERE id = 1"
    ).fetchone()

    connection.close()

    assert row[0] == "Rahul Shetgaonkar"


def test_delete_contact(tmp_path, monkeypatch):
    db_file = setup_test_database(tmp_path, monkeypatch)

    insert_sample_contact(db_file)

    inputs = iter([
        "1",
        "y",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    contact_operations.delete_contact()

    connection = sqlite3.connect(db_file)

    row = connection.execute(
        "SELECT * FROM contacts WHERE id = 1"
    ).fetchone()

    connection.close()

    assert row is None


def test_delete_cancelled(tmp_path, monkeypatch):
    db_file = setup_test_database(tmp_path, monkeypatch)

    insert_sample_contact(db_file)

    inputs = iter([
        "1",
        "n",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    contact_operations.delete_contact()

    connection = sqlite3.connect(db_file)

    row = connection.execute(
        "SELECT * FROM contacts WHERE id = 1"
    ).fetchone()

    connection.close()

    assert row is not None


def test_show_all_contacts(tmp_path, monkeypatch, capsys):
    db_file = setup_test_database(tmp_path, monkeypatch)

    insert_sample_contact(db_file)

    contact_operations.show_all_contacts()

    output = capsys.readouterr().out

    assert "Rahul Naik" in output
    assert "Panaji" in output
    assert "Total Contacts: 1" in output