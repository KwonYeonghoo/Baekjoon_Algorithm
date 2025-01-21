import sys

pw_dict = {}
N, M = map(int, input().split())
for _ in range(N):
    site, pw = map(str, sys.stdin.readline().strip().split())
    pw_dict[site] = pw

for _ in range(M):
    print(pw_dict[sys.stdin.readline().strip()])