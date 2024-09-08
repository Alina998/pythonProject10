import pytest
from utils.code import get_mask_card_number

@pytest.fixture
def valid_card_numbers():
    """Фикстура с валидными номерами карт для тестирования"""
    return [
        (1234567812345678, "1234 56** **** 5678"),
        (4000123412345678, "4000 12** **** 5678"),
        (5555555555554444, "5555 55** **** 4444"),
    ]

@pytest.fixture
def invalid_card_numbers():
    """Фикстура с невалидными номерами карт"""
    return [
        -1234567812345678,
        123456,
        123456789012345678901234567890,
        "abcd1234",
        "1234abcd5678",
        "",
    ]

@pytest.mark.parametrize("card_number, expected_mask", [
    (1234567812345678, "1234 56** **** 5678"),
    (4000123412345678, "4000 12** **** 5678"),
    (5555555555554444, "5555 55** **** 4444"),
])
def test_get_mask_card_number_valid(card_number, expected_mask):
    """Тестирование валидных номеров карт"""
    assert get_mask_card_number(card_number) == expected_mask

@pytest.mark.parametrize("card_number", [
    -1234567812345678,
    123456,
    123456789012345678901234567890,
    "abcd1234",
    "1234abcd5678",
    "",
    None
])
def test_get_mask_card_number_invalid(card_number):
    """Тестирование невалидных номеров карт"""
    with pytest.raises(TypeError):
        get_mask_card_number([])
