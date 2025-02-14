import sys

input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())

# K보다 작은 곱이 몇 개인지 찾는 문제

# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


def binary_search(target):
    left, right = 0, target
    while left < right:
        mid = (left + right) // 2

        count = 0
        for i in range(1, N + 1):
            count += min(mid // i, N)

        if count >= target:
            right = mid
        else:
            left = mid + 1
    return right


print(binary_search(K))