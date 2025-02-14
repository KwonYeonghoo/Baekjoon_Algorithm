import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().strip().split()))
dp1 = [1] * N
dp2 = [1] * N

for i in range(1, N):
    # 앞 뒤를 다 봐야함
    for j in range(i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
    for j in range(N - i, N):
        if arr[j] < arr[N - 1 - i]:
            dp2[N - 1 - i] = max(dp2[N - 1 - i], dp2[j] + 1)

max_result = -1
for i in range(N):
    max_result = max(dp1[i] + dp2[i] - 1, max_result)
print(max_result)