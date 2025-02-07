import sys
from collections import deque

N = int(input())
arr = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def OOB(nx, ny):
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        return True
    else:
        return False


result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == "0" or visited[i][j] == 1:
            continue
        count = 1
        Q = deque([(i, j)])
        visited[i][j] = 1
        while Q:
            x, y = Q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if OOB(nx, ny) or visited[nx][ny] == 1 or arr[nx][ny] == "0":
                    continue
                Q.append([nx, ny])
                visited[nx][ny] = 1
                count += 1
        result.append(count)

print(len(result))
print("\n".join(map(str, sorted(result))))
