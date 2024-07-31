# 나이트의 이동

from collections import deque

def find_min_count():
    N = int(input())
    vis = [[-1 for _ in range(N)] for _ in range(N)]
    cur_loc = list(map(int, input().split()))
    target_loc = list(map(int, input().split()))
    
    dx = [-1, -2, 1, 2, 1, 2, -1, -2]
    dy = [2, 1, 2, 1, -2, -1, -2, -1]

    def OOB(nx, ny):
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return True
        else:
            return False
        
    q = deque()
    q.append(cur_loc)
    vis[cur_loc[0]][cur_loc[1]] = 0
    count = 0
    while len(q):
        x, y = q.popleft()
        if x == target_loc[0] and y == target_loc[1]:
            return count
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if OOB(nx, ny) or vis[nx][ny] != -1:
                continue
            q.append([nx,ny])
            vis[nx][ny] = vis[x][y] + 1
            if nx == target_loc[0] and ny == target_loc[1]:
                return vis[nx][ny]
    return -1

T = int(input())
for _ in range(T):
    print(find_min_count())
    
