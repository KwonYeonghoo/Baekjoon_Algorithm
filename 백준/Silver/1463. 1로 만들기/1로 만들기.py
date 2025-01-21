# DP
# 점화식: DP[x] = min(DP[x // 3], DP[x // 2], DP[x - 1]) + 1

N = int(input())
MAX_LEN = 10**6
dp_table = [0] * (MAX_LEN + 1)
dp_table[1], dp_table[2], dp_table[3] = 0, 1, 1
for i in range(4, N + 1):
    if i % 3 == 0 and i % 2 == 0:
        dp_table[i] = min(dp_table[i // 3], dp_table[i // 2], dp_table[i - 1]) + 1
    elif i % 3 == 0:
        dp_table[i] = min(dp_table[i // 3], dp_table[i - 1]) + 1
    elif i % 2 == 0:
        dp_table[i] = min(dp_table[i // 2], dp_table[i - 1]) + 1
    else:
        dp_table[i] = dp_table[i - 1] + 1
print(dp_table[N])