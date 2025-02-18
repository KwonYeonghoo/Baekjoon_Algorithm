import sys
input = sys.stdin.readline

# A**B % C --> O(B)
# O(log B)로 줄이는 게 목표
A, B, C = tuple(map(int, input().strip().split()))
def power(a, b, c):
    if b == 1:
        return a % c
    
    val = power(a, b//2, c)
    if b % 2 == 0:
        return (val * val) % c
    else:
        return (val * val * a) % c

print(power(A, B, C))