import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().strip().split()))
max_dp = arr
min_dp = arr
for _ in range(N-1):
    arr = list(map(int, input().strip().split()))
    max_dp = [arr[0]+max(max_dp[0], max_dp[1]), arr[1]+max(max_dp), arr[2]+max(max_dp[1], max_dp[2])]
    min_dp = [arr[0]+min(min_dp[0], min_dp[1]), arr[1]+min(min_dp), arr[2]+min(min_dp[1], min_dp[2])]
print(max(max_dp), min(min_dp))