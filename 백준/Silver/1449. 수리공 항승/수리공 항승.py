import sys


N, L = map(int, input().split())
arr = sorted(list(map(int, sys.stdin.readline().strip().split())))
visited = [0] * (1000 + 1)


def OOB(nx):
    if nx > 1000:
        return True
    else:
        return False


tape_usage = 0
for i in range(1001):
    if i in arr and visited[i] == 0:
        for j in range(L):
            if OOB(i + j):
                continue
            visited[i + j] = 1
        tape_usage += 1
print(tape_usage)
