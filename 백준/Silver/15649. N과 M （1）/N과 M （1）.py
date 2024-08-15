N, M = tuple(map(int, input().split()))

arr = []
vis = [0 for i in range(8)]

def f(k): # k는 재귀의 깊이라고 이해
    if k == M:
        print(' '.join(map(str, arr)))
        return # 이 전 함수로 되돌아감
    for i in range(1, N+1):
        if vis[i-1] == 1:
            continue
        arr.append(i)
        vis[i-1] = 1
        f(k+1)
        vis[i-1] = 0
        arr.pop()
f(0)