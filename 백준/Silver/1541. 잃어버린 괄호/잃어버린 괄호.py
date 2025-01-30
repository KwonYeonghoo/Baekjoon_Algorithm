formula_list = input().split("-")
result = []
for f in formula_list:
    num = 0
    for c in f.split("+"):
        num += int(c)
    result.append(num)

curr_num = result[0]
for i in range(1, len(result)):
    curr_num -= result[i]
print(curr_num)