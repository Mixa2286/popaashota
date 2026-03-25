def calculate_total_with_tax_and_fee(amount):

    tax = 0.20  # 20% — ставка налога
    fee = 50  # 50 руб. — фиксированная комиссия

    # Расчеты
    tax_amount = amount * tax
    total = amount + tax_amount + fee

    return total


def print_calculation_result(amount):
#    Выводит результат расчета в удобочитаемом формате
    total = calculate_total_with_tax_and_fee(amount)
    print("Итог:", total)


# Использование
if __name__ == "__main__":
    print_calculation_result(1000)


