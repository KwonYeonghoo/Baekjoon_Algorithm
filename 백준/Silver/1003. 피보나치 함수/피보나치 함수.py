# dp_table
zero_table = [0] * (40 + 1)
one_table = [0] * (40 + 1)  # 각각 0과 1이 출력되는 횟수를 저장할 dp 테이블

zero_table[0] += 1
one_table[1] += 1

for i in range(2, 40 + 1):
    zero_table[i] = zero_table[i - 2] + zero_table[i - 1]
    one_table[i] = one_table[i - 2] + one_table[i - 1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(zero_table[N], one_table[N])