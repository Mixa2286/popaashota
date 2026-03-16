def calculate_cart(prices):
    total = sum(prices)

    # Ошибка в логике: проверьте порядок условий для скидок
    if total > 5000:
        total = total * 0.9
    elif total > 10000:
        total = total * 0.8

    # Ошибка: бесплатная доставка считается неправильно
    if total < 3000:
        total = total + 500

    return total


# Пример для теста:
# При покупке на 11 000 скидка должна быть 20%, а доставка — 0.
# Совпадет ли итог с вашими расчетами?
print("Итог корзины:", calculate_cart([6000, 5000]))
