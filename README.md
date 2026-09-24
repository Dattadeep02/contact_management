# Contact Management System — Python, SQLite & Pytest

A terminal-based Contact Management System built with **Python** and **SQLite**.

The application allows you to store, search, view, update, and delete contact information directly from the Ubuntu terminal. It also includes a **pytest test suite** and **pytest-cov code coverage**.

## Features

- Add a new contact
- Search contacts by name, contact number, email, city, state, or local language
- View a complete contact profile
- Update individual contact fields
- Delete contacts with confirmation
- Display all contacts
- SQLite database storage
- Input validation
- Parameterized SQL queries
- Automated tests using pytest
- Code coverage using pytest-cov
- Ubuntu setup and run scripts

## Contact Information Stored

| Field | Description |
|---|---|
| `id` | Unique contact ID |
| `name` | Contact's full name |
| `contact_number` | Phone/contact number |
| `email` | Email address |
| `city` | City |
| `state` | State |
| `local_language` | Local language |
| `age` | Age |
| `created_at` | Record creation timestamp |
| `updated_at` | Last update timestamp |

## Project Structure

```text
contact_management_sqlite/
│
├── main.py
├── database.py
├── contact_operations.py
├── validators.py
├── setup_db.py
│
├── setup.sh
├── run.sh
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    ├── __init__.py
    ├── test_validators.py
    ├── test_database.py
    └── test_contact_operations.py
```

### File Description

- **`main.py`** — Main terminal menu and application flow.
- **`database.py`** — SQLite connection and database/table initialization.
- **`contact_operations.py`** — Add, search, view, update, delete, and list operations.
- **`validators.py`** — Input validation.
- **`setup_db.py`** — Initializes the SQLite database and contacts table.
- **`setup.sh`** — Initial Ubuntu setup.
- **`run.sh`** — Starts the application.
- **`tests/`** — Automated pytest tests.

## Requirements

- Ubuntu/Linux
- Python 3
- Python virtual environment support

SQLite is included with Python, so **MariaDB/MySQL is not required**.

No database server is required.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/contact-management-sqlite.git
cd contact-management-sqlite
```

Make the scripts executable:

```bash
chmod +x setup.sh run.sh
```

Run the setup:

```bash
./setup.sh
```

The setup script checks Python and SQLite, creates a virtual environment, and initializes the database.

## Running the Application

```bash
./run.sh
```

The application displays:

```text
=======================================================
             CONTACT MANAGEMENT SYSTEM
=======================================================

1. Add Contact
2. Search Contact
3. View Contact Profile
4. Update Contact
5. Delete Contact
6. Show All Contacts
7. Exit

Enter your choice:
```

## Database

The application automatically creates:

```text
contacts.db
```

with a table named:

```text
contacts
```

Schema:

```sql
CREATE TABLE contacts (
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
```

The `contacts.db` file is intentionally excluded from Git using `.gitignore` so actual contact records are not uploaded to GitHub.

## Inspecting the SQLite Database

If the SQLite CLI is installed:

```bash
sqlite3 contacts.db
```

List tables:

```sql
.tables
```

View the table structure:

```sql
.schema contacts
```

View all records:

```sql
SELECT * FROM contacts;
```

For a cleaner display:

```sql
.headers on
.mode column
SELECT * FROM contacts;
```

Exit:

```sql
.quit
```

If SQLite CLI is not installed:

```bash
sudo apt update
sudo apt install sqlite3
```

## Testing with Pytest

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install testing packages:

```bash
pip install pytest pytest-cov
```

Run all tests:

```bash
pytest
```

The test suite covers input validation, database initialization, adding contacts, searching, viewing profiles, updating, deleting, and listing contacts.

## Code Coverage

Generate a terminal coverage report:

```bash
pytest \
    --cov=database \
    --cov=validators \
    --cov=contact_operations \
    --cov-report=term-missing
```

Generate an interactive HTML report:

```bash
pytest \
    --cov=database \
    --cov=validators \
    --cov=contact_operations \
    --cov-report=html
```

Then open it:

```bash
firefox htmlcov/index.html
```

The report shows statements, missing lines, and coverage percentage for the application modules.

## Git and GitHub

The `.gitignore` prevents generated and sensitive files from being uploaded.

Examples:

```text
venv/
contacts.db
__pycache__/
.pytest_cache/
htmlcov/
.coverage
.env
```

After making changes:

```bash
git add .
git commit -m "Update contact management system"
git push
```

## SQL Operations Demonstrated

The application demonstrates the four fundamental CRUD database operations.

### INSERT

Used when adding a contact:

```sql
INSERT INTO contacts (...)
VALUES (...);
```

### SELECT

Used when searching and viewing contacts:

```sql
SELECT * FROM contacts
WHERE id = ?;
```

### UPDATE

Used when modifying contact information:

```sql
UPDATE contacts
SET name = ?
WHERE id = ?;
```

### DELETE

Used when removing a contact:

```sql
DELETE FROM contacts
WHERE id = ?;
```

The application uses parameterized SQL queries rather than directly concatenating user input into SQL statements.

## Security and Data Handling

User-provided values are passed to SQLite using parameterized queries, for example:

```python
connection.execute(
    "SELECT * FROM contacts WHERE id = ?",
    (contact_id,)
)
```

The local SQLite database can contain personal contact information, so `contacts.db` should not be committed to a public GitHub repository.

## Future Improvements

Possible extensions include:

- Duplicate contact detection
- Pagination
- Sorting and filtering
- CSV import/export
- Backup and restore
- User authentication
- Contact groups/categories
- Logging
- More extensive test coverage
- GitHub Actions CI/CD
- Web interface using Flask or Django

## License

This project is intended for educational and development purposes.
