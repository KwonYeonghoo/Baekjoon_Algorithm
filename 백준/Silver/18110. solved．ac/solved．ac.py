import sys

# 파이썬의 round() 함수:
#   `오사오입`: 5 미만의 숫자는 내림, 5 초과의 숫자는 올림
#               딱 5인 경우, 앞자리가 홀수이면 올림, 짝수이면 버림을 한다.
# 따라서, 딱 5인 경우 항상 올림으로 처리해주는 my_round 함수 생성

def my_round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

N = int(input())
if N == 0:
    print(0)
else:
    arr = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])
    result = 0

    exclude = my_round(N * 0.15)

    for i in range(0 + exclude, N - exclude):
        result += arr[i]

    print(my_round(result / (N - 2 * exclude)))