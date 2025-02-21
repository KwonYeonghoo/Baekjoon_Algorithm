import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

# N개의 도시(1~N), M개의 버스
# A -> B의 버스 비용을 최소화

N = int(input().strip())  # 1 <= N <= 1000
M = int(input().strip())  # 1 <= M <= 100000
# (출발도시 번호, 도착도시 번호, 0 <= 버스 비용 <= 100000)
# BFS?
# {출발: [도착, 비용]} 이런 구조로 기록
##### M이 10만인 경우, Q에 저장되는 데이터가 너무 많아져서 메모리 초과
##### -> DFS로 풀이
########## 근데 이 마저도 시간, 메모리 측면에서 비효율적
########## 가중치 그래프의 최단 경로 문제이므로 **다익스트라 알고리즘 사용**

graph = defaultdict(list)
for _ in range(M):
    depart, arrive, cost = map(int, input().strip().split())
    graph[depart].append((arrive, cost))
target_d, target_a = map(int, input().strip().split())
# curr_c = 0
# Q = deque([(target_d, curr_c)])
# result = []
# while Q:
#     x, c = Q.popleft()
#     for nx, nc in graph[x]:
#         if nx == 5:
#             result.append(c + nc)
#             continue
#         Q.append([nx, c + nc])
# print(min(result))
##############################################
# curr_c = 0
# visited = [0] * (N + 1)
# min_cost = float('inf')


# def dfs(x, c):
#     global min_cost
#     visited[x] = 1
#     if x == target_a:
#         min_cost = min(min_cost, c)
#         return
#     for nx, nc in graph[x]:
#         # visited 추가해주기
#         if visited[nx] == 1:
#             continue
#         visited[nx] = 1
#         dfs(nx, c + nc)
#         visited[nx] = 0


# for x, c in graph[target_d]:
#     cost = dfs(x, curr_c + c)
# print(min_cost)
#############################################3


# 다익스트라: 최소 이동거리를 업데이트해가며 목적지까지의 최단거리를 찾아내는 알고리즘
def dijkstra(start):
    INF = float("inf")
    distance = [INF] * (N + 1)  # 모든 거리 무한대로 초기화
    distance[start] = 0
    pq = [(0, start)]  # 우선순위 큐 (최소 힙)

    while pq:
        curr_cost, curr_city = heapq.heappop(pq)

        if distance[curr_city] < curr_cost:
            continue

        for next_city, next_cost in graph[curr_city]:
            new_cost = curr_cost + next_cost
            if new_cost < distance[next_city]:
                distance[next_city] = new_cost
                heapq.heappush(pq, (new_cost, next_city))

    return distance[target_a]


result = dijkstra(target_d)
print(result if result != float("inf") else -1)
