from collections import deque

n, m = map(int , input().split())
arr = [list(map(int, input().split())) for _ in range(n)] # 그림
vis = [[0 for _ in range(m)] for _ in range(n)] # 방문한 곳 표시

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def OOB(nx, ny):
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return True
    else:
        return False

ans = 0
max_ = 0
# 시작점
for i in range(n):
    for j in range(m):
        count = 0
        if arr[i][j] == 0 or vis[i][j] == 1:
            continue
        vis[i][j] = 1 # 루트노드 1로 표시
        ans += 1
        q = deque() # 탐색할 노드들
        q.append([i, j])
        while len(q):
            x, y = q.popleft()
            count  += 1
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if OOB(nx, ny) or arr[nx][ny] == 0 or vis[nx][ny] == 1:
                    continue
                vis[nx][ny] = 1
                q.append([nx, ny])
        max_ = max(count, max_)
        
print(ans, max_)
        