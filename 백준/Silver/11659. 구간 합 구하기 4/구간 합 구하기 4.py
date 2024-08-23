N, M = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
commands = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
acc = []
acc.append(arr[0])
for i in range(1, N):
    acc.append(arr[i]+acc[i-1])

for command in commands:
    x = command[0]
    y = command[1]
    if x == 0:
        print(acc[y])
    else:
        print(acc[y]-acc[x-1])