# 누적합?

N = int(input())
arr = sorted(list(map(int, input().split())))
prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
print(sum(prefix_sum))