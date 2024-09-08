import pytest
from utils.code_2 import get_mask_account

@pytest.fixture
def valid_account_numbers():
    """Фикстура с валидными номерами счетов"""
    return [
        (12345678901234567890, "**7890"),
        (98765432101234567890, "**7890"),
        (11112222333344445555, "**5555"),]

@pytest.fixture
def invalid_account_numbers():
    """Фикстура с невалидными номерами счетов"""
    return [
        -12345678901234567890,
        1234567890123456789,
        123456789012345678901234567890,
        "abcdefg1234567890",
        "1234567890123456789",
        '',
        None]

@pytest.mark.parametrize("account_number, expected_mask", [
    (12345678901234567890, "**7890"),
    (98765432101234567890, "**7890"),
    (11112222333344445555, "**5555")])
def test_get_mask_account_valid(account_number, expected_mask):
    """Тестирование валидных номеров счетов"""
    result = get_mask_account(account_number)
    assert result == expected_mask

@pytest.mark.parametrize("account_number", [
    -12345678901234567890,
    1234567890123456789,
    123456789012345678901234567890,
    "abcdefg1234567890",
    "1234567890123456789",
    '',
    None])
def test_get_mask_account_invalid(account_number):
    """Тестирование невалидных номеров счетов"""
    with pytest.raises(TypeError):
        get_mask_account({})
