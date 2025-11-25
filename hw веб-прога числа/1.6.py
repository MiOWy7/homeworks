N = int(input("Введите N: "))
factors = {}
tmp = N
i = 2
while i * i <= tmp:
    while N % i == 0:
        factors[i] = factors.get(i, 0) + 1
        N //= i
    i += 1
if N > 1:
    factors[N] = factors.get(N, 0) + 1
for k in sorted(factors):
    print(f"Множитель: {k}, степень: {factors[k]}")
