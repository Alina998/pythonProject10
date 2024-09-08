import pytest
from utils.code_5 import filter_by_state

@pytest.fixture
def valid_data():
    """Фикстура с валидными данными"""
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "PENDING"},
    ]

@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]),
    ("CANCELED", [{"id": 2, "state": "CANCELED"}]),
    ("PENDING", [{'id': 4, 'state': 'PENDING'}]),
])
def test_filter_by_state_valid(valid_data, state, expected):
    """Тестирование валидных входных данных"""
    assert filter_by_state(valid_data, state) == expected

# Тест для невалидных данных
@pytest.mark.parametrize("data", [
    "Invalid Data",  # Не список
    123,            # Не список
    [{"state": "EXECUTED"}, "Invalid Item"],  # Смешанный тип (словарь и строка)
    [1, 2, 3],      # Список не словарей
])
def test_filter_by_state_invalid(data):
    """Тестирование невалидных входных данных"""
    with pytest.raises(ValueError, match="Некорректные данные"):
        filter_by_state(data)
