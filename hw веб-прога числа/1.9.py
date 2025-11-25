n = int(input("Введите число: "))
from math import isqrt
def is_fibonacci(num):
    x1 = 5 * num * num + 4
    x2 = 5 * num * num - 4
    return any(isqrt(x)**2 == x for x in (x1, x2))
print("Число принадлежит ряду Фибоначчи" if is_fibonacci(n) else "Число НЕ принадлежит ряду Фибоначчи")
