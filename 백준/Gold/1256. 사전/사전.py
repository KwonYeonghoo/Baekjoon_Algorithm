import sys
input = sys.stdin.readline

# N개의 a, M개의 z
N, M, K = map(int, input().strip().split())
dp_table = [[1] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]

if dp_table[N][M] < K:
    print(-1)
else:
    result = ""
    while N > 0 and M > 0:
        if K <= dp_table[N - 1][M]:
            result += "a"
            N -= 1
        else:
            result += "z"
            K -= dp_table[N - 1][M]
            M -= 1
    result += N * "a" + M * "z"

    print(result)
