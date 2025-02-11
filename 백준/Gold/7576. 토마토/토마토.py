import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
Q = deque()


def OOB(nx, ny):
    return nx < 0 or ny < 0 or nx >= N or ny >= M


unripe_tomato = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            unripe_tomato += 1
        elif arr[i][j] == 1:
            Q.append([i, j])
            visited[i][j] = 0
        else:
            visited[i][j] = 0

day_count = 0
while Q:
    x, y = Q.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if OOB(nx, ny) or visited[nx][ny] != -1:
            continue
        Q.append([nx, ny])
        visited[nx][ny] = visited[x][y] + 1
        unripe_tomato -= 1
        day_count = visited[nx][ny]

if unripe_tomato != 0:
    print(-1)
else:
    print(day_count)
