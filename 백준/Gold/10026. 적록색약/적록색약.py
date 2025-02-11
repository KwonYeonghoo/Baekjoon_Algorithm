import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
arr = [input().strip() for _ in range(N)]
weak_visited = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def OOB(nx, ny):
    return nx < 0 or ny < 0 or nx >= N or ny >= N


weakQ = deque()
Q = deque()
weak_result = 0
result = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] != 1:
            Q.append([i, j])
            visited[i][j] = 1
            current_color = arr[i][j]
            size = 0
            while Q:
                x, y = Q.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if (
                        OOB(nx, ny)
                        or visited[nx][ny] == 1
                        or arr[nx][ny] != current_color
                    ):
                        continue
                    Q.append([nx, ny])
                    visited[nx][ny] = 1
                    size += 1
            result += 1
        if weak_visited[i][j] != 1:
            weakQ.append([i, j])
            weak_visited[i][j] = 1
            current_color = arr[i][j]
            size = 0
            while weakQ:
                x, y = weakQ.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if OOB(nx, ny) or weak_visited[nx][ny] == 1:
                        continue
                    if current_color in "RG":
                        if arr[nx][ny] not in "RG":
                            continue
                    else:
                        if arr[nx][ny] != current_color:
                            continue
                    weakQ.append([nx, ny])
                    weak_visited[nx][ny] = 1
                    size += 1
            weak_result += 1

print(result, weak_result)
