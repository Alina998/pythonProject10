import pytest
from utils.code_4 import get_date

@pytest.fixture
def valid_dates():
    """Фикстура с валидными датами для тестирования."""
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2000-01-01T00:00:00", "01.01.2000"),
        ("1999-07-07T15:45:30", "07.07.1999"),
    ]

@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ("2000-01-01T00:00:00", "01.01.2000"),
    ("1999-07-07T15:45:30", "07.07.1999"),
])
def test_get_date_valid(valid_dates, date_str, expected):
    """Тестирование валидных входных данных"""
    assert get_date(date_str) == expected

# Тест невалидных дат
@pytest.mark.parametrize("date_str", [
    "Invalid Date",
    "2023-02-30T12:00:00",
    "2024-13-01T00:00:00"
])
def test_get_date_invalid(date_str):
    """Тестирование невалидных входных данных"""
    with pytest.raises(ValueError):
        get_date(date_str)
