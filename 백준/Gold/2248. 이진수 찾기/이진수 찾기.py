import sys
input = sys.stdin.readline

# 이진수 문제는 패턴을 잘 살펴보기
N, L, I = map(int, input().strip().split())
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    dp[i][0] = 1
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

answer = ''
for i in reversed(range(N)): # 4 3 2 1 0
    temp = sum(dp[i][:L+1])
    if I > temp:
        answer += "1"
        I -= temp
        L -= 1
    else:
        answer += "0"
print(answer)