# 식의 결과가 최소가 돼야함
# - 뒤에 오는 수가 가능한 한 커야함
# - 뒤에 +가 오는 경우에만 괄호 치면 됨 --> .split('-')

formula_list = input().split("-")
result = []
for f in formula_list:
    num = 0
    temp = ""
    for c in f:
        if ord(c) != 43:
            temp += c
        else:
            num += int(temp)
            temp = ""
    num += int(temp)
    result.append(num)

curr_num = result[0]
for i in range(1, len(result)):
    curr_num -= result[i]
print(curr_num)
