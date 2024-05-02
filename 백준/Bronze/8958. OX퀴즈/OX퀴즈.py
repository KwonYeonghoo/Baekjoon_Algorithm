n = int(input())
arr = [input() for _ in range(n)]
# OOXXOXXOOO
for a in arr:
    score = 0
    add = 1
    for ox in a:
        if ox == 'O':
            score += add
            add += 1
        if ox == 'X':
            add = 1
    print(score)