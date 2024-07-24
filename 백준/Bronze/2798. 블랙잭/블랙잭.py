N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

# N의 길이가 최대 100장이므로, 100^3을 해도 제한시간 안에 들어온다.
# -> 모든 경우의 수를 다 볼 수 있음
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            add = arr[i]+arr[j]+arr[k]
            if add > M:
                continue
            ans = max(ans, add)
print(ans)