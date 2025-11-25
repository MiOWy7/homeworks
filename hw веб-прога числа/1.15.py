N = int(input("Введите N: "))
M = int(input("Введите M: "))
for num in range(N, M+1):
    s = sum(int(x) for x in str(num))
    if s != 0 and num % s == 0:
        print(num)
