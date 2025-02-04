import sys


# 완전탐색 X, DP
# 2차원 DP 테이블
# 각 테이블의 요소: 해당 요소를 선택했을 때 스티커 합의 최댓값
# 점화식:
# DP[0][i] = max(DP[1][i-1], DP[1][i-2], DP[0][i-2]) + stickers[0][i]
# DP[1][i] = max(DP[0][i-1], DP[0][i-2], DP[1][i-2]) + stickers[1][i]


T = int(input())
for _ in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    if N == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue
    dp_table = [[0] * N for _ in range(2)]
    dp_table[0][0], dp_table[1][0] = stickers[0][0], stickers[1][0]
    dp_table[0][1], dp_table[1][1] = (
        stickers[0][1] + dp_table[1][0],
        stickers[1][1] + dp_table[0][0],
    )
    for i in range(2, N):
        dp_table[0][i] = (
            max(dp_table[1][i - 1], dp_table[1][i - 2], dp_table[0][i - 2])
            + stickers[0][i]
        )
        dp_table[1][i] = (
            max(dp_table[0][i - 1], dp_table[0][i - 2], dp_table[1][i - 2])
            + stickers[1][i]
        )

    print(max(dp_table[0][N - 1], dp_table[1][N - 1]))
