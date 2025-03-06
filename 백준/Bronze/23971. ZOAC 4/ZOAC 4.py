import sys
input = sys.stdin.readline

H, W, N, M = map(int, input().strip().split())

a = H // (N + 1) if H % (N + 1) == 0 else H // (N + 1) + 1
b = W // (M + 1) if W % (M + 1) == 0 else W // (M + 1) + 1
print(a * b)