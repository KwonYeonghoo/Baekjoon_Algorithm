# ACM 호텔

T = int(input())
arrs = [list(map(int,input().split())) for _ in range(T)]

def get_room_num(arr):
    H = arr[0]
    W = arr[1]
    N = arr[2]

    # N = 10일 때
    h_index = 1
    w_index = 1
    if N <= H:
        h_index = N
    else:
        while N > H:
            N -= H
            w_index += 1
        h_index = N
    return w_index, h_index

for arr in arrs:
    W, H = get_room_num(arr)
    if len(str(W)) == 1:
        print(f"{H}0{W}")
    else:
        print(f"{H}{W}")