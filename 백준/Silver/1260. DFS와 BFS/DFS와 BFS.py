import sys
from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]  # 이중리스트로 그래프 표현
# 양방향 연결이므로, graph[a][b] & graph[b][a] 로 간선 연결 표현

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

result_dfs = []
result_bfs = []


def bfs(v):
    q = deque([v])
    visited_bfs[v] = True

    while q:
        x = q.popleft()
        result_bfs.append(x)
        for i in range(1, N + 1):
            if not visited_bfs[i] and graph[x][i]:
                q.append(i)
                visited_bfs[i] = True


def dfs(v):
    visited_dfs[v] = True
    result_dfs.append(v)
    for i in range(1, N + 1):
        if not visited_dfs[i] and graph[v][i]:
            dfs(i)


bfs(V)
dfs(V)
print(" ".join(map(str, result_dfs)))
print(" ".join(map(str, result_bfs)))