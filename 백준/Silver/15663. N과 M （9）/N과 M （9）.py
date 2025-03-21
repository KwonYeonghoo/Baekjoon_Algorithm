N, M = tuple(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
vis = [0 for _ in range(N)]
ans = []

def backtracking(curr):
    if curr == M:
        print(' '.join(map(str, ans)))
        return
    overlap = 0
    for i in range(N):
        if vis[i] == 1 or overlap == arr[i]:
            continue
        ans.append(arr[i])
        vis[i] = 1
        overlap = arr[i]
        backtracking(curr+1)
        ans.pop()
        vis[i] = 0
        
backtracking(0)
