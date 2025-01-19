import sys

K, N = map(int, input().split())
arr = [int(sys.stdin.readline().strip()) for _ in range(K)]

# 2^31은 대충 20억 --> O(N)으로도 통과 안됨
# O(logN) 알고리즘으로 풀어야 함 --> 이분탐색

# 랜선의 길이가 2^31-1이라 가정하고, 이를 절반씩 줄여가며 K개의 랜선을 N개로 만드는 최대 랜선의 길이를 찾기
# 이분탐색 함수에서 상태함수를 문제에 맞게 변형시켜가며 풀기

MAX_CABLE_LEN = 2**31 - 1


def binary_search(arr, max_cable_len):
    low, high = 1, max_cable_len + 1
    while low + 1 < high:
        mid = (low + high) // 2
        if is_satisfying(arr, mid):
            low = mid
        else:
            high = mid
    return low


def is_satisfying(arr, cut_len):
    count = 0
    for cable in arr:
        count += cable // cut_len
    if count >= N:
        return True
    else:
        return False


print(binary_search(arr, MAX_CABLE_LEN))
