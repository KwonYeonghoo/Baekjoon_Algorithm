import sys

input = sys.stdin.readline

H, W, N, M = map(int, input().strip().split())


def OOB(x, y):
    return x >= H or y >= W


count = 0
for i in range(0, H, N + 1):
    for j in range(0, W, M + 1):
        if OOB(i, j):
            continue
        count += 1

print(count)