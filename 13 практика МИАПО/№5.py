list_a = [1, 2, 3]
list_b = [1, 2, 4]

if list_a == list_b:
    print("Значения списков одинаковы")
else:
    print("Значения списков разные")

if list_a is list_b:
    print("Это один и тот же объект")
else:
    print("Это разные объекты в памяти")