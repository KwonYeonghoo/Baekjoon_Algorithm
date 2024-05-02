A, B, V = list(map(int, input().split()))

if V-A == 0:
    print(1)
elif (V - A) % (A - B) == 0:
    print(int((V - A) / (A - B) + 1))
else:
    print(int((V - A) / (A - B) + 2))