import sys
input = sys.stdin.readline

# 2번과 동일한 문제, but 수열을 이루는 숫자가 음수가 될 수도 있음

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
    if idx == len(result):
        result.append(a)
    else:
        result[idx] = a
        
print(len(result))