# 숨바꼭질
from collections import deque

N, K = list(map(int, input().split()))

def find_min_time(N, K):
    if N == K:
        return 0
    
    max_pos = 100000
    dist = [-1] * (max_pos + 1)
    
    q = deque()
    q.append(N)
    dist[N] = 0
    
    while len(q):
        loc = q.popleft()
        for nloc in [loc-1, loc+1, loc*2]:
            if nloc < 0 or nloc > max_pos:
                continue
            if dist[nloc] != -1:
                continue
            dist[nloc] = dist[loc] + 1
            q.append(nloc)
            
            if nloc == K:
                return dist[nloc]
    return -1
            
print(find_min_time(N, K))