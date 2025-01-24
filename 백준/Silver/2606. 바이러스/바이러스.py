# 완전탐색? 백트래킹?
# 컴퓨터 간의 연결을 어떻게 표현할지 --> 딕셔너리?
N = int(input())
T = int(input())
pc_dict = {i: [] for i in range(1, N + 1)}
is_infected = [0] * (N + 1)

for _ in range(T):
    a, b = map(int, input().split())
    pc_dict[a].append(b)
    pc_dict[b].append(a)


def count_infected_pc(key):
    if len(pc_dict[key]) == 0:
        return sum(is_infected)
    for val in pc_dict[key]:
        if is_infected[val] == 1:
            continue
        is_infected[val] = 1
        count_infected_pc(val)
    return sum(is_infected)


if len(pc_dict[1]) == 0:
    print(count_infected_pc(1))
else:
    print(count_infected_pc(1) - 1)