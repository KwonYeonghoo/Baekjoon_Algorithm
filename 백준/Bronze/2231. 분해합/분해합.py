N = int(input())

flag = False
for num in range(1, N+1):
    bhh = num
    str_num = str(num)
    for s in str_num:
        bhh += int(s)
    if bhh == N:
        flag = True
        break
print(num if flag==True else 0)