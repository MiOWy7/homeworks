N = int(input("Введите N: "))
divisors = [i for i in range(1, N+1) if N % i == 0]
print("Делители:", divisors)
