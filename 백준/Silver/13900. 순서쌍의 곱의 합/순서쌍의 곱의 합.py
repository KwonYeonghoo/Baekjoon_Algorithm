import sys

N = int(input())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))

# 순서쌍 싹 다 구하기 --> O(N^2)
# ab + ac + ad
# bc + bd
# cd
# --> a(b+c+d) + b(c+d) + c(d)
# --> prefix_sum = [a+b+c+d, b+c+d, c+d, d]
prefix_sum = [0] * N
prefix_sum[0] = sum(arr)  #
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i - 1] - arr[i]

result = 0
for i in range(N):
    result += arr[i] * prefix_sum[i]
print(result)