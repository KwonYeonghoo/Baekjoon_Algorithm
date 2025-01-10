import sys

N = int(sys.stdin.readline())
cnt_arr = [0] * (10000 + 1)

for _ in range(N):
    cnt_arr[int(sys.stdin.readline())] += 1
    
for i in range(len(cnt_arr)):
    for _ in range(cnt_arr[i]):
        print(i, end="\n")