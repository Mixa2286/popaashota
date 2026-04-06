numbers = [1, 2, 4, 3, 6]
for n in numbers[:]:
    if n % 2 == 0:
        numbers.remove(n)

print(numbers)
