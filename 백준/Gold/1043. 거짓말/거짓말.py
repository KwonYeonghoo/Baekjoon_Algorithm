# list 대신 set를 써야하는 경우

import sys

input = sys.stdin.readline

# 사람의 수 N
# 파티의 수 M
N, M = map(int, input().strip().split())
truth_knowers = list(map(int, input().strip().split()))
if len(truth_knowers) != 1:
    truth_knowers.pop(0)
truth_knowers = set(truth_knowers)

party_list = []
for _ in range(M):
    party_people = set(map(int, input().strip().split()[1:]))
    party_list.append(party_people)

for _ in range(M):
    for party in party_list:
        if party & truth_knowers:
            truth_knowers = truth_knowers.union(party)

count = 0
for party in party_list:
    if party & truth_knowers:
        continue
    count += 1
print(count)
# print(count)

# 가장 먼저 떠오르는 방법은, 파티마다 순회하면서 거짓말쟁이가 존재하는지 확인하기
# 시간복잡도: O(N^2 * M)
