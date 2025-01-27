N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + abs((arr[i] - arr[i - 1]))

for _ in range(Q):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i])