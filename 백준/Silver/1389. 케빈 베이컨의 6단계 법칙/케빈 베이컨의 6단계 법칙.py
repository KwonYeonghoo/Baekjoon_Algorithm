import sys
from collections import deque, defaultdict

# 최단거리: BFS
N, M = map(int, input().split())
arr = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

results = []
for i in range(1, N + 1):  # 출발점
    result = 0
    for j in range(1, N + 1):  # 타겟
        if i == j:
            continue
        visited = [-1] * (N + 1)
        visited[i] = 0
        flag = False
        depth = 1
        Q = deque([[i, depth]])

        while Q:
            x, d = Q.popleft()
            for y in arr[x]:
                if y == j:
                    flag = True
                    break
                if visited[y] != -1:
                    continue
                Q.append([y, d + 1])
                visited[y] = d
            if flag == True:
                break
        result += d
    results.append(result)
print(results.index(min(results)) + 1)