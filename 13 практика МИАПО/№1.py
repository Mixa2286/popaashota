def add_to_cart(item, cart = None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_to_cart("Хлеб",["<UNK>","<UNK>"]))
print(add_to_cart("Молоко"))