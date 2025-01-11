# 계수 정렬

N = int(input())
count_arr = {i:[] for i in range(201)}

for _ in range(N):
    info = input().split()
    count_arr[int(info[0])].append(info[1])

for i in range(len(count_arr)):
    for name in count_arr[i]:
        print(i, name)