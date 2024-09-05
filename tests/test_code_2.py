import pytest

from utils.code_2 import get_mask_account


@pytest.fixture
def valid_account_numbers():
    """Фикстура с валидными номерами счетов для тестирования"""
    return [
        (12345678901234567890, "**7890"),
        (98765432101234567890, "**7890"),
        (11112222333344445555, "**5555"),
    ]


@pytest.fixture
def invalid_account_numbers():
    """Фикстура с невалидными номерами счетов для тестирования"""
    return [
        -12345678901234567890,
        1234567890123456789,
        123456789012345678901234567890,
        "abcdefg1234567890",
        "1234567890123456789",
    ]


@pytest.mark.parametrize("account_number, expected_mask", [
    (12345678901234567890, "**7890"),
    (98765432101234567890, "**7890"),
    (11112222333344445555, "**5555"),
])
def test_valid_account_numbers(valid_account_numbers, account_number, expected_mask):
    assert get_mask_account(account_number) == expected_mask


@pytest.mark.parametrize("account_number", [
    -12345678901234567890,
    1234567890123456789,
    123456789012345678901234567890,
    "abcdefg1234567890",
    "1234567890123456789",
])
def test_invalid_account_numbers(account_number):
    assert get_mask_account(account_number) == "Некорректные данные"
