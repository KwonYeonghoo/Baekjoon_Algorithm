import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
# 3차원 배열
# (H, N, M) 인덱스로 접근
# 익은 토마토: 1, 익지 않은 토마토: 0, 토마토 없는 칸: -1
arr = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]
visited = [[[-1] * M for _ in range(N)] for _ in range(H)]
Q = deque()

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


def OOB(nx, ny, nh):
    return nx < 0 or ny < 0 or nh < 0 or nx >= N or ny >= M or nh >= H


for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == -1:
                visited[k][i][j] = 0
                continue
            if arr[k][i][j] == 0 or visited[k][i][j] != -1:
                continue
            Q.append([k, i, j])
            visited[k][i][j] += 1

day_count = 0
while Q:
    h, x, y = Q.popleft()
    for dir in range(6):
        nh = h + dh[dir]
        nx = x + dx[dir]
        ny = y + dy[dir]
        if OOB(nx, ny, nh) or visited[nh][nx][ny] != -1 or arr[nh][nx][ny] in [1, -1]:
            continue
        Q.append([nh, nx, ny])
        visited[nh][nx][ny] = visited[h][x][y] + 1
        day_count = visited[nh][nx][ny]


flag = False
for h in range(H):
    for i in range(N):
        for j in range(M):
            if visited[h][i][j] == -1:
                flag = True
                break
if flag:
    print(-1)
else:
    print(day_count)