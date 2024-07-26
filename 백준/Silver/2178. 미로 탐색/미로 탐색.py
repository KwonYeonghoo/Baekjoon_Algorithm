
from collections import deque


N, M = list(map(int, input().split()))
maze = [input() for _ in range(N)]
dist = [[-1 for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

min_distance = 10000

# 시작점 (0,0)
dist[0][0] = 1
# 큐에 삽입
q = deque()
q.append([0, 0])
while len(q):
    x, y = q.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx == (N-1) and ny == (M-1):
            ans = dist[x][y] + 1
            min_distance = min(min_distance, ans)
            break
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if dist[nx][ny] != -1 or maze[nx][ny] == '0':
            continue
        q.append([nx, ny])
        dist[nx][ny] = dist[x][y] + 1
print(min_distance)