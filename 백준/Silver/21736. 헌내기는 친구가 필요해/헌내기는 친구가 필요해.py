import sys
from collections import deque

# BFS
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
count = 0


def OOB(nx, ny):
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        return True
    else:
        return False


Q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == "I":
            Q.append([i, j])
            visited[i][j] = 1
            break

while Q:
    x, y = Q.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if OOB(nx, ny):
            continue
        if visited[nx][ny] == 1 or arr[nx][ny] == "X":
            continue
        if arr[nx][ny] == "P":
            count += 1
        Q.append([nx, ny])
        visited[nx][ny] = 1
if count == 0:
    print("TT")
else:
    print(count)