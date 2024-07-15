# 숫자의 개수
A, B, C = [int(input()) for _ in range(3)]
num = str(A * B * C)
arr = [0 for _ in range(10)]
for n in num:
    arr[int(n)] += 1

for i in arr:
    print(str(i))