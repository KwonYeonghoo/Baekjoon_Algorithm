import sys

# 누적합
# 소문자 알파벳으로만 구성
# 26개 알파벳에 대해 누적합 리스트 생성
# ord('a'): 97
S = "_" + sys.stdin.readline().strip()
q = int(sys.stdin.readline().strip())
prefix_sum = {s: [0] * len(S) for s in list(set(S))}
for target in list(prefix_sum.keys()):
    count = 0
    for j in range(len(S)):
        if S[j] == target:
            count += 1
        prefix_sum[target][j] = count

# print(prefix_sum)
for _ in range(q):
    a, l, r = map(str, sys.stdin.readline().strip().split())
    l, r = int(l) + 1, int(r) + 1
    if a not in list(prefix_sum.keys()):
        print(0)
        continue
    result = prefix_sum[a][r] - prefix_sum[a][l - 1]
    print(result)