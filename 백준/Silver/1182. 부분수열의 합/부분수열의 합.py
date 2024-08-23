N, S = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

count = 0
def backtracking(curr, sum):
    if curr == N:
        if sum == S:
            global count
            count += 1
        return
    backtracking(curr+1, sum + arr[curr])
    backtracking(curr+1, sum)
    
backtracking(0,0)
if S == 0:
    count -= 1
print(count)