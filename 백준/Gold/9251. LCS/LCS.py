import sys
input = sys.stdin.readline

# 2차원 dp
sub1 = input().strip()
sub2 = input().strip()

dp = [[0] * (len(sub2) + 1) for _ in range(len(sub1) + 1)]

for i in range(1, len(sub1) + 1):
    for j in range(1, len(sub2) + 1):
        if sub1[i - 1] == sub2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])