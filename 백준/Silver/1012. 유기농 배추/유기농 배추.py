# 유기농 배추

from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def OOB(nx, ny):
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        return True
    else:
        return False
    
def find_min_earthworm(M,N,K):
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        a,b = list(map(int, input().split()))
        arr[b][a] = 1
    vis = [[0 for _ in range(M)] for _ in range(N)]
    
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 or vis[i][j] == 1:
                vis[i][j] = 1
                continue
            q = deque()
            q.append([i,j])
            vis[i][j] = 1
            
            while len(q):
                x, y = q.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if OOB(nx, ny) or vis[nx][ny] == 1 or arr[nx][ny] == 0:
                        continue
                    vis[nx][ny] = 1
                    q.append([nx, ny])
            count += 1
    return count

T = int(input())
for i in range(T):
    M, N, K = list(map(int, input().split()))
    print(find_min_earthworm(M,N,K))