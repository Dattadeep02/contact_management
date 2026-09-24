#!/usr/bin/env python3

from database import initialize_database

from contact_operations import (
    add_contact,
    search_contacts,
    show_contact,
    update_contact,
    delete_contact,
    show_all_contacts,
)


def print_banner():
    print("\n" + "=" * 55)
    print("             CONTACT MANAGEMENT SYSTEM")
    print("=" * 55)


def print_menu():
    print("""
1. Add Contact
2. Search Contact
3. View Contact Profile
4. Update Contact
5. Delete Contact
6. Show All Contacts
7. Exit
""")


def main():
    print_banner()

    print("Checking SQLite database...")

    if not initialize_database():
        print("\nCould not initialize the database.")
        return

    print("Database connection OK.")
    print("Database file: contacts.db")

    while True:
        print_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            search_contacts()

        elif choice == "3":
            show_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            show_all_contacts()

        elif choice == "7":
            print("\nThank you. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
