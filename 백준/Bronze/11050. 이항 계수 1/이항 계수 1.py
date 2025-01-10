import sys

N, K = map(int, sys.stdin.readline().split())

### 이항 계수
# : N개의 원소 중에서 K개의 원소를 선택하는 방법의 수
# (n / k)  =  n! / k!(n-k)!

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def binomial_coefficient(n, k):
    if k == 0 or n == k:
        return 1
    return factorial(n) // (factorial(k) * factorial(n-k))

print(binomial_coefficient(N,K))