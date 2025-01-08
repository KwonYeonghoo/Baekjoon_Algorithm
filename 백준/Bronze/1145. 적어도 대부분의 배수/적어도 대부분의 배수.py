arr = list(map(int, input().split()))

MAX = 100**3


def f(x):
    count = 0
    for a in arr:
        if x % a == 0:
            count += 1
    return count


for i in range(1, MAX):
    count = f(i)
    if count >= 3:
        break
print(i)