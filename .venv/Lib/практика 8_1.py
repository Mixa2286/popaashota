def calculate_cart(prices):
    total = sum(prices)

    # сначала пишем большую скидку
    if total > 10000:
        total = total * 0.8
    elif total > 5000:
        total = total * 0.9

    # доставка платная, если сумма заказа выше 3000 рублей
    if total > 3000:
        total = total
    else:
        total = total + 500

    return total


# Пример для теста:
# При покупке на 11 000 скидка должна быть 20%, а доставка — 0.
# Совпадет ли итог с вашими расчетами? (да) ответ должен быть 8800
print("Итог корзины:", calculate_cart([6000, 5000]))
