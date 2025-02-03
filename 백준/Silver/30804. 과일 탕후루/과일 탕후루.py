import sys
from collections import defaultdict

# 투 포인터? 그리디?
N = int(input())  # 과일의 개수 (종류 X)
tanghuru = list(map(int, sys.stdin.readline().strip().split()))

left, right, count = 0, 0, 0
fruit = defaultdict(int)
answer = 0
while right < N:
    if fruit[tanghuru[right]] == 0:
        count += 1
    fruit[tanghuru[right]] += 1

    while count > 2:
        fruit[tanghuru[left]] -= 1
        if fruit[tanghuru[left]] == 0:
            count -= 1
        left += 1

    answer = max(answer, right - left + 1)
    right += 1
print(answer)
