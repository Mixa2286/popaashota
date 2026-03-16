z = "?*^$№@_ "

login = input("Введите логин: ")

found = sorted(set(char for char in login if char in z))

if found:
    print("Обнаружены запрещенные символы:", ", ".join(found))