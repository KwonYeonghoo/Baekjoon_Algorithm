N,M = tuple(map(int, input().split()))

arr = []

def backtracking(curr):
    if curr == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        arr.append(i)
        backtracking(curr+1)
        arr.pop()
        
backtracking(0)