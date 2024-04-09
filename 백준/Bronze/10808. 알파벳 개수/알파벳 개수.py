S = input()
result = [0] * 26

for s in S:
    index = ord(s) - 97
    result[index] += 1

print(" ".join(list(map(str, result))))