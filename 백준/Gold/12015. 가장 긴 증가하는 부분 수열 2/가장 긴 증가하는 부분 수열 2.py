import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().strip().split()))


def binary_search(arr, k):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= k:
            right = mid
        else:
            left = mid + 1
    return left


result = []
for a in arr:
    idx = binary_search(result, a)
    if len(result) == idx:
        result.append(a)
    else:
        result[idx] = a
print(len(result))
