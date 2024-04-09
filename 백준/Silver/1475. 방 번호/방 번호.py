N = input()

arr = [0] * 10

for n in N:
    n = int(n)
    if n == 9:
        arr[6] += 1 
    else:
        arr[n] += 1

if arr[6] % 2 == 0:
    arr[6] = arr[6] // 2
else:
    arr[6] = arr[6] // 2 + 1

print(max(arr))