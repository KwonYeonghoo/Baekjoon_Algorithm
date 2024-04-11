# 1 ~ N까지의 번호가 매겨진 N개의 바구니
# 바구니당 공 1개씩

# M번 공 투입

N, M = tuple(map(int, input().split()))

basket = [0 for _ in range(1,N+1)]
balls = [list(map(int, input().split())) for _ in range(M)]

for ball in balls:
    i = ball[0]
    j = ball[1]
    k = ball[2]
    
    for idx in range(i, j+1):
        basket[idx-1] = k

print(' '.join(map(str,basket)))
