import sys

N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().strip().split()))
# 이분탐색으로 절단기 높이를 조절
# 나무의 수(N)은 100만이므로, O(N) 시간에 돌 수 있음
MAX_HEIGHT = 10000000000


def binary_search(max_height, k):
    left = 0
    right = max_height
    while left + 1 < right:
        mid = (left + right) // 2
        if cut_tree(mid) >= k:
            left = mid
        else:
            right = mid
        # print(f"left: {left} / right: {right} / mid: {mid}")
    return left


def cut_tree(height):
    result = 0
    for tree in trees:
        if tree <= height:
            continue
        else:
            result += tree - height
    return result


print(binary_search(MAX_HEIGHT, M))