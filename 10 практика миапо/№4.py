def check_temp(t):
    if t < 0:
        print("Мороз")
    elif t < 15:
        print("Холодно")
    elif t < 25:
        print("Нормально")
    else:
        print("Жара")
    return ""
print(check_temp(int(input())))

