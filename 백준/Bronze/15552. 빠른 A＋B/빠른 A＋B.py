import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    A, B = list(map(int, sys.stdin.readline().rstrip().split()))
    print(A + B)
