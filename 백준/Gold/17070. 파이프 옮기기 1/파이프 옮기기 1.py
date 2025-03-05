import sys
from collections import deque
input = sys.stdin.readline

# 3 <= N <= 16
# 백트래킹? BFS?
# 큐에 하나씩 담아가며 탐색, 이미 놓여져있는 모양이면 패스

# 파이프 이동 경우의 수는 dx, dy로 처리
## 가로 세로 대각선은 어떻게 판별?
### 좌표 계산으로

# 방문 여부: 파이프의 두 점이 모두 visited이면 continue

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[[0] * 3 for _ in range(N)] for _ in range(N)]

dxdy_list = [  # ((파이프 끝 쪽 좌표), shape)
    [(0, 1, 0), (1, 1, 2)],  # 0은 가로, 1은 세로, 2는 대각선
    [(1, 0, 1), (1, 1, 2)],
    [(0, 1, 0), (1, 0, 1), (1, 1, 2)],
]

# Q = deque([(0, 1, 0)])
# while Q:
#     x, y, shape = Q.popleft()

#     for dx, dy, next_shape in dxdy_list[shape]:
#         nx, ny = x + dx, y + dy

#         if nx >= N or ny >= N or arr[nx][ny] == 1:
#             continue
#         if next_shape == 2 and (arr[nx][y] == 1 or arr[x][ny] == 1):
#             continue
#         Q.append((nx, ny, next_shape))
#         visited[nx][ny][next_shape] += 1

# print(sum(visited[N - 1][N - 1]))

#####################################################
visited[0][1][0] = 1

for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            continue
        for shape in range(3):
            if visited[x][y][shape] == 0:
                continue
            for dx, dy, next_shape in dxdy_list[shape]:
                nx, ny = x + dx, y + dy
                if nx >= N or ny >= N or arr[nx][ny] == 1:
                    continue
                if next_shape == 2 and (arr[nx][y] == 1 or arr[x][ny] == 1):
                    continue
                visited[nx][ny][next_shape] += visited[x][y][shape]

print(sum(visited[N - 1][N - 1]))
