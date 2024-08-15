N, S = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
vis = [0 for _ in range(N)]

count = 0

def f(k, sum):
    global count
    # 탈출 조건
    if k == N:
        if sum == S:
            count += 1
        return
    # k번째 숫자를 포함 한거, 안한거
    f(k+1, sum)
    f(k+1, sum + arr[k])

f(0, 0)
if S == 0:
    count -= 1
print(count)