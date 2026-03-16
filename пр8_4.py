def student_status(grades):
    # Проверка на пустой список
    if not grades:
        return "Нет оценок"

    # Сначала проверяем наличие двоек
    if 2 in grades:
        return "Пересдача"

    # Если двоек нет, вычисляем среднее
    avg = sum(grades) / len(grades)

    # Определяем статус по среднему баллу
    if avg >= 4.5:
        return "Отлично"
    elif avg < 3.5:
        return "Нужно подтянуться"
    else:
        return "Хорошо"


# Тесты
print("Статус:", student_status([5, 5, 2]))  # Пересдача
print("Статус:", student_status([5, 5, 5]))  # Отлично
print("Статус:", student_status([3, 4, 3]))  # Нужно подтянуться (avg=3.33)
print("Статус:", student_status([]))  # Нет оценок