def moderator(text):
    # Приводим текст к нижнему регистру для проверки
    text_lower = text.lower()

    # Проверяем наличие спама в любом регистре
    if "спам" in text_lower or "реклама" in text_lower:
        return False

    # Проверяем минимальную длину (предположим, что нужно блокировать <=3)
    if len(text) <= 3:  # или < 3, в зависимости от требований
        return False

    return True


# Тесты
print("Тест 'СПАМ':", moderator("Купите СпАм!"))  # False (обнаружен спам)
print("Тест 'реклама':", moderator("тут РеклаМА"))  # False
print("Тест 'Эй!':", moderator("Эй!"))  # False (если <=3) или True (если <3)
print("Тест 'Привет':", moderator("Привет"))  # True
print("Тест 'Ok':", moderator("Ok"))  # False
