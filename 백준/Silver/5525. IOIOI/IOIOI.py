import sys
from collections import deque

# OOIOIOIOIIOII
N = int(input())
M = int(input())
S = input()

count = 0
result = 0
i = 0
while i < len(S) - 2:
    if S[i] == "I" and S[i + 1] == "O" and S[i + 2] == "I":
        count += 1
        if count >= N:
            result += 1
        i += 2
    else:
        count = 0
        i += 1
print(result)
