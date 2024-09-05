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
    """Фикстура с невалидными номерами карт для тестирования"""
    return [
        -1234567812345678,
        123456,
        123456789012345678901234567890,
        "abcd1234",
        ]

@pytest.mark.parametrize("card_number, expected_mask", [
    (1234567812345678, "1234 56** **** 5678"),
    (4000123412345678, "4000 12** **** 5678"),
    (5555555555554444, "5555 55** **** 4444"),
])
def test_valid_card_numbers(valid_card_numbers, card_number, expected_mask):
    assert get_mask_card_number(card_number) == expected_mask

@pytest.mark.parametrize("card_number", [
    -1234567812345678,
    123456,
    123456789012345678901234567890,
    "abcd1234",
])
def test_invalid_card_numbers(card_number):
    assert get_mask_card_number(card_number) == 'Некорректные данные'