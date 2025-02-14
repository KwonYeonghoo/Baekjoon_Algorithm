import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = sorted(list(map(int, input().strip().split())))

result = []
visited = [0] * N


def backtracking(d):
    if d == M:
        print(" ".join(map(str, result)))
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        result.append(arr[i])
        visited[i] = 1
        backtracking(d + 1)
        result.pop()
        visited[i] = 0


backtracking(0)
