# DP인 것 같다 -->
# 계단오르기 문제처럼 거꾸로 생각해보기
# ex) 4를 만드는 경우의 수: dp[3]+1, dp[2]+2, dp[1]+3 세 개 뿐
# ex) 5를 만드는 경우의 수: dp[4]+1, dp[3]+2, dp[2]+3 세 개 뿐
# --> 점화식: DP[x] = DP[x-1] + D[x-2] + DP[x-3]

dp = [0] * (10 + 1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 10 + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

N = int(input())
for _ in range(N):
    print(dp[int(input())])