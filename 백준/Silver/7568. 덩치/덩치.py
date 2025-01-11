def is_bigger(a: list, b: list):
    flag_a, flag_b = False, False
    if a[0] < b[0]:
        flag_a = True
    if a[1] < b[1]:
        flag_b = True

    if flag_a and flag_b:
        return True
    else:
        False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    count = 1
    for j in range(N):
        if i == j:
            continue
        if is_bigger(arr[i], arr[j]):
            count += 1
    print(count)