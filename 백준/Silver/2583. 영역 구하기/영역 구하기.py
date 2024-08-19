
from collections import deque

M, N, K = tuple(map(int, input().split()))
areas = [list(map(int, input().split())) for _ in range(K)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = [[0 for _ in range(N)] for _ in range(M)]
vis = [[0 for _ in range(N)] for _ in range(M)]

def OOB(nx, ny):
    if nx<0 or nx>=M or ny<0 or ny>=N:
        return True
    else:
        return False

for area in areas:
    x1, y1, x2, y2 = area
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

count = 0
sizes = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 or vis[i][j] == 1:
            continue
        q = deque()
        vis[i][j] = 1
        q.append([i,j])
        count += 1
        size = 1
        while len(q):
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if OOB(nx, ny) or vis[nx][ny] == 1 or arr[nx][ny] == 1:
                    continue
                vis[nx][ny] = 1
                q.append([nx, ny])
                size += 1
        sizes.append(size)

print(count)
print(' '.join(map(str, sorted(sizes))))