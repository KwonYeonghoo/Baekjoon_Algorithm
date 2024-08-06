
from collections import deque


N = int(input())
arr = [input() for _ in range(N)]
vis = [[0 for _ in range(N)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def OOB(nx, ny):
    if nx<0 or nx>=N or ny<0 or ny>=N:
        return True
    else:
        return False
    
ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '0' or vis[i][j] == 1:
            continue
        q = deque()
        q.append([i,j])
        vis[i][j] = 1
        apt_size = 1
        while len(q):
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if OOB(nx, ny) or vis[nx][ny] == 1 or arr[nx][ny] == '0':
                    continue
                q.append([nx,ny])
                vis[nx][ny] = 1
                apt_size += 1
        ans.append(apt_size)
print(len(ans))
for a in sorted(ans):
    print(a)