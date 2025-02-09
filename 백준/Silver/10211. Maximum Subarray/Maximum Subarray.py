import sys

# sys.stdin = open("/Users/hoo/Hoo/Study/알고리즘/2025/input.txt", "r")

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    dp_table = [0] * (N)
    dp_table[0] = arr[0]
    for i in range(1, N):
        dp_table[i] = max(dp_table[i - 1] + arr[i], arr[i])
    print(max(dp_table))