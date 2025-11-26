from string import ascii_uppercase


def greeting(name: str, age: int) -> str:
    return f"Привет, {name}! Через год тебе будет {age + 1}"


def sum_avg(a: float | int, b: float | int) -> str:
    return f"sum = {round(a+b, 2)}; avg = {round((a + b) / 2, 2)}"


def discount_vat(price: float, discount: float, vat: float) -> list[str]:
    base = price * (1 - discount / 100)
    vat_amount = base * (vat / 100)
    total = base + vat_amount
    result = []
    result.append(f"База полсе скидки: {round(base, 2)}")
    result.append(f"НДС: {round(base, 2)}")
    result.append(f"Итого к оплате: {round(total, 2)}")
    return result


def minutes_to_hhmm(mns: int) -> str:
    return f"{mns // 60}:{mns % 60}"


def initials_and_len(name: list[str]) -> list[str]:
    total_len = sum(len(i) for i in name)
    result = []
    result.append(f"Инициалы: {name[0][0]}{name[1][0]}{name[2][0]}")
    result.append(f"Длина (символы): {total_len + 2}")
    return result


def attendance(visitors: list[str, str, int, bool]) -> str:
    out_class, on_class = 0, 0
    for one in visitors:
        name, surname, age, visit = one
        if visit:
            on_class += 1
        else:
            out_class += 1
    return f"out: {on_class}, {out_class}"


def transcript(cipher: str) -> str:
    first, seconde = 0, 0

    for i in range(len(cipher)):
        if cipher[i] in ascii_uppercase:
            first = i
            if seconde:
                break
        elif cipher[i].isdigit():
            seconde = i + 1
            if first:
                break

    return cipher[first :: seconde - first]
