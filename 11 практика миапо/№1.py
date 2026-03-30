def check_status(age, has_ticket): return "Допуск разрешен" if age >= 18 and has_ticket else "Допуск запрещен"
print(check_status(20, True))