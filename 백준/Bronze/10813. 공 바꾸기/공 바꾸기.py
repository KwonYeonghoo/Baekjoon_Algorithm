N, M = tuple(map(int, input().split()))

basket = [i for i in range(1,N+1)]
balls = [list(map(int, input().split())) for _ in range(M)]

for ball in balls:
    i = ball[0]-1
    j = ball[1]-1
    
    basket[i], basket[j] = basket[j], basket[i]
    
print(' '.join(map(str, basket)))