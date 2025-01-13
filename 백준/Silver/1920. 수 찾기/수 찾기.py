# O(NM) 불가능 --> O(M log N)으로 풀어야함
# 이분 탐색
N = int(input())
arr_n = sorted(list(map(int, input().split())))
M = int(input())
arr_m = list(map(int, input().split()))


def binary_search(arr, val):
    low, high = -1, len(arr)
    while low + 1 < high:
        mid = (low + high) // 2
        if arr[mid] >= val:
            high = mid
        else:
            low = mid

    if high == len(arr):
        return False

    if arr[high] == val:
        return True
    else:
        return False


for val in arr_m:
    if binary_search(arr_n, val):
        print(1)
    else:
        print(0)
