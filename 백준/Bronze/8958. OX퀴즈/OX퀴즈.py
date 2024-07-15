# OX 퀴즈
n = int(input())
arrs = [[a for a in input()] for _ in range(n)]

def get_score(arr):
    result = 0
    score = 0
    for a in arr:
        if a == "O":
            score += 1
        else:
            score = 0
        result += score
    return result

for arr in arrs:
    print(get_score(arr))