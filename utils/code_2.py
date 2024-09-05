def get_mask_account(b: int) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""
    account_number = str(b)

    # Проверка на корректность типа данных
    if not isinstance(b, (int, str)):
        raise TypeError("Некорректные данные")

    number_in_str = str(b)

    # Проверка на корректность данных
    if number_in_str.isdigit() == False or len(number_in_str) != 20:
        return "Некорректные данные"

    mask_account = "**" + account_number[-4:]
    return mask_account
