def get_discount(status):
    if status == "Gold":
        discount = 20
    elif status == "Silver":
        discount = 10
    elif status == "Bronze":
        discount = 5
    else:
        discount = 0

    print(f"Статус: {status}, Скидка: {discount}%")
    return discount


# Вызов функции
get_discount("Gold")