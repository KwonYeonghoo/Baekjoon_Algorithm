import sys
from collections import deque

# 완전탐색
N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
visited = [0] * (N + 1)
Q = deque()
count = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if visited[i] == 1:
        continue
    Q.append(i)
    visited[i] = 1
    count += 1
    while Q:
        a = Q.popleft()
        for b in graph[a]:
            if visited[b] == 1:
                continue
            Q.append(b)
            visited[b] = 1
    # print(visited)

print(count)
