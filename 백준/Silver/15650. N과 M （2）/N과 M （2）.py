N, M = tuple(map(int, input().split()))

arr = []
vis = [0 for _ in range(N)]

def backtracking(curr):
    if curr == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        if len(arr) > 0 and arr[-1] >= i:
            continue
        if vis[i-1] == 1:
            continue
        arr.append(i)
        vis[i-1] = 1
        backtracking(curr+1)
        arr.pop()
        vis[i-1] = 0

backtracking(0)