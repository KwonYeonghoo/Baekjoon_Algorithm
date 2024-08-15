K, N = tuple(map(int, input().split()))
cables = [int(input()) for _ in range(K)]
MAX_CABLE_LEN = 2 ** 31 - 1

def is_satisfying(arr, cut_len):
    count = 0 
    for a in arr:
        line_count = a // cut_len
        count += line_count
    if count >= N:
        return True
    else:
        return False
    
def binary_search(arr, num):
    low, high = 1, num+1
    while low+1 < high:
        mid = (low + high) // 2
        if is_satisfying(arr, mid):
            low = mid
        else:
            high = mid
    return low
    
print(binary_search(cables, MAX_CABLE_LEN))