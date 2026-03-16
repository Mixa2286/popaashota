def student_status(grades):
    # Ошибка: программа не видит двойку, если она не последняя в списке
    for g in grades:
        if g == 2:
            status = "Пересдача"
        else:
            avg = sum(grades) / len(grades)
            if avg >= 4.5:
                status = "Отлично"
            elif avg < 3.5:
                status = "Нужно подтянуться"
            else:
                status = "Хорошо"
    return status


# Тест-кейс: оценки [5, 5, 2]. Ожидаем "Пересдача".
# Тест-кейс: пустой список []. Что произойдет с программой?
print("Статус:", student_status([5, 5, 2]))
print("Статус:", student_status([]))