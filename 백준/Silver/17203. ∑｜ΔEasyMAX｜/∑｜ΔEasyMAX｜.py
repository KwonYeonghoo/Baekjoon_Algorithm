N, Q = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(Q):
    i, j = map(int, input().split())
    variance = 0
    for idx in range(i, j):
        variance += abs(arr[idx] - arr[idx - 1])
    print(variance)