M, N = tuple(map(int, input().split()))
snacks = list(map(int, input().split()))
MAX_SNACK_LEN = 1000000000

def is_satisfying(snacks, cut_len):
    count = 0
    for snack in snacks:
        snack_count = snack // cut_len
        count += snack_count
    if count >= M:
        return True
    else:
        return False
    
def binary_search(snacks, max_snack_len):
    low, high = 0, max_snack_len+1
    while low+1 < high:
        mid = (low + high) // 2
        if is_satisfying(snacks, mid):
            low = mid
        else:
            high = mid
    return low
print(binary_search(snacks, MAX_SNACK_LEN))