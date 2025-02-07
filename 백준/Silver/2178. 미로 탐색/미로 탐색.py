import sys
from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def OOB(nx, ny):
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        return True
    else:
        return False


depth = 1
visited[0][0] = depth
Q = deque([(0, 0, depth)])
while Q:
    x, y, d = Q.popleft()
    if x == N - 1 and y == M - 1:
        print(d)
        break
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if OOB(nx, ny) or arr[nx][ny] == '0' or visited[nx][ny] != 0:
            continue
        Q.append((nx, ny, d + 1))
        visited[nx][ny] = d + 1
