N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

orders = [list(map(int, input().split())) for _ in range(M)]

for order in orders:
    start = order[0]-1
    end = order[1]-1
    size = end - start + 1
    for i in range(size // 2):
        temp1 = arr[start+i]
        temp2 = arr[end-i]
        arr[start+i] = temp2
        arr[end-i] = temp1
print(' '.join(list(map(str, arr))))