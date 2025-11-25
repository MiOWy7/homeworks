from math import gcd
a1 = int(input("Введите числитель первого числа: "))
b1 = int(input("Введите знаменатель первого числа: "))
a2 = int(input("Введите числитель второго числа: "))
b2 = int(input("Введите знаменатель второго числа: "))
num = a1 * a2
den = b1 * b2
g = gcd(num, den)
print(f"Произведение: {num//g}/{den//g}")
num = a1 * b2
den = b1 * a2
g = gcd(num, den)
print(f"Частное: {num//g}/{den//g}")
