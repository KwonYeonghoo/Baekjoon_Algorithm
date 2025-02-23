import sys
input = sys.stdin.readline

# 메모리 4mb
N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
prev_dp = [[arr[0][0], arr[0][0]], [arr[0][1], arr[0][1]], [arr[0][2], arr[0][2]]]
curr_dp = [[0, 0] for _ in range(3)]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            curr_dp[j][0] = max(prev_dp[j][0], prev_dp[j + 1][0]) + arr[i][j]
            curr_dp[j][1] = min(prev_dp[j][1], prev_dp[j + 1][1]) + arr[i][j]
        elif j == 1:
            curr_dp[j][0] = (
                max(prev_dp[j - 1][0], prev_dp[j][0], prev_dp[j + 1][0]) + arr[i][j]
            )
            curr_dp[j][1] = (
                min(prev_dp[j - 1][1], prev_dp[j][1], prev_dp[j + 1][1]) + arr[i][j]
            )
        else:
            curr_dp[j][0] = max(prev_dp[j - 1][0], prev_dp[j][0]) + arr[i][j]
            curr_dp[j][1] = min(prev_dp[j - 1][1], prev_dp[j][1]) + arr[i][j]
    prev_dp, curr_dp = curr_dp, [[0, 0] for _ in range(3)]

print(
    max(prev_dp[0][0], prev_dp[1][0], prev_dp[2][0]),
    min(prev_dp[0][1], prev_dp[1][1], prev_dp[2][1]),
)
