N, M = tuple(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
ans = []

def backtracking(curr):
    if curr == M:
        print(' '.join(map(str, ans)))
        return
    overlap = 0
    for i in range(N):
        if overlap == arr[i]:
            continue
        if len(ans) > 0 and ans[-1] > arr[i]:
            continue
        ans.append(arr[i])
        overlap = arr[i]
        backtracking(curr+1)
        ans.pop()

backtracking(0)