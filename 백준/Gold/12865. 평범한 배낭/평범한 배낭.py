import sys
input = sys.stdin.readline

# ✅ 입력 처리
N, K = map(int, input().strip().split())
items = [tuple(map(int, input().strip().split())) for _ in range(N)]  # (weight, value)


# ✅ DP 배열을 1차원으로 최적화
dp = [0] * (K + 1)

# ✅ Knapsack DP
for weight, value in items:
    for w in range(K, weight - 1, -1):  # 현재 무게에서 역순으로 갱신
        dp[w] = max(dp[w], dp[w - weight] + value)

# ✅ 최대 가치 출력
print(max(dp))