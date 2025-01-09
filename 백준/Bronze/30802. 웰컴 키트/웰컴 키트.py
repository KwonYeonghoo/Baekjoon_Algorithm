N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

tshirt_count = 0
for size in sizes:
    if size <= T:
        if size == 0:
            continue
        tshirt_count += 1
    else:
        if size % T == 0:
            tshirt_count += (size // T)
        else: tshirt_count += (size // T + 1)
    
pen_set_count = N // P
pen_count = N % P

print(tshirt_count)
print(pen_set_count, pen_count)