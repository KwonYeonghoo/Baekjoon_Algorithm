import sys

input = sys.stdin.readline

# 증가하는 부분 수열 중에서 합이 가장 큰 것
# 그럼 dp 테이블에는 증가하는 부분수열의 합 중 가장 큰 것이 와야함
# 1. 증가하는지 판별
# 2. i보다 작은 j 중 dp_table[j]의 최댓값

N = int(input().strip())
arr = list(map(int, input().strip().split()))
dp_table = arr.copy()

for i in range(1, N):
    temp_max = -1
    for j in range(i):
        if arr[j] < arr[i]:
            temp_max = max(temp_max, dp_table[j])
    if temp_max == -1:
        dp_table[i] = arr[i]
    else:
        dp_table[i] = arr[i] + temp_max

print(max(dp_table))
