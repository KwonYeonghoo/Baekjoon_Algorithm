arr = [0] * 10
A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)

for n in result:
    # n은 0~9 사이
    # arr의 인덱스도 0~9 사이
    n = int(n)
    arr[n] += 1

# print(result)
for i in arr:
    print(i)