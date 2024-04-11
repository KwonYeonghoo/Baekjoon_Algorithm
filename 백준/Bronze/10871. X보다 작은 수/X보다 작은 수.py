# 수열 A, 정수 X
# A에서 X보다 작은 수를 모두 출력

N, X = tuple(map(int, input().split()))
A = list(map(int, input().split()))
result = []

for num in A:
    if num < X:
        result.append(str(num))
        
print(" ".join(result))