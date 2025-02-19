import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().strip().split())
    arr[r - 1][c - 1] = 1

def OOB(nx, ny):
    return nx<0 or ny<0 or nx>=N or ny>=M

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

Q = deque()
result = -1

for i in range(N):
    for j in range(M):
        if visited[i][j] == 1 or arr[i][j] == 0:
            continue
        Q.append([i, j])
        visited[i][j] = 1
        size = 1
        while Q:
            x, y = Q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if OOB(nx, ny) or visited[nx][ny] == 1 or arr[nx][ny] == 0:
                    continue
                Q.append([nx, ny])
                visited[nx][ny] = 1
                size += 1
        result = max(size, result)
        
print(result)