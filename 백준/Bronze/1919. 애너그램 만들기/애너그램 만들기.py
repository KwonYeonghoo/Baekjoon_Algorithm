ans = 0

w1 = input()
w2 = input()

w1_count = [0] * 26
w2_count = [0] * 26

for w in w1:
    w1_count[ord(w)-97] += 1

for w in w2:
    w2_count[ord(w)-97] += 1

for i in range(26):
    ans += abs((w1_count[i] - w2_count[i]))

print(ans)