import sys

N, M = map(int, input().split())
never_heard_set = set()
result = []
for _ in range(N):
    never_heard = sys.stdin.readline().strip()
    never_heard_set.add(never_heard)

for _ in range(M):
    never_seen = sys.stdin.readline().strip()
    # if len(never_heard_set - {never_seen}) != N: # O(N) 연산
    #     result.append(never_seen)
    if never_seen in never_heard_set:  # O(1) 연산
        result.append(never_seen)

print(len(result))
print("\n".join(sorted(result)))