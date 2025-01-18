T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    i = 0
    count = 0
    while True:
        max_value = max(arr)
        if arr[i] == max_value:
            count += 1
            arr[i] = -1
            if i == M:
                break
            else:
                i = (i + 1) % N
        else:
            i = (i + 1) % N
    print(count)