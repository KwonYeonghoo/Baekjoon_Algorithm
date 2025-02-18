import sys
input = sys.stdin.readline

N = int(input().strip())
triangle = [list(map(int, input().strip().split())) for _ in range(N)]
dp_table = [[0] * i for i in range(1, N + 1)]

dp_table[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(len(triangle[i])):
        for op in [j - 1, j]:
            if op < 0 or op > len(triangle[i - 1]) - 1:
                continue
            dp_table[i][j] = max(dp_table[i - 1][op] + triangle[i][j], dp_table[i][j])
print(max(dp_table[-1]))