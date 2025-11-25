n = int(input("Введите число: "))
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
print("Число простое" if is_prime(n) else "Число составное")
