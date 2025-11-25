N = int(input("Введите N: "))
def double_fact(n):
    res = 1
    for i in range(n, 0, -2):
        res *= i
    return res
print("(N)!! =", double_fact(N))
