def is_perfect(num):
    return sum(i for i in range(1, num) if num % i == 0) == num
N = int(input("Введите N (N < 5): "))
count, num = 0, 2
while count < N:
    if is_perfect(num):
        print(num)
        count += 1
    num += 1
