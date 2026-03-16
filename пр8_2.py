def register_client(age, height, weight):
    # Проверяем допустимый возраст (от 14 до 80 лет включительно?)
    if age < 14 or age > 80:
        return "Ошибка: недопустимый возраст"

    # Расчет индекса массы тела
    bmi = weight / (height / 100) ** 2

    # Если BMI >= 30, то щадящий режим
    if bmi >= 30:  # или > 30, в зависимости от требований
        return "Режим: Щадящий"
    else:
        return "Режим: Стандарт"


# Тест-кейсы
print(register_client(age=14, height=180, weight=100))  # Щадящий
print(register_client(age=13, height=170, weight=70))   # Ошибка: недопустимый возраст
print(register_client(age=30, height=170, weight=87))   # BMI=30.1 -> Щадящий