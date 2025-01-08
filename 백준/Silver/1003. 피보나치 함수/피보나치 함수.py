dp_table = [-1 for _ in range(41)]
zero_table = [-1 for _ in range(41)]
one_table = [-1 for _ in range(41)]

dp_table[0], zero_table[0], one_table[0] = 0, 1, 0
dp_table[1], zero_table[1], one_table[1] = 1, 0, 1

for i in range(2, 41):
    dp_table[i] = dp_table[i-1] + dp_table[i-2]
    zero_table[i] = zero_table[i-1] + zero_table[i-2]
    one_table[i] = one_table[i-1] + one_table[i-2]

T = int(input())
for _ in range(T):
    n = int(input())
    print(zero_table[n], one_table[n])