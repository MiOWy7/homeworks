a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
import math
print("Числа взаимно просты" if math.gcd(a, b) == 1 else "Числа не взаимно просты")
