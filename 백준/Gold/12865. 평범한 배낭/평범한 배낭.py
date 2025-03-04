import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
items = [tuple(map(int, input().strip().split())) for _ in range(N)]
dp_table = [0] * (K + 1)

for weight, cost in items:
    for i in range(K, weight - 1, -1):
        dp_table[i] = max(dp_table[i - weight] + cost, dp_table[i])
print(max(dp_table))