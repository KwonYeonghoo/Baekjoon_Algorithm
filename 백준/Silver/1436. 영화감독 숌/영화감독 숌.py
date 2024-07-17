def check_666(n):
    cnt = 0
    num = str(n)
    for w in num:
        if w == "6":
            cnt += 1
            if cnt == 3:
                return True
        else:
            cnt = 0
    return False


N = int(input())

num = 666
cnt = 0
while cnt <= 10000:
    if check_666(num):
        cnt += 1
        if cnt == N:
            print(num)
            break
    num += 1