N = int(input())
arr1 = sorted(list(map(int, input().split())))
M = int(input())
arr2 = list(map(int, input().split()))

def lower_bound(arr, k):
    low, high = -1, len(arr)
    while low+1 < high:
        mid = (low + high) // 2
        if arr[mid] >= k:
            high = mid
        else:
            low = mid
    # if high == len(arr):
    #     return -1
    return high

def upper_bound(arr, k):
    low, high = -1, len(arr)
    while low+1 < high:
        mid = (low+high) // 2
        if arr[mid] > k:
            high = mid
        else:
            low = mid
    # if high == len(arr)-1:
    #     return -1
    return high

for k in arr2:
    ub = upper_bound(arr1, k)
    lb = lower_bound(arr1, k)
    print(ub - lb)