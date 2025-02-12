import sys
from collections import deque

input = sys.stdin.readline

# DSLR
# A --> B로 변환하는데 필요한 최소 명령어 횟수
# BFS로?

## 문자열 연결 --> 문자열을 불변 객체이므로 메모리 많이 잡아먹고, 문자열이 길어질수록 시간도 많이 듦
## 가변 객체인 리스트로 관리하는게 더 좋음

## int(), str() 함수도 너무 반복적으로 사용될 경우 시간 많이 소요


def D(x):
    result = (2 * int(x)) % 10000
    return result


def S(x):
    result = (x - 1) if x > 0 else 9999
    return result


def L(x):
    result = (x % 1000) * 10 + (x // 1000)
    return result


def R(x):
    result = (x % 10) * 1000 + (x // 10)
    return result


T = int(input().strip())
for _ in range(T):
    A, B = map(int, input().strip().split())
    visited = [False] * 10000
    Q = deque([(A, [])])  # (인자, 함수명)
    visited[A] = True
    while Q:
        x, f = Q.popleft()
        for func, func_name in [(D, "D"), (S, "S"), (L, "L"), (R, "R")]:
            result = func(x)
            if visited[result]:
                continue
            if result == B:
                print("".join(f + [func_name]))
                Q.clear()
                break
            Q.append((result, f + [func_name]))
            visited[result] = True
