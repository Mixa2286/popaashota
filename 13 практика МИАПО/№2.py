actions = []
for i in range(10):
    def say_number(num = i):
        print(num)
    actions.append(say_number)

for act in actions:
    act()
