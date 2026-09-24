import sqlite3

from database import get_connection

from validators import (
    prompt_name,
    prompt_phone,
    prompt_email,
    prompt_text,
    prompt_age,
    validate_name,
    validate_phone,
    validate_email,
    validate_text,
    validate_age,
)


def add_contact():
    print("\n" + "=" * 50)
    print("                ADD CONTACT")
    print("=" * 50)

    name = prompt_name()
    phone = prompt_phone()
    email = prompt_email()
    city = prompt_text("Enter City", 100)
    state = prompt_text("Enter State", 100)
    language = prompt_text("Enter Local Language", 50)
    age = prompt_age()

    sql = """
        INSERT INTO contacts
        (name, contact_number, email, city, state, local_language, age)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    connection = get_connection()

    try:
        cursor = connection.execute(
            sql,
            (name, phone, email, city, state, language, age)
        )

        connection.commit()

        print(
            f"\nContact added successfully! "
            f"Contact ID: {cursor.lastrowid}"
        )

    except sqlite3.Error as exc:
        connection.rollback()
        print(f"\nCould not add contact: {exc}")

    finally:
        connection.close()


def search_contacts():
    print("\n" + "=" * 50)
    print("              SEARCH CONTACTS")
    print("=" * 50)

    query = input("Enter search term: ").strip()

    if not query:
        print("Search term cannot be empty.")
        return

    sql = """
        SELECT id, name, contact_number, email, city, state
        FROM contacts
        WHERE name LIKE ?
           OR contact_number LIKE ?
           OR email LIKE ?
           OR city LIKE ?
           OR state LIKE ?
           OR local_language LIKE ?
        ORDER BY name
    """

    pattern = f"%{query}%"
    params = (pattern,) * 6

    connection = get_connection()

    try:
        rows = connection.execute(sql, params).fetchall()

        if not rows:
            print("\nNo contacts found.")
            return

        print(f"\n{len(rows)} contact(s) found:\n")

        print("-" * 95)
        print(
            f"{'ID':<5}"
            f"{'NAME':<25}"
            f"{'PHONE':<18}"
            f"{'CITY':<18}"
            f"{'STATE':<20}"
        )
        print("-" * 95)

        for row in rows:
            print(
                f"{row['id']:<5}"
                f"{row['name'][:24]:<25}"
                f"{row['contact_number'][:17]:<18}"
                f"{row['city'][:17]:<18}"
                f"{row['state'][:19]:<20}"
            )

        print("-" * 95)

        contact_id = input(
            "\nEnter Contact ID to view profile, "
            "or press Enter to return: "
        ).strip()

        if contact_id:
            try:
                show_contact(int(contact_id))
            except ValueError:
                print("Invalid Contact ID.")

    except sqlite3.Error as exc:
        print(f"\nSearch error: {exc}")

    finally:
        connection.close()


def get_contact(contact_id):
    sql = """
        SELECT
            id,
            name,
            contact_number,
            email,
            city,
            state,
            local_language,
            age,
            created_at,
            updated_at
        FROM contacts
        WHERE id = ?
    """

    connection = get_connection()

    try:
        return connection.execute(sql, (contact_id,)).fetchone()

    except sqlite3.Error as exc:
        print(f"\nDatabase error: {exc}")
        return None

    finally:
        connection.close()


def show_contact(contact_id=None):
    if contact_id is None:
        raw_id = input("Enter Contact ID: ").strip()

        try:
            contact_id = int(raw_id)
        except ValueError:
            print("Invalid Contact ID.")
            return

    contact = get_contact(contact_id)

    if not contact:
        print("\nContact not found.")
        return

    print("\n" + "=" * 50)
    print("                CONTACT PROFILE")
    print("=" * 50)

    print(f"Contact ID      : {contact['id']}")
    print(f"Name            : {contact['name']}")
    print(f"Contact Number  : {contact['contact_number']}")
    print(f"Email           : {contact['email']}")
    print(f"City            : {contact['city']}")
    print(f"State           : {contact['state']}")
    print(f"Local Language  : {contact['local_language']}")
    print(f"Age             : {contact['age']}")
    print(f"Created At      : {contact['created_at']}")
    print(f"Updated At      : {contact['updated_at']}")

    print("=" * 50)


def update_contact():
    print("\n" + "=" * 50)
    print("              UPDATE CONTACT")
    print("=" * 50)

    raw_id = input("Enter Contact ID: ").strip()

    try:
        contact_id = int(raw_id)
    except ValueError:
        print("Invalid Contact ID.")
        return

    contact = get_contact(contact_id)

    if not contact:
        print("Contact not found.")
        return

    print("\nCurrent Details:")
    print(f"Name            : {contact['name']}")
    print(f"Contact Number  : {contact['contact_number']}")
    print(f"Email           : {contact['email']}")
    print(f"City            : {contact['city']}")
    print(f"State           : {contact['state']}")
    print(f"Local Language  : {contact['local_language']}")
    print(f"Age             : {contact['age']}")

    print("\nWhich field do you want to update?")

    fields = {
        "1": ("name", "Name", validate_name),
        "2": ("contact_number", "Contact Number", validate_phone),
        "3": ("email", "Email", validate_email),
        "4": ("city", "City", lambda x: validate_text(x, "City", 100)),
        "5": ("state", "State", lambda x: validate_text(x, "State", 100)),
        "6": (
            "local_language",
            "Local Language",
            lambda x: validate_text(x, "Local Language", 50),
        ),
        "7": ("age", "Age", validate_age),
    }

    print("""
1. Name
2. Contact Number
3. Email
4. City
5. State
6. Local Language
7. Age
8. Cancel
""")

    choice = input("Enter choice: ").strip()

    if choice == "8":
        print("Update cancelled.")
        return

    if choice not in fields:
        print("Invalid choice.")
        return

    field, label, validator = fields[choice]

    value = input(
        f"Enter new {label} [{contact[field]}]: "
    ).strip()

    if not value:
        print("No changes made.")
        return

    try:
        value = validator(value)
    except ValueError as exc:
        print(exc)
        return

    # field comes only from the hard-coded fields dictionary above.
    sql = f"UPDATE contacts SET {field} = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?"

    connection = get_connection()

    try:
        cursor = connection.execute(sql, (value, contact_id))
        connection.commit()

        if cursor.rowcount:
            print("\nContact updated successfully.")
        else:
            print("\nNo changes were made.")

    except sqlite3.Error as exc:
        connection.rollback()
        print(f"\nUpdate error: {exc}")

    finally:
        connection.close()


def delete_contact():
    print("\n" + "=" * 50)
    print("              DELETE CONTACT")
    print("=" * 50)

    raw_id = input("Enter Contact ID: ").strip()

    try:
        contact_id = int(raw_id)
    except ValueError:
        print("Invalid Contact ID.")
        return

    contact = get_contact(contact_id)

    if not contact:
        print("Contact not found.")
        return

    print(f"\nName  : {contact['name']}")
    print(f"Phone : {contact['contact_number']}")

    confirmation = input(
        "\nAre you sure you want to permanently delete "
        "this contact? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("Delete cancelled.")
        return

    connection = get_connection()

    try:
        cursor = connection.execute(
            "DELETE FROM contacts WHERE id = ?",
            (contact_id,)
        )

        connection.commit()

        if cursor.rowcount:
            print("\nContact deleted successfully.")
        else:
            print("\nContact not found.")

    except sqlite3.Error as exc:
        connection.rollback()
        print(f"\nDelete error: {exc}")

    finally:
        connection.close()


def show_all_contacts():
    sql = """
        SELECT id, name, contact_number, email, city, state
        FROM contacts
        ORDER BY id
    """

    connection = get_connection()

    try:
        rows = connection.execute(sql).fetchall()

        if not rows:
            print("\nNo contacts in the database.")
            return

        print("\n" + "=" * 100)
        print("                         ALL CONTACTS")
        print("=" * 100)

        print(
            f"{'ID':<5}"
            f"{'NAME':<25}"
            f"{'PHONE':<18}"
            f"{'CITY':<18}"
            f"{'STATE':<25}"
        )

        print("-" * 100)

        for row in rows:
            print(
                f"{row['id']:<5}"
                f"{row['name'][:24]:<25}"
                f"{row['contact_number'][:17]:<18}"
                f"{row['city'][:17]:<18}"
                f"{row['state'][:24]:<25}"
            )

        print("-" * 100)
        print(f"Total Contacts: {len(rows)}")

    except sqlite3.Error as exc:
        print(f"\nDatabase error: {exc}")

    finally:
        connection.close()
