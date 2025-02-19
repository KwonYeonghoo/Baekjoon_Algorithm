import sys
input = sys.stdin.readline

N = int(input().strip())
real = sorted(list(map(int, input().strip().split())))

if len(real) == 1:
    print(real[0] ** 2)
else:
    print(real[0] * real[-1])