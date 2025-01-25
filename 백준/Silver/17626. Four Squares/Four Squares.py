# DP
# 15663 = 125^2 + 6^2 + 1^2 + 1^2
# 일단 N에 가장 근접한 제곱수(X1)를 찾는다.
# N - X에 가장 근접한 제곱수(X2)를 찾는다.
# DP 점화식: DP[x] = DP[x - int(x ** 0.5)] + 1
N = int(input())
dp_table = [0] * (N + 1)
for i in range(1, N + 1):
    min_num = 5
    j_limit = int(i**0.5)
    for j in range(1, j_limit + 1):
        min_num = min(min_num, dp_table[i - j**2])
    dp_table[i] = min_num + 1
print(dp_table[N])