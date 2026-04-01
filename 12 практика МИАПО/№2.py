def has_negative_transaction(transactions):
    return any(t < 0 for t in transactions)
print(has_negative_transaction([10,5,-2]))