import sys
input = sys.stdin.readline

# DP 풀이
## N * 3 배열 만들어서 최솟값 기록해주기
N = int(input().strip())
cost = [tuple(map(int, input().strip().split())) for _ in range(N)]
dp_table = [[1000000] * 3 for _ in range(N)]
dp_table[0][0], dp_table[0][1], dp_table[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp_table[i][j] = min(cost[i][j] + dp_table[i - 1][k], dp_table[i][j])

print(min(dp_table[-1]))
