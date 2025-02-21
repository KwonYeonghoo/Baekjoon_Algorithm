import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

# 주어진 시작점에서 다른 모든 정점으로의 최단 경로

V, E = map(int, input().strip().split())
start = int(input().strip())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))


INF = float("inf")
distance = [INF] * (V + 1)
distance[start] = 0


def dijkstra(start):
    pq = [(0, start)]

    while pq:
        curr_cost, curr_node = heapq.heappop(pq)
        if distance[curr_node] < curr_cost:
            continue

        for next_node, next_cost in graph[curr_node]:
            new_cost = next_cost + curr_cost
            if distance[next_node] < new_cost:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


dijkstra(start)

for i in range(1, V + 1):
    print(distance[i] if distance[i] != float("inf") else "INF")
