import sys

# 누적합
# 소문자 알파벳으로만 구성
# 26개 알파벳에 대해 누적합 리스트 생성
# ord('a'): 97
S = "_" + sys.stdin.readline().strip()
q = int(input())
prefix_sum = [[0] * len(S) for _ in range(26)]
for i in range(26):
    target = chr(i + 97)
    count = 0
    for j in range(len(S)):
        if S[j] == target:
            count += 1
        prefix_sum[i][j] = count
# print(prefix_sum)

for _ in range(q):
    a, l, r = map(str, input().split())
    l, r = int(l) + 1, int(r) + 1
    idx = ord(a) - 97
    result = prefix_sum[idx][r] - prefix_sum[idx][l - 1]
    print(result)
