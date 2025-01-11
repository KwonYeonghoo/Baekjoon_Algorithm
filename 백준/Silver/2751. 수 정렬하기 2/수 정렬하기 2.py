import sys

# N의 최대 길이: 100만
# 요소의 최댓값: 100만 --> 계수 정렬 X

N = int(input())
arr = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])
print('\n'.join(map(str, arr)))