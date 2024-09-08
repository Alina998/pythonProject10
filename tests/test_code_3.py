import pytest

from utils.code_3 import mask_account_card


@pytest.fixture
def valid_card_info():
    """Фикстура с валидными данными для карт"""
    return [
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
        ("Mastercard 4000123412345678", "Mastercard 4000 12** **** 5678"),
        ("Maestro 5555555555554444", "Maestro 5555 55** **** 4444"),
        ("Счет 12345678901234567890", "**7890"),
    ]


@pytest.fixture
def invalid_card_info():
    """Фикстура с невалидными данными для карт"""
    return [
        "Visa abcdefghijklmnop",
        "Mastercard 123",
        "Счет 123456789012345678901234567890",
        "Тип 1234567890123456789",
    ]


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
        ("Mastercard 4000123412345678", "Mastercard 4000 12** **** 5678"),
        ("Maestro 5555555555554444", "Maestro 5555 55** **** 4444"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_mask_account_card_valid(valid_card_info, info, expected):
    """Тестирование валидных входных данных"""
    assert mask_account_card(info) == expected


@pytest.mark.parametrize(
    "info",
    [
        "Visa abcdefghijklmnop",
        "Mastercard 123",
        "Счет 123456789012345678901234567890",
        "Тип 1234567890123456789",
    ],
)
def test_mask_account_card_invalid(info):
    """Тестирование невалидных входных данных"""
    with pytest.raises(ValueError):
        mask_account_card(info)
