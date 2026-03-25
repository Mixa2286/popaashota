def get_squares(numbers, result=None):
    if result is None:
        result = []
    for n in numbers:
        result.append(n * n)
    return result


print(get_squares([1, 4]))  # [1, 4]
print(get_squares([3, 4]))  # [9, 16]