def get_mask_account(b: int) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""

    # Проверка на корректность типа данных
    if not isinstance(b, (int, str)):
        raise TypeError("Некорректные данные")

    account_number = str(b)

    # Проверка на корректность данных
    if not account_number.isdigit() or len(account_number) != 20:
        return "Некорректные данные"

    mask_account = "**" + account_number[-4:]
    return mask_account
