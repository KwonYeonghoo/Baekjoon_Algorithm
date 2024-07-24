picture = [input() for _ in range(5)]
ans = ""
length = 1

while length <= 15:
    for row in picture:
        if len(row) >= length:
            ans += row[length-1]
    length += 1
print(ans)