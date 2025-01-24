N = int(input())

# 계단 꼭대기부터 생각하기
# 계단 꼭대기에 도착하는 경우의 수: 1. 한 칸 올라온 경우 2. 두 칸 올라온 경우
# dp[x] = max(dp[x-3] + stairs[x-1] + stairs[x], dp[x-2] + stairs[x])
stairs = [0] + [int(input()) for _ in range(N)]
dp_table = [0] * (N + 1)
if N == 1:
    print(stairs[N])
elif N == 2:
    print(stairs[N-1]+stairs[N])
else:
    dp_table[1], dp_table[2] = stairs[1], stairs[1] + stairs[2]
    for i in range(3, N + 1):
        dp_table[i] = max(
            dp_table[i - 3] + stairs[i - 1] + stairs[i], dp_table[i - 2] + stairs[i]
        )
    print(dp_table[N])