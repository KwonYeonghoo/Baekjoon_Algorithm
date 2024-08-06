from collections import deque

M, N, K = tuple(map(int, input().split()))
rectangles = [list(map(int, input().split())) for _ in range(K)]

arr = [[0 for _ in range(N)] for _ in range(M)]
vis = [[0 for _ in range(N)] for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = []

def OOB(nx, ny):
    if nx<0 or nx>=M or ny<0 or ny>=N:
        return True
    else:
        return False

# 직사각형 표시하기
for rectangle in rectangles:
    x1, y1 = rectangle[0], rectangle[1]
    x2, y2 = rectangle[2], rectangle[3]
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

# 모든 영역 순회하기
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 or vis[i][j] == 1:
            continue
        q = deque()
        q.append([i,j])
        vis[i][j] = 1
        area_size = 1
        while len(q):
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if OOB(nx, ny) or vis[nx][ny] == 1 or arr[nx][ny] == 1:
                    continue
                q.append([nx,ny])
                vis[nx][ny] = 1
                area_size += 1
        ans.append(area_size)

print(len(ans))
print(' '.join(map(str, sorted(ans))))