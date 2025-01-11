N = int(input())


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


n_fac = str(factorial(N))

count = 0
for i in range(len(n_fac)-1, -1, -1):
    if n_fac[i] == "0":
        count += 1
    else:
        print(count)
        break