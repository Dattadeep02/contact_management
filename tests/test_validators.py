import pytest

from validators import (
    validate_name,
    validate_phone,
    validate_email,
    validate_text,
    validate_age,
)


def test_validate_name():
    assert validate_name("Rahul Naik") == "Rahul Naik"


def test_validate_phone():
    assert validate_phone("9876543210") == "9876543210"


def test_validate_email():
    assert validate_email("rahul@gmail.com") == "rahul@gmail.com"


def test_validate_city():
    assert validate_text("Panaji", "City", 100) == "Panaji"


def test_validate_age():
    assert validate_age("25") == 25


def test_invalid_name():
    with pytest.raises(ValueError):
        validate_name("A")


def test_invalid_phone():
    with pytest.raises(ValueError):
        validate_phone("abc123")


def test_invalid_email():
    with pytest.raises(ValueError):
        validate_email("rahul@")


def test_invalid_age():
    with pytest.raises(ValueError):
        validate_age("150")