import sys
from collections import deque

N, M = list(map(int, input().split()))
arr = [input() for _ in range(N)]
vis = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def OOB(nx, ny):
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        return True
    else:
        return False


ans = 0
q = deque()
q.append([0, 0])
vis[0][0] = 1

while len(q):
    x, y = q.popleft()
    if x == (N - 1) and y == (M - 1):
        print(vis[x][y])
        break
    count = 0
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if OOB(nx, ny) or arr[nx][ny] == "0" or vis[nx][ny] != 0:
            continue
        count += 1
        q.append([nx, ny])
        vis[nx][ny] = vis[x][y] + 1
    if count != 0:
        ans += 1