arr = [0, 1, 1, 1, 2, 2] + [0] * 95
for i in range(6, 101):
    arr[i] = arr[i - 5] + arr[i - 1]


def padovan(n):
    return arr[n]


T = int(input())
for _ in range(T):
    N = int(input())
    print(padovan(N))