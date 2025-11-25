from math import gcd
a1 = int(input("Введите числитель первого числа: "))
b1 = int(input("Введите знаменатель первого числа: "))
a2 = int(input("Введите числитель второго числа: "))
b2 = int(input("Введите знаменатель второго числа: "))
num = a1 * b2 + a2 * b1
den = b1 * b2
g = gcd(num, den)
print(f"Сумма: {num//g}/{den//g}")
num = a1 * b2 - a2 * b1
g = gcd(num, den)
print(f"Разность: {num//g}/{den//g}")
