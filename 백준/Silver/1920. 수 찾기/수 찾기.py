

N = int(input())
arr1 = sorted(list(map(int, input().split())))
M = int(input())
arr2 = list(map(int, input().split()))

def compare(x, k):
    if x <= k:
        return True
    else:
        return False

def binary_search(arr1, k):
    low, high = -1, len(arr1)
    while low + 1 < high:
        mid = (low + high) // 2
        is_true = compare(arr1[mid], k)
        if is_true:
            low = mid
        else:
            high = mid
    if arr1[low] == k:
        return 1
    return 0
    
for k in arr2:
    print(binary_search(arr1, k))