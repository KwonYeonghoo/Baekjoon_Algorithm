import sys
from collections import deque

input = sys.stdin.readline

# 치킨 거리: 집에서 가장 가까운 치킨집까지의 거리
N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
MAX_DISTANCE = float("inf")

# N 최댓값이 50 밖에 안 됨
# 최악의 경우: 13C2 * 250
# 치킨집 중 M개만 선택해서 최소 치킨거리 구하기

chickens, houses = [], []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i, j))
        if arr[i][j] == 1:
            houses.append((i, j))


def calc_chicken_distance(chicken_list):
    sum_distance = 0
    for hx, hy in houses:
        min_distance = MAX_DISTANCE
        for cx, cy in chicken_list:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        sum_distance += min_distance
    return sum_distance


# 서로 다른 두 수를 뽑는 법: 백트래킹
chicken_result = []
visited = [0] * len(chickens)
min_city_distance = MAX_DISTANCE


def backtracking(start, depth):
    global min_city_distance
    if depth == M:
        city_distance = calc_chicken_distance(chicken_result)
        min_city_distance = min(min_city_distance, city_distance)
        return
    for i in range(start, len(chickens)):
        chicken_result.append(chickens[i])
        backtracking(i+1, depth+1)
        chicken_result.pop()


backtracking(0, 0)
print(min_city_distance)
