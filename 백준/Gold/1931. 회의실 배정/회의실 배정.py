import sys

# 끝나는 시간으로 정렬
N = int(input())
times = sorted(
    [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)],
    key=lambda x: (x[1], x[0])
)

curr_end_time = times[0][1]
count = 1
for i in range(1, len(times)):
    if curr_end_time > times[i][0]:
        continue
    curr_end_time = times[i][1]
    count += 1
print(count)
