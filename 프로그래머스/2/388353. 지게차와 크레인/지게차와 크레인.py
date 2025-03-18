from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(storage, requests):
    answer = 0
    n, m = len(storage), len(storage[0])
    storage = [list(row) for row in storage]
    
    def is_outside(x, y):
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                return True
        return False
    
    def is_adjacent(x, y):
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if storage[nx][ny] == 0:
                return True
        return False
    
    
    def forklift(target):
        nonlocal answer
        
        forklift_update = []
        for i in range(n):
            for j in range(m):
                if storage[i][j] == target and (is_outside(i, j) or is_adjacent(i, j)):
                    forklift_update.append((i,j))
                    
        for x, y in forklift_update:
            storage[x][y] = 0
            answer += 1
        
        for i in range(n):
            for j in range(m):
                if storage[i][j] == -1:
                    if is_adjacent(i, j):
                        bfs(i, j)
        

    def bfs(x, y, target=None):
        visited = [[0]*m for _ in range(n)]
        Q = deque([(x, y)])
        visited[x][y] = 1
        storage[x][y] = 0
        while Q:
            x, y = Q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if visited[nx][ny]:
                    continue
                if storage[nx][ny] != target and storage[nx][ny] != -1:
                    continue
                    
                Q.append((nx, ny))
                visited[nx][ny] = 1
                storage[nx][ny] = 0
                

    def crane(target):
        nonlocal answer
        crane_update = []
        for i in range(n):
            for j in range(m):
                if storage[i][j] == target:
                    crane_update.append((i, j))
                    answer += 1
                if storage[i][j] == -1:
                    crane_update.append((i, j))
        
        for x, y in crane_update:
            if is_outside(x, y) or is_adjacent(x, y):
                bfs(x, y, target)
            else:
                storage[x][y] = -1
            

    for request in requests:
        if len(request) == 1:
            forklift(request)
        else:
            crane(request[0])
    
    return n*m - answer