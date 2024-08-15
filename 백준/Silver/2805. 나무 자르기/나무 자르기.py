N, M = tuple(map(int, input().split()))
trees = list(map(int, input().split()))
MAX_TAKEAWAY_LEN = 2000000000

def is_satisfying(trees, cut_len):
    count = 0
    for tree in trees:
        if cut_len >= tree: # 절단기보다 나무가 짧은 경우
            continue
        takeaway = tree - cut_len
        count += takeaway
    if count >= M:
        return True
    else:
        return False
    
def binary_search(trees, max_takeaway_len):
    low, high = 0, max_takeaway_len+1
    while low+1 < high:
        mid = (low + high) // 2
        if is_satisfying(trees, mid):
            low = mid
        else:
            high = mid
    return low

print(binary_search(trees, MAX_TAKEAWAY_LEN))