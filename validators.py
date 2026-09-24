import re


def prompt_required(label):
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print("This field cannot be empty.")


def prompt_name():
    while True:
        value = prompt_required("Enter Name")

        if len(value) < 2:
            print("Name must contain at least 2 characters.")
            continue

        if len(value) > 100:
            print("Name must not exceed 100 characters.")
            continue

        return value


def prompt_phone():
    pattern = re.compile(r"^\+?[0-9][0-9\s\-()]{6,18}$")

    while True:
        value = prompt_required("Enter Contact Number")

        if not pattern.fullmatch(value):
            print(
                "Enter a valid phone number, "
                "e.g. 9876543210 or +91 9876543210."
            )
            continue

        return value


def prompt_email():
    pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    while True:
        value = prompt_required("Enter Email")

        if not pattern.fullmatch(value):
            print("Enter a valid email address.")
            continue

        if len(value) > 150:
            print("Email must not exceed 150 characters.")
            continue

        return value


def prompt_text(label, max_length=100):
    while True:
        value = prompt_required(label)

        if len(value) > max_length:
            print(f"{label} must not exceed {max_length} characters.")
            continue

        return value


def prompt_age():
    while True:
        value = input("Enter Age: ").strip()

        try:
            age = int(value)
        except ValueError:
            print("Age must be a whole number.")
            continue

        if not 1 <= age <= 120:
            print("Age must be between 1 and 120.")
            continue

        return age


def validate_name(value):
    value = value.strip()

    if len(value) < 2 or len(value) > 100:
        raise ValueError("Name must contain 2-100 characters.")

    return value


def validate_phone(value):
    value = value.strip()

    if not re.fullmatch(r"^\+?[0-9][0-9\s\-()]{6,18}$", value):
        raise ValueError("Invalid phone number.")

    return value


def validate_email(value):
    value = value.strip()

    if not re.fullmatch(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value):
        raise ValueError("Invalid email address.")

    if len(value) > 150:
        raise ValueError("Email must not exceed 150 characters.")

    return value


def validate_text(value, label, max_length=100):
    value = value.strip()

    if not value:
        raise ValueError(f"{label} cannot be empty.")

    if len(value) > max_length:
        raise ValueError(f"{label} must not exceed {max_length} characters.")

    return value


def validate_age(value):
    try:
        age = int(value.strip())
    except ValueError:
        raise ValueError("Age must be a whole number.")

    if not 1 <= age <= 120:
        raise ValueError("Age must be between 1 and 120.")

    return age
