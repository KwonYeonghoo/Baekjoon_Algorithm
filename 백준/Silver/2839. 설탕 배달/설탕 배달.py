# 최소한의 개수를 찾는 문제 --> 그리디 또는 dp

N = int(input())

bags = 0
while N >= 0:
    if N % 5 == 0:
        bags += N // 5
        print(bags)
        break
    N -= 3  # 5로 나누어 떨어지지 않으면 3kg 봉지 하나 추가
    bags += 1
else:
    print(-1)