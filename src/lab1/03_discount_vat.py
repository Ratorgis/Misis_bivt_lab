price, discount, vat = map(float, input().split())
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База полсе скидки: {round(base, 2)}")
print(f"НДС: {round(base, 2)}")
print(f"Итого к оплате: {round(base, 2)}")
