N = int(input("Введите N: "))
M = int(input("Введите M: "))
for num in range(N, M+1):
    digits = [int(x) for x in str(num) if x != '0']
    if digits and all(num % d == 0 for d in digits):
        print(num)
