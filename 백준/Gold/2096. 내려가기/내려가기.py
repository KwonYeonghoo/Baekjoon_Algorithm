import sys
input = sys.stdin.readline

# ✅ 입력 처리
N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

# ✅ DP 테이블을 2줄로 최적화 (prev_dp, curr_dp)
prev_dp = [[arr[0][0], arr[0][0]], [arr[0][1], arr[0][1]], [arr[0][2], arr[0][2]]]
curr_dp = [[0, 0] for _ in range(3)]  # 현재 행을 저장할 배열

# ✅ DP 업데이트 (메모리 최적화)
for i in range(1, N):
    for j in range(3):
        if j == 0:
            curr_dp[j][0] = max(prev_dp[j][0], prev_dp[j + 1][0]) + arr[i][j]
            curr_dp[j][1] = min(prev_dp[j][1], prev_dp[j + 1][1]) + arr[i][j]
        elif j == 1:
            curr_dp[j][0] = (
                max(prev_dp[j - 1][0], prev_dp[j][0], prev_dp[j + 1][0]) + arr[i][j]
            )
            curr_dp[j][1] = (
                min(prev_dp[j - 1][1], prev_dp[j][1], prev_dp[j + 1][1]) + arr[i][j]
            )
        else:
            curr_dp[j][0] = max(prev_dp[j - 1][0], prev_dp[j][0]) + arr[i][j]
            curr_dp[j][1] = min(prev_dp[j - 1][1], prev_dp[j][1]) + arr[i][j]

    # ✅ prev_dp를 curr_dp로 업데이트 (한 줄만 유지)
    prev_dp, curr_dp = curr_dp, [[0, 0] for _ in range(3)]  # 새 배열로 초기화

# ✅ 최종 결과 계산
max_result = max(prev_dp[0][0], prev_dp[1][0], prev_dp[2][0])
min_result = min(prev_dp[0][1], prev_dp[1][1], prev_dp[2][1])

print(max_result, min_result)