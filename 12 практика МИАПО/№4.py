def get_tax_price(price, is_pensioner):
    return price * 0.95 if is_pensioner else price
print(get_tax_price(10, False))