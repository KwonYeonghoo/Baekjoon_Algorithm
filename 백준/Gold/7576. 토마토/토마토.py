from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M, N = list(map(int, input().split()))
tomatoes = [list(map(int, input().split())) for _ in range(N)]
day_count = [[0 for _ in range(M)] for _ in range(N)]

ans = 0
q = deque()
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            q.append([i, j])

while len(q):
    x, y = q.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or ny < 0  or nx >= N or ny >= M:
            continue
        if tomatoes[nx][ny] == 1 or tomatoes[nx][ny] == -1:
            continue
        # tomatoes[nx][ny]가 0일 때
        tomatoes[nx][ny] = 1
        q.append([nx, ny])
        day_count[nx][ny] = day_count[x][y] + 1
        ans = day_count[nx][ny]

flag = False
for row in tomatoes:
    if 0 in row:
        flag = True
        break

if flag == True:
    print(-1)
else:
    print(ans)
