N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
for n in range(1, N+1):
    for value in arr:
        if n % value == 0:
            answer += n
            break
print(answer)