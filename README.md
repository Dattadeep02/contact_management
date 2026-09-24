# Contact Management System — SQLite

A terminal-based contact management system using Python and SQLite.

No MariaDB, MySQL, server, or password is required.

## Requirements

- Ubuntu/Linux
- Python 3

SQLite is normally included with Python, so there is no database server to install.

## Run

From the extracted project directory:

```bash
cd ~/Desktop/contact_management_sqlite
chmod +x setup.sh run.sh
./setup.sh
```

Then:

```bash
./run.sh
```

## What the application does

1. Add Contact
2. Search Contact
3. View Contact Profile
4. Update Contact
5. Delete Contact
6. Show All Contacts
7. Exit

The application automatically creates:

```text
contacts.db
```

with a table named:

```text
contacts
```

## Database schema

```text
contacts
├── id
├── name
├── contact_number
├── email
├── city
├── state
├── local_language
├── age
├── created_at
└── updated_at
```

## SQL operations

The program demonstrates:

- INSERT
- SELECT
- UPDATE
- DELETE

## Inspect the database manually

SQLite CLI is optional. If installed:

```bash
sqlite3 contacts.db
```

Then:

```sql
.tables
.schema contacts
SELECT * FROM contacts;
.quit
```

The Python application itself does not require the `sqlite3` command-line program.
