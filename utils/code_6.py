from datetime import datetime


def sort_by_date(data: list, descending=True):
    """Функция, которая сортирует список по дате (по умолчанию — по убыванию)"""
    # Проверяем, что data является списком
    if not isinstance(data, list):
        raise ValueError("Некорректные данные")

    for item in data:
        # Проверяем, что каждый элемент является словарем и содержит ключ "date"
        if not isinstance(item, dict) or "date" not in item:
            raise ValueError("Некорректные данные")

        # Проверяем, что значение "date" корректно
        try:
            datetime.fromisoformat(item["date"])
        except ValueError:
            raise ValueError("Некорректные данные")

    return sorted(
        data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending
    )
