# DP
# 끝에서부터 경우의 수 고려해보기
# 제일 끝 타일을 채울 수 있는 경우의 수: 1x2 1개 or 2x1 2개
# DP 테이블에 저장되어야 할 정보: n번째 타일을 채우기 위해 가능한 경우의 수
# 점화식: DP[x] = DP[x-1] + DP[x-2]
# DP[1] = 1, DP[2] = 2

N = int(input())
dp_table = [0] * (N + 1)
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    dp_table[1], dp_table[2] = 1, 2
    for i in range(3, N + 1):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
    print(dp_table[N] % 10007)