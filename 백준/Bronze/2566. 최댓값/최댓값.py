arr = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_row = 0
max_col = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num:
            max_num = max(max_num, arr[i][j])
            max_row = i
            max_col = j
print(max_num)
print(max_row+1, max_col+1)