import sys

N = int(input())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))
M = int(input())

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
