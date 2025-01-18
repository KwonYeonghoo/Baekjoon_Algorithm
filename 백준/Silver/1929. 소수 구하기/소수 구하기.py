# 일반적으로 반복문을 돌며 소수인지 판별하는 방식은 시간 초과할 듯
# 다른 방식으로 소수를 구해야 함.
# --> 어떤 수 N이 소수가 아닌 경우, 그 약수 중 최소 하나는 \sqrt{N} 이하이다.
# Ex) 12 = 3 * 4
# Ex) 30 = 5 * 6
# 따라서, \sqrt{N}까지만 돌아도 충분히 소수 판별이 가능하다.
M, N = map(int, input().split())


def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for n in range(M, N + 1):
    if is_prime_number(n):
        print(n)