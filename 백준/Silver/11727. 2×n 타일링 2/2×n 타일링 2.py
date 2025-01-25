# DP
# 점화식: DP[x] = DP[x-1] + 2*DP[x-2]

N = int(input())
dp_table = [0] * (N + 1)
if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    dp_table[1], dp_table[2] = 1, 3
    for i in range(3, N + 1):
        dp_table[i] = dp_table[i - 1] + 2 * dp_table[i - 2]
    print(dp_table[N] % 10007)