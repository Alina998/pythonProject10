from utils.code import get_mask_card_number
from utils.code_2 import get_mask_account


def mask_account_card(info: str) -> str:
    """Функция принимает на вход строку с типом карта/счет и номером, и возвращает строку с замаскированным номером"""
    parts = info.split()
    type_info = ""
    number = ""

    for part in parts:
        if part.isalpha():
            type_info += part + " "  # Получаем тип (Visa/Maestro/Mastercard/Счет)
        elif part.isdigit():
            number = part  # Получаем номер карты/счета

    type_info = type_info.strip()

    # Проверяем тип карты и применяем соответствующую функцию маскирования
    if any(t in type_info.lower() for t in ["visa", "maestro", "mastercard"]):
        if len(number) != 16:  # Примерные допустимые длины номера карты
            raise ValueError("Некорректные данные")
        result = f"{type_info} {get_mask_card_number(int(number))}"
    elif type_info.lower() == "счет":
        if len(number) != 20:  # Примерные допустимые длины номера счета
            raise ValueError("Некорректные данные")
        result = f"{type_info} {get_mask_account(int(number))}"
    else:
        raise ValueError("Неизвестный тип карты или счета.")

    return result
