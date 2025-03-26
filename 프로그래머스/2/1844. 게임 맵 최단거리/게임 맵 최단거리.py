from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    def OOB(nx, ny):
        return nx<0 or ny<0 or nx>=n or ny>=m
    
    Q = deque([(0,0)])
    visited[0][0] = 1
    while Q:
        x, y = Q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx == n-1 and ny == m-1:
                print(visited)
                return visited[x][y] + 1
            if OOB(nx, ny) or visited[nx][ny] != 0 or maps[nx][ny] == 0:
                continue
            Q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
    return -1