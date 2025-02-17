import sys
from collections import deque
input = sys.stdin.readline

# 2를 곱한다
# 1을 수의 가장 오른쪽에 추가한다.

# A -> B로 바꾸는 데 필요한 연산의 최솟값.
# 완전탐색

A, B = map(int, input().strip().split())


def bfs(A, B):
    Q = deque([(A, 1)])  # 현재 숫자, 연산횟수
    while Q:
        x, count = Q.popleft()

        if x == B:
            return count

        for nx in (x * 2, x * 10 + 1):
            if nx > B:
                continue
            Q.append((nx, count + 1))
    return -1


print(bfs(A, B))
