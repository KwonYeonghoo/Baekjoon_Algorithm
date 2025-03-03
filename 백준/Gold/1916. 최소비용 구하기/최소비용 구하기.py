import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

dict_ = defaultdict(list)
MAX_COST = float("inf")
costs = [MAX_COST] * (N + 1)

for _ in range(M):
    start, end, cost = map(int, input().strip().split())
    dict_[start].append((end, cost))
target_start, target_end = map(int, input().strip().split())


def dijkstra(start):
    costs[start] = 0
    pq = [(0, start)]  # 우선순위 큐

    while pq:
        cost, city = heapq.heappop(pq)
        if costs[city] < cost:
            continue

        for next_city, next_cost in dict_[city]:
            new_cost = costs[city] + next_cost
            if new_cost < costs[next_city]:
                costs[next_city] = new_cost
                heapq.heappush(pq, (new_cost, next_city))


dijkstra(target_start)
print(costs[target_end])