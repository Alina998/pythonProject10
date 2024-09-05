def get_mask_card_number(a: int) -> str:
    """Функция принимает на вход номер карты и возвращает маску номера"""

    # Проверка на корректность типа данных
    if not isinstance(a, (int, str)):
        raise TypeError('Некорректные данные')

    number_in_str = str(a)

    # Проверка на корректность данных
    if number_in_str.isdigit() == False or len(number_in_str) != 16:
        return "Некорректные данные"


    mask_card_number = (
            number_in_str[:6] + (len(number_in_str[6:-4]) * "*") + number_in_str[-4:]
    )

    parts_of_number, parts_size = len(mask_card_number), len(mask_card_number) // 4
    return " ".join(
        [
            mask_card_number[i: i + parts_size]
            for i in range(0, parts_of_number, parts_size)
        ]
    )
