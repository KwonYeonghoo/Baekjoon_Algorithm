while True:
    count = 0
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    arr_N = [int(input()) for _ in range(N)]
    arr_M = [int(input()) for _ in range(M)]
    
    i, j = 0, 0
    while (i <= N-1) and (j <= M-1):
        if arr_N[i] == arr_M[j]:
            count += 1
            i += 1
            j += 1
        elif arr_N[i] < arr_M[j]:
            i += 1
        elif arr_N[i] > arr_M[j]:
            j += 1
    print(count)