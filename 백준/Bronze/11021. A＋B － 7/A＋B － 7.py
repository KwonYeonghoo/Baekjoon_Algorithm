T = int(input())

for i in range(1, T+1):
    A, B = list(map(int, input().split()))
    print(f"Case #{i}: {A+B}")