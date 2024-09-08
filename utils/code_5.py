def filter_by_state(data: list, state="EXECUTED"):
    """Функция, которая фильтрует список словарей по ключу state"""
    # Проверяем, что data является списком и все элементы — словарями
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Некорректные данные")

    return [item for item in data if item.get("state") == state]
