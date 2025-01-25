import sys
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def OOB(nx, ny):
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        return True
    else:
        return False


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    Q = deque()

    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 or visited[i][j] == 1:
                continue
            Q.append([i, j])
            visited[i][j] = 1
            count += 1
            while Q:
                x, y = Q.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if OOB(nx, ny) or visited[nx][ny] == 1:
                        continue
                    if arr[nx][ny] == 0:
                        continue
                    Q.append([nx, ny])
                    visited[nx][ny] = 1
    print(count)