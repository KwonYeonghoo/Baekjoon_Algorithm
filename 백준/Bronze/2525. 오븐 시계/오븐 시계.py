A, B = list(map(int, input().split()))
C = int(input())

if B + C < 60:
    print(A, B+C)
else:
    min_total = B+C
    hour = min_total // 60
    min_left = min_total % 60
    
    if A + hour < 24:
        print(A+hour, min_left)
    else:
        print(A+hour-24, min_left)