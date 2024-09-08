import pytest
from datetime import datetime
from utils.code_6 import sort_by_date


@pytest.fixture
def valid_data():
    """Фикстура с валидными данными для сортировки"""
    return [
        {"id": 1, "date": "2024-03-11T02:26:18"},
        {"id": 2, "date": "2023-12-31T23:59:59"},
        {"id": 3, "date": "2000-01-01T00:00:00"},
        {"id": 4, "date": "1999-07-07T15:45:30"}]

@pytest.mark.parametrize("descending, expected_ids", [
    (True, [1, 2, 3, 4]),
    (False, [4, 3, 2, 1])])

def test_sort_by_date(valid_data, descending, expected_ids):
    """Тестирование функции сортировки по дате"""
    sorted_data = sort_by_date(valid_data, descending)
    assert [item["id"] for item in sorted_data] == expected_ids

# Параметризованный тест для невалидных данных
@pytest.mark.parametrize("data", [
    "Invalid Data",
    123,
    [{"date": "2024-03-11T02:26:18"}, "Invalid Item"],
    [{"id": 1}],
    [{"date": "Invalid Date"}],
    [{}, {"date": "2024-03-11T02:26:18"}]])

def test_sort_by_date_invalid(data):
    """Тестирование невалидных входных данных"""
    with pytest.raises(ValueError, match="Некорректные данные"):
        sort_by_date(data)
