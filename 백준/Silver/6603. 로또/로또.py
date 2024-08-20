def backtracking(curr):
    if curr == 6:
        print(' '.join(map(str, ans)))
        return
    for i in range(k):
        if vis[i] == 1:
            continue
        if len(ans) > 0 and ans[-1] >= S[i]:
            continue
        ans.append(S[i])
        vis[i] = 1
        backtracking(curr+1)
        ans.pop()
        vis[i] = 0
        

while True:
    temp = input()
    if temp == '0':
        break
    kS = list(map(int, temp.split()))
    k = kS[0]
    S = kS[1:]
    ans = []
    vis = [0 for _ in range(k)]
    backtracking(0)
    
    print()