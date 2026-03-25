def nalog(doxod):
    fee = int(input("процент налога:")) / 100
    result = doxod * fee
    return result

print("Налог составляет", nalog(10000))
