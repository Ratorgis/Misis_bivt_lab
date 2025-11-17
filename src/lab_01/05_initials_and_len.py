name = list(input("ФИО: ").split())
total_len = sum(len(i) for i in name)
print(f"Инициалы: {name[0][0]}{name[1][0]}{name[2][0]}")
print(f"Длина (символы): {total_len + 2}")
