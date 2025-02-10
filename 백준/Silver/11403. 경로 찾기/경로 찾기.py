import sys
from collections import defaultdict, deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * N for _ in range(N)]
dict_ = defaultdict(list)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dict_[i].append(j)


def bfs(start_node, target):
    visited = [0] * N
    Q = deque([start_node])
    visited[start_node] = 1
    while Q:
        x = Q.popleft()
        for nx in dict_[x]:
            if nx == target:
                return True
            if visited[nx] == 1:
                continue
            Q.append(nx)
            visited[nx] = 1
    return False


for i in range(N):
    for j in range(N):
        if i in dict_.keys():
            if bfs(i, j):
                answer[i][j] = 1

for row in answer:
    print(*row)
