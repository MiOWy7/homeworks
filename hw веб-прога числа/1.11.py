N = int(input("Введите N: "))
M = int(input("Введите M: "))
for a in range(N, M+1):
    for b in range(a, M+1):
        c2 = a*a + b*b
        c = int(c2 ** 0.5)
        if c >= a and c >= b and c <= M and c*c == c2:
            print(f"{a}, {b}, {c}")
