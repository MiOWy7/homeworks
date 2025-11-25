def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
N = int(input("Введите N: "))
M = int(input("Введите M: "))
for num in range(N, M+1):
    if num % 2 == 1 and num > 5:
        found = False
        for i in range(2, num):
            for j in range(2, num):
                k = num - i - j
                if i <= j <= k and is_prime(i) and is_prime(j) and is_prime(k):
                    print(f"{num} = {i} + {j} + {k}")
                    found = True
                    break
            if found:
                break
