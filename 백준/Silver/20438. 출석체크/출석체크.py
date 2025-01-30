import sys

# 1 <= K, Q <= N <= 5000
# 1 <= M <= 50000

N, K, Q, M = map(int, input().split())
sleeping = list(map(int, sys.stdin.readline().strip().split()))
qr_list = list(map(int, sys.stdin.readline().strip().split()))
student_list = [0] * (N + 3)

for s in qr_list:
    if s in sleeping:
        continue
    for i in range(s, N + 3, s):
        if i not in sleeping:
            student_list[i] = 1

prefix_sum = [0] * (N + 3)
for i in range(3, N + 3):
    prefix_sum[i] = prefix_sum[i - 1] + student_list[i]


for _ in range(M):
    S, E = list(map(int, sys.stdin.readline().strip().split()))
    result = (E - S + 1) - (prefix_sum[E] - prefix_sum[S - 1])
    print(result)
