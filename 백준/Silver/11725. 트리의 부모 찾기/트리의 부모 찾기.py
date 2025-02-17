import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input().strip())
nodes = defaultdict(list)
visited = [-1] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().strip().split())
    nodes[a].append(b)
    nodes[b].append(a)

Q = deque([1])
visited[1] = 0
while Q:
    x = Q.popleft()
    for val in nodes[x]:
        if visited[val] != -1:
            continue
        Q.append(val)
        visited[val] = x

for i in range(2, N+1):
    print(visited[i])
