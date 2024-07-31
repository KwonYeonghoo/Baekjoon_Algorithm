# 적록색약

from collections import deque

N = int(input())
arr = [input() for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def OOB(nx, ny):
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        return True
    else:
        return False

def color_weak(arr):
    RG, B = 0, 0
    cw_vis = [[-1 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            q = deque()
            q.append([i,j])
            if arr[i][j] in ['R','G'] and cw_vis[i][j] == -1:
                cw_vis[i][j] = 0
                while len(q):
                    x, y = q.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if arr[x][y] in ['R','G']:
                            if not OOB(nx, ny) and arr[nx][ny] in ['R','G'] and cw_vis[nx][ny] == -1:
                                q.append([nx, ny])
                                cw_vis[nx][ny] = 0
                RG += 1
            elif arr[i][j] == 'B' and cw_vis[i][j] == -1:
                cw_vis[i][j] = 1
                while len(q):
                    x, y = q.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if not OOB(nx, ny) and arr[nx][ny] == 'B' and cw_vis[nx][ny] == -1:
                            q.append([nx, ny])
                            cw_vis[nx][ny] = 1
                B += 1
    return RG + B

def non_color_weak(arr):
    R, G, B = 0, 0, 0
    ncw_vis = [[-1 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            q = deque()
            q.append([i, j])
            if arr[i][j] == 'R' and ncw_vis[i][j] == -1:
                ncw_vis[i][j] = 0
                while len(q):
                    x, y = q.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if not OOB(nx, ny) and arr[nx][ny] == 'R' and ncw_vis[nx][ny] == -1:
                            q.append([nx, ny])
                            ncw_vis[nx][ny] = 0
                R += 1
            if arr[i][j] == 'G' and ncw_vis[i][j] == -1:
                ncw_vis[i][j] = 1
                while len(q):
                    x, y = q.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if not OOB(nx, ny) and arr[nx][ny] == 'G' and ncw_vis[nx][ny] == -1:
                            q.append([nx, ny])
                            ncw_vis[nx][ny] = 1
                G += 1
            if arr[i][j] == 'B' and ncw_vis[i][j] == -1:
                ncw_vis[i][j] = 2
                while len(q):
                    x, y = q.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if not OOB(nx, ny) and arr[nx][ny] == 'B' and ncw_vis[nx][ny] == -1:
                            q.append([nx, ny])
                            ncw_vis[nx][ny] = 2
                B += 1
    return R+G+B

print(non_color_weak(arr), color_weak(arr))