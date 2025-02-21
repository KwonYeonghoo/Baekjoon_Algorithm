import sys
input = sys.stdin.readline

# 딱 보면 BFS 문제처럼 보임
# 여러 경우의 수 중 최대/최소를 구하는 문제 --> DP로 접근해보기

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    arr = [list(map(int, input().strip().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]
    if N == 1:
        print(max(arr[0][0], arr[1][0]))
        continue
    dp[0][0], dp[1][0] = arr[0][0], arr[1][0]
    dp[0][1], dp[1][1] = dp[1][0] + arr[0][1], dp[0][0] + arr[1][1]

    for i in range(2, N):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + arr[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i]
    print(max(dp[0][-1], dp[1][-1]))
