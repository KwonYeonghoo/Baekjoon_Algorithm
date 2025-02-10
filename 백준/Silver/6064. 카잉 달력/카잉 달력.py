import sys
import math

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().strip().split())
    # <x:y>
    # x' = x + 1 (x < M) / x' = 1
    # y' = y + 1 (y < N) / y' = 1
    # <M:N>은 달력의 마지막 해
    # 종말의 해 구하기 --> 최소공배수 math.lcm()

    dooms_day = math.lcm(M, N)
    val = x
    flag = False
    while val <= dooms_day:
        if (val % N if val % N != 0 else val % N + N) == y:
            flag = True
            break
        val += M
    if flag == True:
        print(val)
    else:
        print(-1)