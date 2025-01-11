def is_jongmal_number(num):
    num = str(num)
    count = 1
    for i in range(len(num) - 1):
        if num[i] == "6" and num[i + 1] == "6":
            count += 1
        else:
            count = 1
        if count >= 3:
            return True
    return False


N = int(input())
ans = 0
n = 1
while True:
    if is_jongmal_number(n):
        ans += 1
        if ans == N:
            print(n)
            break
    n += 1