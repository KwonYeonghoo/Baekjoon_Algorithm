import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().strip().split())
visited = [-1] * 100001

# 1초 후 X-1, X+1
# 0초 후 2X


def OOB(nx):
    return nx < 0 or nx > 100000


def bfs(n):
    Q = deque([(n, 0)])
    visited[n] = 0
    while Q:
        x, cost = Q.popleft()
        for nx, c in [(x + 1, 1), (x - 1, 1), (2 * x, 0)]:
            if OOB(nx):
                continue
            if visited[nx] != -1 and visited[nx] <= cost + c:
                continue
            Q.append((nx, cost + c))
            visited[nx] = cost + c


bfs(N)
print(visited[K])
