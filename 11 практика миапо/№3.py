def filter_positive_numbers(numbers):
    return [n for n in numbers if n > 0]
print(filter_positive_numbers([1, 2, 3, 4, -5]))