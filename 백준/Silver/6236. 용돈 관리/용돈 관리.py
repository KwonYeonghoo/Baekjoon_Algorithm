import sys

# sys.stdin = open("/Users/hoo/Hoo/Study/알고리즘/2025/input.txt", "r")

N, M = map(int, input().split())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]


def get_withdrawl_count(amount):
    usage = 0 
    withdrawl_count = 1 

    for i in range(N):
        if usage + arr[i] > amount:
            withdrawl_count += 1
            usage = arr[i] 
        else:
            usage += arr[i] 

    return withdrawl_count


def binary_search(k):
    left, right = max(arr), sum(arr)

    while left < right:
        mid = (left + right) // 2 

        if get_withdrawl_count(mid) <= k:
            right = mid
        else:
            left = mid + 1 

    return left


print(binary_search(M))
