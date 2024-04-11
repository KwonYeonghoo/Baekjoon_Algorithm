# N개의 정수 (-1000000과 1000000 사이)
# 최소, 최대값

N = int(input())
A = list(map(int, input().split()))

# A.sort()
# print(A[0], A[-1])

min = 1000000
max = -1000000

for num in A:
    if num > max:
        max = num
    
    if num < min:
        min = num

print(min, max)